"""
Locale registry for REDTEXT.

Usage:
    from redtext_generator.locales import load_locale, SUPPORTED_LANGUAGES

    strings = load_locale("fr")  # French
    strings = load_locale("en")  # English (default)
"""

SUPPORTED_LANGUAGES = ("en", "fr", "es", "de")

_cache = {}


def load_locale(lang="en"):
    """Load and cache locale strings for the given language code."""
    if lang not in SUPPORTED_LANGUAGES:
        raise ValueError(
            f"Unsupported language: {lang}. "
            f"Choose from: {', '.join(SUPPORTED_LANGUAGES)}"
        )
    if lang not in _cache:
        module = __import__(
            f"redtext_generator.locales.{lang}",
            fromlist=["STRINGS"],
        )
        _cache[lang] = module.STRINGS
    return _cache[lang]


def validate_locale(strings, reference):
    """Compare a locale dict against the English reference to find missing keys.

    Returns a list of dotted key paths that are missing.
    """
    missing = []

    def _check(ref, target, path=""):
        if isinstance(ref, dict):
            for key in ref:
                full = f"{path}.{key}" if path else key
                if key not in target:
                    missing.append(full)
                else:
                    _check(ref[key], target[key], full)
        elif isinstance(ref, list) and isinstance(target, list):
            if len(target) < len(ref):
                missing.append(f"{path} (expected {len(ref)} items, got {len(target)})")

    _check(reference, strings)
    return missing
