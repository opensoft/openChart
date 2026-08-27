# Telehealth Slot Types — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines bookable telehealth capacity with modality, jurisdiction, technology, and patient-readiness constraints.
Topics: openchart-feature-catalog, scheduling, frappe, telehealth-slots
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-031 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Readiness check** — Offer an optional pre-visit device and connection test.

## Focus

This feature isolates scheduling characteristics unique to remote visits, not video-care delivery.

## Behavior

- Managers mark appointment types or time bands as video, audio, or other approved remote modality.
- Booking checks provider jurisdiction, patient location declaration, technology prerequisites, and permitted service.
- Patients receive modality-specific arrival instructions and connection timing.
- A telehealth slot may reserve a virtual-room resource but does not expose its access token until authorized.
- Modality changes trigger rule revalidation and updated instructions.
- Failed readiness checks route to staff assistance or an approved in-person alternative search.

## Frappe realization

- **DocTypes:** `OC Telehealth Slot Policy` and `OC Virtual Room Reservation` with modality, jurisdictions, prerequisites, interval, and secure join reference.
- **Surface:** appointment type forms, native Calendar views, and portal booking pages display modality badges and safe instructions.
- **API/hooks:** booking validation calls jurisdiction and resource rules; secrets remain outside ordinary DocType fields and logs.

## Boundaries

Owns: telehealth booking eligibility and slot metadata. Consumes: patient location, provider authority, and virtual resources. Emits: remote booking instructions. Does not own: video session content.

## Open questions

- At what point must the patient reconfirm their physical location?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Type Catalog](openchart-feature-catalog-sch-004-appointment-type-catalog.md)
