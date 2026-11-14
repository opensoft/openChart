# Order Clarification Thread — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides a patient-scoped, auditable clarification conversation between ordering and fulfillment staff without mutating signed intent.
Topics: openchart-feature-catalog, cpoe, frappe, order-clarification
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-026 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Structured clarification types** — Route dose, specimen, laterality, destination, and scheduling questions to appropriate responders.

## Focus

This feature isolates accountable resolution of ambiguities after an order is signed.

## Behavior

- Fulfillment staff open a thread with a coded question type, message, urgency, and requested responder.
- The order may remain active or enter Clarification Requested according to class policy.
- Participants add timestamped messages and attachments under patient-access controls.
- A response that changes clinical intent requires a successor order; thread text cannot edit signed fields.
- Resolution records who accepted the answer and whether fulfillment may proceed.
- Urgent unanswered threads escalate through configured assignments without autonomous clinical decisions.

## Frappe realization

- **DocTypes:** `OC Order Clarification` with order, type, urgency, requester, responder pool, state, and child `OC Clarification Message`.
- **Workflow:** Open → Responded → Resolved or Escalated/Cancelled.
- **Roles/permissions:** order participants and routed roles receive access; Comment permissions alone do not grant patient-record access.
- **Hooks/API/surface:** `after_insert` creates assignments and Notification Logs; REST filters by state/assignee/urgency drive worklists; resolution can invoke successor preparation.

## Boundaries

Owns: clarification communication and resolution evidence. Consumes: signed order and role routing. Emits: response, escalation, or successor request. Does not own: amendment of accepted intent.

## Open questions

- When should clarification automatically pause fulfillment eligibility?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Fulfillment-Class Order Queues](openchart-feature-catalog-ord-028-fulfillment-class-order-queues.md)
