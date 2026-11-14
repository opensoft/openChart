# Mobile Clinical Task Inbox — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Unifies assigned mobile work into an actionable inbox with explicit ownership, due state, and links back to authoritative workflows.
Topics: openchart-feature-catalog, mobile-devices, frappe, task-inbox
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-007 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Shift handoff bundles** — Transfer selected unresolved assignments with acknowledgement and audit evidence.

## Focus

This entry isolates mobile discovery and disposition of assigned work rather than creating a second task authority.

## Behavior

- Users see assignments from supported clinical workflows grouped by urgency, due time, patient, and source type.
- Each item identifies owner, assigner, source record, due state, and permitted actions.
- Claim, acknowledge, complete, defer, or reassign actions are offered only when the source workflow allows them.
- Completing an inbox item invokes the source transition and never marks work done solely in the presentation layer.
- Offline users may read cached assignments and queue allowed acknowledgements with visible pending state.
- Conflicting reassignment or completion is rejected on sync and returns the current owner and state.
- Restricted patient details disappear while a non-PHI audit stub may remain for operational reconciliation.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Use Frappe `ToDo`/Assignment plus `OC Mobile Task Projection` containing source Dynamic Link, action schema, due state, and source version.
- **Roles and permissions:** Source DocPerms govern visibility and transitions; `OC Clinical Supervisor` may reassign only within configured facility and team user permissions.
- **API and auth:** Expose TLS token-authenticated `open_chart.api.v1.mobile.tasks` and `act_on_task`; resolve allowed actions server-side and block projection writes.
- **Realtime and jobs:** Send assignment invalidations over websocket and use server-side RQ jobs to project heterogeneous queues and retry notifications.
- **Files and surfaces:** Source files remain private Frappe attachments fetched only after fresh authorization; mobile inbox mirrors Desk assignments and a Query Report.

## Boundaries

Owns: mobile task projection and action routing. Consumes: assignments and source workflow permissions. Emits: authoritative transition requests and acknowledgements. Does not own: clinical priority, source completion rules, or staffing policy.

## Open questions

- Which source workflows are safe for offline acknowledgement versus online-only completion?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
