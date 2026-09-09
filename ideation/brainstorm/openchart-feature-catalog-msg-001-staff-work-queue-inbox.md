# Staff Work-queue Inbox — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives staff a pooled, filterable inbox for accountable handling of clinical and operational work items.
Topics: openchart-feature-catalog, messaging-tasks, frappe, work-queue
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-001 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Queue load balancing** — Suggest pool-to-pool transfers when aging and staffing thresholds diverge.

## Focus

This feature isolates the staff-facing In-Basket-style surface where personal and pooled work becomes visible, claimable, and auditable.

## Behavior

- Authorized staff see personal, delegated, and pool tabs with counts by urgency and age.
- Each item shows patient context when permitted, source, type, assignee, due time, and latest activity without exposing unrelated chart data.
- A user may claim an unowned pool item, release it with a reason, or open it without claiming.
- Filters cover facility, patient panel, result type, status, overdue state, and sender; saved views remain private or role-shared.
- Concurrent claims resolve transactionally so only one claimant succeeds and the losing client receives a refresh prompt.
- Read, claimed, waiting, escalated, completed, and cancelled states are distinct and timestamped.
- Pool managers may rebalance items; ordinary members cannot move work outside pools granted by user permissions.
- Empty, stale, permission-revoked, and source-deleted items retain enough provenance for safe resolution.

## Frappe realization

- **DocTypes:** `OC Work Item`, `OC Work Pool`, and child `OC Work Pool Member` hold source Dynamic Links, patient Link, priority, state, assignee, due datetime, and claim version.
- **Workflow:** Frappe Workflow governs New → Claimed → Waiting/Escalated → Completed/Cancelled with role-limited transitions.
- **Roles/permissions:** Work Queue User, Work Pool Manager, and Clinical Supervisor combine DocPerms with facility and pool user permissions.
- **Surfaces:** Desk workspace, List and Kanban views, Number Cards, and a Script Report provide inbox projections; websocket events refresh counts.
- **Hooks/API:** guarded `open_chart.api.v1.messaging.claim_work_item` and release/transition methods use row locks; `after_insert` creates Notification Log entries.

## Boundaries

Owns: work-item queue state and projections. Consumes: source records, patient identity, assignments, and routing decisions. Emits: claims, transitions, notifications, and aging metrics. Does not own: source clinical records or staffing authority.

## Open questions

- Should opening a pooled item implicitly claim it, or must claiming always be explicit?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Assignment Rule Engine](openchart-feature-catalog-msg-011-assignment-rule-engine.md)
