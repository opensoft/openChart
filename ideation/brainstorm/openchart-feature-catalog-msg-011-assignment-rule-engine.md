# Assignment Rule Engine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates governed criteria to assign incoming work deterministically and preserve a human-readable decision trace.
Topics: openchart-feature-catalog, messaging-tasks, frappe, assignment-engine
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-011 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Shadow evaluation** — Compare a proposed assignment policy with production outcomes without changing destinations.

## Focus

This feature isolates the reusable evaluation runtime that turns approved routing policies into assignments across messages, tasks, and inbound requests.

## Behavior

- An eligible event is evaluated against active rules for its DocType, facility, and effective timestamp.
- Criteria use a constrained field/operator vocabulary and cannot execute arbitrary code.
- Deterministic precedence produces one destination, a documented fan-out, or an exception outcome.
- The engine rechecks destination eligibility immediately before assignment.
- Reprocessing the same event and policy version is idempotent.
- Failed evaluations retain the item in an exception queue with structured cause and retry eligibility.
- A dry run returns matched facts, skipped rules, chosen action, and fallback without mutating work.
- Manual override records actor, reason, former decision, and whether future reevaluation is suppressed.

## Frappe realization

- **Model:** Frappe Assignment Rules perform supported document assignment; `OC Assignment Decision` stores event key, rule, facts digest, destination, outcome, and override.
- **Hooks:** `after_insert` or explicit integration events enqueue evaluation; no heavy rule processing runs synchronously inside an unbounded request.
- **API:** `open_chart.api.v1.messaging.evaluate_assignment` supports guarded execution and preview modes.
- **Permissions:** Assignment Rule Manager authors criteria; Clinical Supervisor activates clinical policies; Audit Reviewer sees decision traces.
- **Surfaces:** exception List view, policy test dialog, and Script Report for unmatched, overridden, and failed decisions.

## Boundaries

Owns: constrained evaluation, assignment application, and decision evidence. Consumes: approved policies and event facts. Emits: assignments or exceptions. Does not own: clinical routing semantics, staffing, or credentialing.

## Open questions

- Which event types may fan out to multiple accountable destinations rather than one owner?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Clinical Message Routing Rules](openchart-feature-catalog-msg-002-clinical-message-routing-rules.md)
