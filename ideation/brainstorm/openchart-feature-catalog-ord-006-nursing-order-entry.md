# Nursing Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures nursing care instructions with task cadence, parameters, escalation conditions, and accountable service.
Topics: openchart-feature-catalog, cpoe, frappe, nursing-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-006 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Task-instance projection** — Derive shift-visible tasks while preserving the signed parent order.

## Focus

This feature isolates structured orders fulfilled by nursing teams.

## Behavior

- Authorized clinicians select a nursing intervention and enter cadence, start time, parameters, and stop conditions.
- Parameterized instructions define observable thresholds and who to contact when crossed.
- Ambiguous free-text-only instructions are flagged for clarification before signing where a structured template exists.
- Nursing staff acknowledge receipt and record fulfillment against generated tasks without editing the order.
- Missed or refused tasks preserve reason, actor, and timestamp.
- Unsafe or impossible schedules can be returned to the ordering clinician for clarification.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` with order_class `Nursing`; child `OC Nursing Instruction` stores intervention, cadence, parameters, and escalation contact.
- **Workflow:** Draft → Pending Signature → Active → Acknowledged → Completed, with Clarification Requested and Discontinued paths.
- **Roles/permissions:** `OC Ordering Clinician` submits; `OC Nurse` acknowledges and records task outcomes; intent fields are read-only after submission.
- **Hooks/API/surface:** `on_submit` queues task projection, v1 APIs record guarded acknowledgments, and Nursing Orders REST filters feed a shift worklist.

## Boundaries

Owns: nursing-care instruction. Consumes: care context and intervention catalog. Emits: actionable nursing order and task projections. Does not own: nursing observations or staffing.

## Open questions

- Which instructions require individual task instances versus continuous visibility?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [PRN Order Capture](openchart-feature-catalog-ord-020-prn-order-capture.md)
