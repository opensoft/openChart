# eCQM Execution Engine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Executes versioned electronic clinical quality measure logic against accepted clinical records and produces reproducible patient and aggregate results.
Topics: openchart-feature-catalog, quality-reporting, frappe, ecqm-engine
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-001 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Incremental recalculation** — Recompute only patients affected by newly accepted or amended source records.

## Focus

Deterministic execution of computable measure specifications without turning measure output into clinical truth or autonomous action.

## Behavior

- A quality administrator selects an approved measure release, population, facility scope, and performance period.
- The engine resolves value sets and logic dependencies to immutable release identifiers before a run starts.
- Runs move through queued, evaluating, completed, completed-with-errors, failed, and superseded states.
- Each patient result records initial population, denominator, numerator, exclusion, exception, and observation outcomes with source references.
- Late or succession-amended clinical records mark affected results stale and queue governed recalculation.
- Unsupported logic, missing terminology, and data-type mismatches fail visibly rather than coercing values.
- Aggregate rates are published only from completed results and retain the run, specification, and source cutoff used.

## Frappe realization

- **DocTypes:** Add `OC Measure Execution` and `OC Patient Measure Result` with measure release, period, scope JSON, source cutoff, population flags, evidence table, and naming series `OC-QME-.YYYY.-`.
- **Workflow:** Use draft, queued, evaluating, completed, completed-with-errors, failed, and superseded states; accepted results are superseded rather than edited.
- **Roles and API:** Permit `OC Quality Administrator` to launch and `OC Measure Reviewer` to read via guarded `open_chart.api.v1.quality.run_measure` and status methods.
- **Jobs and surfaces:** Execute bounded patient batches in rq, publish realtime progress, and expose a Quality Measures workspace with Script Reports and Dashboard Charts.

## Boundaries

Owns: measure execution and derived results. Consumes: approved specifications, terminology releases, accepted clinical records, patient identity, and reporting scope. Emits: traceable patient results, aggregate rates, stale-result events, and errors. Does not own: clinical diagnosis, source-record correction, measure policy, or submission acceptance.

## Open questions

- Which expression languages and CMS artifact formats form the first supported execution profile?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
