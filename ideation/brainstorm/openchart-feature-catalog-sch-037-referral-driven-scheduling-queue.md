# Referral-driven Scheduling Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes accepted referral scheduling needs into prioritized work queues with completeness, outreach, and booking states.
Topics: openchart-feature-catalog, scheduling, frappe, referral-queue
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-037 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Referral capacity routing** — Suggest a permitted location when the preferred queue cannot meet the target window.

## Focus

This feature isolates operational scheduling after a referral source authorizes and supplies a request.

## Behavior

- Accepted requests enter a queue with service, priority, target window, completeness, and source provenance.
- Incomplete requests remain Needs Information and list specific missing scheduling inputs.
- Assignment rules route work by service, location, urgency band, and staff coverage.
- Staff record outreach attempts, patient preferences, booking, deferral, refusal, or return to referral review.
- Target-window breaches escalate without silently changing clinical priority.
- A booked appointment links to the request and closes only the scheduling portion of the workflow.

## Frappe realization

- **DocTypes:** `OC Referral Scheduling Task` with source Dynamic Link, completeness items, target window, assignee, state, and appointment.
- **Workflow:** Needs Information → Ready → Outreach → Booked/Deferred/Returned/Closed; Assignment Rules distribute work.
- **Surface:** Kanban, List, and Script Reports expose queue age and SLA bands; Notifications alert on assignment and escalation.

## Boundaries

Owns: referral scheduling work queue. Consumes: accepted referral intent and scheduling inputs. Emits: outreach and linked booking. Does not own: referral acceptance or clinical priority.

## Open questions

- Which missing inputs block all outreach versus only final booking?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Request Triage](openchart-feature-catalog-sch-043-appointment-request-triage.md)
