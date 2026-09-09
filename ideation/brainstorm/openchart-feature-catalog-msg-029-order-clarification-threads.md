# Order Clarification Threads — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates a closed-loop clarification conversation between ordering and performing staff without silently changing the clinical order.
Topics: openchart-feature-catalog, messaging-tasks, frappe, order-clarification
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-029 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Clarification reason analytics** — Identify recurring order defects for human-reviewed order-set improvement.

## Focus

This feature isolates laboratory, imaging, pharmacy, and procedure clarification while protecting the authority boundary of the source order.

## Behavior

- Performing staff open a clarification from an order with a coded reason, question, urgency, and optional proposed correction.
- The thread snapshots order version, requester, performer context, and relevant fields at creation.
- Authorized ordering clinicians may answer, amend the order through its governed API, cancel it, or redirect the question.
- A text reply never modifies dose, test, priority, indication, or other order fields.
- The thread shows whether a linked order amendment superseded the questioned version.
- Urgent unanswered clarifications follow an approved escalation ladder and preserve service coverage resolution.
- Closure requires disposition and, when applicable, a link to accepted order amendment or cancellation evidence.
- Multiple clarifications on one order remain distinct but surface potential duplicates.

## Frappe realization

- **DocTypes:** `OC Order Clarification`, `OC Clarification Entry`, and `OC Clarification Disposition` use order Dynamic Link, snapshot JSON, reason code, urgency, state, and resolution Link.
- **Workflow:** Open → Awaiting Orderer/Awaiting Performer → Resolved/Cancelled/Escalated.
- **Hooks/API:** creation and replies are guarded under `open_chart.api.v1.messaging`; order changes invoke the owning versioned order API, never direct writes.
- **Assignment/notifications:** Assignment Rules route by performing service and current ordering coverage; Notification Log records attention events.
- **Reports:** age, reason, service, escalation, and order-amendment linkage appear in Query Reports.

## Boundaries

Owns: clarification conversation and disposition evidence. Consumes: order snapshot, ordering authority, service routing, and amendments. Emits: questions, answers, and resolution links. Does not own: order content or execution status.

## Open questions

- Which clarification reasons should suspend order execution automatically versus require a human hold?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Abnormal-result Notification Composition](openchart-feature-catalog-msg-031-abnormal-result-notification-composition.md)
