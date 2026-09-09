# Operational Queue SLA Timers — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies versioned service-time policies to operational queue items with pause reasons, escalation, and explainable deadlines.
Topics: openchart-feature-catalog, platform, frappe, sla-timers
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-046 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **SLA policy simulator** — Replay historical timestamps against proposed calendars and pause rules without changing records.

## Focus

This feature isolates operational accountability timers and does not reinterpret clinical urgency or create care decisions.

## Behavior

- Operations administrators define task class, priority, response and resolution targets, working calendar, pause reasons, and escalation ladder.
- Policies move through Draft, Review, Active, Retired, and Superseded states with effective dates.
- New queue items pin the policy version and calculate explainable deadlines from site-local working time.
- Authorized transitions may pause or resume a timer with reason; retroactive edits require supervisor correction evidence.
- Warning and breach events create notifications or assignments once per threshold and remain visible after resolution.
- Missing calendars or malformed policy fail safe to a visible review state rather than an untracked deadline.

## Frappe realization

- **DocTypes:** `OC SLA Policy` and `OC SLA Timer` store task class, targets, Holiday List/Location Calendar, pauses, deadlines, state, and policy version.
- **Automation:** scheduler events find approaching or breached timers; document hooks recalculate on authorized state transitions.
- **Permissions:** SLA Administrator publishes policies; queue workers view timers; supervisors correct pauses and acknowledge breaches.
- **Surface:** List indicators, Number Cards, Dashboard Charts, and Script Reports show age, risk, breaches, and exclusions.

## Boundaries

Owns: operational deadline calculation, pause evidence, and escalation events. Consumes: queue state, priority, and working calendars. Emits: deadlines, warnings, breaches, and assignments. Does not own: clinical urgency or labor commitments.

## Open questions

- When policy changes, should open items retain their pinned target or adopt the new version prospectively?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Skill-based Task Routing](openchart-feature-catalog-plt-045-skill-based-task-routing.md) · [Location Holiday Calendars](openchart-feature-catalog-plt-041-location-holiday-calendars.md)
