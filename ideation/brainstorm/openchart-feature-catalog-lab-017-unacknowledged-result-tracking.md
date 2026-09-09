# Resulted-But-Unacknowledged Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Identifies filed results whose responsible clinical recipient has not yet completed the required acknowledgment step.
Topics: openchart-feature-catalog, laboratory, frappe, result-acknowledgment
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-017 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Resulted-But-Unacknowledged Tracking assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates laboratory-side projection of acknowledgment status as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Result Oversight supplies filed result, accountable recipient, filing time, urgency, acknowledgment evidence, coverage transfers, and deadlines.
- The system produces an aging queue and escalation signal for unacknowledged results and exposes its current state to permitted users.
- The governed lifecycle is Filed → Assigned → Acknowledged or Overdue → Escalated; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Opening a chart or inbox item does not count as acknowledgment; corrected results can reopen the obligation.

## Frappe realization

- **DocTypes:** `OC Unacknowledged Result Projection` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Filed → Assigned → Acknowledged or Overdue → Escalated; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Result Oversight` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.unacknowledged_result_tracking` is the supported write method, with allowlisted `/api/resource/OC%20Unacknowledged%20Result%20Projection` reads and a Desk worklist or report.

## Boundaries

Owns: laboratory-side projection of acknowledgment status. Consumes: filed results and the named Result Accountability process. Emits: an aging queue and escalation signal for unacknowledged results. Does not own: ownership rules, follow-up completion, or patient communication.

## Open questions

- Which organization-level policy values and exception thresholds for resulted-but-unacknowledged tracking must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
