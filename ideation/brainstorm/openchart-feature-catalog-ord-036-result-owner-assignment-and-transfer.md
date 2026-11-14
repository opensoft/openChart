# Result Owner Assignment And Transfer — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assigns each result to an eligible clinician or pool and requires accepted handoff for responsibility transfer.
Topics: openchart-feature-catalog, cpoe, frappe, result-ownership
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-036 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Coverage-aware transfer preview** — Show recipient availability and unresolved workload before handoff.

## Focus

This feature isolates initial ownership resolution and accountable transfer.

## Behavior

- Initial ownership resolves from ordering clinician, delegated principal, service policy, and current coverage.
- An owner may request transfer to an eligible clinician or pool with reason and urgency.
- Responsibility remains with the current owner until the recipient accepts, except for governed emergency reassignment.
- Declined or timed-out transfers return to the sender and may escalate.
- Departed, inactive, or unavailable owners are detected and routed to oversight.
- Every assignment and transfer records policy, actors, times, and acceptance evidence.

## Frappe realization

- **DocTypes:** `OC Result Ownership Event` with accountability record, from/to identity or pool, reason, state, policy, and timestamps.
- **Workflow:** Proposed → Accepted or Declined/Expired; accepted event updates current owner atomically.
- **Roles/permissions:** eligible clinicians and `OC Result Oversight` transfer; users cannot assign to unauthorized recipients.
- **Hooks/API/surface:** guarded transfer API validates recipient eligibility and row-locks; scheduler expires offers; REST owner/transfer filters drive handoff queues.

## Boundaries

Owns: ownership resolution and handoff evidence. Consumes: order attribution, coverage, and eligibility. Emits: current accountable owner. Does not own: result acknowledgment.

## Open questions

- When may oversight reassign responsibility without recipient acceptance?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [On-Call Result Routing Pools](openchart-feature-catalog-ord-042-on-call-result-routing-pools.md)
