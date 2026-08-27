# Skill-based Task Routing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes operational tasks to eligible teams or users using reviewed skill, scope, workload, and fallback rules.
Topics: openchart-feature-catalog, platform, frappe, task-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-045 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Routing fairness review** — Compare assignments across eligible staff to detect persistent imbalance.

## Focus

This feature isolates accountable operational assignment and leaves clinical priority and source-task creation to domain workflows.

## Behavior

- Routing administrators define task class, required skills, site and department scope, availability rules, capacity limits, priority, and fallback queue.
- Skill claims have source, verifier, effective dates, and status rather than being free-text user preferences.
- Rules move through Draft, Simulation, Review, Active, Paused, Failed, Retired, and Superseded states.
- Simulation explains eligible candidates and exclusions against synthetic tasks without creating assignments.
- Runtime routing records considered pool, selected target, rule version, reason, and fallback; no eligible target creates an unassigned escalation.
- Manual reassignment requires a reason and never erases the original routing evidence.

## Frappe realization

- **DocTypes:** `OC Routing Rule`, `OC Staff Skill`, and `OC Routing Decision` store task class, requirements, scopes, workload policy, candidates, and outcome.
- **Integration:** Frappe Assignment Rule hooks call the governed resolver and create native Assignments or queue records.
- **Permissions:** Routing Designer authors; Operations Approver activates; supervisors may reassign within permitted scopes.
- **Surface/API:** simulation Desk page, Kanban queues, and `open_chart.api.v1.platform.explain_task_route` provide decision traces.

## Boundaries

Owns: operational eligibility, routing selection, and assignment evidence. Consumes: tasks, verified skills, availability, delegation, workload, and organization scope. Emits: Assignments or escalation queues. Does not own: clinical triage or staff credentialing.

## Open questions

- Which workload signals can be used without encouraging staff to defer difficult tasks?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Provider Delegation And Coverage](openchart-feature-catalog-plt-044-provider-delegation-and-coverage.md) · [Operational Queue SLA Timers](openchart-feature-catalog-plt-046-operational-queue-sla-timers.md)
