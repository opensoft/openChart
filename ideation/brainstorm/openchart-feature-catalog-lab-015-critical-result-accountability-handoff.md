# Critical Result Accountability Handoff — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates an urgent, traceable handoff from verified critical laboratory results into the named Result Accountability process.
Topics: openchart-feature-catalog, laboratory, frappe, critical-results
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-015 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Critical Result Accountability Handoff assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates critical-result detection-to-accountability handoff as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Result Reviewer supplies critical result, severity, verification evidence, responsible service, routing pool, deadline, and source range.
- The system produces a deduplicated accountability handoff with urgency and provenance and exposes its current state to permitted users.
- The governed lifecycle is Detected → Verified → Routed → Accepted or Escalated; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- If no eligible owner resolves, escalation follows configured coverage paths while preserving the unresolved state.

## Frappe realization

- **DocTypes:** `OC Critical Result Handoff` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Detected → Verified → Routed → Accepted or Escalated; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Result Reviewer` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.critical_result_accountability_handoff` is the supported write method, with allowlisted `/api/resource/OC%20Critical%20Result%20Handoff` reads and a Desk worklist or report.

## Boundaries

Owns: critical-result detection-to-accountability handoff. Consumes: verified results, range rules, coverage pools, and Result Accountability. Emits: a deduplicated accountability handoff with urgency and provenance. Does not own: the Result Accountability lifecycle, clinical response, or autonomous outreach.

## Open questions

- Which organization-level policy values and exception thresholds for critical result accountability handoff must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
