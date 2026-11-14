# Procedure Preparation Instructions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Delivers versioned, appointment-specific preparation instructions and records patient acknowledgement and exceptions.
Topics: openchart-feature-catalog, scheduling, frappe, prep-instructions
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-039 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Preparation question routing** — Send patient questions to the responsible team with appointment context.

## Focus

This feature isolates scheduling delivery and acknowledgement of authorized preparation content.

## Behavior

- Confirmed procedures resolve the effective instruction set by procedure, location, and patient-specific authorized additions.
- Patients receive instructions through permitted portal, email, SMS link, or print channels.
- Content is rendered in the approved language and records template version and delivery channel.
- Patients can acknowledge receipt, report inability to comply, or request help.
- Reported exceptions create assigned review tasks and never trigger autonomous clinical advice.
- Reschedule or material procedure change reevaluates due dates and sends an explicit updated version.

## Frappe realization

- **DocTypes:** `OC Preparation Instruction Set`, child steps, and `OC Appointment Preparation` with template snapshot, due dates, delivery, and acknowledgement.
- **Automation:** Notification doctypes and `scheduler_events` send due instruction steps; portal Web Forms capture acknowledgement and exceptions.
- **Surface:** Jinja Print Formats support handouts; staff List/Kanban views show outstanding preparation tasks.

## Boundaries

Owns: instruction delivery, version snapshot, and acknowledgement. Consumes: clinically authorized content and procedure booking. Emits: readiness evidence or exception task. Does not own: clinical instruction authorship.

## Open questions

- Which preparation exceptions require immediate escalation versus routine review?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Procedure Scheduling](openchart-feature-catalog-sch-038-procedure-scheduling.md)
