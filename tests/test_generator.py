"""Tests for the core generator engine."""

import re
import random
import unittest
import datetime
from unittest.mock import patch

from redtext_generator.generator import (
    _random_id,
    _random_name,
    _get_quarter,
    _random_date_near,
    _build_signature,
    RedtextGenerator,
)
from redtext_generator.templates import INDUSTRIES, PERSONAS, URGENCY_TRIGGERS


# ── Helper function tests ─────────────────────────────────────

class TestRandomId(unittest.TestCase):
    def test_default_length(self):
        result = _random_id()
        self.assertEqual(len(result), 6)

    def test_custom_length(self):
        for length in (1, 4, 10, 20):
            result = _random_id(length)
            self.assertEqual(len(result), length)

    def test_digits_only(self):
        result = _random_id(50)
        self.assertTrue(result.isdigit())


class TestRandomName(unittest.TestCase):
    def test_format(self):
        name = _random_name()
        parts = name.split()
        self.assertEqual(len(parts), 2, f"Expected 'First Last', got '{name}'")

    def test_non_empty_parts(self):
        name = _random_name()
        first, last = name.split()
        self.assertTrue(len(first) > 0)
        self.assertTrue(len(last) > 0)


class TestGetQuarter(unittest.TestCase):
    def test_q1(self):
        for month in (1, 2, 3):
            with patch("redtext_generator.generator.datetime") as mock_dt:
                mock_dt.datetime.now.return_value = datetime.datetime(2025, month, 15)
                mock_dt.timedelta = datetime.timedelta
                self.assertEqual(_get_quarter(), "q1")

    def test_q2(self):
        for month in (4, 5, 6):
            with patch("redtext_generator.generator.datetime") as mock_dt:
                mock_dt.datetime.now.return_value = datetime.datetime(2025, month, 15)
                mock_dt.timedelta = datetime.timedelta
                self.assertEqual(_get_quarter(), "q2")

    def test_q3(self):
        for month in (7, 8, 9):
            with patch("redtext_generator.generator.datetime") as mock_dt:
                mock_dt.datetime.now.return_value = datetime.datetime(2025, month, 15)
                mock_dt.timedelta = datetime.timedelta
                self.assertEqual(_get_quarter(), "q3")

    def test_q4(self):
        for month in (10, 11, 12):
            with patch("redtext_generator.generator.datetime") as mock_dt:
                mock_dt.datetime.now.return_value = datetime.datetime(2025, month, 15)
                mock_dt.timedelta = datetime.timedelta
                self.assertEqual(_get_quarter(), "q4")


class TestRandomDateNear(unittest.TestCase):
    def test_parseable_date(self):
        date_str = _random_date_near()
        parsed = datetime.datetime.strptime(date_str, "%B %d, %Y")
        self.assertIsInstance(parsed, datetime.datetime)

    def test_within_range(self):
        now = datetime.datetime.now()
        date_str = _random_date_near()
        parsed = datetime.datetime.strptime(date_str, "%B %d, %Y")
        delta = (parsed - now).days
        self.assertGreaterEqual(delta, 0)  # at least today (offset=1, but day boundary)
        self.assertLessEqual(delta, 15)    # at most 14 days + day boundary


class TestBuildSignature(unittest.TestCase):
    def test_contains_title_and_company(self):
        sig = _build_signature("IT Manager", "TestCo")
        self.assertIn("IT Manager", sig)
        self.assertIn("TestCo", sig)

    def test_contains_phone_number(self):
        sig = _build_signature("Analyst", "Corp")
        self.assertRegex(sig, r"\+1 \(\d{3}\) \d{3}-\d{4}")

    def test_contains_name(self):
        sig = _build_signature("Role", "Co")
        lines = sig.strip().split("\n")
        self.assertTrue(len(lines) >= 4, "Signature should have name, title, company, phone")


# ── Constructor tests ──────────────────────────────────────────

class TestRedtextGeneratorInit(unittest.TestCase):
    def test_valid_defaults(self):
        gen = RedtextGenerator()
        self.assertEqual(gen.industry_key, "tech")
        self.assertEqual(gen.persona_key, "it_support")
        self.assertEqual(gen.urgency, "medium")
        self.assertEqual(gen.company_name, "Target Corp")

    def test_all_industries_accepted(self):
        for industry in INDUSTRIES:
            gen = RedtextGenerator(industry=industry)
            self.assertEqual(gen.industry_key, industry)

    def test_all_personas_accepted(self):
        for persona in PERSONAS:
            gen = RedtextGenerator(persona=persona)
            self.assertEqual(gen.persona_key, persona)

    def test_all_urgency_levels_accepted(self):
        for urgency in URGENCY_TRIGGERS:
            gen = RedtextGenerator(urgency=urgency)
            self.assertEqual(gen.urgency, urgency)

    def test_invalid_industry_raises(self):
        with self.assertRaises(ValueError):
            RedtextGenerator(industry="doesnotexist")

    def test_invalid_persona_raises(self):
        with self.assertRaises(ValueError):
            RedtextGenerator(persona="doesnotexist")

    def test_invalid_urgency_raises(self):
        with self.assertRaises(ValueError):
            RedtextGenerator(urgency="doesnotexist")

    def test_custom_company_name(self):
        gen = RedtextGenerator(company_name="Acme Inc")
        self.assertEqual(gen.company_name, "Acme Inc")


# ── Phishing generation tests ─────────────────────────────────

class TestGeneratePhishingEmail(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        self.gen = RedtextGenerator()

    def test_required_keys(self):
        result = self.gen.generate_phishing_email()
        for key in ("type", "template", "subject", "body", "target", "attacker_persona", "urgency_level"):
            self.assertIn(key, result, f"Missing key: {key}")

    def test_target_keys(self):
        result = self.gen.generate_phishing_email()
        for key in ("name", "department", "company"):
            self.assertIn(key, result["target"], f"Missing target key: {key}")

    def test_type_value(self):
        result = self.gen.generate_phishing_email()
        self.assertEqual(result["type"], "phishing_email")

    def test_company_name_in_target(self):
        gen = RedtextGenerator(company_name="TestCorp")
        result = gen.generate_phishing_email()
        self.assertEqual(result["target"]["company"], "TestCorp")

    def test_no_leftover_placeholders_in_subject(self):
        for _ in range(20):
            result = self.gen.generate_phishing_email()
            self.assertNotRegex(result["subject"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in subject: {result['subject']}")

    def test_no_leftover_placeholders_in_body(self):
        for _ in range(20):
            result = self.gen.generate_phishing_email()
            self.assertNotRegex(result["body"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in body: {result['body']}")

    def test_specific_template_id(self):
        result = self.gen.generate_phishing_email(template_id="credential_harvest")
        self.assertEqual(result["template"], "Credential Harvesting")

    def test_invalid_template_id_no_crash(self):
        result = self.gen.generate_phishing_email(template_id="nonexistent_template")
        self.assertIn("type", result)

    def test_seed_determinism(self):
        random.seed(99)
        result1 = RedtextGenerator().generate_phishing_email()
        random.seed(99)
        result2 = RedtextGenerator().generate_phishing_email()
        self.assertEqual(result1["subject"], result2["subject"])
        self.assertEqual(result1["body"], result2["body"])

    def test_all_industries(self):
        for industry in INDUSTRIES:
            gen = RedtextGenerator(industry=industry)
            result = gen.generate_phishing_email()
            self.assertEqual(result["type"], "phishing_email")


# ── Vishing generation tests ──────────────────────────────────

class TestGenerateVishingScript(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        self.gen = RedtextGenerator()

    def test_required_keys(self):
        result = self.gen.generate_vishing_script()
        for key in ("type", "template", "caller", "target", "manager", "script",
                     "urgency_level", "recommended_principles", "preparation_notes"):
            self.assertIn(key, result, f"Missing key: {key}")

    def test_script_sections(self):
        result = self.gen.generate_vishing_script()
        for section in ("opening", "escalation", "objective", "red_flags_to_avoid"):
            self.assertIn(section, result["script"], f"Missing script section: {section}")

    def test_type_value(self):
        result = self.gen.generate_vishing_script()
        self.assertEqual(result["type"], "vishing_script")

    def test_no_leftover_placeholders(self):
        for _ in range(20):
            result = self.gen.generate_vishing_script()
            for section_name, section_text in result["script"].items():
                self.assertNotRegex(section_text, r"\{[a-z_]+\}",
                                    f"Leftover placeholder in {section_name}: {section_text}")

    def test_specific_script_id(self):
        result = self.gen.generate_vishing_script(script_id="it_support_call")
        self.assertEqual(result["template"], "IT Support Call")

    def test_invalid_script_id_no_crash(self):
        result = self.gen.generate_vishing_script(script_id="nonexistent")
        self.assertIn("type", result)

    def test_target_keys(self):
        result = self.gen.generate_vishing_script()
        for key in ("name", "department", "company"):
            self.assertIn(key, result["target"])

    def test_preparation_notes_non_empty(self):
        result = self.gen.generate_vishing_script()
        self.assertIsInstance(result["preparation_notes"], list)
        self.assertTrue(len(result["preparation_notes"]) > 0)


# ── Physical pretext tests ─────────────────────────────────────

class TestGeneratePhysicalPretext(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        self.gen = RedtextGenerator()

    def test_required_keys(self):
        result = self.gen.generate_physical_pretext()
        for key in ("type", "template", "operator", "script", "target_areas",
                     "objectives", "urgency_level", "preparation_notes"):
            self.assertIn(key, result, f"Missing key: {key}")

    def test_operator_keys(self):
        result = self.gen.generate_physical_pretext()
        for key in ("name", "cover_identity", "appearance", "props"):
            self.assertIn(key, result["operator"], f"Missing operator key: {key}")

    def test_type_value(self):
        result = self.gen.generate_physical_pretext()
        self.assertEqual(result["type"], "physical_pretext")

    def test_no_leftover_placeholders(self):
        for _ in range(20):
            result = self.gen.generate_physical_pretext()
            self.assertNotRegex(result["script"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in script: {result['script']}")

    def test_specific_pretext_id(self):
        result = self.gen.generate_physical_pretext(pretext_id="hvac_technician")
        self.assertEqual(result["template"], "HVAC Technician")

    def test_invalid_pretext_id_no_crash(self):
        result = self.gen.generate_physical_pretext(pretext_id="nonexistent")
        self.assertIn("type", result)

    def test_props_is_list(self):
        result = self.gen.generate_physical_pretext()
        self.assertIsInstance(result["operator"]["props"], list)
        self.assertTrue(len(result["operator"]["props"]) > 0)

    def test_target_areas_non_empty(self):
        result = self.gen.generate_physical_pretext()
        self.assertIsInstance(result["target_areas"], list)
        self.assertTrue(len(result["target_areas"]) > 0)


# ── Full scenario tests ────────────────────────────────────────

class TestGenerateFullScenario(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        self.gen = RedtextGenerator()

    def test_required_keys(self):
        result = self.gen.generate_full_scenario()
        for key in ("operation_name", "quarter", "target_company", "industry",
                     "seasonal_hook", "phishing", "social", "physical",
                     "recon_tasks", "opsec_notes"):
            self.assertIn(key, result, f"Missing key: {key}")

    def test_operation_name_format(self):
        result = self.gen.generate_full_scenario()
        self.assertTrue(result["operation_name"].startswith("Operation "))
        parts = result["operation_name"].split()
        self.assertEqual(len(parts), 3, f"Expected 'Operation WORD WORD', got '{result['operation_name']}'")

    def test_sub_scenarios_have_type(self):
        result = self.gen.generate_full_scenario()
        self.assertEqual(result["phishing"]["type"], "phishing_email")
        self.assertEqual(result["social"]["type"], "vishing_script")
        self.assertEqual(result["physical"]["type"], "physical_pretext")

    def test_company_propagated(self):
        gen = RedtextGenerator(company_name="AcmeCo")
        result = gen.generate_full_scenario()
        self.assertEqual(result["target_company"], "AcmeCo")
        self.assertEqual(result["phishing"]["target"]["company"], "AcmeCo")

    def test_recon_tasks_non_empty(self):
        result = self.gen.generate_full_scenario()
        self.assertIsInstance(result["recon_tasks"], list)
        self.assertTrue(len(result["recon_tasks"]) > 0)

    def test_opsec_notes_non_empty(self):
        result = self.gen.generate_full_scenario()
        self.assertIsInstance(result["opsec_notes"], list)
        self.assertTrue(len(result["opsec_notes"]) > 0)

    def test_quarter_valid(self):
        result = self.gen.generate_full_scenario()
        self.assertIn(result["quarter"], ("q1", "q2", "q3", "q4"))


# ── Smishing generation tests ────────────────────────────────

class TestGenerateSmishingMessage(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        self.gen = RedtextGenerator()

    def test_required_keys(self):
        result = self.gen.generate_smishing_message()
        for key in ("type", "template", "message", "target", "attacker_persona",
                     "urgency_level", "short_code", "malicious_link"):
            self.assertIn(key, result, f"Missing key: {key}")

    def test_target_keys(self):
        result = self.gen.generate_smishing_message()
        for key in ("name", "department", "company"):
            self.assertIn(key, result["target"], f"Missing target key: {key}")

    def test_type_value(self):
        result = self.gen.generate_smishing_message()
        self.assertEqual(result["type"], "smishing")

    def test_company_name_in_target(self):
        gen = RedtextGenerator(company_name="TestCorp")
        result = gen.generate_smishing_message()
        self.assertEqual(result["target"]["company"], "TestCorp")

    def test_no_leftover_placeholders(self):
        for _ in range(20):
            result = self.gen.generate_smishing_message()
            self.assertNotRegex(result["message"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in message: {result['message']}")

    def test_specific_template_id(self):
        result = self.gen.generate_smishing_message(template_id="account_verify")
        self.assertEqual(result["template"], "Account Verification")

    def test_invalid_template_id_no_crash(self):
        result = self.gen.generate_smishing_message(template_id="nonexistent_template")
        self.assertIn("type", result)

    def test_seed_determinism(self):
        random.seed(99)
        result1 = RedtextGenerator().generate_smishing_message()
        random.seed(99)
        result2 = RedtextGenerator().generate_smishing_message()
        self.assertEqual(result1["message"], result2["message"])

    def test_all_industries(self):
        for industry in INDUSTRIES:
            gen = RedtextGenerator(industry=industry)
            result = gen.generate_smishing_message()
            self.assertEqual(result["type"], "smishing")

    def test_short_code_is_numeric(self):
        result = self.gen.generate_smishing_message()
        self.assertTrue(result["short_code"].isdigit())

    def test_malicious_link_is_url(self):
        result = self.gen.generate_smishing_message()
        self.assertTrue(result["malicious_link"].startswith("https://"))


if __name__ == "__main__":
    unittest.main()
