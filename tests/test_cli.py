"""Tests for CLI argument parsing and command dispatch."""

import io
import unittest
from io import StringIO
from unittest.mock import patch

from redtext_generator.__main__ import main


class TestCLIEncoding(unittest.TestCase):
    def test_banner_survives_legacy_codepage(self):
        # Simulate a stock Windows console: stdout backed by cp1252 with strict
        # errors. Without the UTF-8 reconfigure in main(), printing the banner
        # (box-drawing/block characters) would raise UnicodeEncodeError.
        legacy = io.TextIOWrapper(io.BytesIO(), encoding="cp1252", errors="strict")
        with patch("sys.argv", ["redtext-gen", "list"]):
            with patch("sys.stdout", legacy):
                main()  # must not raise UnicodeEncodeError


class TestCLINoArgs(unittest.TestCase):
    def test_no_args_exits(self):
        with patch("sys.argv", ["redtext-gen"]):
            with patch("sys.stdout", new_callable=StringIO):
                with self.assertRaises(SystemExit) as ctx:
                    main()
                self.assertEqual(ctx.exception.code, 0)


class TestCLIListCommand(unittest.TestCase):
    def test_list_runs(self):
        with patch("sys.argv", ["redtext-gen", "list"]):
            with patch("sys.stdout", new_callable=StringIO):
                main()  # should not raise


class TestCLIPhishingCommand(unittest.TestCase):
    def test_default_phishing(self):
        with patch("sys.argv", ["redtext-gen", "--no-banner", "--no-disclaimer", "phishing"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_out:
                main()
            output = mock_out.getvalue()
            self.assertTrue(len(output) > 0)

    def test_phishing_with_options(self):
        with patch("sys.argv", [
            "redtext-gen", "--no-banner", "--no-disclaimer", "phishing",
            "--industry", "finance",
            "--urgency", "high",
            "--persona", "executive",
            "--company", "TestBank",
        ]):
            with patch("sys.stdout", new_callable=StringIO) as mock_out:
                main()
            output = mock_out.getvalue()
            self.assertTrue(len(output) > 0)


class TestCLIVishingCommand(unittest.TestCase):
    def test_default_vishing(self):
        with patch("sys.argv", ["redtext-gen", "--no-banner", "--no-disclaimer", "vishing"]):
            with patch("sys.stdout", new_callable=StringIO):
                main()


class TestCLIPhysicalCommand(unittest.TestCase):
    def test_default_physical(self):
        with patch("sys.argv", ["redtext-gen", "--no-banner", "--no-disclaimer", "physical"]):
            with patch("sys.stdout", new_callable=StringIO):
                main()


class TestCLIFullCommand(unittest.TestCase):
    def test_default_full(self):
        with patch("sys.argv", ["redtext-gen", "--no-banner", "--no-disclaimer", "full"]):
            with patch("sys.stdout", new_callable=StringIO):
                main()


class TestCLISeedReproducibility(unittest.TestCase):
    def test_seed_produces_same_output(self):
        outputs = []
        for _ in range(2):
            with patch("sys.argv", [
                "redtext-gen", "--no-banner", "--no-disclaimer", "phishing",
                "--seed", "12345",
            ]):
                with patch("sys.stdout", new_callable=StringIO) as mock_out:
                    main()
                outputs.append(mock_out.getvalue())
        self.assertEqual(outputs[0], outputs[1])


if __name__ == "__main__":
    unittest.main()
