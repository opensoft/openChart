# Microbiology Culture Workbench — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides organism, colony, isolate, susceptibility, resistance, and comment grids for preliminary-to-final microbiology reporting.
Topics: openchart-feature-catalog, laboratory, frappe, microbiology
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-022 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Microbiology Culture Workbench assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates culture and susceptibility result structure as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Microbiology Technologist supplies specimen, collection source, culture status, organisms, isolate identifiers, antimicrobial results, methods, comments, and verification.
- The system produces a structured culture report with isolate-level susceptibility history and exposes its current state to permitted users.
- The governed lifecycle is Received → Incubating → Preliminary → Final → Corrected; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Mixed flora, contaminants, no-growth outcomes, amended identifications, and multiple isolates remain explicitly representable.

## Frappe realization

- **DocTypes:** `OC Microbiology Result` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Received → Incubating → Preliminary → Final → Corrected; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Microbiology Technologist` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.microbiology_culture_workbench` is the supported write method, with allowlisted `/api/resource/OC%20Microbiology%20Result` reads and a Desk worklist or report.

## Boundaries

Owns: culture and susceptibility result structure. Consumes: accessions, microbiology methods, antimicrobial terminology, and reviewer identity. Emits: a structured culture report with isolate-level susceptibility history. Does not own: antibiotic prescribing or infection diagnosis.

## Open questions

- Which organization-level policy values and exception thresholds for microbiology culture workbench must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
