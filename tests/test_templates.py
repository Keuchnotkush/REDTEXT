"""Tests for template data integrity."""

import unittest

from redtext_generator.templates import (
    INDUSTRIES,
    PERSONAS,
    URGENCY_TRIGGERS,
    SEASONAL_HOOKS,
    PHISHING_TEMPLATES,
    VISHING_SCRIPTS,
    PHYSICAL_PRETEXTS,
    PSYCH_PRINCIPLES,
    FAKE_DOCUMENTS,
)


class TestIndustries(unittest.TestCase):
    REQUIRED_KEYS = {"name", "departments", "software", "jargon", "pain_points"}

    def test_at_least_one_industry(self):
        self.assertTrue(len(INDUSTRIES) > 0)

    def test_all_industries_have_required_keys(self):
        for key, data in INDUSTRIES.items():
            for req in self.REQUIRED_KEYS:
                self.assertIn(req, data, f"Industry '{key}' missing key '{req}'")

    def test_lists_are_non_empty(self):
        for key, data in INDUSTRIES.items():
            for field in ("departments", "software", "jargon", "pain_points"):
                self.assertTrue(len(data[field]) > 0,
                                f"Industry '{key}' has empty '{field}'")

    def test_name_is_string(self):
        for key, data in INDUSTRIES.items():
            self.assertIsInstance(data["name"], str)


class TestPersonas(unittest.TestCase):
    REQUIRED_KEYS = {"name", "titles", "pretexts"}

    def test_at_least_one_persona(self):
        self.assertTrue(len(PERSONAS) > 0)

    def test_all_personas_have_required_keys(self):
        for key, data in PERSONAS.items():
            for req in self.REQUIRED_KEYS:
                self.assertIn(req, data, f"Persona '{key}' missing key '{req}'")

    def test_lists_are_non_empty(self):
        for key, data in PERSONAS.items():
            self.assertTrue(len(data["titles"]) > 0, f"Persona '{key}' has no titles")
            self.assertTrue(len(data["pretexts"]) > 0, f"Persona '{key}' has no pretexts")


class TestUrgencyTriggers(unittest.TestCase):
    EXPECTED_LEVELS = {"low", "medium", "high", "critical"}

    def test_all_levels_present(self):
        for level in self.EXPECTED_LEVELS:
            self.assertIn(level, URGENCY_TRIGGERS, f"Missing urgency level: {level}")

    def test_each_level_non_empty(self):
        for level, triggers in URGENCY_TRIGGERS.items():
            self.assertIsInstance(triggers, list)
            self.assertTrue(len(triggers) > 0, f"Urgency level '{level}' has no triggers")

    def test_all_triggers_are_strings(self):
        for level, triggers in URGENCY_TRIGGERS.items():
            for t in triggers:
                self.assertIsInstance(t, str, f"Non-string trigger in '{level}'")


class TestSeasonalHooks(unittest.TestCase):
    EXPECTED_QUARTERS = {"q1", "q2", "q3", "q4"}

    def test_all_quarters_present(self):
        for q in self.EXPECTED_QUARTERS:
            self.assertIn(q, SEASONAL_HOOKS, f"Missing quarter: {q}")

    def test_each_quarter_non_empty(self):
        for q, hooks in SEASONAL_HOOKS.items():
            self.assertIsInstance(hooks, list)
            self.assertTrue(len(hooks) > 0, f"Quarter '{q}' has no hooks")


class TestPhishingTemplates(unittest.TestCase):
    REQUIRED_KEYS = {"id", "name", "subject_lines", "body"}

    def test_at_least_one_template(self):
        self.assertTrue(len(PHISHING_TEMPLATES) > 0)

    def test_all_templates_have_required_keys(self):
        for template in PHISHING_TEMPLATES:
            for req in self.REQUIRED_KEYS:
                self.assertIn(req, template,
                              f"Phishing template '{template.get('id', '?')}' missing key '{req}'")

    def test_subject_lines_non_empty(self):
        for template in PHISHING_TEMPLATES:
            self.assertTrue(len(template["subject_lines"]) > 0,
                            f"Template '{template['id']}' has no subject lines")

    def test_body_non_empty(self):
        for template in PHISHING_TEMPLATES:
            self.assertTrue(len(template["body"].strip()) > 0,
                            f"Template '{template['id']}' has empty body")

    def test_unique_ids(self):
        ids = [t["id"] for t in PHISHING_TEMPLATES]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate phishing template IDs found")


class TestVishingScripts(unittest.TestCase):
    REQUIRED_KEYS = {"id", "name", "opening", "escalation", "objective", "red_flags_to_avoid"}

    def test_at_least_one_script(self):
        self.assertTrue(len(VISHING_SCRIPTS) > 0)

    def test_all_scripts_have_required_keys(self):
        for script in VISHING_SCRIPTS:
            for req in self.REQUIRED_KEYS:
                self.assertIn(req, script,
                              f"Vishing script '{script.get('id', '?')}' missing key '{req}'")

    def test_unique_ids(self):
        ids = [s["id"] for s in VISHING_SCRIPTS]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate vishing script IDs found")

    def test_sections_non_empty(self):
        for script in VISHING_SCRIPTS:
            for section in ("opening", "escalation", "objective", "red_flags_to_avoid"):
                self.assertTrue(len(script[section].strip()) > 0,
                                f"Script '{script['id']}' has empty '{section}'")


class TestPhysicalPretexts(unittest.TestCase):
    REQUIRED_KEYS = {"id", "name", "appearance", "props", "script", "target_areas", "objectives"}

    def test_at_least_one_pretext(self):
        self.assertTrue(len(PHYSICAL_PRETEXTS) > 0)

    def test_all_pretexts_have_required_keys(self):
        for pretext in PHYSICAL_PRETEXTS:
            for req in self.REQUIRED_KEYS:
                self.assertIn(req, pretext,
                              f"Physical pretext '{pretext.get('id', '?')}' missing key '{req}'")

    def test_unique_ids(self):
        ids = [p["id"] for p in PHYSICAL_PRETEXTS]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate physical pretext IDs found")

    def test_props_non_empty(self):
        for pretext in PHYSICAL_PRETEXTS:
            self.assertTrue(len(pretext["props"]) > 0,
                            f"Pretext '{pretext['id']}' has no props")

    def test_target_areas_non_empty(self):
        for pretext in PHYSICAL_PRETEXTS:
            self.assertTrue(len(pretext["target_areas"]) > 0,
                            f"Pretext '{pretext['id']}' has no target areas")


class TestPsychPrinciples(unittest.TestCase):
    REQUIRED_KEYS = {"name", "description", "application", "example"}

    def test_at_least_one_principle(self):
        self.assertTrue(len(PSYCH_PRINCIPLES) > 0)

    def test_all_principles_have_required_keys(self):
        for key, data in PSYCH_PRINCIPLES.items():
            for req in self.REQUIRED_KEYS:
                self.assertIn(req, data, f"Principle '{key}' missing key '{req}'")

    def test_all_values_non_empty_strings(self):
        for key, data in PSYCH_PRINCIPLES.items():
            for field in self.REQUIRED_KEYS:
                self.assertIsInstance(data[field], str)
                self.assertTrue(len(data[field]) > 0,
                                f"Principle '{key}' has empty '{field}'")


class TestFakeDocuments(unittest.TestCase):
    def test_non_empty(self):
        self.assertTrue(len(FAKE_DOCUMENTS) > 0)

    def test_all_strings(self):
        for doc in FAKE_DOCUMENTS:
            self.assertIsInstance(doc, str)

    def test_all_have_extensions(self):
        for doc in FAKE_DOCUMENTS:
            self.assertRegex(doc, r"\.\w+$", f"Document '{doc}' has no file extension")


if __name__ == "__main__":
    unittest.main()
