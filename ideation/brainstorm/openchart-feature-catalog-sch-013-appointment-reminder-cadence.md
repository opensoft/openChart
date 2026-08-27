# Appointment Reminder Cadence — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Schedules consent-aware email, SMS, and push reminders according to configurable appointment cadence rules.
Topics: openchart-feature-catalog, scheduling, frappe, reminder-cadence
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-013 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Adaptive cadence** — Adjust reminder timing from patient-stated preference and prior response patterns.

## Focus

This feature isolates when and through which permitted channel appointment reminders are sent.

## Behavior

- Managers define reminder steps by appointment type, channel, offset, local send window, and fallback order.
- Booking or rescheduling computes planned reminder instances from the effective rule.
- Delivery honors current consent, verified destinations, quiet hours, and preferred language.
- Cancelled or completed appointments suppress all unsent reminders.
- Failed delivery records the provider response and may activate an allowed fallback channel.
- Staff can inspect scheduled, sent, suppressed, failed, and acknowledged reminder states.

## Frappe realization

- **DocTypes:** `OC Reminder Cadence` with child steps and `OC Appointment Reminder` with due_at, channel, consent snapshot, and status.
- **Automation:** `scheduler_events` enqueues due reminders; Frappe Notification doctypes, `frappe.email`, SMS settings, and push adapters perform delivery.
- **Surface:** List and Script Report views expose due and failed reminders with role-limited contact fields.

## Boundaries

Owns: reminder plans and delivery state. Consumes: appointment changes, consent, and contact channels. Emits: reminder attempts and acknowledgements. Does not own: contact identity verification.

## Open questions

- Which failed channels may fall back automatically without fresh consent?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Two-way SMS Appointment Confirmation](openchart-feature-catalog-sch-014-two-way-sms-appointment-confirmation.md)
