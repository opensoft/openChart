# Genomic Test Ordering — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures assay-specific genomic orders with indication, specimen, family context, performing laboratory, and reviewable prerequisites.
Topics: openchart-feature-catalog, laboratory, frappe, genomic-ordering
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-024 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Genomic Test Ordering assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates genomic assay ordering detail as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Genetics Clinician supplies patient, assay, genes or panel, indication, specimen, family history context, destination, consent evidence, and counseling status.
- The system produces a signed genomic order gated by required evidence and exposes its current state to permitted users.
- The governed lifecycle is Draft → Prerequisite Review → Pending Signature → Ordered → Completed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Orders cannot transmit when required consent, counseling, or specimen prerequisites are absent or expired.

## Frappe realization

- **DocTypes:** `OC Genomic Order` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Prerequisite Review → Pending Signature → Ordered → Completed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Genetics Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.genomic_test_ordering` is the supported write method, with allowlisted `/api/resource/OC%20Genomic%20Order` reads and a Desk worklist or report.

## Boundaries

Owns: genomic assay ordering detail. Consumes: lab catalog, patient context, genetic consent evidence, and ordering privileges. Emits: a signed genomic order gated by required evidence. Does not own: genetic counseling conclusions or result interpretation.

## Open questions

- Which organization-level policy values and exception thresholds for genomic test ordering must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
