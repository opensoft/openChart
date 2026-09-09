# Payment Model Scenario Modeling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Models how alternative performance rates, category weights, thresholds, and attribution assumptions could affect value-based payment outcomes.
Topics: openchart-feature-catalog, quality-reporting, frappe, payment-scenario
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-021 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Intervention break-even view** — Estimate the performance-rate change needed to cross a configured payment threshold.

## Focus

Transparent what-if modeling for planning, clearly separated from official payer calculation and financial accounting.

## Behavior

- An analyst selects a program model, period, entity scope, baseline rates, and approved rule release.
- Scenarios vary performance rates, thresholds, weights, benchmarks, attribution, and shared-savings assumptions.
- Results show modeled score, adjustment range, contributing measures, uncertainty, and excluded financial terms.
- Users can compare scenarios and lock a reviewed planning baseline without changing quality results.
- Missing contract terms or unsupported formulas produce incomplete-model warnings rather than inferred values.
- Every output carries assumptions, source fingerprints, currency basis where used, and a non-official disclaimer.
- Rule or baseline changes mark saved scenarios stale.

## Frappe realization

- **DocTypes:** Add `OC Payment Model`, `OC Payment Scenario`, and child assumption/result rows with rule release, rates, thresholds, weights, Currency, ranges, and fingerprints.
- **Workflow:** Govern models through draft/review/approved/retired and scenarios through working/reviewed/locked/superseded.
- **Permissions and API:** Limit financial assumptions to `OC Value Based Analyst` at permlevel 1 and expose guarded simulation methods.
- **Surfaces:** Provide tornado and waterfall Dashboard Charts, comparison Script Reports, and planning Print Formats.

## Boundaries

Owns: local quality-linked payment scenarios. Consumes: quality rates, approved model rules, attribution, and user-entered assumptions. Emits: modeled ranges and sensitivities. Does not own: contracts, accounting, claims, or payer settlement.

## Open questions

- Should contract-specific models live in openChart or be supplied through a governed openPractice integration?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
