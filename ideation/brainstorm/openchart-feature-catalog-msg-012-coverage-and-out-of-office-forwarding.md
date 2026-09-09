# Coverage and Out-of-office Forwarding — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Redirects eligible work during approved absences while preserving original responsibility, scope, and forwarding evidence.
Topics: openchart-feature-catalog, messaging-tasks, frappe, coverage-forwarding
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-012 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Coverage readiness check** — Detect uncovered pools, conflicting delegates, and expiring handoffs before an absence begins.

## Focus

This feature isolates time-bounded absence coverage and forwarding policy for new and already-open work.

## Behavior

- A user or manager records an absence interval, reason category, scope, and authorized delegate or pool.
- Policy distinguishes forwarding newly arriving items from transferring selected open items.
- Clinical task types may require manager approval or prohibit forwarding outside a qualified role.
- Forwarded items display the absent owner, current covering destination, and coverage end time.
- Overlapping absences resolve by explicit precedence and surface conflicts before activation.
- Coverage begins and ends at timezone-safe instants; end processing does not pull back work already accepted.
- If the delegate becomes unavailable, work follows the configured coverage fallback or exception queue.
- Every generated transfer links to the coverage record and retains per-item success or failure.

## Frappe realization

- **DocTypes:** `OC Coverage Arrangement` and child `OC Coverage Scope` store owner, delegate, interval, item classes, facility, approval, and fallback.
- **Workflow:** Draft → Pending Approval → Active → Ended/Cancelled, with manager approval for protected scopes.
- **Automation:** `scheduler_events` activates and ends arrangements; background jobs process bounded item batches idempotently.
- **Assignment:** Frappe Assignment Rules consume active coverage as a destination resolver; explicit `OC Task Transfer` records move existing items.
- **Permissions/surfaces:** users manage their drafts, Coverage Managers approve scoped records, and Calendar/List views show active coverage.

## Boundaries

Owns: absence forwarding policy and transfer provenance. Consumes: staff identity, task classes, and destination eligibility. Emits: routing substitutions and explicit transfers. Does not own: leave approval, payroll, or credentialing.

## Open questions

- Which open urgent items must be positively accepted by coverage before an absence begins?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [On-call Coverage Calendar](openchart-feature-catalog-msg-013-on-call-coverage-calendar.md)
