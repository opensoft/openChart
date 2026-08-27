# Critical Value Call Documentation With Read-Back — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents critical-value phone or secure-contact communication, recipient identity, exact read-back, attempts, and escalation outcome.
Topics: openchart-feature-catalog, laboratory, frappe, critical-call
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-048 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Critical Value Call Documentation With Read-Back assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates critical-value communication and read-back evidence as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Communicator supplies critical result, caller, recipient, contact method, attempts, communicated value, read-back value, timestamps, and escalation.
- The system produces immutable communication evidence linked to the critical result and exposes its current state to permitted users.
- The governed lifecycle is Pending Contact → Attempted → Read-Back Confirmed or Failed → Escalated or Closed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Wrong-recipient, mismatched read-back, no-answer, and interrupted-call outcomes remain unresolved and trigger continued escalation.

## Frappe realization

- **DocTypes:** `OC Critical Value Communication` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Pending Contact → Attempted → Read-Back Confirmed or Failed → Escalated or Closed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Communicator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.critical_value_call_readback` is the supported write method, with allowlisted `/api/resource/OC%20Critical%20Value%20Communication` reads and a Desk worklist or report.

## Boundaries

Owns: critical-value communication and read-back evidence. Consumes: verified critical results, contact directory, coverage routes, and escalation policy. Emits: immutable communication evidence linked to the critical result. Does not own: clinical acknowledgment, treatment response, or the broader Result Accountability process.

## Open questions

- Which organization-level policy values and exception thresholds for critical value call documentation with read-back must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
