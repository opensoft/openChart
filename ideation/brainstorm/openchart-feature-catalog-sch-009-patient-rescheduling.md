# Patient Rescheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients or staff move an appointment while preserving policy checks, resource integrity, and change history.
Topics: openchart-feature-catalog, scheduling, frappe, rescheduling
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-009 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **One-click alternatives** — Offer equivalent nearby openings when a disruption requires a move.

## Focus

This feature isolates moving an existing booking rather than cancelling and recreating it without lineage.

## Behavior

- Authorized actors request a new slot from the appointment or patient portal.
- The system evaluates notice policy, eligibility, resources, and any downstream linked appointments.
- A temporary hold protects the new slot while the move is confirmed.
- Success releases the original capacity and records old and new details in one change event.
- Failure leaves the original appointment intact and explains the unmet condition.
- Restricted or in-progress appointments require staff intervention rather than self-service movement.

## Frappe realization

- **DocTypes:** `OC Appointment Change` records appointment, prior interval, proposed interval, actor, channel, reason, and outcome.
- **Workflow/API:** Proposed → Validated → Applied/Rejected; `open_chart.api.v1.scheduling.reschedule` performs an atomic guarded transition.
- **Notifications:** Frappe Notification doctypes notify the patient and affected operational roles after application, not proposal.

## Boundaries

Owns: reschedule transition and lineage. Consumes: booking rules, holds, and linked-pathway context. Emits: capacity release and confirmed change. Does not own: cancellation policy.

## Open questions

- When must linked sequential appointments move as one itinerary?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Cancellation Policies](openchart-feature-catalog-sch-010-appointment-cancellation-policies.md)
