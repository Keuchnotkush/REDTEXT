"""Tests for MITRE ATT&CK integration in REDTEXT scenarios."""

import re
import random
import unittest

from redtext_generator.mitre import (
    ATTACK_PHASES,
    PHASE_TO_SCENARIO,
    SCENARIO_TECHNIQUES,
    get_mitre_data,
    get_phase_scenario_type,
)
from redtext_generator.generator import RedtextGenerator


# ── Test mitre.py module directly ─────────────────────────────

class TestMitreModule(unittest.TestCase):
    """Test the mitre.py module's data structures and public API."""

    def setUp(self):
        random.seed(42)

    # -- get_mitre_data returns valid data for all known combos --

    def test_get_mitre_data_all_phishing_templates(self):
        """All phishing_email template_ids return valid MITRE data."""
        template_ids = [
            "credential_harvest", "malicious_attachment", "bec_wire",
            "callback_phishing", "supply_chain", "credential_breach",
        ]
        for tid in template_ids:
            data = get_mitre_data("phishing_email", tid)
            self.assertIn("techniques", data, f"Missing 'techniques' for phishing_email/{tid}")
            self.assertIn("tactic", data, f"Missing 'tactic' for phishing_email/{tid}")
            self.assertIn("detection", data, f"Missing 'detection' for phishing_email/{tid}")

    def test_get_mitre_data_all_smishing_templates(self):
        """All smishing template_ids return valid MITRE data."""
        template_ids = ["account_verify", "package_delivery", "mfa_code", "payment_alert"]
        for tid in template_ids:
            data = get_mitre_data("smishing", tid)
            self.assertIn("techniques", data)
            self.assertIn("tactic", data)
            self.assertIn("detection", data)

    def test_get_mitre_data_all_quishing_templates(self):
        """All quishing template_ids return valid MITRE data."""
        template_ids = ["wifi_portal", "parking_payment", "document_access", "employee_verify"]
        for tid in template_ids:
            data = get_mitre_data("quishing", tid)
            self.assertIn("techniques", data)
            self.assertIn("tactic", data)
            self.assertIn("detection", data)

    def test_get_mitre_data_all_vishing_templates(self):
        """All vishing_script template_ids return valid MITRE data."""
        template_ids = [
            "it_support_call", "vendor_support_call", "executive_impersonation_call",
            "password_reset_escalation", "service_account_audit",
        ]
        for tid in template_ids:
            data = get_mitre_data("vishing_script", tid)
            self.assertIn("techniques", data)
            self.assertIn("tactic", data)
            self.assertIn("detection", data)

    def test_get_mitre_data_all_physical_templates(self):
        """All physical_pretext template_ids return valid MITRE data."""
        template_ids = [
            "hvac_technician", "fire_inspector", "delivery_driver",
            "telecom_technician", "copier_technician", "it_asset_inventory",
        ]
        for tid in template_ids:
            data = get_mitre_data("physical_pretext", tid)
            self.assertIn("techniques", data)
            self.assertIn("tactic", data)
            self.assertIn("detection", data)

    # -- Each returned dict has required keys --

    def test_returned_dict_has_required_keys(self):
        """Every entry in SCENARIO_TECHNIQUES has techniques, tactic, detection."""
        for scenario_type, templates in SCENARIO_TECHNIQUES.items():
            for template_id, data in templates.items():
                self.assertIn("techniques", data,
                              f"Missing 'techniques' in {scenario_type}/{template_id}")
                self.assertIn("tactic", data,
                              f"Missing 'tactic' in {scenario_type}/{template_id}")
                self.assertIn("detection", data,
                              f"Missing 'detection' in {scenario_type}/{template_id}")

    # -- Detection has should_detect and often_fails lists --

    def test_detection_has_should_detect_and_often_fails(self):
        """Every detection dict contains 'should_detect' and 'often_fails' lists."""
        for scenario_type, templates in SCENARIO_TECHNIQUES.items():
            for template_id, data in templates.items():
                detection = data["detection"]
                self.assertIn("should_detect", detection,
                              f"Missing 'should_detect' in {scenario_type}/{template_id}")
                self.assertIn("often_fails", detection,
                              f"Missing 'often_fails' in {scenario_type}/{template_id}")
                self.assertIsInstance(detection["should_detect"], list)
                self.assertIsInstance(detection["often_fails"], list)
                self.assertTrue(len(detection["should_detect"]) > 0,
                                f"Empty 'should_detect' in {scenario_type}/{template_id}")
                self.assertTrue(len(detection["often_fails"]) > 0,
                                f"Empty 'often_fails' in {scenario_type}/{template_id}")

    # -- Techniques are tuples of (id_string, name_string) --

    def test_techniques_are_tuples_of_strings(self):
        """Every technique entry is a tuple of (id_string, name_string)."""
        for scenario_type, templates in SCENARIO_TECHNIQUES.items():
            for template_id, data in templates.items():
                techniques = data["techniques"]
                self.assertIsInstance(techniques, list)
                self.assertTrue(len(techniques) > 0,
                                f"Empty techniques list in {scenario_type}/{template_id}")
                for tech in techniques:
                    self.assertIsInstance(tech, tuple,
                                         f"Technique not a tuple in {scenario_type}/{template_id}: {tech}")
                    self.assertEqual(len(tech), 2,
                                     f"Technique tuple wrong length in {scenario_type}/{template_id}: {tech}")
                    tech_id, tech_name = tech
                    self.assertIsInstance(tech_id, str,
                                         f"Technique ID not string in {scenario_type}/{template_id}")
                    self.assertIsInstance(tech_name, str,
                                         f"Technique name not string in {scenario_type}/{template_id}")
                    self.assertTrue(tech_id.startswith("T"),
                                    f"Technique ID should start with 'T': {tech_id}")

    # -- Unknown template_id falls back to default data --

    def test_unknown_template_falls_back_to_default(self):
        """Unknown template_id returns fallback data with generic techniques."""
        data = get_mitre_data("phishing_email", "totally_unknown_id")
        self.assertIn("techniques", data)
        self.assertIn("tactic", data)
        self.assertIn("detection", data)
        self.assertEqual(data["tactic"], "Initial Access")
        self.assertEqual(data["techniques"], [("T1566", "Phishing")])

    def test_unknown_scenario_type_falls_back_to_default(self):
        """Unknown scenario_type returns fallback data."""
        data = get_mitre_data("nonexistent_type", "nonexistent_template")
        self.assertEqual(data["tactic"], "Initial Access")
        self.assertEqual(data["techniques"], [("T1566", "Phishing")])

    def test_fallback_detection_structure(self):
        """Fallback data has proper detection structure."""
        data = get_mitre_data("fake_type", "fake_id")
        self.assertIn("should_detect", data["detection"])
        self.assertIn("often_fails", data["detection"])
        self.assertIsInstance(data["detection"]["should_detect"], list)
        self.assertIsInstance(data["detection"]["often_fails"], list)

    # -- get_phase_scenario_type returns valid scenario types --

    def test_get_phase_scenario_type_all_phases(self):
        """get_phase_scenario_type returns a valid type for every defined phase."""
        valid_types = {"phishing", "smishing", "quishing", "vishing", "physical", "full"}
        for phase in PHASE_TO_SCENARIO:
            result = get_phase_scenario_type(phase)
            self.assertIn(result, valid_types,
                          f"Phase '{phase}' mapped to invalid type '{result}'")

    def test_get_phase_scenario_type_unknown_phase(self):
        """Unknown phase falls back to 'phishing'."""
        result = get_phase_scenario_type("nonexistent_phase")
        self.assertEqual(result, "phishing")

    def test_get_phase_scenario_type_specific_mappings(self):
        """Spot-check specific phase-to-scenario mappings."""
        self.assertEqual(get_phase_scenario_type("recon"), "full")
        self.assertEqual(get_phase_scenario_type("initial-access"), "phishing")
        self.assertEqual(get_phase_scenario_type("credential-access"), "vishing")
        self.assertEqual(get_phase_scenario_type("defense-evasion"), "smishing")
        self.assertEqual(get_phase_scenario_type("discovery"), "physical")
        self.assertEqual(get_phase_scenario_type("lateral-movement"), "physical")
        self.assertEqual(get_phase_scenario_type("collection"), "physical")
        self.assertEqual(get_phase_scenario_type("c2"), "full")
        self.assertEqual(get_phase_scenario_type("exfiltration"), "full")

    # -- All ATTACK_PHASES have string values --

    def test_attack_phases_all_string_values(self):
        """Every value in ATTACK_PHASES is a non-empty string."""
        self.assertTrue(len(ATTACK_PHASES) > 0, "ATTACK_PHASES is empty")
        for key, value in ATTACK_PHASES.items():
            self.assertIsInstance(key, str, f"ATTACK_PHASES key not string: {key}")
            self.assertIsInstance(value, str, f"ATTACK_PHASES value not string for key '{key}'")
            self.assertTrue(len(value) > 0, f"ATTACK_PHASES value empty for key '{key}'")

    def test_attack_phases_expected_count(self):
        """ATTACK_PHASES has the expected number of phases."""
        self.assertEqual(len(ATTACK_PHASES), 12)


# ── Test MITRE data in generated scenarios ────────────────────

class TestMitreInGenerator(unittest.TestCase):
    """Test that MITRE ATT&CK data is correctly included in generator output."""

    def setUp(self):
        random.seed(42)
        self.gen = RedtextGenerator()

    # -- All 6 generate methods include mitre_attack in output --

    def test_phishing_email_has_mitre_attack(self):
        result = self.gen.generate_phishing_email()
        self.assertIn("mitre_attack", result)
        self.assertIsInstance(result["mitre_attack"], dict)

    def test_smishing_message_has_mitre_attack(self):
        result = self.gen.generate_smishing_message()
        self.assertIn("mitre_attack", result)
        self.assertIsInstance(result["mitre_attack"], dict)

    def test_quishing_scenario_has_mitre_attack(self):
        result = self.gen.generate_quishing_scenario()
        self.assertIn("mitre_attack", result)
        self.assertIsInstance(result["mitre_attack"], dict)

    def test_vishing_script_has_mitre_attack(self):
        result = self.gen.generate_vishing_script()
        self.assertIn("mitre_attack", result)
        self.assertIsInstance(result["mitre_attack"], dict)

    def test_physical_pretext_has_mitre_attack(self):
        result = self.gen.generate_physical_pretext()
        self.assertIn("mitre_attack", result)
        self.assertIsInstance(result["mitre_attack"], dict)

    def test_full_scenario_has_mitre_attack(self):
        result = self.gen.generate_full_scenario()
        self.assertIn("mitre_attack", result)
        self.assertIsInstance(result["mitre_attack"], dict)

    # -- Phishing email mitre_attack has correct tactic per template_id --

    def test_phishing_credential_harvest_tactic(self):
        result = self.gen.generate_phishing_email(template_id="credential_harvest")
        self.assertEqual(result["mitre_attack"]["tactic"], "Initial Access")

    def test_phishing_malicious_attachment_tactic(self):
        result = self.gen.generate_phishing_email(template_id="malicious_attachment")
        self.assertEqual(result["mitre_attack"]["tactic"], "Initial Access")

    def test_phishing_bec_wire_tactic(self):
        result = self.gen.generate_phishing_email(template_id="bec_wire")
        self.assertEqual(result["mitre_attack"]["tactic"], "Initial Access")

    def test_phishing_callback_phishing_tactic(self):
        result = self.gen.generate_phishing_email(template_id="callback_phishing")
        self.assertEqual(result["mitre_attack"]["tactic"], "Initial Access")

    def test_phishing_supply_chain_tactic(self):
        result = self.gen.generate_phishing_email(template_id="supply_chain")
        self.assertEqual(result["mitre_attack"]["tactic"], "Initial Access")

    def test_phishing_credential_breach_tactic(self):
        result = self.gen.generate_phishing_email(template_id="credential_breach")
        self.assertEqual(result["mitre_attack"]["tactic"], "Credential Access")

    # -- Vishing script mitre_attack has correct tactic --

    def test_vishing_password_reset_escalation_tactic(self):
        result = self.gen.generate_vishing_script(script_id="password_reset_escalation")
        self.assertEqual(result["mitre_attack"]["tactic"], "Privilege Escalation")

    def test_vishing_service_account_audit_tactic(self):
        result = self.gen.generate_vishing_script(script_id="service_account_audit")
        self.assertEqual(result["mitre_attack"]["tactic"], "Credential Access")

    # -- Physical pretext mitre_attack has correct tactic --

    def test_physical_copier_technician_tactic(self):
        result = self.gen.generate_physical_pretext(pretext_id="copier_technician")
        self.assertEqual(result["mitre_attack"]["tactic"], "Lateral Movement")

    def test_physical_it_asset_inventory_tactic(self):
        result = self.gen.generate_physical_pretext(pretext_id="it_asset_inventory")
        self.assertEqual(result["mitre_attack"]["tactic"], "Discovery")

    # -- Full scenario has aggregated mitre_attack --

    def test_full_scenario_mitre_has_techniques(self):
        result = self.gen.generate_full_scenario()
        mitre = result["mitre_attack"]
        self.assertIn("techniques", mitre)
        self.assertIsInstance(mitre["techniques"], list)
        self.assertTrue(len(mitre["techniques"]) > 0)

    def test_full_scenario_mitre_has_tactics(self):
        result = self.gen.generate_full_scenario()
        mitre = result["mitre_attack"]
        self.assertIn("tactics", mitre)
        self.assertIsInstance(mitre["tactics"], list)
        self.assertTrue(len(mitre["tactics"]) > 0)

    def test_full_scenario_mitre_has_detection_analysis(self):
        result = self.gen.generate_full_scenario()
        mitre = result["mitre_attack"]
        self.assertIn("detection_analysis", mitre)
        self.assertIsInstance(mitre["detection_analysis"], dict)

    def test_full_scenario_detection_analysis_structure(self):
        result = self.gen.generate_full_scenario()
        detection = result["mitre_attack"]["detection_analysis"]
        self.assertIn("should_detect", detection)
        self.assertIn("often_fails", detection)
        self.assertIsInstance(detection["should_detect"], list)
        self.assertIsInstance(detection["often_fails"], list)
        self.assertTrue(len(detection["should_detect"]) > 0)
        self.assertTrue(len(detection["often_fails"]) > 0)

    def test_full_scenario_techniques_are_tuples(self):
        """Aggregated techniques in full scenario are still tuples of (id, name)."""
        result = self.gen.generate_full_scenario()
        for tech in result["mitre_attack"]["techniques"]:
            self.assertIsInstance(tech, tuple)
            self.assertEqual(len(tech), 2)
            self.assertIsInstance(tech[0], str)
            self.assertIsInstance(tech[1], str)

    def test_full_scenario_techniques_are_deduplicated(self):
        """Aggregated techniques should have no duplicate technique IDs."""
        result = self.gen.generate_full_scenario()
        tech_ids = [t[0] for t in result["mitre_attack"]["techniques"]]
        self.assertEqual(len(tech_ids), len(set(tech_ids)),
                         "Duplicate technique IDs found in full scenario aggregation")

    # -- Full scenario now includes 'smishing' key --

    def test_full_scenario_includes_smishing(self):
        result = self.gen.generate_full_scenario()
        self.assertIn("smishing", result)
        self.assertEqual(result["smishing"]["type"], "smishing")


# ── Test the 6 new templates work ─────────────────────────────

class TestNewTemplates(unittest.TestCase):
    """Test that the 6 new templates generate valid output."""

    def setUp(self):
        random.seed(42)
        self.gen = RedtextGenerator()

    # -- supply_chain phishing template --

    def test_supply_chain_phishing_generates(self):
        result = self.gen.generate_phishing_email(template_id="supply_chain")
        self.assertEqual(result["type"], "phishing_email")
        self.assertEqual(result["template"], "Supply Chain Vendor Compromise")
        self.assertIn("subject", result)
        self.assertIn("body", result)
        self.assertTrue(len(result["subject"]) > 0)
        self.assertTrue(len(result["body"]) > 0)

    def test_supply_chain_no_unreplaced_placeholders_subject(self):
        for _ in range(10):
            result = self.gen.generate_phishing_email(template_id="supply_chain")
            self.assertNotRegex(result["subject"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in subject: {result['subject']}")

    def test_supply_chain_no_unreplaced_placeholders_body(self):
        for _ in range(10):
            result = self.gen.generate_phishing_email(template_id="supply_chain")
            self.assertNotRegex(result["body"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in body: {result['body']}")

    # -- credential_breach phishing template --

    def test_credential_breach_phishing_generates(self):
        result = self.gen.generate_phishing_email(template_id="credential_breach")
        self.assertEqual(result["type"], "phishing_email")
        self.assertEqual(result["template"], "Credential Breach Notification")
        self.assertIn("subject", result)
        self.assertIn("body", result)
        self.assertTrue(len(result["subject"]) > 0)
        self.assertTrue(len(result["body"]) > 0)

    def test_credential_breach_no_unreplaced_placeholders_subject(self):
        for _ in range(10):
            result = self.gen.generate_phishing_email(template_id="credential_breach")
            self.assertNotRegex(result["subject"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in subject: {result['subject']}")

    def test_credential_breach_no_unreplaced_placeholders_body(self):
        for _ in range(10):
            result = self.gen.generate_phishing_email(template_id="credential_breach")
            self.assertNotRegex(result["body"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in body: {result['body']}")

    # -- password_reset_escalation vishing template --

    def test_password_reset_escalation_vishing_generates(self):
        result = self.gen.generate_vishing_script(script_id="password_reset_escalation")
        self.assertEqual(result["type"], "vishing_script")
        self.assertEqual(result["template"], "Password Reset / Privilege Escalation")
        self.assertIn("script", result)
        for section in ("opening", "escalation", "objective", "red_flags_to_avoid"):
            self.assertIn(section, result["script"])
            self.assertTrue(len(result["script"][section]) > 0)

    def test_password_reset_escalation_no_unreplaced_placeholders(self):
        for _ in range(10):
            result = self.gen.generate_vishing_script(script_id="password_reset_escalation")
            for section_name, section_text in result["script"].items():
                self.assertNotRegex(section_text, r"\{[a-z_]+\}",
                                    f"Leftover placeholder in {section_name}: {section_text}")

    # -- service_account_audit vishing template --

    def test_service_account_audit_vishing_generates(self):
        result = self.gen.generate_vishing_script(script_id="service_account_audit")
        self.assertEqual(result["type"], "vishing_script")
        self.assertEqual(result["template"], "Service Account Security Audit")
        self.assertIn("script", result)
        for section in ("opening", "escalation", "objective", "red_flags_to_avoid"):
            self.assertIn(section, result["script"])
            self.assertTrue(len(result["script"][section]) > 0)

    def test_service_account_audit_no_unreplaced_placeholders(self):
        for _ in range(10):
            result = self.gen.generate_vishing_script(script_id="service_account_audit")
            for section_name, section_text in result["script"].items():
                self.assertNotRegex(section_text, r"\{[a-z_]+\}",
                                    f"Leftover placeholder in {section_name}: {section_text}")

    # -- copier_technician physical pretext template --

    def test_copier_technician_physical_generates(self):
        result = self.gen.generate_physical_pretext(pretext_id="copier_technician")
        self.assertEqual(result["type"], "physical_pretext")
        self.assertEqual(result["template"], "Copier / Printer Technician")
        self.assertIn("script", result)
        self.assertTrue(len(result["script"]) > 0)
        self.assertIn("operator", result)
        self.assertIn("target_areas", result)
        self.assertIn("objectives", result)

    def test_copier_technician_no_unreplaced_placeholders(self):
        for _ in range(10):
            result = self.gen.generate_physical_pretext(pretext_id="copier_technician")
            self.assertNotRegex(result["script"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in script: {result['script']}")

    # -- it_asset_inventory physical pretext template --

    def test_it_asset_inventory_physical_generates(self):
        result = self.gen.generate_physical_pretext(pretext_id="it_asset_inventory")
        self.assertEqual(result["type"], "physical_pretext")
        self.assertEqual(result["template"], "IT Asset Inventory Specialist")
        self.assertIn("script", result)
        self.assertTrue(len(result["script"]) > 0)
        self.assertIn("operator", result)
        self.assertIn("target_areas", result)
        self.assertIn("objectives", result)

    def test_it_asset_inventory_no_unreplaced_placeholders(self):
        for _ in range(10):
            result = self.gen.generate_physical_pretext(pretext_id="it_asset_inventory")
            self.assertNotRegex(result["script"], r"\{[a-z_]+\}",
                                f"Leftover placeholder in script: {result['script']}")


# ── Test phase command mapping ────────────────────────────────

class TestPhaseCommand(unittest.TestCase):
    """Test that ATTACK_PHASES keys map to valid scenario types."""

    def test_all_attack_phases_have_scenario_mapping(self):
        """Every ATTACK_PHASES key has a mapping in PHASE_TO_SCENARIO
        or falls back to 'phishing' via get_phase_scenario_type."""
        valid_types = {"phishing", "smishing", "quishing", "vishing", "physical", "full"}
        for phase in ATTACK_PHASES:
            result = get_phase_scenario_type(phase)
            self.assertIn(result, valid_types,
                          f"Phase '{phase}' mapped to invalid scenario type '{result}'")

    def test_phase_scenario_types_in_valid_set(self):
        """All values in PHASE_TO_SCENARIO are in the valid set."""
        valid_types = {"phishing", "smishing", "quishing", "vishing", "physical", "full"}
        for phase, scenario_type in PHASE_TO_SCENARIO.items():
            self.assertIn(scenario_type, valid_types,
                          f"PHASE_TO_SCENARIO['{phase}'] = '{scenario_type}' not in valid set")

    def test_persistence_phase_falls_back(self):
        """A phase defined in ATTACK_PHASES but not in PHASE_TO_SCENARIO
        should fall back to 'phishing'."""
        # 'persistence' is in ATTACK_PHASES but not in PHASE_TO_SCENARIO
        self.assertIn("persistence", ATTACK_PHASES)
        result = get_phase_scenario_type("persistence")
        self.assertEqual(result, "phishing")

    def test_all_phase_to_scenario_keys_are_valid_phases(self):
        """Every key in PHASE_TO_SCENARIO should be a recognized ATTACK_PHASES key."""
        for phase in PHASE_TO_SCENARIO:
            self.assertIn(phase, ATTACK_PHASES,
                          f"PHASE_TO_SCENARIO key '{phase}' not in ATTACK_PHASES")


if __name__ == "__main__":
    unittest.main()
