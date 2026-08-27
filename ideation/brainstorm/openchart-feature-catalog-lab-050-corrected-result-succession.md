# Corrected Laboratory Result Succession — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Issues corrected, amended, and cancelled laboratory results as linked successors that preserve prior values and notify affected workflows.
Topics: openchart-feature-catalog, laboratory, frappe, result-corrections
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-050 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Corrected Laboratory Result Succession assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates result correction lineage and change evidence as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Reviewer supplies prior result, correction type, reason, changed observations, source evidence, verifier, effective time, and notification scope.
- The system produces a submitted successor result with an explicit difference set and lineage and exposes its current state to permitted users.
- The governed lifecycle is Draft → Verification → Submitted → Filed and Notifications Pending → Complete; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Corrections cannot mutate the accepted predecessor; duplicate corrections and out-of-order source versions enter review.

## Frappe realization

- **DocTypes:** `OC Laboratory Result Correction` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Verification → Submitted → Filed and Notifications Pending → Complete; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Reviewer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.corrected_result_succession` is the supported write method, with allowlisted `/api/resource/OC%20Laboratory%20Result%20Correction` reads and a Desk worklist or report.

## Boundaries

Owns: result correction lineage and change evidence. Consumes: filed results, source corrections, duplicate detection, recipients, and accountability state. Emits: a submitted successor result with an explicit difference set and lineage. Does not own: erasing prior clinical records or deciding clinical follow-up.

## Open questions

- Which organization-level policy values and exception thresholds for corrected laboratory result succession must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
