# Group and Class Appointments — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Schedules capacity-limited group sessions while preserving each participant's privacy and attendance record.
Topics: openchart-feature-catalog, scheduling, frappe, group-appointments
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-018 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Course enrollment** — Link multiple group sessions into a bounded curriculum.

## Focus

This feature isolates shared-session capacity and participant enrollment rather than ordinary one-patient bookings.

## Behavior

- Staff create a session with facilitator, location or telehealth room, capacity, enrollment rules, and waitlist behavior.
- Each patient receives an individual enrollment linked to the shared session.
- Participants cannot see the names or status of other participants through portal or notifications.
- Full sessions reject new enrollment or route eligible patients to a class-specific waitlist.
- Session cancellation notifies all active enrollments and records delivery outcomes separately.
- Attendance is recorded per participant without changing the shared session's completion state prematurely.

## Frappe realization

- **DocTypes:** `OC Group Session` and child-linked `OC Group Enrollment` with patient, state, consent, and attendance.
- **Surface:** native Calendar view shows sessions once; enrollment List/Kanban views and portal pages enforce row-level ownership.
- **Automation:** auto-repeat can seed recurring class sessions; Notification doctypes render participant-specific messages.

## Boundaries

Owns: session capacity and enrollment. Consumes: facilitator and location availability. Emits: individual attendance scheduling records. Does not own: group clinical notes.

## Open questions

- Should recurring classes require enrollment in all sessions or permit drop-in attendance?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Recurring Appointment Series](openchart-feature-catalog-sch-005-recurring-appointment-series.md)
