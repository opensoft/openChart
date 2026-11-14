# Blood Bank Product Request Hooks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides governed handoff hooks from clinical product requests to an external or future blood-bank workflow without pretending openChart controls inventory.
Topics: openchart-feature-catalog, laboratory, frappe, blood-bank
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-046 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Blood Bank Product Request Hooks assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates blood-product request intent and handoff evidence as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies patient, product class, quantity, urgency, indication, special requirements, consent reference, destination, and requester.
- The system produces a signed request envelope with dispatch and acknowledgment evidence and exposes its current state to permitted users.
- The governed lifecycle is Draft → Signed → Dispatched → Acknowledged, Rejected, or Reconciliation; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Emergency, unmatched, rejected, and modified requests remain explicit; no product availability is inferred from message delivery.

## Frappe realization

- **DocTypes:** `OC Blood Product Request Handoff` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Signed → Dispatched → Acknowledged, Rejected, or Reconciliation; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.blood_bank_product_request_hooks` is the supported write method, with allowlisted `/api/resource/OC%20Blood%20Product%20Request%20Handoff` reads and a Desk worklist or report.

## Boundaries

Owns: blood-product request intent and handoff evidence. Consumes: patient context, ordering authority, consent references, and connector configuration. Emits: a signed request envelope with dispatch and acknowledgment evidence. Does not own: crossmatching, inventory, allocation, issue, transfusion, or blood-bank authority.

## Open questions

- Which organization-level policy values and exception thresholds for blood bank product request hooks must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
