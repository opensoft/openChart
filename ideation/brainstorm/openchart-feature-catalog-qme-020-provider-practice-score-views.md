# Provider And Practice Score Views — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents consistent provider, facility, TIN, and practice quality scores with explicit attribution, suppression, and rollup logic.
Topics: openchart-feature-catalog, quality-reporting, frappe, score-rollups
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-020 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Peer comparison guardrails** — Offer statistically bounded comparisons only when cohort size and risk context are sufficient.

## Focus

Multi-level performance views that explain why provider-level and organization-level rates differ.

## Behavior

- Users select measure, period, participation scope, and organizational level: provider, facility, TIN, or practice.
- Each rate displays attribution rule, denominator size, suppression state, data freshness, and calculation release.
- Rollups use stored patient membership and never average provider percentages when patient-level aggregation is required.
- Patients attributed to multiple providers follow the configured counting rule and remain traceable in drill-down.
- Small cells, sensitive measures, and unauthorized providers are suppressed or hidden by policy.
- Comparisons flag material differences in scope, period, measure release, or completeness.
- Exports preserve applied filters, suppression, and an as-of timestamp.

## Frappe realization

- **DocTypes:** Reuse patient results and attribution; add `OC Quality Rollup Snapshot` with level, entity Dynamic Link, scope fingerprint, counts, rate, and suppression reason.
- **Jobs:** Materialize approved rollups after runs and invalidate snapshots when underlying result or attribution versions change.
- **Permissions:** Apply provider/facility/TIN User Permissions and distinct aggregate export rights for `OC Quality Analyst`.
- **Surfaces:** Provide pivot-style Script Reports, Dashboard Charts, Number Cards, and controlled CSV/PDF exports.

## Boundaries

Owns: quality rollup calculation and presentation. Consumes: patient results, attribution, organizations, and suppression policy. Emits: comparable score views and snapshots. Does not own: employment evaluation, compensation, or official payment adjustment.

## Open questions

- Which risk-adjustment and confidence information must accompany provider comparisons?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
