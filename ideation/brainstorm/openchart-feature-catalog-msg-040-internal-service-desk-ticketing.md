# Internal Service-desk Ticketing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides nonclinical IT and administrative ticket intake, assignment, service levels, conversation, and resolution inside the platform.
Topics: openchart-feature-catalog, messaging-tasks, frappe, service-desk
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-040 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Known-issue deflection** — Suggest approved internal guidance before ticket submission without exposing other reporters' data.

## Focus

This feature isolates internal operational support work while keeping clinical messaging and patient-care tasks visibly separate.

## Behavior

- Staff submit a ticket with category, facility, affected service, impact, urgency, description, and secure attachments.
- Intake warns against unnecessary PHI and supports a restricted sensitivity class when patient context is essential.
- Assignment rules route tickets to IT, facilities, access, data, or administrative pools.
- Agents claim, comment, request information, change priority with reason, link duplicates, and resolve with outcome code.
- Service-level clocks account for waiting-on-requester state and approved business calendars.
- Requesters receive status and reply notifications but cannot view internal notes or unrelated tickets.
- Reopening preserves the prior resolution and reason; duplicate closure links to the retained primary ticket.
- Clinical urgency entered in a service-desk ticket triggers guidance to the appropriate clinical channel, not automatic clinical routing.

## Frappe realization

- **DocTypes:** `OC Service Ticket`, `OC Ticket Entry`, `OC Ticket SLA`, and `OC Ticket Resolution` hold requester, category, assignment, priority, timers, visibility, links, and outcomes.
- **Workflow:** New → Assigned/In Progress/Waiting → Resolved/Closed/Reopened with role-gated priority and cancellation actions.
- **Assignment/notifications:** Frappe Assignment Rules route categories; Notification Log and configured Email Accounts provide staff updates.
- **Views:** Desk workspace, Kanban, SLA Number Cards, Calendar/Gantt for planned work, and aging/resolution Script Reports.
- **Permissions:** Service Desk User, Service Agent, Pool Manager, and Restricted Ticket Reviewer use permlevels and facility user permissions.

## Boundaries

Owns: internal nonclinical ticket state, conversation, SLA, and resolution. Consumes: staff identity, service catalog, assignment policy, and attachments. Emits: support work and operational metrics. Does not own: clinical advice, patient messaging, enterprise asset management, or external customer support.

## Open questions

- Which restricted ticket categories require separate storage or security-team-only access?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Staff Work-queue Inbox](openchart-feature-catalog-msg-001-staff-work-queue-inbox.md)
