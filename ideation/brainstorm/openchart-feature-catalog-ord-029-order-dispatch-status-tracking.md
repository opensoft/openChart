# Order Dispatch Status Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks delivery, acknowledgment, acceptance, rejection, and completion signals between ordering and fulfillment destinations.
Topics: openchart-feature-catalog, cpoe, frappe, order-dispatch
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-029 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Destination latency dashboard** — Compare dispatch-to-acknowledgment timing by route without exposing unnecessary clinical detail.

## Focus

This feature isolates transport-facing state evidence for signed orders.

## Behavior

- Each destination attempt records route, destination, payload identifier, send time, response, and retry count.
- Users distinguish clinically active order state from technical delivery state.
- Rejections and ambiguous responses create actionable exceptions with source details.
- Retries are idempotent and never create duplicate local orders.
- Acknowledgment from a destination does not imply clinical completion.
- Staff may resolve routing errors but cannot fabricate destination acknowledgments.

## Frappe realization

- **DocTypes:** `OC Order Dispatch` with order, destination, external identifier, status, attempts, payload digest, and response attachment.
- **Workflow:** Pending → Sent → Acknowledged or Rejected/Failed; retry transitions retain attempt children.
- **Roles/permissions:** `OC Interface Service` writes technical events; `OC Interface Operator` resolves failures; clinicians have read-only summary access.
- **Hooks/API/surface:** `on_submit` queues dispatch jobs, callbacks use guarded whitelisted methods, and REST status/error filters plus a Script Report expose exceptions.

## Boundaries

Owns: delivery-state evidence. Consumes: signed order and destination routing. Emits: acknowledgments and exceptions. Does not own: destination fulfillment or clinical status.

## Open questions

- How long should technical dispatch evidence and raw responses be retained?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Fulfillment-Class Order Queues](openchart-feature-catalog-ord-028-fulfillment-class-order-queues.md)
