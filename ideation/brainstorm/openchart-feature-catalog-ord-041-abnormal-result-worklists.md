# Abnormal Result Worklists — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives clinicians and oversight teams prioritized, permissioned worklists for abnormal results and unresolved accountability states.
Topics: openchart-feature-catalog, cpoe, frappe, abnormal-results
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-041 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Trend-aware context row** — Display prior comparable values without changing laboratory abnormality classification.

## Focus

This feature isolates operational visibility over abnormal and unresolved results.

## Behavior

- Users filter by owner, pool, abnormality severity, result class, facility, state, due range, and escalation tier.
- Rows show patient-safe identifiers, result summary, finalization time, owner, acknowledgment, and follow-up status.
- Critical, newly corrected, unassigned, and overdue items receive deterministic priority styling.
- Opening a row does not acknowledge it.
- Bulk actions may assign operational work but cannot bulk-acknowledge clinical results.
- Exports and saved views enforce the same row-level permissions as the worklist.

## Frappe realization

- **DocTypes:** worklists query `OC Result Accountability`, linked result metadata, and follow-up records without copying result content.
- **Roles/permissions:** permission query conditions constrain clinician, pool, service, and facility; oversight access is separately audited.
- **API/surface:** REST filters on owner/pool/state/severity/due_at plus Query Reports and a Results Accountability workspace provide views.
- **Events:** result and accountability updates publish websocket refresh hints; server rechecks all permissions on detail fetch.

## Boundaries

Owns: abnormal-result queue projection and prioritization. Consumes: result flags and accountability state. Emits: navigation and assignments. Does not own: abnormality calculation or acknowledgment.

## Open questions

- Should worklist priority incorporate trend magnitude in addition to source severity?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Accountability Record](openchart-feature-catalog-ord-035-result-accountability-record.md)
