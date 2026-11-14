# Registration Worklists — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Organizes incomplete, exception, and review-driven registration work into accountable queues with priority and aging.
Topics: openchart-feature-catalog, registration, frappe, registration-worklists
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-041 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Policy-based assignment rules** — Route issue types to trained teams while preserving manual reassignment authority.

## Focus

Provide one operational surface for registration tasks without collapsing each feature's domain state into generic status.

## Behavior

- Worklists aggregate intake corrections, identity reviews, demographic approvals, document checks, and other registration exceptions.
- Each item retains its source record, issue type, patient, facility, priority, due date, owner, and blocked reason.
- Users claim, assign, reassign, defer, escalate, or resolve according to role and source-state rules.
- Resolving a work item requires the source feature to confirm completion; queue closure alone cannot change domain data.
- Duplicate items may consolidate into one view while retaining every originating reference.
- Supervisors see aging, throughput, unassigned, and blocked views without exposing restricted patient facts unnecessarily.

## Frappe realization

- **DocTypes:** `OC Registration Work Item` with Dynamic Link source, issue_type, patient, facility, priority, due_on, assignment, and resolution.
- **Workflow:** Open → Assigned → In Progress → Waiting, Escalated, Resolved, or Canceled.
- **Roles/permissions:** source-specific roles act; `OC Registration Supervisor` manages queues; permission queries inherit patient restrictions.
- **API/surfaces:** `open_chart.api.v1.registration.transition_work_item`; Desk workspace, Kanban, list filters, Number Cards, and aging Script Report.

## Boundaries

Owns: registration task routing and operational status. Consumes: exception events from registration features. Emits: assignments, escalations, and resolution requests. Does not own: source-record decisions.

## Open questions

- Should work items be immutable event projections or standard editable task records with an audit log?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
