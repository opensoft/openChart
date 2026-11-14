# Immunization Measure Reporting Hooks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts accepted immunization evidence and schedule interpretations into versioned quality-measure inputs without duplicating vaccine records.
Topics: openchart-feature-catalog, quality-reporting, frappe, immunization-measures
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-023 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Registry reconciliation indicator** — Distinguish locally documented, registry-confirmed, patient-reported, and disputed dose evidence in measure traces.

## Focus

A reporting adapter between immunization evidence and measure logic, preserving dose validity, source, and schedule-release context.

## Behavior

- Measure mappings select accepted administration, historical, registry, and validity-review evidence by source class.
- Dose date, product, code, series, validity, and provenance are normalized against an approved terminology release.
- Invalid, indeterminate, duplicate, or patient-reported doses follow explicit measure-specific counting rules.
- Schedule forecasts may inform missing-data review but do not count as completed vaccination evidence.
- Source succession or validity disposition marks affected patient results stale.
- Drill-down shows which doses counted, which did not, and the rule or evidence reason.
- Reporting hooks never alter the immunization record or independently decide clinical validity.

## Frappe realization

- **DocTypes:** Add `OC Immunization Measure Mapping` with measure release, dose/source classes, value-set release, validity rules, and effective dates.
- **Hooks:** Listen for accepted immunization succession and validity-review events, then enqueue bounded affected-result recalculation.
- **API:** Provide a read-only normalized evidence adapter under `open_chart.api.v1.quality` with patient and purpose permission checks.
- **Surfaces:** Offer mapping review forms, counted-dose trace panels, and data-quality Query Reports.

## Boundaries

Owns: immunization-to-measure normalization and recalculation hooks. Consumes: accepted dose evidence, validity decisions, terminology, and measure mappings. Emits: traceable measure inputs and stale events. Does not own: vaccine administration, schedule policy, or registry exchange.

## Open questions

- How should conflicting local and registry validity decisions be prioritized by different programs?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
