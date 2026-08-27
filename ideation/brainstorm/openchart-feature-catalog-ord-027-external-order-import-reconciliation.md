# External Order Import Reconciliation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Stages externally sourced orders for identity, terminology, duplicate, authority, and lifecycle reconciliation before local acceptance.
Topics: openchart-feature-catalog, cpoe, frappe, external-order-reconciliation
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-027 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Source trust profiles** — Apply organization-approved reconciliation requirements by sending system and message type.

## Focus

This feature isolates safe intake of orders created outside openChart.

## Behavior

- Incoming payloads enter a staging record with source, message identifier, received time, raw attachment reference, and parse status.
- Patient, encounter, orderable, ordering identity, status, and duplicate candidates are shown to a reconciler.
- The reconciler may accept, map, reject, mark duplicate, or request information with a reason.
- Acceptance creates a local order carrying external provenance and current local fulfillment status.
- Unresolved identity or material terminology ambiguity can never auto-create an active local order.
- Replayed source messages are idempotently recognized by source and identifier.

## Frappe realization

- **DocTypes:** `OC External Order Import` with source identifiers, payload digest, mappings, provenance, and reconciliation decision; accepted data creates submittable `OC Clinical Order`.
- **Workflow:** Received → Parsed → Needs Reconciliation → Accepted, Rejected, or Duplicate.
- **Roles/permissions:** `OC Interface Service` inserts staging records; `OC Order Reconciler` decides; raw payload access is permlevel 2.
- **Hooks/API/surface:** background jobs parse imports, guarded reconcile methods create orders, and REST filters by source/state/error support an exception worklist.

## Boundaries

Owns: external-order staging and reconciliation decision. Consumes: source payload, identity mapping, and terminology. Emits: accepted local order or rejection evidence. Does not own: transport interfaces or source-system authority.

## Open questions

- Which trusted sources may bypass selected reconciliation steps without bypassing human review entirely?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Dispatch Status Tracking](openchart-feature-catalog-ord-029-order-dispatch-status-tracking.md)
