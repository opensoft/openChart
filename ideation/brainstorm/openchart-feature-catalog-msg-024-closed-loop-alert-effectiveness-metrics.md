# Closed-loop Alert Effectiveness Metrics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures alert delivery, acknowledgment, escalation, and interruption burden to support human review of alarm-fatigue reduction.
Topics: openchart-feature-catalog, messaging-tasks, frappe, alert-fatigue
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-024 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Alert policy review packets** — Assemble high-volume, low-action, and escalation-heavy alert classes for governance review.

## Focus

This feature isolates closed-loop messaging measures that reveal responsiveness and burden without autonomously suppressing clinical alerts.

## Behavior

- Authorized reviewers select alert class, service, facility, policy version, period, and permitted strata.
- Measures distinguish generated, attempted, delivered, read, acknowledged, declined, escalated, exhausted, and linked-action states.
- Duplicate or correlated alerts are counted under a documented episode rule and remain drillable to source evidence.
- Time-to-read, time-to-acknowledgment, escalation depth, after-hours volume, and repeat-recipient burden are reported.
- Delivery failure and unavailable-recipient causes remain visible rather than disappearing from denominators.
- Small-cell suppression and role checks protect patient and staff confidentiality.
- Trend flags invite human review but do not change routing, severity, or suppression automatically.
- Every chart displays metric definition, data freshness, and policy versions.

## Frappe realization

- **DocTypes:** `OC Alert Metric Definition` and `OC Alert Metric Snapshot` store episode logic, dimensions, measures, suppression, versions, and refresh time.
- **Automation:** `scheduler_events` aggregates immutable message, receipt, escalation, and call events in bounded jobs.
- **Surfaces:** Dashboard Charts, Number Cards, Script Reports, and role-scoped drilldown pages.
- **Permissions:** Messaging Quality Analyst and Clinical Safety Reviewer see aggregates; Audit Reviewer accesses source events under separate authority.
- **Audit:** exports and policy-review annotations are logged; no dashboard action directly edits active routing rules.

## Boundaries

Owns: alert-effectiveness and burden measures. Consumes: generation, delivery, read, acknowledgment, escalation, and action-link events. Emits: reviewable metrics. Does not own: alert clinical logic or autonomous suppression.

## Open questions

- What linked action evidence is reliable enough to distinguish useful alerts from acknowledged-only noise?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Recipient Read and Acknowledgment Tracking](openchart-feature-catalog-msg-006-recipient-read-and-acknowledgment-tracking.md)
