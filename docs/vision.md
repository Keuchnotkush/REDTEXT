# Vision

**Redtext is a social-engineering detection & defense framework — an
operator↔defender loop.** The offensive scenario generator is the *engine* that
drives the loop; the curated detection and awareness content is the *headline*
and the publishable magnet.

## The loop

```
   authorized engagement                     detection & defense
  ┌─────────────────────┐                   ┌─────────────────────┐
  │  OPERATOR (engine)   │   ATT&CK techniques│  DEFENDER (headline) │
  │  scenario generation │ ────────────────▶ │  telemetry • controls│
  │  phishing / vishing /│   shared mapping   │  gaps • red flags •  │
  │  physical pretext    │ ◀──────────────── │  IR steps • awareness│
  └─────────────────────┘    coverage/gaps   └─────────────────────┘
```

A red-team operator runs an authorized, evidence-logged engagement. Every
scenario is tagged with the MITRE ATT&CK techniques it exercises. The defender
side consumes those same techniques and produces blue-team output — what to
collect, what should detect it, where the gaps are, and how to respond — without
reproducing any offensive content. Red informs blue; blue measures red; the
honest ATT&CK coverage/gap matrix is the scorecard for both.

## Why this framing

The offensive generator is commodity-adjacent and, on its own, is the part of a
social-engineering tool that invites misuse and skepticism. The durable value is
on the defensive side: curated, validated detection content and awareness
material that a blue team can actually use. So we lead with defense and keep the
offensive core visible as the engine that makes the defensive content concrete
and technique-accurate — not as the product.

## Principles

- **Authorization-first** — no scenario output without a rules-of-engagement /
  authorization context and an evidence log.
- **Dual-use gate** — an attack capability ships paired with its detection and
  awareness output, never alone.
- **Honest labeling & limits** — detection content is a "starting point, tune
  before deploy"; efficacy claims are bounded to what the evidence supports
  ("detects-on-this-sample, not detects-in-your-SIEM").
- **Curated, not a magic emitter** — detection content is human-authored and
  validated, indexed by technique; prose does not auto-compile into rules.
- **Zero-dependency core** — the stdlib-only runtime is auditable and
  air-gap-friendly; validation and heavy outputs live at the edges (CI / optional
  extras), never in the runtime.

## Scope and non-goals

- **In scope:** authorized engagement generation, the defense playbook, an
  honest ATT&CK coverage/gap matrix, reporting on real engagement results.
- **Parked / non-goals:** a hosted SaaS, an LLM lure backend (parked
  indefinitely — it commoditizes the weakest part and raises the dual-use
  ceiling), and a full web dashboard.

See [ADR-0001](adr/0001-license.md) for the licensing decision that supports this
as an open, community detection project.
