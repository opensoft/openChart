# AI Drift Monitoring — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Monitors capability quality proxies such as acceptance, edit distance, failure mix, latency, and input shift over time.
Topics: openchart-feature-catalog, clinical-ai, frappe, drift-monitoring
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-026 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Change-point review packet** — Assemble model, prompt, workflow, and population changes around a detected metric shift.

## Focus

This feature isolates longitudinal drift signals without allowing proxy metrics to trigger automatic model changes.

## Behavior

- Governors define capability-specific metrics, baselines, windows, stratification, warning bands, and minimum sample sizes.
- Scheduled aggregation tracks acceptance, rejection, edit distance, unsupported claims, escalations, errors, latency, cost, and context-feature shift.
- Dashboards distinguish insufficient data, expected variation, warning, and breach states.
- Breaches create review assignments and may invoke a preapproved suspension policy, never silent retraining.
- Users can annotate operational changes that explain discontinuities.
- Patient-level drill-down requires explicit audit permission and purpose.

## Frappe realization

- **DocTypes:** `OC AI Drift Metric`, `OC AI Drift Baseline`, and `OC AI Drift Signal` store definitions, aggregate windows, strata, thresholds, annotations, and review state.
- **Workflow:** signal Open → Investigating → Resolved/Accepted Variation → Escalated.
- **Roles/permissions:** aggregate dashboards for AI governors; patient-level evidence restricted to `OC AI Auditor`.
- **Jobs/surfaces:** scheduler_events aggregate metrics; Dashboard Charts and Number Cards show trends; Notifications and Assignments route breaches.

## Boundaries

Owns: longitudinal quality-proxy monitoring and review signals. Consumes: artifact dispositions, telemetry, and cohort aggregates. Emits: drift evidence and governance tasks. Does not own: automatic retraining or causal conclusions.

## Open questions

- Which metrics are reliable enough to support automatic suspension rather than human investigation only?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Stratified Bias Monitoring](openchart-feature-catalog-aic-027-stratified-bias-monitoring.md)
