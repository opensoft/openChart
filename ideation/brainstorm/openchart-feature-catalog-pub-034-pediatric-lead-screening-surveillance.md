# Pediatric Lead Screening Surveillance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks pediatric lead-screening eligibility, capillary and venous results, confirmatory testing, and jurisdictional follow-up.
Topics: openchart-feature-catalog, public-health, frappe, lead-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-034 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Environmental referral handoff** — Track authorized referral status without importing agency case authority.

## Focus

Closed-loop lead screening and confirmatory follow-up with specimen-method and threshold provenance.

## Behavior

- Clinicians record risk assessment and link screening orders and source results.
- Results display value, unit, specimen method, collection date, source, and threshold-profile version.
- Elevated capillary results can create a confirmatory venous task under governed rules.
- Threshold crossings create review or reporting candidates but never autonomous diagnosis.
- External follow-up status remains source-attributed and cannot close clinical review without authorization.
- Amended laboratory results trigger reevaluation while preserving prior dispositions.

## Frappe realization

- **DocTypes:** Add `OC Lead Screening Episode`, `OC Lead Threshold Profile`, and child follow-up milestones linked to orders/results.
- **Workflow:** Use due, ordered, awaiting-result, confirmatory-needed, review, reporting, follow-up, and complete states.
- **Permissions:** Pediatric clinicians review results; public-health reporters access reporting fields; environmental details use permlevel 1.
- **Hooks and surfaces:** Evaluate accepted result successors, create assignments, and provide cohort and overdue Query Reports.

## Boundaries

Owns: lead screening coordination and threshold evaluation. Consumes: risk assessment, orders, results, and jurisdiction profiles. Emits: follow-up and reporting candidates. Does not own: diagnosis, treatment, or environmental agency cases.

## Open questions

- How should changing reference thresholds affect unresolved historical episodes?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
