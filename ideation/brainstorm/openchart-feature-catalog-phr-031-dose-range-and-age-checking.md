# Dose-Range And Age Checking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates prescribed dose and frequency against age-, weight-, indication-, and product-aware pediatric, adult, and geriatric ranges.
Topics: openchart-feature-catalog, eprescribing, frappe, dose-range
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-031 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Growth-aware pediatric context** — Dose review could show weight trajectory and measurement freshness beside weight-based calculations.

## Focus

This feature isolates dose-range and age-context checking. Calculations expose their inputs and evidence and never select or correct a dose without prescriber action.

## Behavior

- The engine evaluates single dose, daily dose, frequency, duration, and cumulative limits when rules support them.
- Pediatric checks show age, weight, body-surface area when used, measurement time, and calculation formula.
- Geriatric and adult checks show applicable age thresholds, indication assumptions, and evidence limits.
- Missing or stale weight, unknown indication, unit mismatch, or unsupported dosage form yields an explicit unable-to-evaluate state.
- Out-of-range findings show expected range and require correction or a reasoned prescriber disposition according to severity.
- Signed evidence retains patient inputs, rule release, calculation, units, and disposition.

## Frappe realization

- **DocTypes:** `OC Dose Range Rule` is versioned; `OC Prescription Safety Finding` stores calculation inputs, normalized units, expected range, and outcome.
- **Hooks:** Client preview and authoritative server evaluation rerun when dose, age, weight, indication, or product changes.
- **Permissions:** Clinical safety stewards publish rules; prescribers alone disposition patient-specific findings.
- **Surfaces:** Calculation drawer, measurement-freshness warning, and rule-coverage Script Report make evaluation explainable.

## Boundaries

Owns: configured dose-range evaluation and evidence. Consumes: prescription, demographics, accepted measurements, indication, and rules release. Emits: findings and unable-to-evaluate states. Does not own: dose selection or autonomous correction.

## Open questions

- Which measurement freshness limits should vary by age, medication, and care setting?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Renal And Hepatic Adjustment Guidance](openchart-feature-catalog-phr-032-renal-and-hepatic-adjustment-guidance.md)
