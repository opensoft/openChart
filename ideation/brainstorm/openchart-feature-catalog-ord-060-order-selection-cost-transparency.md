# Order Selection Cost Transparency — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Displays attributable patient and organization cost estimates with source, assumptions, freshness, and uncertainty during order selection.
Topics: openchart-feature-catalog, cpoe, frappe, cost-transparency
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-060 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Comparable option view** — Compare clinically eligible alternatives by estimated cost without ranking clinical suitability automatically.

## Focus

This feature isolates non-coercive cost information inside ordering workflows.

## Behavior

- Users see whether a value is patient estimate, organization estimate, list price, range, or unavailable.
- Every amount displays currency, source, retrieved time, assumptions, and uncertainty or disclaimer.
- Alternatives appear only when a governed clinical or formulary rule marks them eligible.
- Cost cannot suppress safety alerts or force substitution.
- Clinicians may proceed without cost data and are not required to attest affordability.
- Accepted orders record which estimate was displayed without making the estimate a guarantee.

## Frappe realization

- **DocTypes:** `OC Order Cost Estimate` with orderable, context references, estimate_type, amount/range, currency, source, assumptions, retrieved_at, and provenance.
- **Roles/permissions:** ordering roles see encounter-relevant estimates; payer-sensitive details use restricted fields and audit.
- **Hooks/API/surface:** whitelisted lookup runs on selection; order `on_submit` links the displayed estimate; failures return Unavailable rather than zero.
- **Reports:** aggregate coverage and freshness reports support operations without exposing patient-level financial data broadly.

## Boundaries

Owns: contextual estimate presentation and provenance. Consumes: orderable, coverage context, and cost sources. Emits: informative estimate. Does not own: billing, claims, guarantees, or clinical choice.

## Open questions

- Which estimate sources are reliable enough to show for each order class?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Formulary Checks At Order Time](openchart-feature-catalog-ord-059-formulary-checks-at-order-time.md)
