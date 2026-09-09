# Task Delegation and Reassignment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Transfers task responsibility between authorized people and pools while preserving acceptance, reason, and custody history.
Topics: openchart-feature-catalog, messaging-tasks, frappe, task-delegation
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-008 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Delegation guardrails** — Warn when a proposed assignee lacks role, facility, panel, or workload suitability.

## Focus

This feature isolates accountable custody transfer rather than treating assignee edits as ordinary field changes.

## Behavior

- A current assignee, pool manager, or supervisor may propose reassignment to an eligible user or pool.
- Policy determines whether transfer is immediate or requires the recipient to accept before custody changes.
- The proposal includes reason, requested-by, old destination, new destination, and effective timestamp.
- A recipient may accept, decline with reason, or let the proposal expire while the original assignee remains accountable.
- Urgent tasks cannot be left unowned during transfer and continue their existing escalation clock.
- Bulk reassignment supports coverage events but returns a per-task success or denial result.
- Reassignment to an unauthorized or inactive destination fails without changing the current task.
- History shows every proposal, acceptance, decline, override, and system-generated coverage transfer.

## Frappe realization

- **DocTypes:** `OC Task Transfer` links `OC Clinical Task`, from/to user or pool, reason, acceptance mode, expiry, actor, and outcome.
- **Workflow:** Proposed → Accepted/Declined/Expired/Cancelled; accepted transfer updates task custody in one transaction.
- **Roles/permissions:** Task User, Work Pool Manager, and Task Supervisor; user permissions constrain facility and pool destinations.
- **Automation:** `scheduler_events` expires proposals and coverage jobs submit explicit transfer records rather than editing assignees directly.
- **Notifications/API:** Notification Log prompts recipients; guarded transfer methods expose structured eligibility failures.

## Boundaries

Owns: custody-transfer requests and history. Consumes: task state, eligibility, and coverage policy. Emits: accepted assignment changes and notifications. Does not own: workforce credentialing or task content.

## Open questions

- Which task classes permit immediate supervisor override without recipient acceptance?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Coverage and Out-of-office Forwarding](openchart-feature-catalog-msg-012-coverage-and-out-of-office-forwarding.md)
