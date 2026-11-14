# Standby List — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains opt-in patients able to accept very short-notice openings under explicit contact and response rules.
Topics: openchart-feature-catalog, scheduling, frappe, standby-list
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-041 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Day-of standby check-in** — Let patients confirm temporary readiness for a specific facility day.

## Focus

This feature isolates immediate short-notice readiness, distinct from general requests for an earlier appointment.

## Behavior

- Patients or staff opt into standby with appointment type, valid dates, travel readiness, channels, and expiration.
- Entries are active only while eligibility and contact consent remain current.
- Staff search standby candidates for a specific opening and see match reasons and last-confirmed readiness.
- Contact attempts do not reserve a slot unless an explicit offer is created.
- Acceptance revalidates booking constraints and the patient's existing appointment disposition.
- Expiry, withdrawal, or successful booking closes the standby entry with provenance.

## Frappe realization

- **DocTypes:** `OC Standby Entry` with patient, appointment_type, readiness window, preferences, consent snapshot, state, and expires_at.
- **Surface:** portal Web Form and staff List/Kanban views; role permissions restrict contact details.
- **Automation:** `scheduler_events` expires entries and Notification doctypes request bounded readiness reconfirmation.

## Boundaries

Owns: short-notice availability intent. Consumes: eligibility, consent, and patient preferences. Emits: standby match candidates. Does not own: waitlist priority or final booking.

## Open questions

- How recently must travel readiness be reconfirmed for day-of offers?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Waitlist Management](openchart-feature-catalog-sch-011-waitlist-management.md)
