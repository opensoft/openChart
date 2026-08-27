# Immunization Catch Up Calculation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Calculates a reviewable catch-up path for delayed or incomplete vaccine series using minimum-age and interval rules.
Topics: openchart-feature-catalog, public-health, frappe, catch-up-immunization
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-004 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Catch-up visit planner** — Group compatible candidate doses into clinician-approved visits.

## Focus

An explainable catch-up calculation that retains uncertainty and leaves clinical decisions to authorized users.

## Behavior

- Clinicians start from a patient schedule evaluation and choose an as-of date.
- The calculation considers valid prior doses, minimum ages, minimum intervals, and series-specific restart rules.
- Output lists earliest eligible dates, routine target dates, and rule explanations for each candidate dose.
- Unknown dates or uncertain products produce bounded scenarios rather than false precision.
- Users may record a reasoned disposition without altering the underlying calculation.
- A changed history or rule release marks prior plans stale and requires recalculation.

## Frappe realization

- **DocTypes:** Add immutable `OC Immunization Catch Up Plan` and child `OC Catch Up Dose Candidate` linked to schedule evaluation and rule release.
- **Workflow:** Use calculated, clinician-reviewed, superseded, and withdrawn states; review records actor and rationale.
- **Permissions:** Permit calculation to clinical users and final review to `OC Clinician`; patient User Permissions apply throughout.
- **API and surfaces:** Provide `open_chart.api.v1.calculate_catch_up`, a patient-chart panel, and a printable plan clearly labeled as reviewable guidance.

## Boundaries

Owns: catch-up calculations and their review state. Consumes: schedule evaluation and dose history. Emits: dated candidate doses with evidence. Does not own: appointment booking, ordering, or administration.

## Open questions

- How should partially known historical dose dates constrain earliest-date scenarios?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
