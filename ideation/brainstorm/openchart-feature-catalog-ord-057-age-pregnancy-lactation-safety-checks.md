# Age Pregnancy And Lactation Safety Checks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates medication and procedure orders against governed age, pregnancy, and lactation safety guidance while representing unknown context explicitly.
Topics: openchart-feature-catalog, cpoe, frappe, reproductive-safety
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-057 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Context-sensitive question prompt** — Ask only policy-relevant safety questions and require human-confirmed answers.

## Focus

This feature isolates demographic and reproductive-context safety evaluation at order time.

## Behavior

- Rules evaluate precise age and authorized pregnancy or lactation context only when clinically relevant.
- Unknown, stale, declined, not-applicable, and confirmed states remain distinct.
- Alerts explain the triggering order, context fact and date, risk, evidence, alternatives, and rule owner.
- The interface avoids inferring pregnancy or lactation from sex, gender, diagnosis, or appearance.
- A clinician may document context through the appropriate clinical workflow or use a governed override.
- Guidance may suggest a draft alternative but never changes or submits the order autonomously.

## Frappe realization

- **DocTypes:** `OC CDS Rule` type Demographic/Reproductive Safety with age bands, context predicates, evidence, provenance, and effective dates.
- **Roles/permissions:** evaluation reads only consent- and role-authorized context; sensitive facts are not copied into general order fields.
- **Hooks/API/surface:** order preview and `on_submit` orchestrator return pass/alert/unknown outcomes with source timestamps.
- **Audit:** `OC CDS Evaluation` records referenced fact identifiers, rule version, missing-data state, and clinician resolution.

## Boundaries

Owns: safety-rule evaluation for age, pregnancy, and lactation. Consumes: authorized context and proposed order. Emits: guidance or uncertainty. Does not own: reproductive-status capture or clinical decision.

## Open questions

- Which contexts permit a declined-to-answer state while still allowing order signature?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Dose Range Checking](openchart-feature-catalog-ord-052-dose-range-checking.md)
