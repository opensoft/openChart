# Repeat And Series Lab Orders — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Schedules finite or conditional laboratory series such as weekly INR with occurrence-level status and stop criteria.
Topics: openchart-feature-catalog, laboratory, frappe, serial-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-029 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Repeat And Series Lab Orders assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates repeat schedule and occurrence generation as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies test, frequency, start and end, maximum occurrences, timing window, stop criteria, indication, and responsible recipient.
- The system produces a signed series with independently traceable order occurrences and exposes its current state to permitted users.
- The governed lifecycle is Draft → Active → Occurrences Due → Completed, Stopped, or Expired; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Missed, delayed, cancelled, and extra occurrences remain visible; stop criteria require explicit authorized closure.

## Frappe realization

- **DocTypes:** `OC Lab Order Series` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Active → Occurrences Due → Completed, Stopped, or Expired; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.repeat_series_lab_orders` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Order%20Series` reads and a Desk worklist or report.

## Boundaries

Owns: repeat schedule and occurrence generation. Consumes: lab catalog, patient context, and ordering authority. Emits: a signed series with independently traceable order occurrences. Does not own: autonomous dose adjustment or indefinite standing authority.

## Open questions

- Which organization-level policy values and exception thresholds for repeat and series lab orders must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
