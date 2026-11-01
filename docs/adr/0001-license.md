# 1. License: GPL-3.0-or-later + a Contributor License Agreement

- **Status:** Accepted
- **Date:** 2026-11-01
- **Deciders:** project maintainer
- **Supersedes:** the earlier, briefly-shipped MIT classifier (corrected to GPL in v2.2.0)

## Context

RedTEXT is a social-engineering **detection & defense** framework whose offensive
generator is the engine, not the product. In practice it is a credibility /
portfolio project: solo, part-time, open detection content as the magnet, and
**monetization is parked** (see the roadmap). There is no SaaS lane on the table.

Three things forced a deliberate decision rather than a default:

1. The repository had shipped an **MIT classifier over GPL intent** — a
   contradiction that blocked tooling and misrepresented the license. v2.2.0
   corrected the metadata to `GPL-3.0-or-later` and shipped the full license
   text. This ADR records *why* that is the intended license, not an accident.
2. The project will start **accepting external contributors** (recruiting a
   co-maintainer is an explicit roadmap exit criterion). Inbound contributions
   need a clear, recorded licensing basis *before* the first PR is merged, not
   after.
3. We had been **agonizing over AGPL vs. permissive** — a question that only
   has teeth for a hosted-service business model we are explicitly not pursuing.
   That deliberation was pure cost.

## Decision

1. **License the project under `GPL-3.0-or-later`.** Keep the full license text
   in `LICENSE`, the `GPL-3.0-or-later` SPDX expression in `pyproject.toml`, and
   the matching OSI classifier. This is the status quo; this ADR ratifies it.

2. **Require a Contributor License Agreement (CLA)** from external contributors
   before their contributions are merged. The CLA grants the project a broad,
   irrevocable license to the contribution (and a patent grant), so that the
   maintainer can **relicense or dual-license in the future without hunting down
   every past contributor for consent** — the relicensing-consent trap that
   sinks many GPL projects that later want optionality.

3. **Stop revisiting the permissive-vs-copyleft question** unless and until a
   concrete commercial lane is chosen. If that ever happens, the CLA is what
   makes revisiting *possible*; this ADR is the trigger to reopen the question.

## Rationale

- **Why copyleft (GPLv3), not permissive:** for a credibility project whose
  value is published detection content and an auditable, zero-dependency core,
  copyleft protects the "improvements flow back" norm and signals the project's
  defensive, community posture. There is no distribution model that permissive
  licensing would unlock for us.
- **Why not AGPL:** AGPL's network-use clause only matters for hosted services.
  We ship a CLI/library, not a SaaS, so AGPL would add friction (enterprise
  legal teams routinely blocklist it) for a protection we do not need.
- **Why a CLA despite being GPL:** the GPL governs *outbound* distribution; it
  does **not** by itself give the maintainer the right to relicense the
  aggregate work. A CLA keeps that door open cheaply and now, while there are
  zero external contributors, which is the only time it is free to introduce.
- **Honest limit:** a CLA adds a small amount of contributor friction and is not
  free of controversy in open-source culture. We judge the future-optionality
  it preserves worth that cost for a project that may one day need to move; a
  DCO-only alternative was considered and rejected (see below).

## Consequences

- `CONTRIBUTING.md` must state the CLA requirement and link the mechanism
  (e.g. a CLA-assistant bot or a signed statement) **before** the first external
  PR is merged. *(Follow-up task — this ADR records the decision, not the
  tooling.)*
- Every source/distribution artifact stays under `GPL-3.0-or-later`; new files
  should carry a GPL header or rely on the repository-level `LICENSE`.
- Contributors retain copyright in their work; the CLA is a license grant, not
  an assignment.
- Revisiting the license is now a deliberate, ADR-superseding act, not an
  ongoing background debate.

## Alternatives considered

- **MIT / Apache-2.0 (permissive):** rejected — unlocks no model we are
  pursuing and weakens the "contributions flow back" norm that fits a community
  detection library. (Apache-2.0's explicit patent grant was its one real draw.)
- **AGPL-3.0:** rejected — network-copyleft protection we do not need, with real
  enterprise-adoption friction.
- **DCO (Developer Certificate of Origin) instead of a CLA:** rejected for this
  project — the DCO certifies provenance but grants the maintainer no
  relicensing latitude, which is the specific optionality this decision is
  buying. (If CLA friction measurably deters contributors, revisit this as the
  fallback.)
- **Public domain / Unlicense:** rejected — forfeits copyleft and attribution.
