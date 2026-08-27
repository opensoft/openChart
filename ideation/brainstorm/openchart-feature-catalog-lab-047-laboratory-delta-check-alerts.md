# Laboratory Delta Check Alerts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Compares new results with eligible prior values and raises reviewable alerts when configured change thresholds are exceeded.
Topics: openchart-feature-catalog, laboratory, frappe, delta-checks
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-047 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Laboratory Delta Check Alerts assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates mechanical longitudinal comparison and review flag as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Reviewer supplies current and prior observations, time interval, units, method, specimen, patient context, rule version, and exclusions.
- The system produces a pass, alert, or indeterminate delta-check decision with pinned inputs and exposes its current state to permitted users.
- The governed lifecycle is Pending → Passed, Alerted, or Indeterminate → Reviewed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Method changes, incomparable units, corrected priors, transfusion context, and missing history can make the check indeterminate rather than normal.

## Frappe realization

- **DocTypes:** `OC Lab Delta Check` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Pending → Passed, Alerted, or Indeterminate → Reviewed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Reviewer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.laboratory_delta_check_alerts` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Delta%20Check` reads and a Desk worklist or report.

## Boundaries

Owns: mechanical longitudinal comparison and review flag. Consumes: filed observations, normalized concepts, methods, units, and governed rules. Emits: a pass, alert, or indeterminate delta-check decision with pinned inputs. Does not own: clinical diagnosis, result suppression, or autonomous recollection.

## Open questions

- Which organization-level policy values and exception thresholds for laboratory delta check alerts must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
