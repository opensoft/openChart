# No-answer Cross-channel Retry Ladders — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Executes bounded, preference-aware retries across SMS, email, phone, and portal when a required patient contact receives no answer.
Topics: openchart-feature-catalog, messaging-tasks, frappe, retry-ladders
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-036 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Reachability policy simulation** — Show how a synthetic contact episode advances across channels, quiet hours, and stop conditions.

## Focus

This feature isolates contact retry state and channel progression, distinct from reminder content and the clinical reason for outreach.

## Behavior

- A contact episode references purpose, patient, required response, urgency, deadline, and active retry policy.
- Policy defines ordered attempts, delays, channel eligibility, maximum count, and final unresolved action.
- Before each attempt, the service rechecks response state, preference resolution, do-not-contact rules, destination validity, and quiet hours.
- Delivery failure, delivered-no-response, explicit decline, opt-out, and wrong destination follow distinct transitions.
- Any qualifying patient response stops pending attempts idempotently and records the satisfying event.
- Cross-channel messages share an episode identifier and avoid repeating sensitive content beyond each channel's policy.
- Exhaustion creates assigned manual follow-up or review rather than continuing indefinitely.
- Policy changes apply to new episodes unless an authorized migration records the revised future path.

## Frappe realization

- **DocTypes:** `OC Contact Retry Policy`, child `OC Retry Step`, `OC Contact Episode`, and `OC Contact Attempt` hold purpose, sequence, timing, channel, outcome, and stop event.
- **Automation:** `scheduler_events` enqueues due steps; RQ jobs lock episodes and revalidate eligibility before dispatch.
- **Channels:** SMS settings, Email Accounts, portal notifications, and generated Voice Call Tasks use shared idempotency keys.
- **Assignment:** final unresolved actions use Assignment Rules; Notification Log alerts staff to exceptions.
- **Reports:** Script Report exposes reach by step, channel switches, suppressions, exhaustion, and response latency.

## Boundaries

Owns: retry sequence, attempt state, and exhaustion. Consumes: purpose policy, preferences, contact restrictions, delivery, and response events. Emits: channel attempts or manual follow-up work. Does not own: message content or clinical urgency.

## Open questions

- When does switching channels improve reach enough to justify added privacy exposure and cost?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Patient Notification Preference Resolution](openchart-feature-catalog-msg-021-patient-notification-preference-resolution.md)
