# Patient Self-scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authenticated patients search eligible openings and book appointments within governed self-service rules.
Topics: openchart-feature-catalog, scheduling, frappe, self-scheduling
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-008 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Guided service selection** — Translate patient-stated goals into reviewable appointment-type suggestions.

## Focus

This feature isolates patient-facing booking from staff-mediated scheduling while using the same availability authority.

## Behavior

- An authenticated patient selects an eligible service, location or telehealth modality, and search window.
- Only appointment types explicitly enabled for self-scheduling are exposed.
- Required screening answers are collected before slots appear and are evaluated by booking rules.
- Selecting a slot creates a short hold, then confirms only after identity, consent, and prerequisites pass.
- Expired holds release automatically and clearly return the patient to refreshed results.
- The patient receives a confirmation and can view the booking in the portal without seeing other patients' data.

## Frappe realization

- **DocTypes:** `OC Self Scheduling Policy`, `OC Slot Hold`, and `OC Appointment`; Web Forms capture screening responses.
- **Surface/API:** a `www/` portal page uses whitelisted `open_chart.api.v1.scheduling` search, hold, and confirm methods with CSRF and ownership checks.
- **Automation:** `scheduler_events` expires abandoned holds; Frappe Notification doctypes send booking confirmations and failure notices.

## Boundaries

Owns: patient self-service booking journey. Consumes: identity, slot search, rules, and consent. Emits: confirmed appointment or released hold. Does not own: patient account authentication.

## Open questions

- Which screening responses require staff review instead of immediate booking?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Open-slot Search](openchart-feature-catalog-sch-006-open-slot-search.md)
