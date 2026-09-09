# Mass Recall and Disruption Notifications — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates urgent high-volume notifications for closures, product recalls, provider departures, and other governed disruptions.
Topics: openchart-feature-catalog, messaging-tasks, frappe, mass-recall
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-032 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Disruption command board** — Combine audience readiness, approvals, delivery progress, inbound replies, and unresolved exceptions.

## Focus

This feature isolates operationally urgent cohort outreach where speed, authorization, versioned instructions, and exception handling must coexist.

## Behavior

- An incident owner records disruption type, scope, severity, effective interval, authoritative source, and response instructions.
- Authorized audience builders produce a frozen affected-patient or staff snapshot with inclusion evidence.
- Message variants support language, channel, facility, and recipient role while sharing one incident version.
- Dual approval may be required for clinical recall or provider-departure content before release.
- Execution rechecks contact restrictions and uses documented essential-communication exceptions only when applicable.
- Corrected instructions create a new incident communication wave linked to the superseded wave.
- Delivery failures, opt-outs, replies, and unreachable high-priority recipients enter accountable exception queues.
- Closing the incident requires an unresolved-recipient summary and does not erase communication history.

## Frappe realization

- **DocTypes:** `OC Communication Incident`, `OC Incident Audience Snapshot`, `OC Incident Wave`, and `OC Incident Recipient` store scope, source, severity, versions, approvals, and outcomes.
- **Workflow:** Draft → Review → Approved → Active → Resolved/Cancelled with stricter roles for clinical recalls.
- **Automation:** RQ jobs process waves in bounded batches; `scheduler_events` starts scheduled waves and monitors unresolved exceptions.
- **Channels:** Frappe SMS settings and Email Accounts dispatch; Notification Log coordinates staff approvals and exception work.
- **Surfaces:** incident dashboard, delivery map, reply queue, and after-action Script Report.

## Boundaries

Owns: communication incident, audience snapshot, waves, and delivery exceptions. Consumes: authoritative disruption facts, cohort data, consent policy, templates, and gateways. Emits: notifications and unresolved-recipient work. Does not own: incident command, clinical recall adjudication, or scheduling changes.

## Open questions

- Which emergency or essential purposes permit contact despite ordinary channel suppression?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Broadcast Campaigns to Patient Cohorts](openchart-feature-catalog-msg-016-broadcast-campaigns-to-patient-cohorts.md)
