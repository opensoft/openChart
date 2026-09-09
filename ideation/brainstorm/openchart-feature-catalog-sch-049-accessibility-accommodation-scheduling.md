# Accessibility Accommodation Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Matches documented patient accessibility needs to suitable locations, resources, timing, and assistance during booking.
Topics: openchart-feature-catalog, scheduling, frappe, accessibility-accommodations
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-049 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Accommodation readiness check** — Confirm required resources with the facility before the visit.

## Focus

This feature isolates scheduling use of patient-authorized accommodation requirements.

## Behavior

- Authorized users select applicable needs such as mobility access, low-stimulation timing, assistive communication, or extended transition time.
- Search treats required accommodations as hard constraints and optional supports as ranked preferences.
- Results explain facility capabilities without exposing sensitive rationale broadly.
- Booking snapshots the required accommodations and creates operational preparation tasks where needed.
- Unavailable accommodations route to staff assistance rather than returning a generic no-slots message.
- Changes to needs revalidate future appointments with patient consent and provenance.

## Frappe realization

- **DocTypes:** `OC Scheduling Accommodation` with patient, capability_code, requirement_level, valid dates, consent, and source; facility resources carry capability tags.
- **API/permissions:** slot search resolves accommodations server-side; permlevel controls separate sensitive need detail from operational capability codes.
- **Automation:** Assignment Rules create readiness tasks; Notification doctypes avoid disclosing accommodation detail in insecure channels.

## Boundaries

Owns: accommodation-aware booking constraints. Consumes: patient-authorized needs and facility capabilities. Emits: matched booking and preparation tasks. Does not own: disability assessment.

## Open questions

- Which accommodation details should be visible to schedulers versus only operational teams?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Patient Preference Matching](openchart-feature-catalog-sch-048-patient-preference-matching.md)
