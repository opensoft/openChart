# Recurring Appointment Series — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates and maintains bounded recurring appointment series while preserving each occurrence as an auditable booking.
Topics: openchart-feature-catalog, scheduling, frappe, recurring-appointments
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-005 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Adaptive recurrence** — Suggest alternative cadence when repeated exceptions fragment a series.

## Focus

This feature isolates recurrence creation and series-level changes for repeated care appointments.

## Behavior

- A scheduler chooses patient, type, cadence, end condition, preferred time, and required resources.
- The system previews all occurrences and conflicts before any bookings are committed.
- Users may edit one occurrence, this-and-following, or the remaining series with explicit scope.
- Failed occurrences remain unbooked with reasons while policy determines whether partial creation is allowed.
- Cancelling a series never silently cancels completed or already in-progress visits.
- Every occurrence retains its series identity and records divergence from the original pattern.

## Frappe realization

- **DocTypes:** `OC Appointment Series` plus child `OC Appointment Series Occurrence`; generated `OC Appointment` records link back to both.
- **Automation:** use Frappe auto-repeat semantics for cadence modeling, with background jobs creating only validated bounded occurrences.
- **Workflow/API:** Draft → Previewed → Active → Ended/Cancelled; guarded series methods run transactionally and write audit events.

## Boundaries

Owns: recurrence intent and occurrence lineage. Consumes: slot search and booking rules. Emits: individual appointment requests. Does not own: treatment-plan clinical authority.

## Open questions

- When should partial series creation be allowed rather than all-or-none?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Sequential Care Pathway Booking](openchart-feature-catalog-sch-019-sequential-care-pathway-booking.md)
