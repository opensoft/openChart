# Department Document Routing Inbox — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes indexed documents into accountable department queues with assignment, acknowledgment, escalation, and completion evidence.
Topics: openchart-feature-catalog, documents, frappe, department-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-007 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Load-balanced routing rules** — Assign eligible work by department, class, urgency, facility, and current queue load.

## Focus

This feature isolates operational delivery of a document to a responsible department after identity and classification are confirmed.

## Behavior

- An indexer or routing rule sends an accepted document to one department inbox with priority and reason.
- Eligible department staff can claim, reassign, return, or acknowledge the item according to role policy.
- Opening a document does not count as acknowledgment; the user must record a disposition.
- Due times derive from document class and urgency, with reminders and escalation for unclaimed or overdue items.
- A returned item requires a reason and goes to a named resolution queue rather than disappearing.
- Completion records actor, disposition, linked follow-up artifact, and timestamp.
- Superseded documents visibly invalidate open routing items and create replacement work when policy requires.

## Frappe realization

- **DocTypes:** `OC Document Route` (document_version, department, priority, due_at, assigned_to, disposition, successor_route) and `OC Document Routing Rule`.
- **Workflow:** Queued → Claimed → Acknowledged → Completed, with Returned, Escalated, and Invalidated states.
- **Roles/permissions:** Department Document User works own department queue; Document Router reassigns; Health Information Manager audits; user permissions constrain facility and department.
- **Automation:** Assignment Rules, Notifications, scheduler_events, and Notification Log drive claim and escalation without automatic clinical disposition.
- **Surfaces:** Department Desk workspace offers list/Kanban views, Number Cards, and a Script Report for overdue routes.

## Boundaries

Owns: route, assignment, acknowledgment, escalation, and operational completion. Consumes: accepted indexed document and routing policy. Emits: accountable disposition event. Does not own: clinical order fulfillment, document content, or patient identity resolution.

## Open questions

- Which dispositions require a linked chart action before routing can close?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Unmatched-document Resolution Queue](openchart-feature-catalog-dms-008-unmatched-document-resolution-queue.md)
