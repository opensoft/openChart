# Outreach Lab Billing Routing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures client-bill versus patient-bill routing instructions for outreach laboratory orders while keeping clinical fulfillment independent.
Topics: openchart-feature-catalog, laboratory, frappe, billing-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-036 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Outreach Lab Billing Routing assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates clinical-to-billing route metadata as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Coordinator supplies order, performing lab, client account reference, patient responsibility route, contract context, effective dates, and authorizer.
- The system produces an explicit billing-route instruction transmitted with the order and exposes its current state to permitted users.
- The governed lifecycle is Draft → Confirmed → Transmitted → Corrected by Successor; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Missing or conflicting route data blocks only the billing instruction and enters review without changing clinical order content.

## Frappe realization

- **DocTypes:** `OC Lab Billing Route` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Confirmed → Transmitted → Corrected by Successor; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.outreach_lab_billing_routing` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Billing%20Route` reads and a Desk worklist or report.

## Boundaries

Owns: clinical-to-billing route metadata. Consumes: lab orders, organization accounts, patient coverage context, and destination profiles. Emits: an explicit billing-route instruction transmitted with the order. Does not own: invoices, claims, payments, or account balances.

## Open questions

- Which organization-level policy values and exception thresholds for outreach lab billing routing must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
