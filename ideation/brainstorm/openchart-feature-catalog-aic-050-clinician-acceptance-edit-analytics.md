# Clinician Acceptance And Edit Analytics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures exposure, acceptance, rejection, edit patterns, review time, and downstream disposition without equating adoption with safety.
Topics: openchart-feature-catalog, clinical-ai, frappe, acceptance-analytics
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-050 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Workflow burden comparison** — Compare review effort with a non-AI baseline before claiming efficiency gains.

## Focus

This feature isolates human-interaction analytics across AI drafting and suggestion capabilities.

## Behavior

- Each eligible surface records exposure, open time, first action, accept, reject, regenerate, edit distance, material correction class, and final disposition.
- Metrics distinguish full acceptance, acceptance after material edits, partial use, rejection, abandonment, and no exposure.
- Dashboards stratify by capability, model, profile, site, role, and time while suppressing small cohorts.
- Individual clinician metrics are restricted from punitive ranking unless a separately governed purpose permits them.
- High acceptance is never labeled accuracy, safety, or clinical benefit without independent evidence.
- Missing instrumentation and workflow changes are visible in metric coverage.

## Frappe realization

- **DocTypes:** `OC AI Review Interaction` stores artifact, surface, actor pseudonym/role, timestamps, actions, diff metrics, correction class, and instrumentation version.
- **Roles/permissions:** AI governors see aggregates; patient-level or named-user drill-down requires `OC AI Auditor` and recorded purpose.
- **Hooks/jobs/reports:** client events post to a whitelisted append-only API; destination hooks record final disposition; scheduler aggregates; Dashboard Charts and Script Reports apply suppression.
- **Server scripts:** local metric definitions may extend approved event mappings but cannot expose content or bypass privacy thresholds.

## Boundaries

Owns: review interaction telemetry and aggregate adoption metrics. Consumes: artifact, UI events, edits, and destination state. Emits: privacy-aware workflow evidence. Does not own: performance appraisal, safety conclusions, or automatic optimization.

## Open questions

- What governance is required before named-user analytics can support training or workflow coaching?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Drift Monitoring](openchart-feature-catalog-aic-026-ai-drift-monitoring.md)
