# Reporting Data Completeness Checker — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assesses required quality-reporting data coverage before period close and identifies actionable missingness by measure, source, provider, and patient.
Topics: openchart-feature-catalog, quality-reporting, frappe, data-completeness
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-017 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Source-system freshness score** — Correlate missing data with delayed interfaces, unclosed encounters, or mapping outages.

## Focus

Pre-close readiness checks that distinguish true absence, delayed data, inaccessible data, and invalid data.

## Behavior

- An administrator runs completeness rules for a configured period and measure set.
- Checks assess required identifiers, encounters, diagnoses, observations, results, procedures, medications, exclusions, and attribution fields.
- Findings classify missing, late, unmapped, invalid, restricted, duplicate, or not-applicable data.
- Dashboards aggregate findings while preserving permission-bound patient drill-down.
- Thresholds can warn, block close, or require approved waiver according to program configuration.
- Each finding links to its rule, source expectation, owner, freshness time, and remediation path.
- Reruns preserve prior snapshots so improvement and regression are visible.

## Frappe realization

- **DocTypes:** Add `OC Completeness Rule`, `OC Completeness Assessment`, and child finding rows with dimension, status, source, threshold, owner, and scope.
- **Jobs:** Execute checks in rq, snapshot results, and schedule recurring assessments during closing windows.
- **Permissions:** Apply patient/facility User Permissions and restrict rule approval to `OC Quality Approver`.
- **Surfaces:** Deliver heatmap Script Reports, readiness Number Cards, trend Dashboard Charts, and exception assignments.

## Boundaries

Owns: reporting completeness assessments and findings. Consumes: measure requirements, source freshness, clinical records, mappings, and period scope. Emits: readiness status and remediation tasks. Does not own: source-data creation or clinical meaning.

## Open questions

- Which completeness thresholds should block period lock versus require only a visible waiver?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
