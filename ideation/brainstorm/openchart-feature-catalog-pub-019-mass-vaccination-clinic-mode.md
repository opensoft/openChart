# Mass Vaccination Clinic Mode — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides rapid, safety-gated multi-patient vaccination entry with station roles, shared clinic defaults, and immediate exception routing.
Topics: openchart-feature-catalog, public-health, frappe, mass-vaccination
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-019 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Offline station queue** — Stage encrypted entries during connectivity loss with supervised reconciliation.

## Focus

High-throughput vaccination documentation that preserves patient identity, lot, consent, and performer safety checks.

## Behavior

- A clinic manager opens a session with facility, date, vaccine products, lots, stations, and role assignments.
- Vaccinators identify one patient at a time and review critical allergies, contraindications, consent, and forecast.
- Shared defaults accelerate entry but patient, dose, lot, performer, and administration time require confirmation.
- Successful submission resets all patient-specific context before the next patient.
- Identity ambiguity, quarantined lot, or failed safety checks block rapid submit and route an exception lane.
- A live dashboard shows throughput, remaining stock, errors, and unsent registry events without exposing unnecessary PHI.

## Frappe realization

- **DocTypes:** Add `OC Mass Vaccination Session`, child stations/lots, and `OC Vaccination Station Event` linked to standard administrations.
- **Client scripts:** Build a keyboard-efficient Desk page with explicit patient-context reset and barcode hooks.
- **Permissions:** Use session-scoped User Permissions for `OC Mass Vaccination User`; manager controls stations and exceptions.
- **Jobs and surfaces:** Emit realtime aggregate updates, enqueue registry work asynchronously, and provide reconciliation and closeout reports.

## Boundaries

Owns: mass-clinic session orchestration and rapid-entry surface. Consumes: patient identity, consent, forecast, inventory, and administration API. Emits: standard administrations and operational metrics. Does not own: alternate clinical record semantics.

## Open questions

- Which functions must remain available during a validated offline mode?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
