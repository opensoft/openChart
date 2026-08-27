# LOINC Panel Result Normalization — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maps local tests, panels, components, units, and methods to versioned LOINC-centered concepts while retaining source codes.
Topics: openchart-feature-catalog, laboratory, frappe, loinc-normalization
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-012 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **LOINC Panel Result Normalization assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates laboratory terminology mapping and panel structure as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Terminologist supplies source test code, source panel hierarchy, LOINC code, units, method, specimen, effective dates, and confidence.
- The system produces normalized observation identities with pinned mapping provenance and exposes its current state to permitted users.
- The governed lifecycle is Draft → Reviewed → Published → Retired; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Low-confidence, one-to-many, or structurally inconsistent mappings stay unresolved and cannot masquerade as canonical data.

## Frappe realization

- **DocTypes:** `OC Lab Concept Map` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Reviewed → Published → Retired; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Terminologist` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.loinc_panel_result_normalization` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Concept%20Map` reads and a Desk worklist or report.

## Boundaries

Owns: laboratory terminology mapping and panel structure. Consumes: source catalogs, LOINC releases, units, and specialist review. Emits: normalized observation identities with pinned mapping provenance. Does not own: altering source result text or inferring clinical meaning.

## Open questions

- Which organization-level policy values and exception thresholds for loinc panel result normalization must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
