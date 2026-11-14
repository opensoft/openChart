# Interpreter Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates qualified in-person or remote interpreter capacity with patient language and appointment timing needs.
Topics: openchart-feature-catalog, scheduling, frappe, interpreter-scheduling
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-030 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Vendor dispatch integration** — Request external coverage when internal capacity is unavailable.

## Focus

This feature isolates interpreter requests, qualification matching, reservation, and fulfillment.

## Behavior

- A booking can require language, modality, qualification, and coverage interval including pre-visit time.
- Search returns only interpreters or services eligible for the requested language and setting.
- Requests progress through Needed, Requested, Assigned, Confirmed, Fulfilled, Cancelled, or Unfilled.
- Patient-facing details reveal modality and instructions, not private interpreter workforce data.
- Appointment changes recalculate coverage and flag assignments that no longer fit.
- An unfilled request remains a visible operational exception and never silently drops the requirement.

## Frappe realization

- **DocTypes:** `OC Interpreter Resource` and `OC Interpreter Assignment` with language, qualification, modality, interval, appointment, and state.
- **Workflow:** Needed → Requested → Assigned → Confirmed → Fulfilled; Assignment Rules route unfilled needs.
- **Automation:** Notification doctypes send assignment actions; `scheduler_events` escalates unconfirmed near-term requests.

## Boundaries

Owns: interpreter scheduling and assignment state. Consumes: patient language need and interpreter availability. Emits: fulfilled or unfilled coverage. Does not own: language-need clinical assessment.

## Open questions

- How should external vendor confirmations be normalized and audited?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Multi-resource Appointment Booking](openchart-feature-catalog-sch-032-multi-resource-appointment-booking.md)
