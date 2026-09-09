# Catalog-Driven Lab Order Creation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians create laboratory orders from an active test and panel catalog with specimen and destination requirements resolved before signature.
Topics: openchart-feature-catalog, laboratory, frappe, lab-ordering
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-001 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Catalog-Driven Lab Order Creation assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates laboratory order composition as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies patient, encounter, test or panel code, priority, requested date, performing laboratory, and specimen requirements.
- The system produces a signed laboratory order with stable ordered-item identifiers and exposes its current state to permitted users.
- The governed lifecycle is Draft → Pending Signature → Ordered → Completed or Cancelled; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Inactive tests, incompatible specimens, and incomplete required fields block signature with actionable errors.

## Frappe realization

- **DocTypes:** `OC Lab Order` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Pending Signature → Ordered → Completed or Cancelled; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.catalog_driven_lab_order_creation` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Order` reads and a Desk worklist or report.

## Boundaries

Owns: laboratory order composition. Consumes: patient context, orderable catalog versions, and ordering privileges. Emits: a signed laboratory order with stable ordered-item identifiers. Does not own: general CPOE governance or laboratory fulfillment.

## Open questions

- Which organization-level policy values and exception thresholds for catalog-driven lab order creation must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
