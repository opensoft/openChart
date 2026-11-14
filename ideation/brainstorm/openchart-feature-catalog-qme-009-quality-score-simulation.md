# Quality Category Score Simulation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Simulates quality-category scores before submission using selectable measures, benchmarks, completeness assumptions, and transparent uncertainty.
Topics: openchart-feature-catalog, quality-reporting, frappe, score-simulation
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-009 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Sensitivity bands** — Show score ranges under plausible benchmark and missing-data outcomes.

## Focus

Pre-submission decision support that remains clearly labeled as a local estimate rather than an official score.

## Behavior

- A quality analyst selects period, participation scope, candidate measures, benchmark release, and scoring assumptions.
- The simulator checks case minimums, data completeness, measure eligibility, bonus rules, caps, and category weights.
- Results show per-measure points, category subtotal, assumptions, excluded candidates, and uncertainty warnings.
- Users can save named scenarios and compare them without changing locked reporting configuration.
- Missing benchmarks or ambiguous program rules produce ranges or blocked calculations, never fabricated points.
- Simulations become stale when source rates, benchmarks, participation, or rule releases change.
- Exported scenarios carry generated time, inputs, release identifiers, and a non-official disclaimer.

## Frappe realization

- **DocTypes:** Add `OC Quality Score Scenario` with child measure choices, assumptions, computed points, warnings, and source fingerprints.
- **Permissions:** Allow `OC Quality Analyst` creation and `OC Quality Approver` comparison; make official-period inputs read-only.
- **Jobs and API:** Run score calculation through `open_chart.api.v1.quality.simulate_score` and cache only input-fingerprinted outputs.
- **Surfaces:** Provide side-by-side Script Report, waterfall Dashboard Chart, scenario Print Format, and stale-state indicators.

## Boundaries

Owns: local scenario calculation and comparison. Consumes: measured rates, participation, benchmarks, and scoring rules. Emits: estimated points, warnings, and scenario artifacts. Does not own: regulator scoring, payment adjustment, or measure selection approval.

## Open questions

- How should benchmark uncertainty be represented when final deciles are not yet published?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
