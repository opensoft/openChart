# Renal Dose Adjustment Guidance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents transparent renal-function-based dose guidance keyed to identified laboratory values, calculation method, age, and timing.
Topics: openchart-feature-catalog, cpoe, frappe, renal-dosing
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-058 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Renal trend context** — Display recent function trajectory alongside the value used by the rule.

## Focus

This feature isolates kidney-function-aware medication guidance with reproducible calculations.

## Behavior

- The rule selects eligible laboratory observations according to test identity, specimen, final status, and recency policy.
- Guidance shows source value and time, calculation equation, weight basis, resulting category, recommended range, and evidence.
- Missing, stale, rapidly changing, or unit-incompatible data produce explicit uncertainty.
- Clinicians may choose the suggested dose, another dose with override rationale, or order further assessment.
- Accepted guidance only prefills a draft and requires prescriber review and signature.
- Evaluation evidence pins laboratory and rule versions used.

## Frappe realization

- **DocTypes:** `OC CDS Rule` type Renal Dose stores applicable drugs, equations, recency, thresholds, dose bands, evidence, and provenance.
- **Roles/permissions:** prescribers view authorized labs; pharmacy CDS roles govern rules; sensitive values remain in source result permissions.
- **Hooks/API/surface:** medication-order preview and `on_submit` evaluate current finalized labs; result links and calculation details render in the alert.
- **Audit:** `OC CDS Evaluation` records source observation IDs, unit conversion, equation, output, and clinician action.

## Boundaries

Owns: renal-dose calculation and guidance. Consumes: medication draft, finalized labs, age, and permitted measurements. Emits: recommendation or uncertainty. Does not own: renal diagnosis or automatic dosing.

## Open questions

- Which calculation method should apply when patient characteristics make estimates unreliable?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Dose Range Checking](openchart-feature-catalog-ord-052-dose-range-checking.md)
