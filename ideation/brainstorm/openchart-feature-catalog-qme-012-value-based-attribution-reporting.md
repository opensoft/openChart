# Value Based Attribution Reporting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces CPC+, ACO-style, and similar value-based quality views using versioned patient attribution rosters and explicit program rules.
Topics: openchart-feature-catalog, quality-reporting, frappe, attribution-reporting
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-012 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Attribution churn analysis** — Explain patient additions, removals, and provider movement between roster releases.

## Focus

Program-specific quality reporting whose population membership is governed by externally supplied or locally approved attribution evidence.

## Behavior

- An analyst imports or creates a roster with program, payer, effective period, patient identity, provider, TIN, and source provenance.
- Identity conflicts and duplicate cross-roster memberships enter review before they influence rates.
- Roster releases are immutable and can be compared by patient, provider, facility, or attribution reason.
- Measure runs select an explicit roster release and distinguish attributed, unattributed, pending-match, and excluded patients.
- Reports show quality rates, data completeness, utilization inputs when available, and attribution churn.
- Program rules determine whether mid-period additions or removals affect denominators and are recorded with the output.
- Restricted payer data follows purpose-bound permissions and cannot broaden access to clinical records.

## Frappe realization

- **DocTypes:** Add `OC Attribution Roster`, `OC Attribution Member`, and `OC Attribution Match Review` with payer/program, dates, patient Link, external identifiers, provider, TIN, source, and status.
- **Workflow:** Use imported, matching, review-required, approved, active, and superseded roster states.
- **API and jobs:** Support guarded Data Import and idempotent roster ingestion under `open_chart.api.v1.quality`, with background identity matching.
- **Surfaces:** Provide churn and attributed-quality Script Reports, role-scoped dashboards, and match-review queues.

## Boundaries

Owns: attribution roster provenance, matching, and reporting scope. Consumes: patient identity, provider/TIN records, payer rosters, and program rules. Emits: attributed populations and quality views. Does not own: payer adjudication, financial settlement, or patient master merging.

## Open questions

- When rosters disagree, which source hierarchy and effective-date rules should govern each program?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
