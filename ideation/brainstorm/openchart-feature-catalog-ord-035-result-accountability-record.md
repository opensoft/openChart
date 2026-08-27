# Result Accountability Record — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates an explicit accountability object for every result with owner, acknowledgment state, escalation policy, and follow-up deadline.
Topics: openchart-feature-catalog, cpoe, frappe, result-accountability
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-035 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Accountability completeness monitor** — Detect results that arrived without a resolvable owner before they disappear into ordinary inboxes.

## Focus

This feature isolates the durable object that joins a clinical result to responsible human follow-up.

## Behavior

- Every finalized or corrected result creates or updates one accountability record before routine routing completes.
- The record identifies owning clinician or pool, acknowledgment state, priority, follow-up deadline, and escalation ladder.
- Unowned results enter an exception state and route to an accountable service pool.
- Corrected results reopen review when configured and preserve prior acknowledgment evidence.
- Completion requires a human action or documented disposition; no AI or rule may acknowledge clinically.
- The accountability timeline remains linked to the exact result version.

## Frappe realization

- **DocTypes:** `OC Result Accountability` with result Dynamic Link, result_version, owner_user/provider/pool, state, due_at, escalation_policy, provenance, and disposition.
- **Workflow:** Unassigned → Assigned → Reviewed → Follow-Up Pending → Completed, with Escalated and Reopened paths.
- **Roles/permissions:** accountable clinicians and pools act; `OC Result Oversight` resolves unassigned records; permlevel 2 locks provenance.
- **Hooks/API/surface:** result `doc_events.on_submit/on_update` creates or reopens accountability idempotently; REST filters on owner/state/due_at/priority feed worklists.

## Boundaries

Owns: result responsibility state and evidence. Consumes: result versions, order attribution, routing policy, and schedules. Emits: worklist items and escalation events. Does not own: result clinical content.

## Open questions

- Which corrected-result changes should always reopen accountability?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Owner Assignment And Transfer](openchart-feature-catalog-ord-036-result-owner-assignment-and-transfer.md)
