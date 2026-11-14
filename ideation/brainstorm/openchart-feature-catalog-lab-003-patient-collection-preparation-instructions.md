# Patient Collection Preparation Instructions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates patient-specific fasting, timing, medication, and collection instructions from ordered-test requirements with documented delivery.
Topics: openchart-feature-catalog, laboratory, frappe, collection-preparation
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-003 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Patient Collection Preparation Instructions assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates instruction assembly and delivery evidence as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Coordinator supplies ordered tests, catalog preparation rules, collection time, language, delivery channel, and clinician exceptions.
- The system produces a consolidated instruction set with delivery and acknowledgment evidence and exposes its current state to permitted users.
- The governed lifecycle is Draft → Reviewed → Delivered → Acknowledged or Delivery Failed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Conflicting test instructions route to staff review rather than silently choosing the less restrictive rule.

## Frappe realization

- **DocTypes:** `OC Collection Instruction` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Reviewed → Delivered → Acknowledged or Delivery Failed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.patient_collection_preparation_instructions` is the supported write method, with allowlisted `/api/resource/OC%20Collection%20Instruction` reads and a Desk worklist or report.

## Boundaries

Owns: instruction assembly and delivery evidence. Consumes: lab orders, catalog rules, patient preferences, and approved translations. Emits: a consolidated instruction set with delivery and acknowledgment evidence. Does not own: clinical medication changes or proof that the patient complied.

## Open questions

- Which organization-level policy values and exception thresholds for patient collection preparation instructions must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
