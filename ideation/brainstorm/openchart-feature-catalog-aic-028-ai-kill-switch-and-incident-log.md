# AI Kill Switch And Incident Log — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides immediate capability suspension with immutable scope, actor, reason, impact, and recovery evidence.
Topics: openchart-feature-catalog, clinical-ai, frappe, kill-switch
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-028 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Safe-mode banner** — Tell affected users which capability is unavailable and which manual workflow remains authoritative.

## Focus

This feature isolates rapid containment and its incident record across AI capabilities.

## Behavior

- Authorized operators can suspend one capability, model deployment, adapter, site scope, or all external inference immediately.
- New invocations fail closed after switch activation; queued jobs are canceled or quarantined according to scope.
- In-progress user surfaces show unavailability and preserve manual workflows and unsaved user content.
- Activation creates an incident record with actor, reason, scope, time, impacted work, notifications, and artifact quarantine decisions.
- Recovery requires documented validation, approver, staged re-enable scope, and monitoring period.
- No provider callback or model response can clear a kill switch.

## Frappe realization

- **DocTypes:** Single `OC AI Emergency Control` holds current global state; `OC AI Incident` and events preserve scoped changes, impacts, evidence, and recovery plan.
- **Workflow:** incident Open → Contained → Investigating → Recovery Review → Closed; control changes require named whitelisted methods.
- **Roles/permissions:** `OC AI Incident Commander` can suspend; re-enable requires `OC AI Governor`; all changes create audit and Notification Log entries.
- **Hooks/jobs/surfaces:** invoke and queue hooks check uncached control state; background job cancellation/quarantine; prominent Workspace control and incident Script Report.

## Boundaries

Owns: immediate AI suspension and containment evidence. Consumes: operator scope and incident signals. Emits: deny state, quarantines, notifications, and recovery gates. Does not own: deletion of clinical records or bypass of manual care workflows.

## Open questions

- Which emergency scopes may a site operator suspend without central approval?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Incident Response Workflow](openchart-feature-catalog-aic-046-ai-incident-response-workflow.md)
