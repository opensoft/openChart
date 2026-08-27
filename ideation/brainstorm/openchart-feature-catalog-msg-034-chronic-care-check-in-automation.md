# Chronic-care Check-in Automation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates consent-aware chronic-care check-in touchpoints from clinician-approved cadence plans and routes responses to accountable staff.
Topics: openchart-feature-catalog, messaging-tasks, frappe, chronic-care-check-ins
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-034 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Adaptive cadence proposal** — Suggest a clinician-reviewed cadence change from response and reachability patterns without applying it automatically.

## Focus

This feature isolates recurring outreach and response triage for chronic-care programs while preserving clinician ownership of the care plan.

## Behavior

- A clinician enrolls a patient with program, approved cadence, channel options, start/end, and response expectations.
- Each check-in uses a versioned script or questionnaire and revalidates consent, contact restrictions, and active enrollment.
- Responses are stored with source channel, time, patient or proxy identity evidence, and question version.
- Reviewed response rules may classify administrative completion, routine staff review, or urgent review queue placement.
- No patient answer directly changes medication, diagnosis, care plan, or orders.
- Missing responses follow a bounded retry ladder and then create staff follow-up work.
- Clinicians may pause, change, or end cadence with reason; previously captured responses remain linked to the version used.
- Program dashboards distinguish delivered, responded, reviewed, escalated, paused, and unreachable states.

## Frappe realization

- **DocTypes:** `OC Care Check-in Plan`, `OC Check-in Instance`, and `OC Check-in Response` hold care-plan Link, cadence, script version, channel, identity evidence, review class, and state.
- **Workflow:** plan Draft → Active → Paused/Ended; instances Planned → Sent → Responded/No Response → Reviewed/Escalated.
- **Automation:** `scheduler_events` materializes and sends due instances through RQ jobs and the reminder engine.
- **Assignment:** Assignment Rules route responses by program, patient panel, review class, and coverage; Notification Log alerts staff.
- **Permissions/reports:** Care Program Clinician and Care Coordinator roles; dashboard charts show response and review timeliness.

## Boundaries

Owns: check-in cadence execution, response capture, and review routing. Consumes: clinician-approved care plan, scripts, preferences, and patient replies. Emits: response work and engagement metrics. Does not own: care-plan decisions or autonomous clinical action.

## Open questions

- Which response classifications require immediate human review rather than routine queue placement?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [No-answer Cross-channel Retry Ladders](openchart-feature-catalog-msg-036-no-answer-cross-channel-retry-ladders.md)
