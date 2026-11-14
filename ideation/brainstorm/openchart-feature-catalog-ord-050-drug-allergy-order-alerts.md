# Drug-Allergy Order Alerts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects ingredient and class conflicts between proposed medications and recorded allergy statements before signature.
Topics: openchart-feature-catalog, cpoe, frappe, allergy-alerts
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-050 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Allergy quality prompt** — Offer a separate workflow to clarify uncertain allergy records without weakening the current alert.

## Focus

This feature isolates allergy conflict detection at medication ordering time.

## Behavior

- The rule compares proposed ingredients and governed cross-reactivity classes with active allergy statements.
- Alerts display allergen, recorded reaction, severity, verification status, source, match path, and evidence.
- Unverified or patient-reported allergies remain visible and are not silently downgraded.
- Severe matches interrupt signature under organization policy.
- The clinician may cancel, choose an alternative, or use the governed override documentation path.
- Editing an allergy to suppress an alert is a separate permissioned clinical-record action with provenance.

## Frappe realization

- **DocTypes:** `OC CDS Rule` type Drug Allergy stores cross-reactivity value sets and evidence; evaluations link exact `OC Allergy Statement` version.
- **Roles/permissions:** prescribers view patient-authorized allergy context; CDS curators cannot alter allergy records.
- **Hooks/API/surface:** medication-order `validate/on_submit` evaluates active allergies; alert component exposes source statement and guarded override method.
- **Audit:** evaluation captures rule version, allergy version, match path, and clinician resolution.

## Boundaries

Owns: order-to-allergy match outcome. Consumes: proposed drug and allergy statements. Emits: alert and resolution requirement. Does not own: allergy verification or medication choice.

## Open questions

- How should intolerances and non-immune adverse reactions alter severity without being hidden?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Allergy Override Documentation](openchart-feature-catalog-ord-056-allergy-override-documentation.md)
