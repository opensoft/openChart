# Laboratory Result Chart Filing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Matches validated inbound results to the correct patient, order, and accession before creating immutable chart result records.
Topics: openchart-feature-catalog, laboratory, frappe, result-filing
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-011 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Laboratory Result Chart Filing assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates chart filing and result provenance as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Filer supplies canonical result envelope, patient match candidates, order, accession, performing lab, status, observations, and source provenance.
- The system produces a filed preliminary, final, corrected, or cancelled laboratory result and exposes its current state to permitted users.
- The governed lifecycle is Pending Match → Ready to File → Filed or Match Exception; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Ambiguous patient or order matches remain in review; the system never files by weak demographic similarity alone.

## Frappe realization

- **DocTypes:** `OC Laboratory Result` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Pending Match → Ready to File → Filed or Match Exception; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Filer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.result_chart_filing` is the supported write method, with allowlisted `/api/resource/OC%20Laboratory%20Result` reads and a Desk worklist or report.

## Boundaries

Owns: chart filing and result provenance. Consumes: parsed messages, patient identity, orders, accessions, and duplicate checks. Emits: a filed preliminary, final, corrected, or cancelled laboratory result. Does not own: clinical acknowledgment or follow-up accountability.

## Open questions

- Which organization-level policy values and exception thresholds for laboratory result chart filing must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
