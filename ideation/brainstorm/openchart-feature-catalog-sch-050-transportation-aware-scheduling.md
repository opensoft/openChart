# Transportation-aware Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Incorporates patient-declared transportation windows and assistance dependencies into appointment search and confirmation.
Topics: openchart-feature-catalog, scheduling, frappe, transportation-aware
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-050 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Ride coordination hook** — Emit a consented request to an external transportation service after booking.

## Focus

This feature isolates transportation constraints that affect whether an otherwise valid appointment is practical.

## Behavior

- Patients or staff record usable arrival and departure windows, advance notice, escort needs, and transport status.
- Slot search can require enough time for declared transport constraints and rank locations by travel preference.
- Confirmation shows whether transport is Confirmed, Needed, Requested, or Patient Arranged.
- A transportation dependency may warn or hold according to explicit service policy; it never silently denies care.
- Rescheduling marks existing transport arrangements for review and emits an updated coordination event.
- Only minimum necessary transport information appears in scheduling views and outbound messages.

## Frappe realization

- **DocTypes:** `OC Appointment Transportation Need` with appointment/request, windows, assistance, state, consent, and external reference.
- **Workflow:** Needed → Requested → Confirmed/Unable/Patient Arranged/Cancelled; Assignment Rules route unresolved needs.
- **API/hooks:** booking search consumes windows; accepted schedule changes emit idempotent integration events without owning ride fulfillment.

## Boundaries

Owns: scheduling representation of transport dependency. Consumes: patient-declared constraints and consent. Emits: booking warning or coordination hook. Does not own: transportation service delivery.

## Open questions

- When may an unconfirmed ride block final booking rather than create a follow-up task?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Accessibility Accommodation Scheduling](openchart-feature-catalog-sch-049-accessibility-accommodation-scheduling.md)
