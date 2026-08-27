# QRDA III Returned Score Import — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Imports aggregate QRDA Category III or equivalent returned score files and reconciles external outcomes with submitted local results.
Topics: openchart-feature-catalog, quality-reporting, frappe, qrda-iii
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-011 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Variance explanation queue** — Rank returned-versus-local discrepancies by likely mapping, scope, or benchmark cause.

## Focus

Traceable ingestion and reconciliation of aggregate feedback without overwriting locally calculated results.

## Behavior

- A submitter uploads a returned file and records source portal, receipt date, reporting entity, and related submission.
- Import validates structure, identifiers, period, measure versions, population counts, and duplicate receipt fingerprints.
- Parsed values remain separate external assertions linked to the originating package and local aggregates.
- Reconciliation classifies exact matches, expected rounding differences, scope mismatches, count variances, and unknown measures.
- Unmatched entities or periods route to review rather than being attached by name similarity.
- Reviewers record dispositions and corrective actions while preserving the original file and parse log.
- A successor import supersedes, but never silently replaces, an accepted returned score.

## Frappe realization

- **DocTypes:** Add `OC Returned Quality Score`, child measure result and reconciliation rows, source Attach, checksum, submission Link, and parse log.
- **Workflow:** Use uploaded, parsing, exception, reconciled, accepted, and superseded states.
- **Roles and jobs:** Limit upload to `OC Quality Submitter`, acceptance to `OC Quality Approver`, and parse files in a bounded rq job.
- **Surfaces:** Provide variance Script Reports, aggregate comparison Dashboard Charts, and a reconciliation review form.

## Boundaries

Owns: imported external score assertions and reconciliation. Consumes: returned files, submission history, local aggregates, and organization identifiers. Emits: variance findings and accepted feedback records. Does not own: official scoring policy or retroactive clinical-data changes.

## Open questions

- Which non-QRDA feedback formats need equivalent normalized import support?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
