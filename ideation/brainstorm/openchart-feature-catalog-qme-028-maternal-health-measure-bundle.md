# Maternal Health Measure Bundle — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates prenatal, perinatal, postpartum, safety, and equity measure calculations around a versioned pregnancy episode.
Topics: openchart-feature-catalog, quality-reporting, frappe, maternal-health-measures
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-028 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Episode continuity review** — Identify fragmented prenatal, delivery, and postpartum evidence across facilities and external sources.

## Focus

A coherent maternal measure bundle that handles episode identity, gestational timing, outcomes, and sensitive equity dimensions.

## Behavior

- A governed episode resolver links accepted pregnancy, prenatal, delivery, loss, transfer, and postpartum evidence without overwriting sources.
- Measures select explicit episode and measure releases, gestational calculations, attribution, and reporting windows.
- Ambiguous episode linkage, unknown outcome, multiple gestation, or conflicting dates routes to review.
- Bundle views show per-measure status, shared missing data, follow-up milestones, and source completeness.
- Sensitive outcomes and demographic slices follow purpose, consent, role, and minimum-cell restrictions.
- Source succession recalculates only affected episodes and preserves prior result versions.
- Measure gaps never create autonomous obstetric actions or infer pregnancy status from weak evidence.

## Frappe realization

- **DocTypes:** Add `OC Maternal Measure Episode` and `OC Maternal Measure Mapping` with patient, source links, gestational anchors, outcome, release, linkage confidence, and review state.
- **Workflow:** Use candidate, linkage-review, active, closed, exception, and superseded episode states.
- **Jobs and permissions:** Resolve and evaluate episodes in rq under maternal-record permissions; require clinician review for ambiguous linkage.
- **Surfaces:** Provide episode timeline, bundle Script Report, postpartum Gantt milestones, and privacy-protected aggregate charts.

## Boundaries

Owns: maternal reporting episode linkage and bundled measurement. Consumes: authorized pregnancy, encounter, procedure, result, and postpartum evidence. Emits: traceable bundle results and exceptions. Does not own: obstetric care, pregnancy inference policy, or public-health case reporting.

## Open questions

- Which episode-linkage ambiguities require manual review before any aggregate inclusion?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
