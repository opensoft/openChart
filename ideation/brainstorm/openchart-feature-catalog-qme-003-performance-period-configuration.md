# Performance Period Configuration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines governed reporting periods, eligible populations, organizational scopes, and source-data cutoffs for repeatable quality measurement.
Topics: openchart-feature-catalog, quality-reporting, frappe, performance-period
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-003 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Rolling preview period** — Maintain a non-submission projection that advances daily beside the locked regulatory period.

## Focus

One authoritative configuration for the dates and scope that every calculation, simulation, and submission must reference.

## Behavior

- A quality administrator creates a period with program, start and end dates, data cutoff, facilities, providers, TINs, and measure releases.
- Validation rejects overlapping locked periods with incompatible organization or program scopes.
- Periods move through draft, configured, open, closing, locked, submitted, and archived states.
- Opening a period snapshots provider and organization identifiers while retaining later correction paths.
- Locking blocks new calculation baselines until completeness and approval gates are resolved.
- Reopening a locked period requires a reason, elevated permission, and invalidates downstream submission packages.
- Every run and export displays the period and scope fingerprint used.

## Frappe realization

- **DocTypes:** Add `OC Quality Performance Period` with child tables for measures, providers, facilities, TIN scopes, payer programs, and a read-only scope hash.
- **Workflow:** Configure controlled transitions with `OC Quality Administrator`, `OC Quality Approver`, and `OC Compliance Officer` actions.
- **Hooks and API:** Validate dates and scope on save, compute fingerprints on lock, and expose guarded create, lock, reopen, and read methods.
- **Surfaces:** Provide Calendar and Gantt views, a period dashboard, readiness Number Cards, and role-filtered list views.

## Boundaries

Owns: reporting-period scope and lifecycle. Consumes: programs, organizations, providers, measures, and deadlines. Emits: immutable scope snapshots and invalidation events. Does not own: provider credentialing, clinical records, or regulator calendars.

## Open questions

- Which organization identifier changes may be corrected in place before lock versus requiring a successor period?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
