# Duplicate Result Import Detection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects probable duplicate laboratory results before filing using source identifiers, accession, observation identity, timestamps, and payload fingerprints.
Topics: openchart-feature-catalog, laboratory, frappe, duplicate-results
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-040 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Duplicate Result Import Detection assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates duplicate candidate detection and disposition as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Filer supplies inbound message identifiers, accession, patient, test, specimen, values, status, source lab, and payload digest.
- The system produces an automatic duplicate suppression or human adjudication case with evidence and exposes its current state to permitted users.
- The governed lifecycle is Candidate → Auto-Matched, Review Required, Distinct, or Duplicate; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Corrected, preliminary-to-final, split-panel, and repeated identical values are not treated as duplicates solely because values match.

## Frappe realization

- **DocTypes:** `OC Lab Duplicate Review` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Candidate → Auto-Matched, Review Required, Distinct, or Duplicate; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Filer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.duplicate_result_import_detection` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Duplicate%20Review` reads and a Desk worklist or report.

## Boundaries

Owns: duplicate candidate detection and disposition. Consumes: parsed results, filed source identifiers, accessions, and correction status. Emits: an automatic duplicate suppression or human adjudication case with evidence. Does not own: patient identity merge or deletion of accepted clinical records.

## Open questions

- Which organization-level policy values and exception thresholds for duplicate result import detection must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
