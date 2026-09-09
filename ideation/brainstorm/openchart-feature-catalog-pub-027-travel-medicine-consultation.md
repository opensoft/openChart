# Travel Medicine Consultation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Structures destination- and itinerary-aware travel health review, clinician-selected recommendations, counseling, and follow-up.
Topics: openchart-feature-catalog, public-health, frappe, travel-medicine
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-027 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Destination content release** — Load versioned public-health advisories with source citations and effective dates.

## Focus

A clinician-controlled travel consultation record that separates advisory content from individualized decisions.

## Behavior

- Clinicians capture destinations, dates, trip purpose, lodging, activities, rural exposure, and special risk contexts.
- The workspace combines accepted immunizations and versioned destination content into reviewable candidates.
- Recommendations show source, release, rationale, and whether selected, deferred, declined, or not applicable.
- The module never autonomously orders vaccines, medications, tests, or restrictions.
- Itinerary changes mark recommendations stale and invite reassessment.
- Final counseling, patient decisions, and follow-up tasks become an accepted consultation snapshot.

## Frappe realization

- **DocTypes:** Add `OC Travel Medicine Consultation`, child itinerary and recommendation rows, and `OC Travel Advisory Release`.
- **Workflow:** Use draft, clinician-review, accepted, amended, and closed states with succession for accepted changes.
- **Permissions:** Restrict individualized recommendations to `OC Clinician`; content authors manage advisory releases separately.
- **Surfaces:** Provide a Desk consultation workspace, patient instruction Print Format, and due-follow-up Query Report.

## Boundaries

Owns: itinerary, reviewed recommendations, counseling, and dispositions. Consumes: immunizations, patient context, and advisory releases. Emits: clinician-approved plan and tasks. Does not own: border rules, external advisories, or autonomous ordering.

## Open questions

- Which advisory sources have licensing and update terms suitable for first-party distribution?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
