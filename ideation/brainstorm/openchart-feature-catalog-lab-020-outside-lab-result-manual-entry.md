# Outside Lab Result Manual Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized staff enter externally produced laboratory results with required source attribution, verification status, and attached evidence.
Topics: openchart-feature-catalog, laboratory, frappe, outside-results
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-020 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Outside Lab Result Manual Entry assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates manual transcription and source attribution as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Filer supplies patient, source organization, report date, analytes, values, units, ranges, verification method, author, and attachment.
- The system produces a provenance-rich outside result distinguishable from interfaced data and exposes its current state to permitted users.
- The governed lifecycle is Draft → Verification Pending → Filed or Rejected → Superseded; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Unverified transcriptions remain labeled as such; later corrections use succession and preserve the original entry.

## Frappe realization

- **DocTypes:** `OC Outside Lab Result` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Verification Pending → Filed or Rejected → Superseded; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Filer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.outside_lab_result_manual_entry` is the supported write method, with allowlisted `/api/resource/OC%20Outside%20Lab%20Result` reads and a Desk worklist or report.

## Boundaries

Owns: manual transcription and source attribution. Consumes: patient identity, external report evidence, terminology, and permissions. Emits: a provenance-rich outside result distinguishable from interfaced data. Does not own: certifying the external laboratory or fabricating missing source metadata.

## Open questions

- Which organization-level policy values and exception thresholds for outside lab result manual entry must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
