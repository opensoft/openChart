# Appointment Check-in Statuses — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks operational progression from expected through arrived, rooming, in progress, complete, and exception states.
Topics: openchart-feature-catalog, scheduling, frappe, check-in-status
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-026 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Patient-ready signal** — Notify the care team when all configured arrival prerequisites are complete.

## Focus

This feature isolates the appointment's real-time operational status after the patient approaches arrival.

## Behavior

- Authorized front desk and clinical staff transition Expected, Arrived, Checked In, Rooming, In Progress, Complete, No Show, or Left.
- Each transition records actor, timestamp, station, and optional reason.
- Invalid backwards or skipped transitions are blocked unless an authorized correction supplies a reason.
- Patient-facing status uses plain language and omits internal operational notes.
- A no-show transition follows configured timing and never derives solely from a risk score.
- Corrections append a superseding event rather than rewriting historical timestamps.

## Frappe realization

- **DocTypes:** `OC Appointment Flow Event` with appointment, from_state, to_state, occurred_at, actor, station, and correction_of.
- **Workflow/API:** Frappe Workflow governs valid actions; `open_chart.api.v1.scheduling.transition_flow` is the supported write surface.
- **Surface/events:** Form actions and a flow board publish websocket updates; role permissions separate front-desk and clinical transitions.

## Boundaries

Owns: appointment operational state history. Consumes: confirmed appointment and staff actions. Emits: timestamped flow state. Does not own: encounter clinical status.

## Open questions

- Which sites need custom states without losing comparable metrics?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Real-time Patient Flow Board](openchart-feature-catalog-sch-027-real-time-patient-flow-board.md)
