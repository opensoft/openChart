# Declarative Business Rule Builder — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Configures reviewed if-this-then-that document rules with deterministic conditions, bounded actions, and execution evidence.
Topics: openchart-feature-catalog, platform, frappe, business-rules
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-011 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Rule conflict analyzer** — Detect overlapping conditions and incompatible actions before activation.

## Focus

This feature isolates declarative operational automation while prohibiting arbitrary code and autonomous clinical decisions by default.

## Behavior

- Rule designers select a DocType event, build allowlisted conditions, and choose actions such as assign, notify, tag, or set an approved field.
- Rules state priority, effective dates, site scope, stop-processing behavior, and an accountable owner.
- A dry run evaluates synthetic or permission-safe sampled records and explains matched clauses and proposed actions.
- Rules move through Draft, Review, Active, Paused, Failed, Retired, and Superseded states.
- Runtime execution is idempotent per rule version, document event, and action; failures do not roll back the source document.
- Actions that could alter clinical authority, orders, diagnoses, or accepted records are rejected or require a human task instead.

## Frappe realization

- **DocTypes:** `OC Business Rule`, child `OC Rule Condition`, and child `OC Rule Action` store event, JSON logic, priority, scopes, actions, and version.
- **Hooks:** a central `doc_events` dispatcher evaluates active rules after validated events and enqueues non-transactional effects.
- **Permissions:** Rule Designer authors; Rule Approver activates; execution uses a constrained service identity rather than the author.
- **Surface/API:** rule canvas, dry-run report, and `open_chart.api.v1.platform.simulate_rule` return clause-level traces.

## Boundaries

Owns: bounded declarative rule definition and execution evidence. Consumes: document events and approved fields. Emits: assignments, notifications, tags, or safe mutations. Does not own: arbitrary scripts or autonomous clinical action.

## Open questions

- Which document events provide stable enough contracts for long-lived rules?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Workflow Configuration Studio](openchart-feature-catalog-plt-010-workflow-configuration-studio.md) · [Skill-based Task Routing](openchart-feature-catalog-plt-045-skill-based-task-routing.md)
