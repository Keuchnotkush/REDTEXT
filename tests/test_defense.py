"""Tests for the blue-team defense playbook module and CLI command."""

import json
import os
import tempfile
import unittest
from io import StringIO
from unittest.mock import patch

from redtext_generator.defense import (
    build_defense_playbook,
    data_sources_for,
    _base_technique_id,
    _dedupe,
    TECHNIQUE_DATA_SOURCES,
    VECTOR_RED_FLAGS,
    VECTOR_RESPONSE,
    _DEFAULT_DATA_SOURCES,
)
from redtext_generator.formatters import format_defense_playbook, export_html, export_markdown
from redtext_generator.generator import RedtextGenerator
from redtext_generator.__main__ import main


SINGLE_VECTORS = [
    ("phishing", "generate_phishing_email", "phishing_email"),
    ("smishing", "generate_smishing_message", "smishing"),
    ("quishing", "generate_quishing_scenario", "quishing"),
    ("vishing", "generate_vishing_script", "vishing_script"),
    ("physical", "generate_physical_pretext", "physical_pretext"),
    ("recon", "generate_recon_plan", "recon"),
    ("c2", "generate_c2_scenario", "c2"),
]


class TestHelpers(unittest.TestCase):
    def test_base_technique_id_strips_subtechnique(self):
        self.assertEqual(_base_technique_id("T1566.002"), "T1566")
        self.assertEqual(_base_technique_id("T1078"), "T1078")

    def test_dedupe_preserves_order(self):
        self.assertEqual(_dedupe(["a", "b", "a", "c", "b"]), ["a", "b", "c"])

    def test_data_sources_maps_known_prefix(self):
        sources = data_sources_for([("T1566.002", "Phishing: Spearphishing Link")])
        self.assertEqual(sources, TECHNIQUE_DATA_SOURCES["T1566"])

    def test_data_sources_dedupes_across_techniques(self):
        # Two T1566 sub-techniques should not duplicate the same sources.
        sources = data_sources_for([
            ("T1566.001", "a"),
            ("T1566.002", "b"),
        ])
        self.assertEqual(sources, TECHNIQUE_DATA_SOURCES["T1566"])

    def test_data_sources_falls_back_for_unknown(self):
        sources = data_sources_for([("T9999", "Unknown Technique")])
        self.assertEqual(sources, _DEFAULT_DATA_SOURCES)

    def test_data_sources_empty_falls_back(self):
        self.assertEqual(data_sources_for([]), _DEFAULT_DATA_SOURCES)


class TestBuildSingleVectors(unittest.TestCase):
    def test_each_single_vector_builds_a_playbook(self):
        gen = RedtextGenerator(company_name="Acme Corp")
        for _mode, method, expected_type in SINGLE_VECTORS:
            scenario = getattr(gen, method)()
            self.assertEqual(scenario["type"], expected_type)
            pb = build_defense_playbook(scenario)
            self.assertEqual(pb["type"], "defense_playbook")
            self.assertEqual(pb["vector"], expected_type)
            self.assertTrue(pb["techniques"], f"no techniques for {expected_type}")
            self.assertTrue(pb["data_sources"], f"no data sources for {expected_type}")
            self.assertTrue(pb["detection_controls"], f"no controls for {expected_type}")
            self.assertTrue(pb["known_gaps"], f"no gaps for {expected_type}")
            self.assertTrue(pb["awareness_points"])

    def test_red_flags_match_vector(self):
        gen = RedtextGenerator()
        scenario = gen.generate_phishing_email()
        pb = build_defense_playbook(scenario)
        self.assertEqual(pb["user_red_flags"], VECTOR_RED_FLAGS["phishing_email"])
        self.assertEqual(pb["response_steps"], VECTOR_RESPONSE["phishing_email"])

    def test_target_company_carried_through(self):
        gen = RedtextGenerator(company_name="Globex")
        pb = build_defense_playbook(gen.generate_phishing_email())
        self.assertEqual(pb["target_company"], "Globex")


class TestBuildFullScenario(unittest.TestCase):
    def setUp(self):
        self.gen = RedtextGenerator(company_name="Initech")
        self.full = self.gen.generate_full_scenario()
        self.pb = build_defense_playbook(self.full)

    def test_full_vector_label(self):
        self.assertEqual(self.pb["vector"], "full")
        self.assertEqual(self.pb["target_company"], "Initech")

    def test_full_aggregates_multiple_techniques(self):
        self.assertGreater(len(self.pb["techniques"]), 2)

    def test_full_aggregates_response_across_vectors(self):
        # Full scenario spans phishing, smishing, vishing, physical — its
        # response steps should include steps unique to more than one vector.
        steps = set(self.pb["response_steps"])
        self.assertTrue(set(VECTOR_RESPONSE["phishing_email"]) & steps)
        self.assertTrue(set(VECTOR_RESPONSE["physical_pretext"]) & steps)

    def test_full_tactic_is_a_chain(self):
        self.assertIn("→", self.pb["tactic"])

    def test_no_duplicate_response_steps(self):
        steps = self.pb["response_steps"]
        self.assertEqual(len(steps), len(set(steps)))


class TestEmptyScenario(unittest.TestCase):
    def test_minimal_scenario_still_builds(self):
        pb = build_defense_playbook({"type": "phishing_email"})
        self.assertEqual(pb["vector"], "phishing_email")
        self.assertEqual(pb["data_sources"], _DEFAULT_DATA_SOURCES)
        self.assertEqual(pb["target_company"], "the target organization")


class TestFormatting(unittest.TestCase):
    def setUp(self):
        self.pb = build_defense_playbook(RedtextGenerator().generate_quishing_scenario())

    def test_terminal_format_contains_sections(self):
        out = format_defense_playbook(self.pb)
        self.assertIn("BLUE TEAM DEFENSE PLAYBOOK", out)
        self.assertIn("TELEMETRY TO COLLECT", out)
        self.assertIn("INCIDENT RESPONSE STEPS", out)
        self.assertIn("USER RED FLAGS", out)

    def test_html_export_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            path = export_html(self.pb, os.path.join(d, "pb.html"))
            html = open(path, encoding="utf-8").read()
        self.assertIn("BLUE TEAM DEFENSE PLAYBOOK", html)
        self.assertIn("<!DOCTYPE html>", html)

    def test_markdown_export_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            path = export_markdown(self.pb, os.path.join(d, "pb.md"))
            md = open(path, encoding="utf-8").read()
        self.assertIn("DEFENSE PLAYBOOK", md)


class TestDefenseCLI(unittest.TestCase):
    def test_defense_full_runs(self):
        argv = ["redtext-gen", "--no-banner", "--no-disclaimer", "defense", "--mode", "full", "-s", "1"]
        with patch("sys.argv", argv):
            with patch("sys.stdout", new_callable=StringIO) as out:
                main()
        self.assertIn("DEFENSE PLAYBOOK", out.getvalue())

    def test_defense_single_mode_runs(self):
        argv = ["redtext-gen", "--no-banner", "--no-disclaimer", "defense", "--mode", "vishing"]
        with patch("sys.argv", argv):
            with patch("sys.stdout", new_callable=StringIO) as out:
                main()
        self.assertIn("DEFENSE PLAYBOOK", out.getvalue())

    def test_defense_exports_json(self):
        with tempfile.TemporaryDirectory() as d:
            target = os.path.join(d, "pb.json")
            argv = ["redtext-gen", "--no-banner", "--no-disclaimer", "defense",
                    "--mode", "phishing", "-s", "2", "--export-json", target]
            with patch("sys.argv", argv):
                with patch("sys.stdout", new_callable=StringIO):
                    main()
            with open(target, encoding="utf-8") as f:
                data = json.load(f)
        self.assertEqual(data["type"], "defense_playbook")
        self.assertEqual(data["vector"], "phishing_email")


if __name__ == "__main__":
    unittest.main()
