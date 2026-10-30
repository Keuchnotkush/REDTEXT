# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0]

### Added
- **Blue-team defense playbook** (`defense` command). Turns any attack scenario
  into a defender's playbook — telemetry to collect, detection controls to
  verify, known gaps, user-facing red flags, incident-response steps, and
  debrief talking points — mapped to the scenario's MITRE ATT&CK techniques.
  Supports every vector via `--mode` and exports to JSON, Markdown, and HTML.
- `ruff` linting and a `.pre-commit-config.yaml` for contributors.
- A lint job in CI alongside the test matrix.
- `CHANGELOG.md`.

### Changed
- The package version is now single-sourced from `redtext_generator.__version__`
  (declared `dynamic` in `pyproject.toml`), so it no longer drifts across files.

### Fixed
- Exception chaining in the GoPhish client (`raise ... from`).
- Removed dead local variables and unused imports flagged by `ruff`.
- Build no longer requires `setuptools>=77` (which is Python 3.9+), so the
  package installs again on Python 3.8. The license is declared with the
  classic table form plus a classifier instead of the PEP 639 SPDX string.

## [2.1.0]

### Added
- Smishing, quishing (QR phishing), and full multi-vector scenarios.
- Interactive TUI mode and HTML/Markdown/JSON/report exports.
- GoPhish integration (template push, campaign creation, status).
- Localization: English, French, Spanish, German.
- MITRE ATT&CK integration: technique tagging, phase-based generation, and
  detection-gap analysis across all scenarios.
- `--url` flag for custom phishing URLs in quishing mode.

### Fixed
- Repaired `pyproject.toml` packaging metadata and shipped the full GPL-3.0 text.
- Forced UTF-8 output so the CLI runs on legacy Windows consoles (cp1252).

[2.2.0]: https://github.com/keuchnotkush/redtext-generator/releases/tag/v2.2.0
[2.1.0]: https://github.com/keuchnotkush/redtext-generator/releases/tag/v2.1.0
