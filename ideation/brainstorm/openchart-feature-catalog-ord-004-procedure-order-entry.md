# Procedure Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures procedural requests with site, preparation, urgency, indication, and prerequisite evidence.
Topics: openchart-feature-catalog, cpoe, frappe, procedure-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-004 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Prerequisite checklist** — Present organization-governed readiness items before scheduling.

## Focus

This feature isolates clinical intent for non-imaging procedures before scheduling or performance.

## Behavior

- Clinicians select a procedure and specify indication, site, laterality, priority, requested window, and preparation instructions.
- Procedure-specific questions appear from the governed catalog.
- Missing consent, laboratory, or clearance prerequisites are visible but only block when policy explicitly requires them.
- The signer reviews all generated instructions before submission.
- Fulfillment staff can request clarification without modifying the accepted order.
- A superseding order is required when the intended procedure or site changes materially.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` with order_class `Procedure`; child `OC Procedure Instruction` stores site, laterality, preparation, and prerequisite references.
- **Workflow:** Draft → Pending Signature → Active → Ready for Scheduling → In Fulfillment → Completed, with Clarification Requested.
- **Roles/permissions:** `OC Ordering Clinician` submits; `OC Procedure Coordinator` manages readiness; permlevel 1 locks provenance.
- **Hooks/API/surface:** `validate` applies catalog schema, `on_submit` runs rule hooks, and `open_chart.api.v1.orders` exposes guarded writes and filtered procedure worklists.

## Boundaries

Owns: ordered procedure and preparation intent. Consumes: procedure catalog and prerequisite evidence. Emits: schedulable request. Does not own: consent execution, scheduling, or operative documentation.

## Open questions

- How should procedure-specific question schemas be versioned with accepted orders?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Clarification Thread](openchart-feature-catalog-ord-026-order-clarification-thread.md)
