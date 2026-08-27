# CDS Override Analytics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures firing, acceptance, override, error, and downstream review patterns to support rule governance without ranking clinicians punitively by default.
Topics: openchart-feature-catalog, cpoe, frappe, override-analytics
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-055 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Rule tuning cohort** — Create a de-identified review sample of high-frequency low-value alerts for governance analysis.

## Focus

This feature isolates accountable feedback from CDS use into rule stewardship.

## Behavior

- Governance dashboards show firings, unique encounters, overrides by reason, cancellations, errors, latency, and unable-to-evaluate outcomes.
- Filters include rule/version, severity, setting, service, time period, and order class.
- Low-volume cells are suppressed or aggregated according to privacy policy.
- Clinician-level views require explicit governance authority and are not default performance scores.
- Metrics distinguish user override from technical bypass, stale evaluation, and advisory dismissal.
- Dashboard findings create review tasks but never alter rule behavior automatically.

## Frappe realization

- **DocTypes:** analytics derive from `OC CDS Evaluation`, `OC CDS Override`, order outcome, and `OC CDS Review Task`; aggregate snapshots may be stored without PHI.
- **Roles/permissions:** `OC CDS Governance Analyst` reads aggregates; clinician-identifiable drill-down requires audited permlevel 2 access.
- **API/surface:** Script Reports, Number Cards, and Dashboard Charts use allowlisted filters and disclosure controls.
- **Scheduler:** nightly background jobs compute idempotent aggregates and flag threshold breaches for human review assignments.

## Boundaries

Owns: CDS operational and override metrics. Consumes: evaluation, override, and order outcomes. Emits: dashboards and review signals. Does not own: disciplinary assessment or automatic rule tuning.

## Open questions

- Which downstream outcomes can be linked without overstating causality?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Ownership And Review Lifecycle](openchart-feature-catalog-ord-047-cds-ownership-and-review-lifecycle.md)
