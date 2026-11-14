# Overbooking Controls — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs when authorized users may exceed nominal slot capacity and records the operational rationale.
Topics: openchart-feature-catalog, scheduling, frappe, overbooking
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-024 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Overbooking outcome review** — Compare approved overbooks with wait time and attendance outcomes.

## Focus

This feature isolates controlled capacity exceptions rather than ordinary slot booking.

## Behavior

- Policies define maximum excess capacity by provider, appointment type, location, time band, and role.
- A booking beyond capacity shows current commitments and requires an allowed reason.
- Hard limits cannot be bypassed; soft limits require designated permission and provenance.
- Patients are not labeled as overbooked in patient-facing surfaces.
- Multi-resource appointments must pass every resource's capacity rule independently.
- Changes to policy do not retroactively invalidate confirmed appointments.

## Frappe realization

- **DocTypes:** `OC Overbooking Policy` and `OC Overbooking Decision` with scope, limits, actor, reason, appointment, and policy version.
- **Permissions:** Scheduler may use soft allowance; Scheduling Manager configures policy; hard-limit override is absent by design.
- **Validation:** booking `validate` calls transactional capacity checks; Script Reports audit frequency and outcomes.

## Boundaries

Owns: excess-capacity policy and decision evidence. Consumes: current capacity and booking context. Emits: allowed or blocked decision. Does not own: staffing safety policy.

## Open questions

- Which outcome signals should trigger review of an overbooking policy?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Double-booking Warnings](openchart-feature-catalog-sch-025-double-booking-warnings.md)
