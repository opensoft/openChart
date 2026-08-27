# Appointment Arrival Instructions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Delivers location-, modality-, and appointment-specific arrival guidance with versioned timing and acknowledgement.
Topics: openchart-feature-catalog, scheduling, frappe, arrival-instructions
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-054 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Contextual wayfinding** — Link approved parking, entrance, floor, and check-in guidance for the appointment time.

## Focus

This feature isolates practical arrival directions distinct from clinical preparation instructions.

## Behavior

- Booking resolves effective guidance by facility, entrance, modality, appointment type, and operating hours.
- Instructions include requested arrival offset, check-in method, wayfinding, accessibility contact, and late-arrival contact path.
- Patients receive the approved language and can view the latest version in the portal.
- Reschedules, location changes, and closure responses trigger reevaluation and an explicit updated message.
- Delivery and acknowledgement are recorded without implying clinical readiness.
- Missing guidance creates a staff-visible configuration warning rather than sending invented directions.

## Frappe realization

- **DocTypes:** `OC Arrival Instruction Set` and `OC Appointment Arrival Guide` with applicability, content version, rendered snapshot, delivery, and acknowledgement.
- **Automation:** Notification doctypes send channel-safe summaries and portal links; schedule changes queue regeneration.
- **Surface:** portal page and Jinja Print Format provide consistent guidance; staff List view flags missing mappings.

## Boundaries

Owns: operational arrival guidance delivery. Consumes: appointment location, modality, and timing. Emits: versioned patient instructions. Does not own: clinical preparation or facility master data.

## Open questions

- How should temporary entrance changes be approved and propagated quickly?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Procedure Preparation Instructions](openchart-feature-catalog-sch-039-procedure-preparation-instructions.md)
