# Booking Horizon Rules — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Controls the earliest and latest times appointments may be booked by audience, type, service, and channel.
Topics: openchart-feature-catalog, scheduling, frappe, booking-horizon
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-046 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Demand-aware horizon review** — Suggest policy review when horizon limits repeatedly suppress valid demand.

## Focus

This feature isolates advance-booking and minimum-notice windows independently of slot availability.

## Behavior

- Policies define minimum lead time and maximum future horizon by appointment type, facility, audience, and channel.
- Search omits or explains slots outside the actor's effective horizon.
- Staff overrides, where allowed, require a reason and preserve the violated threshold.
- Daylight-saving transitions use facility-local rules while storing comparison timestamps consistently.
- A policy change affects new booking attempts and does not invalidate confirmed appointments.
- Missing policy resolves to an explicit default configured for the service, not unlimited access silently.

## Frappe realization

- **DocTypes:** `OC Booking Horizon Policy` with scope, min_lead_duration, max_horizon_duration, audience, channel, and effective dates.
- **Validation/API:** slot search and booking methods resolve one effective version and return structured exclusion reasons.
- **Permissions:** Scheduling Policy Manager writes; Scheduler and portal actors receive scoped read behavior but not raw internal policy detail.

## Boundaries

Owns: temporal booking eligibility. Consumes: actor, channel, service, and candidate time. Emits: eligible or excluded result. Does not own: provider availability.

## Open questions

- Which channels should receive different horizons, and why?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Open-slot Search](openchart-feature-catalog-sch-006-open-slot-search.md)
