# Visit-Due Preventive Care Prompts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows preventive services due at the current visit using age, history, interval, exclusions, and patient preferences from governed rules.
Topics: openchart-feature-catalog, cpoe, frappe, preventive-prompts
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-064 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Visit agenda handoff** — Add accepted preventive topics to a shared agenda without placing orders.

## Focus

This feature isolates visit-timed preventive guidance distinct from broad quality reporting.

## Behavior

- At encounter preparation and opening, eligible screening, immunization, and counseling prompts appear with due status and evidence.
- The prompt identifies prior qualifying events, interval calculation, exclusions, and data freshness.
- Clinicians may discuss, defer, decline, exclude, mark satisfied with evidence, or create a reviewable draft.
- Patient preference and refusal are documented without suppressing future prompts beyond governed intervals.
- Missing external history appears as uncertainty and may open reconciliation.
- No prompt orders, schedules, or messages autonomously.

## Frappe realization

- **DocTypes:** `OC Preventive Care Prompt` links patient, encounter, rule version, due basis, prior evidence, state, next_due, and provenance.
- **Workflow:** Due → Discussed → Ordered, Deferred, Declined, Excluded, Satisfied, or Needs Reconciliation.
- **Roles/permissions:** care-team roles act in encounter context; sensitive preventive topics use scoped permissions.
- **Hooks/API/surface:** scheduler may precompute due candidates; encounter hooks refresh them; filtered REST methods return visit prompts and accepted actions create drafts.

## Boundaries

Owns: visit-specific preventive prompt and disposition. Consumes: preventive rules, history, and encounter context. Emits: documented decision or draft action. Does not own: population outreach or autonomous ordering.

## Open questions

- Which preventive prompts should be precomputed versus evaluated only during a visit?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Point-Of-Care Quality Gap Prompts](openchart-feature-catalog-ord-063-point-of-care-quality-gap-prompts.md)
