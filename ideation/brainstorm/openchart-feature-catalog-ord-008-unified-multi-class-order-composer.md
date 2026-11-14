# Unified Multi-Class Order Composer — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives clinicians one encounter-aware workspace for composing, reviewing, and signing heterogeneous order classes together.
Topics: openchart-feature-catalog, cpoe, frappe, unified-order-composer
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-008 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Plan-linked draft basket** — Associate a mixed order basket with a care-plan section before signature.

## Focus

This feature isolates the shared user experience joining medication, laboratory, imaging, procedure, referral, nursing, and diet orders.

## Behavior

- Clinicians add different order classes to one patient-scoped basket without losing class-specific fields.
- The basket shows validation, CDS, privilege, and cosign status per item before any signature action.
- Users may sign eligible items while leaving blocked items in draft after explicit confirmation.
- Patient or encounter changes clear the basket and require confirmation to prevent wrong-context orders.
- Every generated or suggested item is visibly marked and requires human review.
- A partial network failure preserves local draft state and reports which submissions succeeded idempotently.

## Frappe realization

- **DocTypes:** `OC Order Basket` with patient, encounter, owner, expires_at, and child `OC Order Basket Item` linking draft `OC Clinical Order` records.
- **Workflow:** Basket Open → Ready for Review → Partially Submitted or Submitted; individual submittable orders retain their own workflows.
- **Roles/permissions:** clinical roles see only permitted classes; server-side permission queries prevent cross-patient basket access.
- **Hooks/API/surface:** Desk page calls idempotent `open_chart.api.v1.orders.submit_batch`; each order `on_submit` fires rules independently and websocket events return per-item outcomes.

## Boundaries

Owns: mixed-order composition and coordinated submission. Consumes: class-specific editors and validations. Emits: independently signed orders. Does not own: any class's clinical schema.

## Open questions

- Should batch signing be one attestation covering all items or one signature artifact per item?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Batch Panel Order Entry](openchart-feature-catalog-ord-009-batch-panel-order-entry.md)
