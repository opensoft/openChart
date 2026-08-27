# Dose Range Checking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Checks proposed medication dose and frequency against governed absolute, weight-based, age-based, and indication-specific ranges.
Topics: openchart-feature-catalog, cpoe, frappe, dose-range
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-052 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Calculation transparency panel** — Show source measurements, equations, units, rounding, and resulting thresholds.

## Focus

This feature isolates transparent dose-range evaluation before medication signature.

## Behavior

- Evaluation normalizes dose, route, frequency, duration, patient measurements, age, indication, and care setting into compatible units.
- The alert shows entered dose, governed range, calculation inputs, measurement times, evidence, and uncertainty.
- Missing or stale required inputs produce an explicit unable-to-evaluate outcome.
- Unit incompatibility blocks evaluation and signature under high-risk policy.
- Suggested values remain editable drafts and require prescriber approval.
- Overrides capture coded reason and exact calculation evidence.

## Frappe realization

- **DocTypes:** `OC CDS Rule` type Dose Range stores route/indication scope, equations, value sets, unit profile, evidence, and provenance.
- **Roles/permissions:** pharmacy CDS roles govern ranges; prescribers review; only authorized observations are consumed.
- **Hooks/API/surface:** order `validate/on_submit` invokes unit-safe evaluation; alert JSON returns inputs, thresholds, rounding, and rule version.
- **Audit:** `OC CDS Evaluation` stores input references and digests rather than mutable copied values where possible.

## Boundaries

Owns: range calculation and explanation. Consumes: proposed dose and authorized patient measurements. Emits: pass, alert, or unable-to-evaluate. Does not own: measurement validity or prescribing decision.

## Open questions

- How old may weight and body-surface measurements be for each clinical context?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Renal Dose Adjustment Guidance](openchart-feature-catalog-ord-058-renal-dose-adjustment-guidance.md)
