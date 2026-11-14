# Urgent Message Escalation Ladders — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Escalates unacknowledged urgent messages through timed, governed recipient tiers until a qualified person responds.
Topics: openchart-feature-catalog, messaging-tasks, frappe, urgent-escalation
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-005 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Escalation rehearsal mode** — Run synthetic drills that measure response paths without sending clinical alerts.

## Focus

This feature isolates timeout-driven escalation for urgent staff communications while keeping acknowledgment distinct from clinical action.

## Behavior

- The sender selects an approved urgency class whose active policy defines acknowledgment deadline and escalation tiers.
- Tier targets may be users, pools, on-call roles, or supervisor roles resolved at the instant of escalation.
- A qualified recipient may acknowledge, decline with reason, or transfer responsibility to an authorized destination.
- Read status alone never stops escalation when explicit acknowledgment is required.
- Each deadline is durable across worker restarts and is recalculated only through a recorded policy exception.
- Failure to resolve a target advances to the next tier and records why the target was unavailable.
- Final-tier exhaustion creates an exception incident and exposes manual contact instructions; it never invents a recipient.
- Cancellation requires reason and authority, and all recipients receive a closure event.

## Frappe realization

- **DocTypes:** `OC Escalation Policy`, child `OC Escalation Tier`, `OC Escalation Instance`, and `OC Escalation Event` hold timing, targets, state, and evidence.
- **Workflow:** Pending → Acknowledged/Declined/Escalating → Closed/Exhausted uses guarded actions and immutable event history.
- **Automation:** `scheduler_events` enqueues idempotent deadline checks; background jobs lock the instance before advancing a tier.
- **Notifications:** Notification Log records in-app alerts, while Frappe Notification, Email Accounts, and SMS settings deliver policy-approved projections.
- **Roles/reports:** Clinical Messaging User, Escalation Supervisor, and Audit Reviewer; Script Reports measure time-to-acknowledgment and exhaustion.

## Boundaries

Owns: escalation state, deadlines, and recipient-tier evidence. Consumes: urgency policy, coverage, preferences, and delivery outcomes. Emits: alerts, acknowledgments, and exception incidents. Does not own: clinical intervention or emergency dispatch.

## Open questions

- Which urgency classes require an explicit licensed-clinician acknowledgment?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Unread Critical Phone Fallback](openchart-feature-catalog-msg-023-unread-critical-phone-fallback.md)
