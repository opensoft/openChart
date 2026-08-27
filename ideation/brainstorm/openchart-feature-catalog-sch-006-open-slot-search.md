# Open-slot Search — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Finds ranked appointment openings that satisfy patient, service, location, provider, and resource criteria.
Topics: openchart-feature-catalog, scheduling, frappe, slot-search
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-006 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Explainable ranking** — Show why each candidate ranks above alternatives.

## Focus

This feature isolates read-only discovery of valid openings before a booking is attempted.

## Behavior

- Staff or patients submit appointment type, date range, location radius, modality, and optional provider preferences.
- Results include start time, duration, location, provider, modality, and any patient-visible prerequisites.
- The engine excludes closures, existing reservations, buffers, and unmet hard constraints.
- Ranking favors declared preferences without converting them into hidden exclusions.
- Searches return an explicit no-results explanation and suggested criteria to relax.
- A result is not a reservation; booking revalidates the slot against concurrent changes.

## Frappe realization

- **DocTypes:** read projections from `OC Provider Schedule`, `OC Resource Reservation`, `OC Appointment Type`, and `OC Appointment`.
- **API:** whitelisted `open_chart.api.v1.scheduling.search_slots` validates filters, enforces permissions, and returns ranked candidates without writes.
- **Surface:** Desk dialog and portal page call the same API; Query Reports support operational search diagnostics.

## Boundaries

Owns: candidate discovery and ranking. Consumes: availability, constraints, and preferences. Emits: ephemeral slot candidates. Does not own: reservation or final booking.

## Open questions

- Which ranking factors may be personalized without creating inequitable access?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Patient Preference Matching](openchart-feature-catalog-sch-048-patient-preference-matching.md)
