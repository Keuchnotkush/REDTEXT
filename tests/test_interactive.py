"""Tests for the interactive TUI mode."""

import io
import os
import random
import tempfile
import unittest
from unittest.mock import patch, call

from redtext_generator.__main__ import (
    _menu_prompt,
    _text_prompt,
    _interactive_header,
    cmd_interactive,
    SCENARIO_TYPES,
)


# ── Menu prompt tests ─────────────────────────────────────────

class TestMenuPrompt(unittest.TestCase):
    @patch("builtins.input", return_value="1")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_valid_first_choice(self, mock_out, mock_input):
        result = _menu_prompt("Pick one", ["Alpha", "Beta", "Gamma"])
        self.assertEqual(result, 0)

    @patch("builtins.input", return_value="3")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_valid_last_choice(self, mock_out, mock_input):
        result = _menu_prompt("Pick one", ["A", "B", "C"])
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["0", "2"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_out_of_range_then_valid(self, mock_out, mock_input):
        result = _menu_prompt("Pick one", ["A", "B", "C"])
        self.assertEqual(result, 1)
        self.assertIn("Invalid choice", mock_out.getvalue())

    @patch("builtins.input", side_effect=["abc", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_non_numeric_then_valid(self, mock_out, mock_input):
        result = _menu_prompt("Pick one", ["X", "Y"])
        self.assertEqual(result, 0)
        self.assertIn("Invalid choice", mock_out.getvalue())

    @patch("builtins.input", side_effect=["5", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_too_high_then_valid(self, mock_out, mock_input):
        result = _menu_prompt("Pick", ["Only"])
        self.assertEqual(result, 0)

    @patch("builtins.input", side_effect=["", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_empty_input_then_valid(self, mock_out, mock_input):
        result = _menu_prompt("Pick", ["A", "B"])
        self.assertEqual(result, 0)
        self.assertIn("Invalid choice", mock_out.getvalue())

    @patch("builtins.input", side_effect=["  ", "2"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_whitespace_then_valid(self, mock_out, mock_input):
        result = _menu_prompt("Pick", ["A", "B"])
        self.assertEqual(result, 1)


# ── Text prompt tests ─────────────────────────────────────────

class TestTextPrompt(unittest.TestCase):
    @patch("builtins.input", return_value="Custom Corp")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_custom_value(self, mock_out, mock_input):
        result = _text_prompt("Company", "Default Co")
        self.assertEqual(result, "Custom Corp")

    @patch("builtins.input", return_value="")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_empty_returns_default(self, mock_out, mock_input):
        result = _text_prompt("Company", "Default Co")
        self.assertEqual(result, "Default Co")

    @patch("builtins.input", return_value="   ")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_whitespace_returns_default(self, mock_out, mock_input):
        result = _text_prompt("Company", "Default Co")
        self.assertEqual(result, "Default Co")


# ── Interactive header test ────────────────────────────────────

class TestInteractiveHeader(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_prints_header(self, mock_out):
        _interactive_header()
        output = mock_out.getvalue()
        self.assertIn("REDTEXT", output)
        self.assertIn("Interactive", output)


# ── Full interactive flow tests ────────────────────────────────

class TestInteractiveFlowPhishing(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "1",    # language: English
        "1",    # scenario: Phishing Email
        "1",    # industry: tech
        "1",    # urgency: low
        "1",    # persona: it_support
        "",     # company: default
        "5",    # action: Quit
    ])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_phishing_flow(self, mock_out, mock_input):
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)
        output = mock_out.getvalue()
        self.assertIn("REDTEXT", output)


class TestInteractiveFlowSmishing(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "1",    # language: English
        "2",    # scenario: Smishing
        "1",    # industry
        "1",    # urgency
        "1",    # persona
        "",     # company
        "5",    # Quit
    ])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_smishing_flow(self, mock_out, mock_input):
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)


class TestInteractiveFlowQuishing(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "1",    # language: English
        "3",    # scenario: Quishing
        "1", "1", "1", "",
        "",     # URL: blank for auto-generated
        "5",
    ])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_quishing_flow(self, mock_out, mock_input):
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)


class TestInteractiveFlowVishing(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "1",    # language: English
        "4",    # scenario: Vishing
        "1", "1", "1", "",
        "5",
    ])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_vishing_flow(self, mock_out, mock_input):
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)


class TestInteractiveFlowPhysical(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "1",    # language: English
        "5",    # scenario: Physical
        "1", "1", "1", "",
        "5",
    ])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_physical_flow(self, mock_out, mock_input):
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)


class TestInteractiveFlowFull(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "1",    # language: English
        "6",    # scenario: Full
        "1", "1", "1", "",
        "5",
    ])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_full_flow(self, mock_out, mock_input):
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)


# ── Export action tests ────────────────────────────────────────

class TestExportActions(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        for f in os.listdir(self.tmpdir):
            os.unlink(os.path.join(self.tmpdir, f))
        os.rmdir(self.tmpdir)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_export_json(self, mock_out, mock_input):
        path = os.path.join(self.tmpdir, "out.json")
        mock_input.side_effect = [
            "1",                     # language: English
            "1", "1", "1", "1", "",  # scenario config
            "1", path,               # Export JSON + filename
            "5",                     # Quit
        ]
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)
        self.assertTrue(os.path.exists(path))

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_export_markdown(self, mock_out, mock_input):
        path = os.path.join(self.tmpdir, "out.md")
        mock_input.side_effect = [
            "1",                     # language: English
            "1", "1", "1", "1", "",
            "2", path,
            "5",
        ]
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)
        self.assertTrue(os.path.exists(path))

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_export_html(self, mock_out, mock_input):
        path = os.path.join(self.tmpdir, "out.html")
        mock_input.side_effect = [
            "1",                     # language: English
            "1", "1", "1", "1", "",
            "3", path,
            "5",
        ]
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)
        self.assertTrue(os.path.exists(path))


# ── Regeneration test ──────────────────────────────────────────

class TestRegenerate(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "1",                       # language: English
        "1", "1", "1", "1", "",   # first scenario
        "4",                       # Generate Another
        "1",                       # language: English
        "1", "1", "1", "1", "",   # second scenario
        "5",                       # Quit
    ])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_generate_another(self, mock_out, mock_input):
        random.seed(42)
        args = type("Args", (), {"no_banner": True})()
        cmd_interactive(args)
        output = mock_out.getvalue()
        # Header printed twice (once per generation)
        self.assertEqual(output.count("Interactive Builder"), 2)


# ── Keyboard interrupt test ────────────────────────────────────

class TestKeyboardInterrupt(unittest.TestCase):
    @patch("builtins.input", side_effect=KeyboardInterrupt)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_ctrl_c_during_menu(self, mock_out, mock_input):
        args = type("Args", (), {"no_banner": True})()
        # cmd_interactive itself raises KeyboardInterrupt;
        # main() catches it, so test the raise here
        with self.assertRaises(KeyboardInterrupt):
            cmd_interactive(args)


if __name__ == "__main__":
    unittest.main()
