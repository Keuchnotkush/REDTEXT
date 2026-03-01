"""Tests for the localization system."""

import re
import random
import unittest

from redtext_generator.locales import load_locale, validate_locale, SUPPORTED_LANGUAGES
from redtext_generator.templates import get_localized_templates
from redtext_generator.generator import RedtextGenerator


# ── Locale registry tests ────────────────────────────────────

class TestLocaleRegistry(unittest.TestCase):
    def test_all_languages_load(self):
        for lang in SUPPORTED_LANGUAGES:
            strings = load_locale(lang)
            self.assertIsInstance(strings, dict)
            self.assertIn("meta", strings)
            self.assertEqual(strings["meta"]["language_code"], lang)

    def test_unsupported_raises(self):
        with self.assertRaises(ValueError):
            load_locale("xx")

    def test_caching(self):
        s1 = load_locale("en")
        s2 = load_locale("en")
        self.assertIs(s1, s2)

    def test_supported_languages_tuple(self):
        self.assertIn("en", SUPPORTED_LANGUAGES)
        self.assertIn("fr", SUPPORTED_LANGUAGES)
        self.assertIn("es", SUPPORTED_LANGUAGES)
        self.assertIn("de", SUPPORTED_LANGUAGES)


# ── Locale completeness tests ────────────────────────────────

class TestLocaleCompleteness(unittest.TestCase):
    def setUp(self):
        self.reference = load_locale("en")

    def test_french_complete(self):
        missing = validate_locale(load_locale("fr"), self.reference)
        self.assertEqual(missing, [], f"French locale missing keys: {missing}")

    def test_spanish_complete(self):
        missing = validate_locale(load_locale("es"), self.reference)
        self.assertEqual(missing, [], f"Spanish locale missing keys: {missing}")

    def test_german_complete(self):
        missing = validate_locale(load_locale("de"), self.reference)
        self.assertEqual(missing, [], f"German locale missing keys: {missing}")


# ── Placeholder preservation tests ────────────────────────────

class TestPlaceholderPreservation(unittest.TestCase):
    """Ensure translated templates preserve all {placeholder} patterns."""

    _PLACEHOLDER_RE = re.compile(r"\{[a-z_]+\}")

    def _collect_placeholders(self, obj):
        """Recursively collect all {placeholder} patterns from a data structure."""
        found = set()
        if isinstance(obj, str):
            found.update(self._PLACEHOLDER_RE.findall(obj))
        elif isinstance(obj, dict):
            for v in obj.values():
                found.update(self._collect_placeholders(v))
        elif isinstance(obj, list):
            for item in obj:
                found.update(self._collect_placeholders(item))
        return found

    def test_phishing_placeholders(self):
        en = load_locale("en")
        for lang in ("fr", "es", "de"):
            loc = load_locale(lang)
            for i, en_tmpl in enumerate(en["phishing_templates"]):
                en_ph = self._collect_placeholders(en_tmpl)
                if i < len(loc.get("phishing_templates", [])):
                    loc_ph = self._collect_placeholders(loc["phishing_templates"][i])
                    self.assertEqual(en_ph, loc_ph,
                                     f"{lang} phishing[{i}] placeholder mismatch: "
                                     f"missing={en_ph - loc_ph}, extra={loc_ph - en_ph}")

    def test_smishing_placeholders(self):
        en = load_locale("en")
        for lang in ("fr", "es", "de"):
            loc = load_locale(lang)
            for i, en_tmpl in enumerate(en["smishing_templates"]):
                en_ph = self._collect_placeholders(en_tmpl)
                if i < len(loc.get("smishing_templates", [])):
                    loc_ph = self._collect_placeholders(loc["smishing_templates"][i])
                    self.assertEqual(en_ph, loc_ph,
                                     f"{lang} smishing[{i}] placeholder mismatch")

    def test_vishing_placeholders(self):
        en = load_locale("en")
        for lang in ("fr", "es", "de"):
            loc = load_locale(lang)
            for i, en_tmpl in enumerate(en["vishing_scripts"]):
                en_ph = self._collect_placeholders(en_tmpl)
                if i < len(loc.get("vishing_scripts", [])):
                    loc_ph = self._collect_placeholders(loc["vishing_scripts"][i])
                    self.assertEqual(en_ph, loc_ph,
                                     f"{lang} vishing[{i}] placeholder mismatch")


# ── All languages produce output ──────────────────────────────

class TestAllLanguagesProduceOutput(unittest.TestCase):
    def _gen(self, lang):
        return RedtextGenerator(
            industry="tech", urgency="medium",
            persona="it_support", company_name="Test Corp",
            language=lang,
        )

    def test_phishing_all_langs(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = self._gen(lang)
            data = gen.generate_phishing_email()
            self.assertEqual(data["type"], "phishing_email")
            self.assertEqual(data["language"], lang)
            self.assertIn("subject", data)
            self.assertIn("body", data)

    def test_smishing_all_langs(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = self._gen(lang)
            data = gen.generate_smishing_message()
            self.assertEqual(data["type"], "smishing")
            self.assertEqual(data["language"], lang)

    def test_quishing_all_langs(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = self._gen(lang)
            data = gen.generate_quishing_scenario()
            self.assertEqual(data["type"], "quishing")
            self.assertEqual(data["language"], lang)

    def test_vishing_all_langs(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = self._gen(lang)
            data = gen.generate_vishing_script()
            self.assertEqual(data["type"], "vishing_script")
            self.assertEqual(data["language"], lang)

    def test_physical_all_langs(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = self._gen(lang)
            data = gen.generate_physical_pretext()
            self.assertEqual(data["type"], "physical_pretext")
            self.assertEqual(data["language"], lang)

    def test_full_all_langs(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = self._gen(lang)
            data = gen.generate_full_scenario()
            self.assertIn("operation_name", data)
            self.assertEqual(data["language"], lang)


# ── No leftover placeholders ─────────────────────────────────

class TestNoLeftoverPlaceholders(unittest.TestCase):
    """Verify no unreplaced {placeholders} remain in generated output."""

    _PLACEHOLDER_RE = re.compile(r"\{[a-z_]+\}")
    # Placeholders that are expected in certain output fields
    _ALLOWED = {"{company}", "{software}", "{departments}"}

    def _check_no_placeholders(self, obj, path=""):
        if isinstance(obj, str):
            found = set(self._PLACEHOLDER_RE.findall(obj)) - self._ALLOWED
            self.assertEqual(found, set(),
                             f"Unreplaced placeholders at {path}: {found}\nText: {obj[:200]}")
        elif isinstance(obj, dict):
            for k, v in obj.items():
                self._check_no_placeholders(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                self._check_no_placeholders(item, f"{path}[{i}]")

    def test_phishing_no_leftover(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = RedtextGenerator(language=lang)
            data = gen.generate_phishing_email()
            self._check_no_placeholders(data, f"{lang}/phishing")

    def test_vishing_no_leftover(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = RedtextGenerator(language=lang)
            data = gen.generate_vishing_script()
            self._check_no_placeholders(data, f"{lang}/vishing")

    def test_physical_no_leftover(self):
        for lang in SUPPORTED_LANGUAGES:
            random.seed(42)
            gen = RedtextGenerator(language=lang)
            data = gen.generate_physical_pretext()
            self._check_no_placeholders(data, f"{lang}/physical")


# ── English backward compatibility ────────────────────────────

class TestEnglishBackwardCompatibility(unittest.TestCase):
    def test_default_is_english(self):
        gen = RedtextGenerator()
        self.assertEqual(gen.language, "en")

    def test_seed_determinism(self):
        random.seed(99)
        gen1 = RedtextGenerator(language="en")
        data1 = gen1.generate_phishing_email()

        random.seed(99)
        gen2 = RedtextGenerator(language="en")
        data2 = gen2.generate_phishing_email()

        self.assertEqual(data1["subject"], data2["subject"])
        self.assertEqual(data1["body"], data2["body"])

    def test_localized_templates_en_returns_originals(self):
        loc = get_localized_templates("en")
        from redtext_generator.templates import INDUSTRIES, PERSONAS
        self.assertIs(loc["INDUSTRIES"], INDUSTRIES)
        self.assertIs(loc["PERSONAS"], PERSONAS)


if __name__ == "__main__":
    unittest.main()
