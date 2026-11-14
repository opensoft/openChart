# Order Discontinuation With Reason — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Ends an active order through a permissioned action that records reason, actor, time, effective point, and fulfillment impact.
Topics: openchart-feature-catalog, cpoe, frappe, order-discontinuation
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-024 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Dependent-task impact review** — Show pending fulfillment activities affected before discontinuation is confirmed.

## Focus

This feature isolates explicit termination of accepted clinical intent.

## Behavior

- Authorized users choose a coded reason, optional explanation, and effective time before confirming discontinuation.
- The interface shows collected, dispensed, scheduled, or in-progress fulfillment that may not be reversible.
- Immediate and future-effective discontinuations are distinguishable.
- The accepted order remains immutable; a submitted lifecycle event changes its operational state.
- Unauthorized or already completed orders reject the action with a clear reason.
- Fulfillment queues receive the state change and must record any exception to stopping work.

## Frappe realization

- **DocTypes:** submittable `OC Order Lifecycle Event` with event_type `Discontinue`, reason_code, narrative, effective_at, actor, and order Link.
- **Workflow:** Active/Held → Discontinued; pending future events can be Cancelled before effective time by authorized users.
- **Roles/permissions:** order-class policy maps roles allowed to discontinue; evidence fields are permlevel 2 immutable.
- **Hooks/API/surface:** guarded `open_chart.api.v1.orders.discontinue` locks the order, validates state, submits the event, and publishes realtime queue updates.

## Boundaries

Owns: discontinuation decision evidence and order state. Consumes: active order and fulfillment status. Emits: effective stop notice. Does not own: undoing completed fulfillment.

## Open questions

- Which discontinuation reasons require direct notification to the original orderer?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Hold And Resume](openchart-feature-catalog-ord-025-order-hold-and-resume.md)
