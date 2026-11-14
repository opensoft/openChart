# Prepayment-required Booking Rules — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Holds eligible bookings pending an external prepayment decision and confirms or releases them according to transparent policy.
Topics: openchart-feature-catalog, scheduling, frappe, prepayment-rules
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-040 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Alternative access routing** — Offer staff assistance when payment cannot be completed without denying care silently.

## Focus

This feature isolates scheduling state around a required payment outcome while leaving finance outside openChart.

## Behavior

- Effective rules identify appointment types and circumstances requiring a prepayment decision before confirmation.
- A selected slot enters Payment Pending with a bounded hold and patient-visible deadline.
- External success confirms the booking after revalidation; failure or expiry releases the hold.
- Exemption or waiver requires an authorized actor, reason, and policy reference.
- Duplicate or delayed callbacks are idempotent and cannot revive an expired hold silently.
- Staff can intervene when technical failure or access concerns prevent normal completion.

## Frappe realization

- **DocTypes:** `OC Prepayment Booking Policy` and `OC Booking Payment Gate` with appointment draft, hold, external_reference, deadline, state, and waiver.
- **API:** signed callback method validates source and idempotency; `open_chart.api.v1.scheduling` owns hold-to-confirm transitions.
- **Automation:** `scheduler_events` expires gates; Notification doctypes send safe status messages without storing payment credentials.

## Boundaries

Owns: payment-gated booking state and slot hold. Consumes: external payment outcome and exemption policy. Emits: confirmed booking or released capacity. Does not own: payment processing, balances, or financial records.

## Open questions

- Which services must never use prepayment as a booking gate?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Scheduling Holds](openchart-feature-catalog-sch-044-scheduling-holds.md)
