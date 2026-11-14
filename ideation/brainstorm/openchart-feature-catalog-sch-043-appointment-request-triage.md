# Appointment Request Triage — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes incoming appointment requests through completeness and human review before search or booking when direct scheduling is unsafe.
Topics: openchart-feature-catalog, scheduling, frappe, request-triage
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-043 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Structured request guidance** — Reduce missing information with channel-specific prompts.

## Focus

This feature isolates operational intake and routing for requests that cannot immediately become bookings.

## Behavior

- Requests arrive from portal, phone, referral, recall, or integration with source and patient identity provenance.
- Required administrative fields are checked and missing items are listed explicitly.
- Rules route direct-schedulable requests to search and ambiguous or restricted requests to a review queue.
- Reviewers may approve an appointment type, request information, redirect service, decline with reason, or escalate for clinical review.
- The system never derives clinical urgency autonomously from free text.
- Every disposition records actor, timestamp, rationale, and downstream task or booking link.

## Frappe realization

- **DocTypes:** `OC Appointment Request` with source, requested_service, reason_text, completeness table, state, disposition, and provenance.
- **Workflow:** Received → Needs Information/In Review → Ready to Schedule/Redirected/Declined/Escalated.
- **Surface:** Web Forms and guarded APIs create requests; Assignment Rules, Kanban, and Notifications support review.

## Boundaries

Owns: request completeness and scheduling disposition. Consumes: patient-stated need and source context. Emits: schedulable request or review escalation. Does not own: clinical triage judgment.

## Open questions

- Which request categories require clinical review before any slot search?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Referral-driven Scheduling Queue](openchart-feature-catalog-sch-037-referral-driven-scheduling-queue.md)
