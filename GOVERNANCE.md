# Governance

Redtext is a small, mostly solo open-source project. This document is
deliberately lightweight: it states who decides what, what a co-maintainer would
**own**, and how someone becomes one — so that the project's top risk (a single
maintainer) is managed in the open rather than ignored.

## Roles

### Maintainer (currently: [@keuchnotkush](https://github.com/keuchnotkush))

The maintainer has final say on scope, releases, and merges, and owns the parts
of the project that are not yet delegated: the stdlib-only runtime core, the
offensive generator, packaging/CI, and overall direction (`docs/vision.md`).

### Co-maintainer (open role — see "Becoming a maintainer")

The first co-maintainer **owns detection-content review**. Concretely, that means:

- Reviewing and approving changes under the detection library — new and modified
  rules, their ATT&CK technique mapping, metadata (UUID, status, references,
  `falsepositives`), and the coverage/gap matrix.
- Guarding the **honest-labeling** bar: rules ship as "detection-engineering
  starting points, tune before deploy"; alert-grade claims require a real
  TP + benign corpus; everything else ships as a documented *hunt* or *gap*.
- Guarding the **dual-use gate**: no attack capability merges without its paired,
  validated detection + awareness output.

A detection-content change approved by the co-maintainer can be merged on their
review alone; the maintainer need not re-review it. This is the point of the
role — it removes the maintainer from the critical path for the project's
headline output.

## Decision-making

- **Normal changes:** lazy consensus on the PR. One maintainer approval (the
  co-maintainer for detection content, the maintainer otherwise) is enough to
  merge.
- **Disagreement:** discuss in the PR or an issue; if unresolved, the maintainer
  decides and records the reasoning.
- **Significant / hard-to-reverse decisions** (license, positioning, dropping a
  non-negotiable): recorded as an ADR under `docs/adr/`.

## Becoming a maintainer

There is no application form. The path is earned contribution: a consistent
track record of high-quality detection-content PRs and reviews, demonstrated
judgment on the honest-labeling and dual-use bars, and reliability over time.
The maintainer invites a co-maintainer on that basis.

The **publication funnel is the recruiting channel**: the blog series,
community submissions, and the growing detection library (roadmap Milestone 4)
exist partly to surface the people who would make good co-maintainers. Recruiting
a second maintainer from that funnel is an explicit project goal, not a
nice-to-have.

## Bus factor — a tracked risk

The project is currently **bus factor 1**: one person. This is the single
biggest risk to its longevity, and it is tracked openly rather than hidden.
Mitigations in place:

- A zero-dependency, documented, tested core that another maintainer can pick up.
- The co-maintainer role defined above, with detection-content ownership ready
  to hand off.
- The publication funnel as the recruiting mechanism.

Until a second maintainer exists, this risk stays on the table and is revisited
as the project grows.

## Related

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to contribute, and the CLA.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — expected conduct.
- [`docs/adr/0001-license.md`](docs/adr/0001-license.md) — license decision.
- [`docs/vision.md`](docs/vision.md) — the operator↔defender loop and scope.
