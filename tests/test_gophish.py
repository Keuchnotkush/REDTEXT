"""Tests for GoPhish integration: API client, bridge, config, and CLI."""

import csv
import json
import os
import random
import ssl
import tempfile
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from redtext_generator.config import (
    get_config_path,
    load_gophish_config,
    save_gophish_config,
)
from redtext_generator.gophish import GoPhishAPIError, GoPhishClient
from redtext_generator.gophish_bridge import (
    build_campaign_config,
    parse_targets_csv,
    phishing_to_template,
    text_to_html,
)


# ── Helpers ────────────────────────────────────────────────────

def _mock_response(data, status=200):
    """Create a mock urllib response as a context manager."""
    mock = MagicMock()
    mock.read.return_value = json.dumps(data).encode("utf-8")
    mock.status = status
    mock.getcode.return_value = status
    mock.__enter__ = lambda s: s
    mock.__exit__ = MagicMock(return_value=False)
    return mock


def _sample_phishing_data():
    """Return a sample phishing_email dict matching generator output."""
    return {
        "type": "phishing_email",
        "template": "Credential Harvest",
        "subject": "Urgent: Password Reset Required",
        "body": "Dear John,\n\nYour password expires today.\n\nPlease reset it immediately.\n\nBest,\nIT Support",
        "target": {
            "name": "John Smith",
            "department": "Engineering",
            "company": "Acme Corp",
        },
        "attacker_persona": "IT Support",
        "urgency_level": "high",
    }


# ── GoPhishAPIError ───────────────────────────────────────────

class TestGoPhishAPIError(unittest.TestCase):
    def test_message(self):
        err = GoPhishAPIError("something failed")
        self.assertEqual(str(err), "something failed")

    def test_status_code_attribute(self):
        err = GoPhishAPIError("fail", status_code=404)
        self.assertEqual(err.status_code, 404)

    def test_response_body_attribute(self):
        err = GoPhishAPIError("fail", response_body='{"error": true}')
        self.assertEqual(err.response_body, '{"error": true}')

    def test_defaults_none(self):
        err = GoPhishAPIError("fail")
        self.assertIsNone(err.status_code)
        self.assertIsNone(err.response_body)


# ── GoPhishClient Init ────────────────────────────────────────

class TestGoPhishClientInit(unittest.TestCase):
    def test_strips_trailing_slash(self):
        client = GoPhishClient("https://localhost:3333/", "testkey")
        self.assertEqual(client.api_url, "https://localhost:3333")

    def test_preserves_url_without_slash(self):
        client = GoPhishClient("https://localhost:3333", "testkey")
        self.assertEqual(client.api_url, "https://localhost:3333")

    def test_ssl_context_verify_true(self):
        client = GoPhishClient("https://localhost", "key", verify_ssl=True)
        self.assertTrue(client._ssl_context.check_hostname)

    def test_ssl_context_verify_false(self):
        client = GoPhishClient("https://localhost", "key", verify_ssl=False)
        self.assertFalse(client._ssl_context.check_hostname)
        self.assertEqual(client._ssl_context.verify_mode, ssl.CERT_NONE)


# ── GoPhishClient Requests ────────────────────────────────────

class TestGoPhishClientRequest(unittest.TestCase):
    def setUp(self):
        self.client = GoPhishClient("https://gophish.local", "testkey123")

    @patch("urllib.request.urlopen")
    def test_get_templates_success(self, mock_urlopen):
        expected = [{"id": 1, "name": "Test Template"}]
        mock_urlopen.return_value = _mock_response(expected)
        result = self.client.get_templates()
        self.assertEqual(result, expected)

    @patch("urllib.request.urlopen")
    def test_create_template_sends_post(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"id": 5, "name": "New"})
        self.client.create_template("New", "Subject", "Body text", "<p>HTML</p>")

        req = mock_urlopen.call_args[0][0]
        self.assertEqual(req.method, "POST")
        body = json.loads(req.data.decode("utf-8"))
        self.assertEqual(body["name"], "New")
        self.assertEqual(body["subject"], "Subject")
        self.assertEqual(body["text"], "Body text")
        self.assertEqual(body["html"], "<p>HTML</p>")

    @patch("urllib.request.urlopen")
    def test_auth_header_has_space_after_bearer(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response([])
        self.client.get_templates()

        req = mock_urlopen.call_args[0][0]
        self.assertEqual(req.get_header("Authorization"), "Bearer testkey123")

    @patch("urllib.request.urlopen")
    def test_content_type_json(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response([])
        self.client.get_templates()

        req = mock_urlopen.call_args[0][0]
        self.assertEqual(req.get_header("Content-type"), "application/json")

    @patch("urllib.request.urlopen")
    def test_create_group_sends_targets(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"id": 3})
        targets = [{"email": "a@b.com", "first_name": "A", "last_name": "B", "position": "Eng"}]
        self.client.create_group("TestGroup", targets)

        req = mock_urlopen.call_args[0][0]
        body = json.loads(req.data.decode("utf-8"))
        self.assertEqual(body["name"], "TestGroup")
        self.assertEqual(body["targets"], targets)

    @patch("urllib.request.urlopen")
    def test_create_campaign_payload_structure(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"id": 10})
        self.client.create_campaign(
            name="Camp1", template_name="T1", page_name="P1",
            smtp_name="S1", url="https://evil.com",
            group_names=["G1", "G2"], launch_date="2025-01-01T08:00:00+00:00",
        )

        req = mock_urlopen.call_args[0][0]
        body = json.loads(req.data.decode("utf-8"))
        self.assertEqual(body["template"], {"name": "T1"})
        self.assertEqual(body["page"], {"name": "P1"})
        self.assertEqual(body["smtp"], {"name": "S1"})
        self.assertEqual(body["groups"], [{"name": "G1"}, {"name": "G2"}])
        self.assertEqual(body["launch_date"], "2025-01-01T08:00:00+00:00")

    @patch("urllib.request.urlopen")
    def test_campaign_without_launch_date(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"id": 11})
        self.client.create_campaign(
            name="Camp2", template_name="T1", page_name="P1",
            smtp_name="S1", url="https://test.com", group_names=["G1"],
        )

        req = mock_urlopen.call_args[0][0]
        body = json.loads(req.data.decode("utf-8"))
        self.assertNotIn("launch_date", body)

    @patch("urllib.request.urlopen")
    def test_get_campaign_results_url(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"stats": {}})
        self.client.get_campaign_results(42)

        req = mock_urlopen.call_args[0][0]
        self.assertIn("/api/campaigns/42/summary", req.full_url)

    @patch("urllib.request.urlopen")
    def test_http_error_raises_gophish_error(self, mock_urlopen):
        http_err = __import__("urllib.error", fromlist=["HTTPError"]).HTTPError(
            "https://gophish.local/api/templates/", 404, "Not Found", {}, StringIO('{"message":"not found"}')
        )
        mock_urlopen.side_effect = http_err

        with self.assertRaises(GoPhishAPIError) as ctx:
            self.client.get_templates()
        self.assertEqual(ctx.exception.status_code, 404)

    @patch("urllib.request.urlopen")
    def test_url_error_raises_gophish_error(self, mock_urlopen):
        url_err = __import__("urllib.error", fromlist=["URLError"]).URLError("Connection refused")
        mock_urlopen.side_effect = url_err

        with self.assertRaises(GoPhishAPIError) as ctx:
            self.client.get_templates()
        self.assertIn("Connection error", str(ctx.exception))

    @patch("urllib.request.urlopen")
    def test_invalid_json_raises_gophish_error(self, mock_urlopen):
        mock = MagicMock()
        mock.read.return_value = b"not json at all"
        mock.__enter__ = lambda s: s
        mock.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock

        with self.assertRaises(GoPhishAPIError) as ctx:
            self.client.get_templates()
        self.assertIn("Invalid JSON", str(ctx.exception))

    @patch("urllib.request.urlopen")
    def test_get_smtp_profiles(self, mock_urlopen):
        expected = [{"id": 1, "name": "SMTP1"}]
        mock_urlopen.return_value = _mock_response(expected)
        result = self.client.get_smtp_profiles()
        self.assertEqual(result, expected)

    @patch("urllib.request.urlopen")
    def test_empty_response_returns_empty_dict(self, mock_urlopen):
        mock = MagicMock()
        mock.read.return_value = b""
        mock.__enter__ = lambda s: s
        mock.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock

        result = self.client._request("DELETE", "/api/templates/1")
        self.assertEqual(result, {})


# ── text_to_html ──────────────────────────────────────────────

class TestTextToHtml(unittest.TestCase):
    def test_wraps_paragraphs_in_p_tags(self):
        html = text_to_html("Hello world\n\nSecond paragraph")
        self.assertIn("<p>Hello world</p>", html)
        self.assertIn("<p>Second paragraph</p>", html)

    def test_single_newlines_become_br(self):
        html = text_to_html("Line1\nLine2")
        self.assertIn("Line1<br>Line2", html)

    def test_tracking_pixel_appended(self):
        html = text_to_html("Test")
        self.assertIn("{{.Tracker}}", html)

    def test_empty_input(self):
        html = text_to_html("")
        self.assertIn("<html>", html)
        self.assertIn("{{.Tracker}}", html)

    def test_html_structure(self):
        html = text_to_html("Content")
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</body></html>"))

    def test_multiple_blank_lines(self):
        html = text_to_html("A\n\n\n\nB")
        self.assertIn("<p>A</p>", html)
        self.assertIn("<p>B</p>", html)


# ── phishing_to_template ─────────────────────────────────────

class TestPhishingToTemplate(unittest.TestCase):
    def setUp(self):
        self.data = _sample_phishing_data()

    def test_default_name_prefix(self):
        result = phishing_to_template(self.data)
        self.assertTrue(result["name"].startswith("REDTEXT - "))
        self.assertIn("Credential Harvest", result["name"])

    def test_custom_name_override(self):
        result = phishing_to_template(self.data, template_name="Custom Template")
        self.assertEqual(result["name"], "Custom Template")

    def test_subject_copied(self):
        result = phishing_to_template(self.data)
        self.assertEqual(result["subject"], self.data["subject"])

    def test_text_is_body(self):
        result = phishing_to_template(self.data)
        self.assertEqual(result["text"], self.data["body"])

    def test_html_contains_tracker(self):
        result = phishing_to_template(self.data)
        self.assertIn("{{.Tracker}}", result["html"])

    def test_returns_correct_keys(self):
        result = phishing_to_template(self.data)
        self.assertEqual(set(result.keys()), {"name", "subject", "text", "html"})


# ── build_campaign_config ─────────────────────────────────────

class TestBuildCampaignConfig(unittest.TestCase):
    def test_required_fields_present(self):
        result = build_campaign_config(
            scenario_name="Op Test", template_name="T1", group_name="G1",
            smtp_name="SMTP1", landing_page="Page1", url="https://test.com",
        )
        self.assertEqual(result["name"], "Op Test")
        self.assertEqual(result["template_name"], "T1")
        self.assertEqual(result["page_name"], "Page1")
        self.assertEqual(result["smtp_name"], "SMTP1")
        self.assertEqual(result["url"], "https://test.com")

    def test_group_names_is_list(self):
        result = build_campaign_config(
            scenario_name="Op", template_name="T", group_name="G",
            smtp_name="S", landing_page="P", url="https://x.com",
        )
        self.assertIsInstance(result["group_names"], list)
        self.assertEqual(result["group_names"], ["G"])

    def test_launch_date_none_by_default(self):
        result = build_campaign_config(
            scenario_name="Op", template_name="T", group_name="G",
            smtp_name="S", landing_page="P", url="https://x.com",
        )
        self.assertIsNone(result["launch_date"])

    def test_launch_date_passed_through(self):
        result = build_campaign_config(
            scenario_name="Op", template_name="T", group_name="G",
            smtp_name="S", landing_page="P", url="https://x.com",
            launch_date="2025-06-01T08:00:00+00:00",
        )
        self.assertEqual(result["launch_date"], "2025-06-01T08:00:00+00:00")


# ── parse_targets_csv ─────────────────────────────────────────

class TestParseTargetsCsv(unittest.TestCase):
    def _write_csv(self, rows, tmpdir):
        path = os.path.join(tmpdir, "targets.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)
        return path

    def test_valid_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = self._write_csv([
                ["email", "first_name", "last_name", "position"],
                ["alice@corp.com", "Alice", "Smith", "Engineer"],
                ["bob@corp.com", "Bob", "Jones", "Manager"],
                ["carol@corp.com", "Carol", "Lee", "Director"],
            ], tmpdir)
            targets = parse_targets_csv(path)
            self.assertEqual(len(targets), 3)
            self.assertEqual(targets[0]["email"], "alice@corp.com")
            self.assertEqual(targets[1]["first_name"], "Bob")
            self.assertEqual(targets[2]["position"], "Director")

    def test_missing_column_raises(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = self._write_csv([
                ["email", "first_name", "last_name"],
                ["a@b.com", "A", "B"],
            ], tmpdir)
            with self.assertRaises(ValueError) as ctx:
                parse_targets_csv(path)
            self.assertIn("position", str(ctx.exception))

    def test_empty_file_raises(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = self._write_csv([
                ["email", "first_name", "last_name", "position"],
            ], tmpdir)
            with self.assertRaises(ValueError) as ctx:
                parse_targets_csv(path)
            self.assertIn("no data rows", str(ctx.exception))

    def test_strips_whitespace(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = self._write_csv([
                ["email", "first_name", "last_name", "position"],
                [" alice@corp.com ", " Alice ", " Smith ", " Engineer "],
            ], tmpdir)
            targets = parse_targets_csv(path)
            self.assertEqual(targets[0]["email"], "alice@corp.com")
            self.assertEqual(targets[0]["first_name"], "Alice")


# ── Config ────────────────────────────────────────────────────

class TestConfig(unittest.TestCase):
    def test_save_and_load_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                save_gophish_config("https://test:3333", "mykey", verify_ssl=False)
                result = load_gophish_config()
            self.assertEqual(result["api_url"], "https://test:3333")
            self.assertEqual(result["api_key"], "mykey")
            self.assertFalse(result["verify_ssl"])

    def test_env_vars_override_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                save_gophish_config("https://file:3333", "filekey")
                env = {
                    "REDTEXT_GOPHISH_URL": "https://env:4444",
                    "REDTEXT_GOPHISH_KEY": "envkey",
                }
                with patch.dict(os.environ, env):
                    result = load_gophish_config()
            self.assertEqual(result["api_url"], "https://env:4444")
            self.assertEqual(result["api_key"], "envkey")

    def test_cli_args_override_all(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                save_gophish_config("https://file:3333", "filekey")
                args = MagicMock()
                args.gophish_url = "https://cli:5555"
                args.gophish_key = "clikey"
                args.no_verify_ssl = True
                result = load_gophish_config(args)
            self.assertEqual(result["api_url"], "https://cli:5555")
            self.assertEqual(result["api_key"], "clikey")
            self.assertFalse(result["verify_ssl"])

    def test_missing_key_raises_valueerror(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "nonexistent", "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                with patch.dict(os.environ, {}, clear=True):
                    with self.assertRaises(ValueError) as ctx:
                        load_gophish_config()
                    self.assertIn("api_url", str(ctx.exception))
                    self.assertIn("api_key", str(ctx.exception))

    def test_verify_ssl_false_env(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                save_gophish_config("https://t:3333", "k", verify_ssl=True)
                env = {"REDTEXT_GOPHISH_VERIFY_SSL": "false"}
                with patch.dict(os.environ, env):
                    result = load_gophish_config()
            self.assertFalse(result["verify_ssl"])

    def test_verify_ssl_zero_env(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                save_gophish_config("https://t:3333", "k")
                with patch.dict(os.environ, {"REDTEXT_GOPHISH_VERIFY_SSL": "0"}):
                    result = load_gophish_config()
            self.assertFalse(result["verify_ssl"])

    def test_config_creates_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "sub", "dir", "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                path = save_gophish_config("https://t:3333", "k")
            self.assertTrue(os.path.isfile(path))

    def test_get_config_path_returns_string(self):
        path = get_config_path()
        self.assertIsInstance(path, str)
        self.assertTrue(path.endswith("config.ini"))


# ── CLI Integration ───────────────────────────────────────────

class TestGophishCLI(unittest.TestCase):
    def test_gophish_no_subcommand(self):
        with patch("sys.argv", ["redtext-gen", "--no-banner", "gophish"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_out:
                from redtext_generator.__main__ import main
                main()
            output = mock_out.getvalue()
            self.assertIn("gophish --help", output)

    def test_gophish_setup_saves_config(self):
        with patch("sys.argv", ["redtext-gen", "--no-banner", "gophish", "setup"]):
            with patch("builtins.input", side_effect=["https://test:3333", "mykey", "y"]):
                with patch("redtext_generator.config.save_gophish_config", return_value="/tmp/config.ini") as mock_save:
                    with patch("sys.stdout", new_callable=StringIO):
                        from redtext_generator.__main__ import main
                        main()
                mock_save.assert_called_once_with("https://test:3333", "mykey", True)

    @patch("urllib.request.urlopen")
    def test_gophish_push_creates_template(self, mock_urlopen):
        mock_urlopen.return_value = _mock_response({"id": 99, "name": "Pushed"})

        with tempfile.TemporaryDirectory() as tmpdir:
            fake_path = os.path.join(tmpdir, "config.ini")
            with patch("redtext_generator.config.get_config_path", return_value=fake_path):
                save_gophish_config("https://test:3333", "testkey", verify_ssl=False)
                with patch("sys.argv", [
                    "redtext-gen", "--no-banner", "gophish", "push",
                    "--industry", "tech", "--seed", "42",
                ]):
                    with patch("sys.stdout", new_callable=StringIO) as mock_out:
                        from redtext_generator.__main__ import main
                        main()
                    output = mock_out.getvalue()
                    self.assertIn("Template created", output)

        self.assertTrue(mock_urlopen.called)
        req = mock_urlopen.call_args[0][0]
        self.assertEqual(req.method, "POST")
        self.assertIn("/api/templates/", req.full_url)


if __name__ == "__main__":
    unittest.main()
