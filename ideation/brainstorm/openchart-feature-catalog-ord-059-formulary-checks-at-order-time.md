# Formulary Checks At Order Time — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows coverage tier, restrictions, preferred alternatives, and formulary provenance while a medication order is composed.
Topics: openchart-feature-catalog, cpoe, frappe, formulary-checks
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-059 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Restriction readiness summary** — Show documented prerequisites for step therapy or prior authorization without initiating them autonomously.

## Focus

This feature isolates timely formulary guidance at medication selection and signature.

## Behavior

- The composer displays plan or organization formulary status, tier, restrictions, effective date, source, and freshness.
- Preferred alternatives are shown with clinically relevant distinctions and require prescriber selection.
- Unknown patient coverage or stale formulary data is labeled explicitly.
- A non-formulary selection may require coded rationale according to local policy.
- Formulary status never overrides allergy, interaction, dose, or clinician judgment.
- The signed order stores the formulary response reference and prescriber decision.

## Frappe realization

- **DocTypes:** `OC Formulary Response` with patient/plan context reference, medication, tier, restrictions, alternatives, source, retrieved_at, and provenance.
- **Roles/permissions:** prescribers see minimum necessary coverage data; formulary integrations write through a service role; administrators manage local policy.
- **Hooks/API/surface:** medication selection invokes a whitelisted lookup with cache freshness; `on_submit` records current response and rationale requirement.
- **Operations:** failures degrade to visible Unknown according to policy and appear on an integration exception report.

## Boundaries

Owns: order-time formulary presentation and decision evidence. Consumes: coverage context and formulary source. Emits: status, alternatives, and rationale requirement. Does not own: benefits adjudication or prior authorization.

## Open questions

- How recent must a formulary response be at signature?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Selection Cost Transparency](openchart-feature-catalog-ord-060-order-selection-cost-transparency.md)
