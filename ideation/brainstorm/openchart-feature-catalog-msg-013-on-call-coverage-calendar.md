# On-call Coverage Calendar — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains a team calendar of effective on-call responsibility that routing and escalation can resolve at a precise instant.
Topics: openchart-feature-catalog, messaging-tasks, frappe, on-call-calendar
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-013 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Schedule handoff attestation** — Require outgoing and incoming clinicians to acknowledge selected handoff periods.

## Focus

This feature isolates authoritative, timezone-safe on-call coverage as an input to messaging rather than a general workforce schedule.

## Behavior

- Authorized coordinators create shifts for service, facility, role, start, end, primary, and optional backup.
- Recurring templates may seed shifts, but every materialized shift remains independently correctable and auditable.
- Conflict detection flags overlapping primaries, uncovered intervals, and ineligible clinicians.
- Published shifts become resolvable by routing and escalation; drafts never receive clinical work.
- Shift swaps require both eligibility validation and the configured acceptance or approval path.
- Emergency overrides identify actor, reason, effective interval, and superseded coverage.
- Routing asks who covered a service at an event timestamp and receives a decision with schedule version.
- Calendar changes notify affected people without exposing patient details.

## Frappe realization

- **DocTypes:** `OC On-call Schedule`, `OC On-call Shift`, and `OC Shift Swap` store service, facility, role, interval, primary, backup, state, and supersession.
- **Views:** native Calendar and Gantt views plus uncovered-interval Script Report and service filters.
- **Workflow:** Draft → Published → Superseded/Cancelled; swaps use Proposed → Accepted → Approved/Rejected as configured.
- **Automation:** Frappe auto-repeat seeds bounded patterns; `scheduler_events` materializes horizons and sends Notification Log reminders.
- **API/permissions:** read-only resolver under `open_chart.api.v1.messaging.resolve_on_call`; On-call Coordinator and Clinical Supervisor control publication.

## Boundaries

Owns: messaging-relevant on-call shifts and resolution evidence. Consumes: user eligibility and service/facility master data. Emits: effective primary and backup destinations. Does not own: employment scheduling or compensation.

## Open questions

- How far ahead must schedules be published before uncovered periods become escalated exceptions?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Urgent Message Escalation Ladders](openchart-feature-catalog-msg-005-urgent-message-escalation-ladders.md)
