# High-Risk Order Dual Authorization — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Requires independent second authorization for organization-defined high-risk orders before activation or fulfillment.
Topics: openchart-feature-catalog, cpoe, frappe, dual-authorization
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-033 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Independent calculation comparison** — Capture two separately entered dose calculations and surface discrepancies.

## Focus

This feature isolates dual authorization distinct from supervisory cosign.

## Behavior

- Policy marks an order as requiring a second qualified authorizer based on orderable, dose, setting, or patient context.
- The second authorizer reviews the complete order and relevant calculations independently.
- The originator cannot serve as second authorizer, and shared-account behavior is prohibited.
- A mismatch results in rejection or clarification, never silent normalization.
- Activation and dispatch wait for both attestations unless an explicit emergency policy applies.
- Both identities, credential checks, timestamps, policy version, and decisions remain immutable.

## Frappe realization

- **DocTypes:** `OC Dual Authorization` with order, sequence, required privilege, decision, calculation evidence, and identity timestamp.
- **Workflow:** Awaiting First Signature → Awaiting Second Authorization → Active or Rejected.
- **Roles/permissions:** second action requires `OC High Risk Order Authorizer` plus current mapped privilege; separation of duties is server-enforced.
- **Hooks/API/surface:** `on_submit` creates the requirement; guarded authorize method uses row locks; pending REST filters and assignments drive the authorizer queue.

## Boundaries

Owns: independent second authorization evidence. Consumes: signed order, risk policy, and privileges. Emits: activation gate decision. Does not own: routine cosign or fulfillment double-checks.

## Open questions

- Which emergency conditions may defer rather than waive second authorization?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Ordering Role Cosign Requirements](openchart-feature-catalog-ord-030-ordering-role-cosign-requirements.md)
