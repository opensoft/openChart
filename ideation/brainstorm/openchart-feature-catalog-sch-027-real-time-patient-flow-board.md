# Real-time Patient Flow Board — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Displays permission-aware live appointment flow across arrival, rooming, care, and completion stages.
Topics: openchart-feature-catalog, scheduling, frappe, flow-board
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-027 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Bottleneck alerting** — Highlight sustained queue delays against locally configured thresholds.

## Focus

This feature isolates a shared operational board for coordinating patients currently moving through a facility.

## Behavior

- Staff choose facility, service, date, and permitted patient-identification mode.
- Cards show current state, scheduled time, elapsed stage time, assigned room, and responsible team where authorized.
- Drag actions invoke valid workflow transitions rather than editing state directly.
- Websocket updates move cards without requiring manual refresh.
- Privacy mode replaces names with approved tokens on wall displays.
- Disconnected clients show stale status and reconcile against server state before accepting actions.

## Frappe realization

- **DocTypes:** projection from `OC Appointment`, `OC Appointment Flow Event`, and `OC Room Assignment`.
- **Surface:** custom Desk page and privacy-safe display page use Kanban semantics and `frappe.publish_realtime` updates.
- **Permissions/API:** facility user permissions filter server queries; transition actions call the guarded scheduling API.

## Boundaries

Owns: live operational projection and interactions. Consumes: flow events and room assignments. Emits: authorized transition requests. Does not own: source states or clinical notes.

## Open questions

- What identifier format is safe and useful for unattended wall displays?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Check-in Statuses](openchart-feature-catalog-sch-026-appointment-check-in-statuses.md)
