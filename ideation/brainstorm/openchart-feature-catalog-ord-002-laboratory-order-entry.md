# Laboratory Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures laboratory tests with specimens, timing, priority, and clinical questions suitable for fulfillment routing.
Topics: openchart-feature-catalog, cpoe, frappe, laboratory-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-002 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Specimen readiness preview** — Show collection prerequisites and container needs before signature.

## Focus

This feature isolates structured ordering for laboratory diagnostics.

## Behavior

- Clinicians choose one or more tests and provide priority, collection timing, specimen source, fasting status, and clinical question.
- Panels expand visibly so the signer can remove optional components where policy allows.
- Duplicate recent or pending tests are shown with dates and statuses before submission.
- Unknown specimen requirements route the draft to clarification rather than guessing.
- Signed orders receive fulfillment status without altering the accepted clinical intent.
- Cancellation after collection is rejected and directs the user to the laboratory exception workflow.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` with order_class `Laboratory`; child `OC Lab Order Item` stores test code, specimen, collection window, and priority.
- **Workflow:** Draft → Pending Signature → Active → In Fulfillment → Completed or Cancelled; only fulfillment roles advance collection states.
- **Roles/permissions:** `OC Ordering Clinician`, `OC Laboratory Staff`, and `OC Order Manager` receive class-scoped DocPerms and user permissions.
- **Hooks/API/surface:** `validate` checks specimen metadata, `on_submit` fires CDS, and `open_chart.api.v1.orders.submit` plus REST filters by order_class/status support the lab queue.

## Boundaries

Owns: laboratory-order intent. Consumes: test catalog, patient context, and specimen rules. Emits: fulfillment-ready test requests. Does not own: specimen accessioning or result values.

## Open questions

- Should collection instructions be snapshotted from the catalog at signing?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Batch Panel Order Entry](openchart-feature-catalog-ord-009-batch-panel-order-entry.md)
