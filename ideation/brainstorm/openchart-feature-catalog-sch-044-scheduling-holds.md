# Scheduling Holds — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Reserves capacity temporarily for a named operational purpose with expiry, ownership, and conversion controls.
Topics: openchart-feature-catalog, scheduling, frappe, slot-holds
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-044 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Hold pressure view** — Show how active holds constrain near-term access.

## Focus

This feature isolates temporary capacity reservation before a confirmed appointment or block exists.

## Behavior

- Authorized actors place a hold with target capacity, purpose code, owner, created time, and expiry.
- Hold policy limits duration and extension count by purpose and role.
- Search excludes active hard holds and labels patient-safe soft-hold behavior consistently.
- Conversion to an appointment revalidates constraints and consumes the hold atomically.
- Expiry or release returns capacity and records the terminating actor or job.
- Orphaned, duplicate, or stale holds are detected and reconciled without deleting history.

## Frappe realization

- **DocTypes:** `OC Slot Hold` with subject resources, interval, purpose, owner, expires_at, state, and converted_appointment.
- **Automation:** `scheduler_events` expires due holds idempotently; background reconciliation finds orphaned reservations.
- **API/surface:** guarded hold, extend, release, and convert methods; native Calendar views render holds by permission-aware purpose color.

## Boundaries

Owns: temporary capacity reservation lifecycle. Consumes: current availability and hold policy. Emits: held, released, or converted capacity. Does not own: final appointment eligibility.

## Open questions

- Which hold purposes should be visible to patients searching for slots?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Slot Release Windows](openchart-feature-catalog-sch-045-slot-release-windows.md)
