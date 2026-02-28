"""Tests for output formatters and file export."""

import json
import os
import random
import tempfile
import unittest

from redtext_generator.generator import RedtextGenerator
from redtext_generator.formatters import (
    _c,
    _strip_ansi,
    _header,
    _field,
    _list_items,
    format_phishing_email,
    format_vishing_script,
    format_physical_pretext,
    format_full_scenario,
    export_json,
    export_markdown,
    export_html,
    Colors,
)


# ── Helper function tests ─────────────────────────────────────

class TestColorHelper(unittest.TestCase):
    def test_wraps_text(self):
        result = _c("hello", Colors.RED)
        self.assertIn("hello", result)
        self.assertTrue(result.startswith(Colors.RED))
        self.assertTrue(result.endswith(Colors.RESET))

    def test_empty_text(self):
        result = _c("", Colors.GREEN)
        self.assertIn(Colors.GREEN, result)


class TestStripAnsi(unittest.TestCase):
    def test_strips_color_codes(self):
        colored = _c("plain text", Colors.RED)
        result = _strip_ansi(colored)
        self.assertEqual(result, "plain text")

    def test_no_ansi_passthrough(self):
        self.assertEqual(_strip_ansi("no colors here"), "no colors here")

    def test_multiple_codes(self):
        text = f"{Colors.BOLD}{Colors.RED}bold red{Colors.RESET} normal"
        result = _strip_ansi(text)
        self.assertEqual(result, "bold red normal")


class TestHeader(unittest.TestCase):
    def test_contains_title(self):
        result = _header("MY TITLE")
        clean = _strip_ansi(result)
        self.assertIn("MY TITLE", clean)

    def test_contains_separator(self):
        result = _header("TEST")
        clean = _strip_ansi(result)
        self.assertIn("═", clean)


class TestField(unittest.TestCase):
    def test_contains_label_and_value(self):
        result = _field("Name", "John")
        clean = _strip_ansi(result)
        self.assertIn("Name:", clean)
        self.assertIn("John", clean)

    def test_default_indent(self):
        result = _field("X", "Y")
        clean = _strip_ansi(result)
        self.assertTrue(clean.startswith("    "))


class TestListItems(unittest.TestCase):
    def test_bullet_per_item(self):
        items = ["alpha", "beta", "gamma"]
        result = _list_items(items)
        clean = _strip_ansi(result)
        for item in items:
            self.assertIn(item, clean)

    def test_empty_list(self):
        result = _list_items([])
        self.assertEqual(result, "")


# ── Format function tests ─────────────────────────────────────

class TestFormatPhishingEmail(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        gen = RedtextGenerator()
        self.data = gen.generate_phishing_email()

    def test_returns_string(self):
        result = format_phishing_email(self.data)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_contains_key_fields(self):
        result = format_phishing_email(self.data)
        clean = _strip_ansi(result)
        self.assertIn(self.data["template"], clean)
        self.assertIn(self.data["target"]["name"], clean)
        self.assertIn(self.data["subject"], clean)


class TestFormatVishingScript(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        gen = RedtextGenerator()
        self.data = gen.generate_vishing_script()

    def test_returns_string(self):
        result = format_vishing_script(self.data)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_contains_sections(self):
        result = format_vishing_script(self.data)
        clean = _strip_ansi(result)
        for section in ("OPENING", "ESCALATION", "OBJECTIVE", "RED FLAGS TO AVOID"):
            self.assertIn(section, clean)


class TestFormatPhysicalPretext(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        gen = RedtextGenerator()
        self.data = gen.generate_physical_pretext()

    def test_returns_string(self):
        result = format_physical_pretext(self.data)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_contains_operator_info(self):
        result = format_physical_pretext(self.data)
        clean = _strip_ansi(result)
        self.assertIn(self.data["operator"]["name"], clean)
        self.assertIn(self.data["template"], clean)


class TestFormatFullScenario(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        gen = RedtextGenerator()
        self.data = gen.generate_full_scenario()

    def test_returns_string(self):
        result = format_full_scenario(self.data)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_contains_phases(self):
        result = format_full_scenario(self.data)
        clean = _strip_ansi(result)
        self.assertIn("PHASE 1", clean)
        self.assertIn("PHASE 2", clean)
        self.assertIn("PHASE 3", clean)
        self.assertIn("PHASE 4", clean)

    def test_contains_operation_name(self):
        result = format_full_scenario(self.data)
        clean = _strip_ansi(result)
        self.assertIn(self.data["operation_name"], clean)


# ── Export function tests ──────────────────────────────────────

class TestExportJson(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        gen = RedtextGenerator()
        self.data = gen.generate_phishing_email()

    def test_writes_valid_json(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
            path = f.name
        try:
            export_json(self.data, path)
            with open(path, "r") as f:
                loaded = json.load(f)
            self.assertEqual(loaded["type"], "phishing_email")
            self.assertEqual(loaded["subject"], self.data["subject"])
        finally:
            os.unlink(path)

    def test_creates_directories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "sub", "dir", "out.json")
            export_json(self.data, path)
            self.assertTrue(os.path.exists(path))

    def test_returns_filepath(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        try:
            result = export_json(self.data, path)
            self.assertEqual(result, path)
        finally:
            os.unlink(path)


class TestExportMarkdown(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        gen = RedtextGenerator()
        self.data = gen.generate_phishing_email()

    def test_writes_file(self):
        with tempfile.NamedTemporaryFile(suffix=".md", delete=False, mode="w") as f:
            path = f.name
        try:
            export_markdown(self.data, path)
            self.assertTrue(os.path.exists(path))
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertTrue(len(content) > 0)
        finally:
            os.unlink(path)

    def test_contains_header(self):
        with tempfile.NamedTemporaryFile(suffix=".md", delete=False, mode="w") as f:
            path = f.name
        try:
            export_markdown(self.data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("# RedTEXT Generator Report", content)
        finally:
            os.unlink(path)

    def test_no_ansi_in_output(self):
        with tempfile.NamedTemporaryFile(suffix=".md", delete=False, mode="w") as f:
            path = f.name
        try:
            export_markdown(self.data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertNotRegex(content, r"\033\[")
        finally:
            os.unlink(path)

    def test_full_scenario_export(self):
        random.seed(42)
        gen = RedtextGenerator()
        full_data = gen.generate_full_scenario()
        with tempfile.NamedTemporaryFile(suffix=".md", delete=False, mode="w") as f:
            path = f.name
        try:
            export_markdown(full_data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("# RedTEXT Generator Report", content)
            self.assertNotRegex(content, r"\033\[")
        finally:
            os.unlink(path)

    def test_returns_filepath(self):
        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as f:
            path = f.name
        try:
            result = export_markdown(self.data, path)
            self.assertEqual(result, path)
        finally:
            os.unlink(path)


class TestExportHtml(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        gen = RedtextGenerator()
        self.data = gen.generate_phishing_email()

    def test_writes_file(self):
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(self.data, path)
            self.assertTrue(os.path.exists(path))
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertTrue(len(content) > 0)
        finally:
            os.unlink(path)

    def test_contains_html_structure(self):
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(self.data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("<!DOCTYPE html>", content)
            self.assertIn("<html", content)
            self.assertIn("</html>", content)
            self.assertIn("<style>", content)
            self.assertIn("REDTEXT", content)
        finally:
            os.unlink(path)

    def test_no_ansi_in_output(self):
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(self.data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertNotRegex(content, r"\033\[")
        finally:
            os.unlink(path)

    def test_phishing_has_email_preview(self):
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(self.data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("email-preview", content)
            self.assertIn(self.data["subject"], content)
            self.assertIn("From:", content)
            self.assertIn("To:", content)
        finally:
            os.unlink(path)

    def test_html_escapes_special_chars(self):
        self.data["subject"] = '<script>alert("xss")</script>'
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(self.data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertNotIn("<script>", content)
            self.assertIn("&lt;script&gt;", content)
        finally:
            os.unlink(path)

    def test_full_scenario_export(self):
        random.seed(42)
        gen = RedtextGenerator()
        full_data = gen.generate_full_scenario()
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(full_data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("<!DOCTYPE html>", content)
            self.assertIn(full_data["operation_name"], content)
            self.assertIn("PHASE 1", content)
            self.assertIn("PHASE 2", content)
        finally:
            os.unlink(path)

    def test_smishing_export(self):
        random.seed(42)
        gen = RedtextGenerator()
        data = gen.generate_smishing_message()
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("SMS/SMISHING", content)
            self.assertIn("<!DOCTYPE html>", content)
        finally:
            os.unlink(path)

    def test_quishing_export(self):
        random.seed(42)
        gen = RedtextGenerator()
        data = gen.generate_quishing_scenario()
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("QUISHING", content)
            self.assertIn("qr-block", content)
        finally:
            os.unlink(path)

    def test_vishing_export(self):
        random.seed(42)
        gen = RedtextGenerator()
        data = gen.generate_vishing_script()
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("VISHING", content)
            self.assertIn("OPENING", content)
        finally:
            os.unlink(path)

    def test_physical_export(self):
        random.seed(42)
        gen = RedtextGenerator()
        data = gen.generate_physical_pretext()
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
            path = f.name
        try:
            export_html(data, path)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("PHYSICAL", content)
            self.assertIn("PROPS", content)
        finally:
            os.unlink(path)

    def test_creates_directories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "sub", "dir", "out.html")
            export_html(self.data, path)
            self.assertTrue(os.path.exists(path))

    def test_returns_filepath(self):
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
            path = f.name
        try:
            result = export_html(self.data, path)
            self.assertEqual(result, path)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
