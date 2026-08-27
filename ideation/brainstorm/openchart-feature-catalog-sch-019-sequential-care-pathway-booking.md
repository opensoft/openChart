# Sequential Care Pathway Booking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Books ordered multi-step itineraries such as labs-before-visit or infusion series with explicit timing dependencies.
Topics: openchart-feature-catalog, scheduling, frappe, pathway-booking
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-019 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Itinerary optimization** — Minimize patient travel and waiting while retaining hard sequence rules.

## Focus

This feature isolates coordinated booking of multiple appointments whose order and spacing matter.

## Behavior

- A scheduler selects an authorized pathway template and patient-specific target window.
- The engine searches combinations that satisfy step order, minimum or maximum gaps, resources, and locations.
- Users preview the complete itinerary and any unresolved steps before confirmation.
- Policy determines whether partial itineraries may be saved as Pending Completion.
- Moving or cancelling one step displays downstream impacts and requires an explicit scope decision.
- Each appointment retains its independent state and its pathway-step lineage.

## Frappe realization

- **DocTypes:** `OC Scheduling Pathway`, child `OC Scheduling Pathway Step`, and `OC Patient Itinerary` with linked appointments.
- **Workflow/API:** Draft → Proposed → Confirmed → In Progress → Complete/Cancelled; guarded methods reserve all selected steps transactionally.
- **Surface:** Gantt and Calendar views show sequence and timing; a portal itinerary page presents patient-safe instructions.

## Boundaries

Owns: scheduling sequence and itinerary linkage. Consumes: authorized pathway intent and slot availability. Emits: linked bookings. Does not own: clinical orders or care-plan authority.

## Open questions

- Which pathways allow partial confirmation when one step has no opening?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Procedure Preparation Instructions](openchart-feature-catalog-sch-039-procedure-preparation-instructions.md)
