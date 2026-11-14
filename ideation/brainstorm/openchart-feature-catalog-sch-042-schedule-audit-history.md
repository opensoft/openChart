# Schedule Audit History — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides a chronological, permission-aware account of appointment and capacity changes with actor, source, reason, and before/after evidence.
Topics: openchart-feature-catalog, scheduling, frappe, schedule-audit
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-042 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Audit anomaly review** — Flag unusual mutation patterns for human investigation.

## Focus

This feature isolates trustworthy reconstruction of who changed a schedule, how, and why.

## Behavior

- Authorized users view a timeline of creates, holds, bookings, moves, cancellations, overrides, and resource changes.
- Each event records actor or integration identity, channel, timestamp, source request, reason, and affected fields.
- Before/after detail respects field-level permissions and masks patient data in broad operational audits.
- Automated events identify the job, rule, and correlation identifier that caused them.
- Corrections append new events and never erase the original accepted history.
- Export requires a reason and produces a bounded, access-logged report.

## Frappe realization

- **DocTypes:** append-only `OC Schedule Audit Event` with subject Dynamic Link, event_type, actor, channel, correlation_id, reason, and change JSON.
- **Hooks:** guarded scheduling APIs emit canonical events; Frappe Version and activity feed provide supporting UI history, not the sole authority.
- **Reports:** permission-aware Script Report and Jinja export; Audit Reviewer role receives read-only access.

## Boundaries

Owns: canonical scheduling change evidence. Consumes: accepted mutations from scheduling services. Emits: timelines and bounded exports. Does not own: general security audit logs.

## Open questions

- Which low-level technical events belong in the canonical clinical operations history?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Schedule Conflict Resolution](openchart-feature-catalog-sch-053-schedule-conflict-resolution.md)
