# Rule-based Booking Constraints — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates explicit room, equipment, staffing, timing, and clinical-need rules before confirming a booking.
Topics: openchart-feature-catalog, scheduling, frappe, booking-rules
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-007 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Constraint simulation** — Test proposed rules against historical demand before activation.

## Focus

This feature isolates deterministic eligibility rules that protect safe and feasible appointment bookings.

## Behavior

- Scheduling managers define versioned rules scoped by appointment type, facility, service, and effective dates.
- Rules can require resource classes, qualifications, lead time, sequence, age range, or documented clinical need.
- The booking service returns pass, warning, or block outcomes with human-readable reasons.
- Authorized overrides require a reason, actor identity, and rule-specific permission.
- Missing required context produces an incomplete evaluation rather than an assumed pass.
- Existing bookings retain the rule version and outcome evaluated at confirmation time.

## Frappe realization

- **DocTypes:** `OC Booking Rule`, child `OC Booking Rule Condition`, and `OC Booking Rule Evaluation` with inputs, version, outcome, and override provenance.
- **Workflow:** Draft → Reviewed → Active → Retired; only Scheduling Rule Manager may activate or retire.
- **Hooks/API:** validate through server-side rule evaluators called by `open_chart.api.v1.scheduling.book`; guarded direct writes cannot bypass evaluation.

## Boundaries

Owns: scheduling feasibility policy and evaluations. Consumes: booking context and clinical-need references. Emits: pass, warning, block, and override evidence. Does not own: diagnosis or treatment decisions.

## Open questions

- Which rule classes may be overridden, and by which roles?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Type Catalog](openchart-feature-catalog-sch-004-appointment-type-catalog.md)
