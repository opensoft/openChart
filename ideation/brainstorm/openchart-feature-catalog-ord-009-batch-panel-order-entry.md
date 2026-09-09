# Batch Panel Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Expands governed panels into a reviewable group of discrete orders with safe batch editing and submission.
Topics: openchart-feature-catalog, cpoe, frappe, order-panels
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-009 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Panel variance memory** — Suggest a user's common panel edits without changing the governed definition.

## Focus

This feature isolates efficient ordering of multiple related items as a panel.

## Behavior

- A clinician selects a panel and sees every expanded component before signing.
- Optional items may be removed and shared fields such as timing or priority may be batch edited.
- Required panel members are visibly identified and cannot be removed without a coded variance reason.
- CDS and privilege checks run against each resulting order, not only the panel label.
- Failed components remain draft while successfully signed components return stable identifiers.
- The accepted orders retain panel identifier and version for provenance.

## Frappe realization

- **DocTypes:** `OC Order Panel` and child `OC Order Panel Item`; generated submittable `OC Clinical Order` records store source_panel and source_version.
- **Workflow:** panel definitions use Draft → Review → Published → Retired; generated orders follow class workflows.
- **Roles/permissions:** `OC Order Set Editor` governs panels; ordering roles instantiate but cannot alter published definitions.
- **Hooks/API/surface:** whitelisted `preview_panel` and idempotent `submit_batch` methods expand server-side; `on_submit` rule hooks run per order.

## Boundaries

Owns: panel expansion and provenance. Consumes: published definitions and class-specific schemas. Emits: discrete accepted orders. Does not own: order-set governance.

## Open questions

- When does removal of required panel members require a reason versus outright prohibition?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Organization Order Set Library](openchart-feature-catalog-ord-013-organization-order-set-library.md)
