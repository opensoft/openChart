# Recall-driven Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts due recalls into traceable scheduling outreach and appointments without treating a recall as a clinical order.
Topics: openchart-feature-catalog, scheduling, frappe, recall-scheduling
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-017 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Recall campaign balancing** — Pace outreach against forecast appointment capacity.

## Focus

This feature isolates the scheduling workflow that begins when an authorized recall becomes due.

## Behavior

- Due recalls enter a scheduling queue with patient, reason, target window, priority, and source provenance.
- Staff can contact, defer with reason, book, mark unreachable, or return an invalid recall for review.
- Self-scheduling links show only appointment types and windows authorized by the recall.
- A successful booking links the recall and closes the scheduling task without altering clinical source data.
- Repeated outreach follows consent and cadence limits and stops after booking or withdrawal.
- Overdue recalls escalate visibly but never generate autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC Recall Scheduling Task` with source Dynamic Link, target window, contact attempts, state, and appointment.
- **Workflow:** Due → Outreach → Booked/Deferred/Unreachable/Returned; Assignment Rules route by service.
- **Automation:** `scheduler_events` opens due tasks and sends approved Notification-doctype outreach through background jobs.

## Boundaries

Owns: recall-to-booking operations. Consumes: authorized recall due dates and consent. Emits: outreach and linked appointment. Does not own: recall clinical criteria.

## Open questions

- How many outreach attempts are appropriate before manual review?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Referral-driven Scheduling Queue](openchart-feature-catalog-sch-037-referral-driven-scheduling-queue.md)
