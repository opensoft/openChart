# Multi State Registry Targeting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Selects the appropriate registry query and submission targets when a patient moves, receives care across states, or has overlapping jurisdiction ties.
Topics: openchart-feature-catalog, public-health, frappe, multi-state-targeting
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-013 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Jurisdiction transition checklist** — Guide registry reconciliation after an address move.

## Focus

Explainable target selection across patient, facility, administration, and reporting jurisdictions.

## Behavior

- Exchange staff see candidate registries derived from effective patient addresses, facility location, and event location.
- Each target states the policy rule and data used to select it.
- Overlapping targets may be retained, suppressed, or escalated according to versioned site policy.
- A moved patient can trigger a new query without deleting prior registry identifiers or provenance.
- Missing jurisdiction data creates a review item and never silently defaults to the facility state.
- Users can override targeting only with authorized reason and an auditable effective period.

## Frappe realization

- **DocTypes:** Add `OC Registry Target Decision` and `OC Jurisdiction Targeting Policy` with effective dates, evidence rows, and override details.
- **Workflow:** Govern policies through review; decisions use proposed, confirmed, overridden, and superseded states.
- **Permissions:** Allow exchange users to review and `OC Public Health Administrator` to approve policy overrides.
- **API and surfaces:** Expose a deterministic target-selection method, patient jurisdiction timeline, and unresolved-target Query Report.

## Boundaries

Owns: registry target decisions. Consumes: effective addresses, event locations, site policy, and registry profiles. Emits: query and submission targets. Does not own: address truth or jurisdiction law.

## Open questions

- How should reciprocal state agreements affect duplicate outbound reporting?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
