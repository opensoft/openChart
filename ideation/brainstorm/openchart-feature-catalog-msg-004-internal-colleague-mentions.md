# Internal Colleague Mentions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets staff mention authorized colleagues in messages and tasks with resolvable notification and accountability semantics.
Topics: openchart-feature-catalog, messaging-tasks, frappe, colleague-mentions
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-004 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Role-aware mention suggestions** — Rank eligible colleagues by care-team relationship, coverage, and current availability.

## Focus

This feature isolates `@mention` behavior so attention signals remain permission-safe and do not silently become task assignments.

## Behavior

- Typing `@` searches only active users the author may involve in the current patient or operational context.
- Selecting a colleague inserts a stable user reference while displaying the current full name.
- Posting creates a mention event and in-app notification; configured email or mobile delivery remains a projection.
- A mention does not assign ownership unless the author explicitly chooses an assign action.
- Mentions to unavailable users display coverage guidance and may offer an authorized alternate.
- Duplicate mentions in one entry collapse to one notification while preserving rendered text.
- If authorization changes before posting, validation rejects the mention and identifies the affected recipient.
- Mention read and acknowledgment state can be inspected without exposing other recipients' private preferences.

## Frappe realization

- **DocTypes:** `OC Mention Event` links source DocType/name, author, mentioned User, patient context, delivery state, and timestamp.
- **Client/hooks:** a Desk editor autocomplete calls a whitelisted eligible-user search; `validate` rechecks authority and `after_insert` creates one event per user.
- **Notifications:** Notification Log is authoritative for in-app delivery; Frappe Notification may project allowed email events through configured channels.
- **Roles/permissions:** source-document permissions and care-team/facility user permissions constrain suggestions and delivery.
- **API:** `open_chart.api.v1.messaging.eligible_mentions` returns minimum user display data and structured denial reasons.

## Boundaries

Owns: mention parsing, stable references, and attention events. Consumes: source permissions, user status, and coverage. Emits: notification events. Does not own: assignment, delegation, or clinical responsibility.

## Open questions

- Should mentioning a pool alias notify every member or create one claimable pool event?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Task Delegation and Reassignment](openchart-feature-catalog-msg-008-task-delegation-and-reassignment.md)
