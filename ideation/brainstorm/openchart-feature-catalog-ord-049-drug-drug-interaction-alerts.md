# Drug-Drug Interaction Alerts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Warns prescribers when a proposed medication conflicts with active or concurrently proposed therapies at governed severity thresholds.
Topics: openchart-feature-catalog, cpoe, frappe, drug-interactions
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-049 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Interaction management options** — Offer reviewable alternatives such as monitoring, timing separation, or substitution from governed content.

## Focus

This feature isolates medication interaction detection during order composition.

## Behavior

- The rule compares the proposed medication and relevant ingredients with active and same-basket therapies.
- The alert identifies interacting agents, severity, clinical effect, onset, evidence, management options, and rule owner.
- Ingredient, class, route, dose, and timing exceptions are applied only from versioned rule content.
- Severe interactions interrupt signature; lower tiers appear as advisories according to policy.
- Missing medication reconciliation data is surfaced as uncertainty rather than assumed safe.
- Overrides require permitted coded reasons and preserve exact rule and medication versions.

## Frappe realization

- **DocTypes:** versioned `OC CDS Rule` type Drug Interaction references governed ingredient/value sets and evidence; `OC CDS Evaluation` records pair and outcome.
- **Workflow:** rule follows Draft → Testing → Review → Active → Retired.
- **Roles/permissions:** pharmacy CDS authors draft; independent clinical reviewers approve; prescribers resolve alerts.
- **Hooks/API/surface:** medication-order preview and `on_submit` orchestration evaluate interactions; alert cards link rationale and override action.

## Boundaries

Owns: interaction rule outcome and alert content. Consumes: proposed and active medication concepts. Emits: alert or advisory. Does not own: medication list reconciliation or substitution decisions.

## Open questions

- Which interaction knowledge source and local severity mappings are authoritative?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Drug-Allergy Order Alerts](openchart-feature-catalog-ord-050-drug-allergy-order-alerts.md)
