# Order Diagnosis And Indication Linkage — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Attaches coded diagnoses and free-text clinical indications to each laboratory order item so medical necessity and clinical intent remain traceable.
Topics: openchart-feature-catalog, laboratory, frappe, medical-necessity
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-002 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Order Diagnosis And Indication Linkage assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates order-to-indication associations as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies laboratory order item, diagnosis code, indication text, onset context, and author.
- The system produces version-pinned indication evidence on the signed order and exposes its current state to permitted users.
- The governed lifecycle is Draft → Confirmed with parent order → Superseded; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Retired codes may be retained on historical orders but cannot be newly selected without an explicit uncoded explanation.

## Frappe realization

- **DocTypes:** `OC Lab Order Indication` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Confirmed with parent order → Superseded; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.order_diagnosis_indication_linkage` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Order%20Indication` reads and a Desk worklist or report.

## Boundaries

Owns: order-to-indication associations. Consumes: diagnosis terminology, problem context, and the parent lab order. Emits: version-pinned indication evidence on the signed order. Does not own: diagnosis authorship, coverage adjudication, or autonomous necessity decisions.

## Open questions

- Which organization-level policy values and exception thresholds for order diagnosis and indication linkage must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
