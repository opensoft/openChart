# Barcode Specimen Labeling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Prints and verifies patient- and order-bound barcode labels at collection to reduce specimen identity and container errors.
Topics: openchart-feature-catalog, laboratory, frappe, barcode-labeling
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-005 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Barcode Specimen Labeling assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates label identity and print lineage as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Phlebotomist supplies patient, collection event, specimen type, container, aliquot count, printer, and label template.
- The system produces unique scannable labels with print and verification evidence and exposes its current state to permitted users.
- The governed lifecycle is Reserved → Printed → Applied → Scan Verified → Voided; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Reprints require a reason and invalidate superseded label identifiers so duplicate active labels are visible.

## Frappe realization

- **DocTypes:** `OC Specimen Label` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Reserved → Printed → Applied → Scan Verified → Voided; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Phlebotomist` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.barcode_specimen_labeling` is the supported write method, with allowlisted `/api/resource/OC%20Specimen%20Label` reads and a Desk worklist or report.

## Boundaries

Owns: label identity and print lineage. Consumes: collection events, barcode configuration, and printer capabilities. Emits: unique scannable labels with print and verification evidence. Does not own: patient identity resolution or external laboratory accession numbers.

## Open questions

- Which organization-level policy values and exception thresholds for barcode specimen labeling must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
