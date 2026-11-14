# Waitlist Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains prioritized patient requests for earlier or otherwise preferred appointment openings.
Topics: openchart-feature-catalog, scheduling, frappe, waitlist
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-011 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Preference freshness prompts** — Ask patients to reconfirm aging waitlist criteria.

## Focus

This feature isolates durable waitlist demand, eligibility, preferences, and staff prioritization.

## Behavior

- Staff or patients add an eligible appointment request with date, time, location, provider, and contact preferences.
- Each entry has Waiting, Offered, Booked, Paused, Expired, or Withdrawn state.
- Priority combines explicit policy factors while retaining an explanation visible to authorized staff.
- Patients may update preferences or withdraw without affecting an already booked appointment.
- Duplicate active entries for the same need are flagged for review.
- Expired eligibility pauses matching until staff or patient revalidates the request.

## Frappe realization

- **DocTypes:** `OC Waitlist Entry` with patient, appointment_type, preferences, priority, eligibility_until, state, and source request.
- **Surface:** Kanban by state, filtered List views, assignments, and a patient portal form support management.
- **Automation:** `scheduler_events` identifies stale or expiring entries; Frappe Notification doctypes request reconfirmation.

## Boundaries

Owns: prioritized unfilled demand. Consumes: patient preferences and eligibility. Emits: match candidates. Does not own: offer delivery or booking confirmation.

## Open questions

- Which priority factors are acceptable and auditable for equitable access?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Automated Waitlist Offer Cascade](openchart-feature-catalog-sch-012-automated-waitlist-offer-cascade.md)
