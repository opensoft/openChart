# Appointment Cancellation Policies — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies transparent cancellation windows, reasons, approvals, and consequences to appointment cancellation requests.
Topics: openchart-feature-catalog, scheduling, frappe, cancellation-policy
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-010 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Policy preview** — Show the exact cancellation effect before the actor confirms.

## Focus

This feature isolates governed cancellation and the resulting release of appointment capacity.

## Behavior

- Patients and staff see whether an appointment is cancellable and the applicable notice window.
- A request captures actor, channel, reason, timestamp, and patient-visible policy text.
- Allowed requests transition the appointment to Cancelled and release associated reservations.
- Requests requiring review enter Pending Cancellation without freeing capacity prematurely.
- Completed, already cancelled, or clinically locked appointments reject duplicate cancellation.
- Policy evaluation records whether a fee hook, waitlist cascade, or follow-up task should be emitted.

## Frappe realization

- **DocTypes:** `OC Cancellation Policy` and `OC Appointment Cancellation` with effective dates, notice threshold, reason, decision, and consequences.
- **Workflow:** Requested → Approved/Rejected → Applied; Scheduler and Patient roles have distinct permitted transitions.
- **Hooks:** `on_update` emits capacity-release and policy events; Frappe Notifications communicate final outcomes.

## Boundaries

Owns: cancellation decision and transition. Consumes: appointment state and effective policy. Emits: released capacity and consequence hooks. Does not own: fee collection.

## Open questions

- Which clinical locks should prevent cancellation without care-team review?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Late-cancellation Fee Hooks](openchart-feature-catalog-sch-016-late-cancellation-fee-hooks.md)
