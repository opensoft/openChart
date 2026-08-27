# Stratified Bias Monitoring — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Compares AI performance and burden across governed demographic and clinical strata with privacy-aware suppression.
Topics: openchart-feature-catalog, clinical-ai, frappe, bias-monitoring
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-027 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Intersectional disparity explorer** — Compare approved multi-attribute strata only when cohort size and privacy controls permit.

## Focus

This feature isolates ongoing equity monitoring after evaluation and activation.

## Behavior

- Governance teams define approved strata, outcomes, reference groups, minimum cohort sizes, uncertainty intervals, and review thresholds.
- Scheduled analyses compare errors, omissions, acceptance, edits, escalations, and workflow burden across strata.
- Small cohorts are suppressed and missing demographic data is reported as its own completeness problem.
- Dashboards show absolute performance and disparity; aggregate parity cannot hide low quality for every group.
- Threshold breaches open equity review and can support suspension, but do not alter model behavior automatically.
- Access to sensitive attributes and patient-level examples is purpose-limited and audited.

## Frappe realization

- **DocTypes:** `OC AI Equity Metric`, `OC AI Equity Analysis`, and child strata rows store definitions, counts, uncertainty, suppression, disparity, and review decisions.
- **Workflow:** Planned → Privacy Review → Running → Equity Review → Closed/Escalated.
- **Roles/permissions:** `OC AI Equity Reviewer` and `OC Privacy Reviewer` have separated duties; aggregate reports mask small cells.
- **Jobs/reports:** rq and scheduler_events calculate approved aggregates; Script Report and Dashboard Charts show trends; exports enforce suppression.

## Boundaries

Owns: stratified performance evidence and equity review. Consumes: approved sensitive attributes and outcome metrics. Emits: privacy-aware disparity findings. Does not own: demographic source quality, automatic remediation, or claims of fairness.

## Open questions

- Which reference-group choices should be fixed centrally versus selected per evaluation question?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Fairness Review Release Gate](openchart-feature-catalog-aic-044-fairness-review-release-gate.md)
