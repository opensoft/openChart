# Laboratory Accessioning — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Registers received specimens under stable accession identifiers and records receipt condition, aliquots, and accepted test scope.
Topics: openchart-feature-catalog, laboratory, frappe, accessioning
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-006 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Laboratory Accessioning assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates receipt identity, accession state, and specimen condition as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Accessioner supplies specimen barcode, received time, temperature or condition, performing lab, accepted tests, and aliquots.
- The system produces a submitted accession connecting received material to ordered tests and exposes its current state to permitted users.
- The governed lifecycle is Expected → Received → Accepted, Partial, or Rejected → Closed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Unknown, duplicate, leaking, insufficient, or mismatched specimens enter an exception state and cannot be silently accepted.

## Frappe realization

- **DocTypes:** `OC Lab Accession` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Expected → Received → Accepted, Partial, or Rejected → Closed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Accessioner` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.laboratory_accessioning` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Accession` reads and a Desk worklist or report.

## Boundaries

Owns: receipt identity, accession state, and specimen condition. Consumes: collected specimens, lab orders, routing, and acceptance policy. Emits: a submitted accession connecting received material to ordered tests. Does not own: analytic testing or clinical result interpretation.

## Open questions

- Which organization-level policy values and exception thresholds for laboratory accessioning must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
