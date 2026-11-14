# Tuberculosis Screening And Read Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates PPD placement and reading or IGRA collection and result review with overdue follow-up visibility.
Topics: openchart-feature-catalog, public-health, frappe, tuberculosis-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-021 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Exposure investigation linkage** — Associate screening episodes with a governed contact-investigation program.

## Focus

One TB screening episode with method-specific milestones, results, interpretation, and follow-up accountability.

## Behavior

- Clinicians choose symptom/risk screen, PPD, IGRA, or combined method and record indication.
- PPD episodes track placement product, lot, site, performer, reading window, induration, reader, and interpretation.
- IGRA episodes track order/specimen/result references and clinician review.
- Overdue PPD reads remain incomplete; the system never fabricates a negative result.
- Positive, indeterminate, or symptomatic outcomes create review tasks according to governed policy.
- Corrections create successors and preserve measurement, source, and interpretation provenance.

## Frappe realization

- **DocTypes:** Add `OC TB Screening Episode` with child milestones and Links to administrations, orders, results, observations, and encounters.
- **Workflow:** Use planned, in-progress, awaiting-read, awaiting-result, clinician-review, complete, and lost-to-follow-up states.
- **Hooks:** Schedule reading-window Notifications and overdue Assignments; result hooks route review but take no autonomous clinical action.
- **Surfaces:** Provide Calendar/List views, a TB worklist Query Report, and clearance-ready read-only extracts.

## Boundaries

Owns: TB screening coordination and interpretation record. Consumes: patient risk context, orders, results, and administration details. Emits: completion status and follow-up tasks. Does not own: diagnosis, treatment, or public-health case adjudication.

## Open questions

- Should interpretation rules be centrally versioned or remain clinician-entered by default?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
