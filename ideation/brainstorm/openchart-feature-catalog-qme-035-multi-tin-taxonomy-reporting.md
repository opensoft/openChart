# Multi TIN Taxonomy Reporting Splits — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Splits quality populations and outputs by versioned TIN, NPI, taxonomy, facility, and participation relationships without duplicating patient results.
Topics: openchart-feature-catalog, quality-reporting, frappe, multi-tin-reporting
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-035 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Identifier change rehearsal** — Preview reporting impact before a provider, taxonomy, or TIN relationship becomes effective.

## Focus

Accurate organizational reporting splits for clinicians practicing under multiple entities or taxonomies across a period.

## Behavior

- Administrators maintain effective-dated provider relationships to NPI, TIN, taxonomy, facility, and participation unit with source evidence.
- Period lock snapshots relationships while allowing governed successor corrections.
- Population assignment uses service date, attribution, program rules, and explicit relationship release.
- Ambiguous, overlapping, missing, or contradictory relationships route patients or encounters to review.
- Reports show included, excluded, duplicated-by-policy, and unresolved counts for every split.
- A patient result is referenced by scoped rollups rather than copied into separate clinical facts.
- Package manifests identify the exact organization relationship snapshot and resolution decisions used.

## Frappe realization

- **DocTypes:** Add `OC Reporting Entity Relationship` and `OC Entity Assignment Review` with provider, NPI, TIN, taxonomy, facility, effective dates, source, priority, and succession fields.
- **Workflow:** Use draft, verification, approved, active, expired, disputed, and superseded states.
- **Hooks and jobs:** Validate overlaps on approval, snapshot relationships on period lock, and recalculate scoped rollups after approved succession.
- **Surfaces:** Provide relationship Gantt views, ambiguity queues, split Script Reports, and entity-scope dashboards.

## Boundaries

Owns: reporting-specific organization relationships, snapshots, assignment, and split outputs. Consumes: provider identifiers, taxonomy, facilities, attribution, service dates, and program rules. Emits: scoped populations and manifests. Does not own: credentialing, tax identity issuance, payroll, or legal entity governance.

## Open questions

- Which source is authoritative when credentialing, roster, and program files disagree on effective relationships?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
