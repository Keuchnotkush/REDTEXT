# Redtext Roadmap

Redtext is evolving from a social-engineering **scenario builder** into a
social-engineering **detection & defense framework** — built as an
*operator ↔ defender loop*: an authorized red-team operator runs an
evidence-logged engagement, and the defender validates against a curated,
CI-validated behavioral detection library with an honest ATT&CK coverage/gap
matrix.

Work is tracked as GitHub issues grouped into milestones. Detection, defense,
reporting, and governance work is planned in the open; some
scenario-generation work is tracked privately until it ships, and is published
here only once built and reviewed.

> **Principle:** every detection rule we publish is a *starting point — validate
> and tune before deploy*. CI proves a rule **converts**, not that it **fires
> correctly in your SIEM**. Alert-grade only where a real test corpus backs it;
> everything else ships as a hunt or an honest gap.

## Milestones

| Milestone | Theme | Issues |
|-----------|-------|--------|
| [M0](https://github.com/Keuchnotkush/REDTEXT/milestone/1) | Licensing, repositioning & governance | [`governance`](https://github.com/Keuchnotkush/REDTEXT/labels/governance) |
| [M1a](https://github.com/Keuchnotkush/REDTEXT/milestone/2) | Authorization + evidence log + first alert-grade detection rules | [`detection`](https://github.com/Keuchnotkush/REDTEXT/labels/detection) |
| [M1b](https://github.com/Keuchnotkush/REDTEXT/milestone/3) | Complete the flagship rule set + rule lifecycle | [`detection`](https://github.com/Keuchnotkush/REDTEXT/labels/detection) |
| [M3](https://github.com/Keuchnotkush/REDTEXT/milestone/4) | Reporting on real engagement results + auditor export | [`reporting`](https://github.com/Keuchnotkush/REDTEXT/labels/reporting) |
| [M4](https://github.com/Keuchnotkush/REDTEXT/milestone/5) | Detection-library growth + continuous publication | [`publication`](https://github.com/Keuchnotkush/REDTEXT/labels/publication) |
| [M5](https://github.com/Keuchnotkush/REDTEXT/milestone/6) | Hardening, docs & v3.0 release | [`hardening`](https://github.com/Keuchnotkush/REDTEXT/labels/hardening) |

Browse [all open issues](https://github.com/Keuchnotkush/REDTEXT/issues) or
[all milestones](https://github.com/Keuchnotkush/REDTEXT/milestones).

## Design principles

- **Zero-dependency core.** The runtime stays stdlib-only (auditable,
  air-gap-friendly, no supply-chain surface). Rule validation and heavy output
  formats live behind CI-only or optional extras, never the core.
- **Curated, not auto-generated.** Detection rules are human-written and
  validated, indexed by ATT&CK technique — we don't claim prose compiles into
  detections.
- **Honest labeling & honest limits.** We say what's alert-grade, what's a hunt,
  and what has no feasible detection (routed to a compensating control).
- **Dual-use discipline.** Offensive scenario generation exists to drive the
  defensive content; it is the engine, not the headline, and is gated behind
  authorization workflow.

## Contributing

New here? The [`good first issue`](https://github.com/Keuchnotkush/REDTEXT/labels/good%20first%20issue)
label marks newcomer-friendly work — docs, detection-content curation, and
coverage-matrix entries are great places to start. We are actively looking for a
**co-maintainer** to help own detection-content review; see the governance
issues in [M0](https://github.com/Keuchnotkush/REDTEXT/milestone/1).

Timeline is best-effort and maintained part-time; milestones ship
independently, so value lands after each one.
