# Block and Bulk Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies reviewed bulk schedule changes and block reservations with previews, per-item outcomes, and rollback safety.
Topics: openchart-feature-catalog, scheduling, frappe, bulk-scheduling
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-020 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Scenario comparison** — Compare alternative block allocations before applying either.

## Focus

This feature isolates high-volume schedule operations that would be unsafe as repeated manual edits.

## Behavior

- Authorized managers select a date range, providers or resources, and an operation such as create blocks, release blocks, or shift sessions.
- A dry-run preview lists every affected slot, appointment, conflict, and notification consequence.
- Confirmation requires a reason and applies only the reviewed operation version.
- Each item records Applied, Skipped, or Failed with a concrete reason.
- Patient appointments are never silently moved by a block operation.
- Retry processes only failed safe items and cannot duplicate successful changes.

## Frappe realization

- **DocTypes:** `OC Bulk Schedule Operation` with child `OC Bulk Schedule Item`, operation payload, preview hash, actor, and results.
- **Workflow:** Draft → Previewed → Approved → Running → Completed/Partial/Failed; Scheduling Manager approves.
- **Jobs:** RQ background jobs process idempotent items; progress publishes through websocket realtime events and a Desk report.

## Boundaries

Owns: reviewed bulk mutation orchestration. Consumes: schedules, blocks, and permissions. Emits: per-item schedule changes. Does not own: automatic patient rebooking.

## Open questions

- Which bulk actions require dual approval due to patient impact?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Day Template Patterns](openchart-feature-catalog-sch-021-day-template-patterns.md)
