# Allergy Override Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures allergy-specific risk assessment, intended mitigation, monitoring, and accountable approval when a conflicting medication is ordered.
Topics: openchart-feature-catalog, cpoe, frappe, allergy-override
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-056 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Mitigation checklist** — Present rule-specific monitoring and rescue-plan fields for clinician confirmation.

## Focus

This feature isolates the heightened documentation needed beyond a generic alert override reason.

## Behavior

- The prescriber selects a clinical rationale and documents expected benefit, allergy assessment, mitigation, monitoring, and contingency plan.
- Severe reaction classes may require allergist input, second authorization, or prohibit override by policy.
- The alert displays the exact allergen, reaction history, verification status, and cross-reactivity path.
- Updating the allergy record is optional and separate; override documentation cannot rewrite it.
- Material medication-order changes invalidate prior allergy override evidence.
- The signed order and result accountability surfaces retain visible override status.

## Frappe realization

- **DocTypes:** submitted `OC Allergy Override` extends `OC CDS Override` with allergy statement version, assessment, benefit, mitigation, monitoring, and contingency fields.
- **Workflow:** Draft → Complete → Submitted, with optional Awaiting Second Authorization.
- **Roles/permissions:** prescribers document; configured specialists or authorizers review high-severity cases; provenance is permlevel 2.
- **Hooks/API/surface:** medication order `validate/on_submit` checks matching current override digest; print and fulfillment views display a safety banner.

## Boundaries

Owns: allergy-specific override evidence. Consumes: alert, allergy statement, medication draft, and policy. Emits: permissioned resolution evidence. Does not own: allergy amendment or monitoring execution.

## Open questions

- Which allergy severities and reaction types prohibit override entirely?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Drug-Allergy Order Alerts](openchart-feature-catalog-ord-050-drug-allergy-order-alerts.md)
