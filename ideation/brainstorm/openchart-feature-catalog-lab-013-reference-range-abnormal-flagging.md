# Reference Range Abnormal Flagging — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Calculates low, high, abnormal, and critical flags from the exact reference range and units applicable to each reported observation.
Topics: openchart-feature-catalog, laboratory, frappe, abnormal-flags
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-013 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Reference Range Abnormal Flagging assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates mechanical range comparison and flag provenance as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Reviewer supplies result value, units, method, specimen, reference range version, and source flags.
- The system produces a reproducible interpretation flag with rule provenance and exposes its current state to permitted users.
- The governed lifecycle is Pending → Calculated → Verified or Exception; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Non-numeric, qualitative, incomparable-unit, or missing-range results preserve source flags and show interpretation uncertainty.

## Frappe realization

- **DocTypes:** `OC Result Interpretation` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Pending → Calculated → Verified or Exception; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Reviewer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.reference_range_abnormal_flagging` is the supported write method, with allowlisted `/api/resource/OC%20Result%20Interpretation` reads and a Desk worklist or report.

## Boundaries

Owns: mechanical range comparison and flag provenance. Consumes: filed observations, normalized units, and active reference ranges. Emits: a reproducible interpretation flag with rule provenance. Does not own: diagnosis, treatment recommendation, or result acknowledgment.

## Open questions

- Which organization-level policy values and exception thresholds for reference range abnormal flagging must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
