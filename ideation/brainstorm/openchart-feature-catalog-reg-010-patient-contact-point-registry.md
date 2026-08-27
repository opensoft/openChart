# Patient Contact Point Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Stores multiple purpose-qualified phone, email, and other contact points with verification and validity metadata.
Topics: openchart-feature-catalog, registration, frappe, contact-points
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-010 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Contact verification challenges** — Confirm ownership through guarded one-time email or SMS checks.

## Focus

Maintain contact endpoints independently from preferences about when or how they may be used.

## Behavior

- Staff or patients add mobile, home, work, email, relay, or other configured contact points.
- Each entry records use, rank, effective dates, verification status, and shared-device warning.
- Phone numbers retain entered form while storing a normalized searchable representation.
- Invalid syntax blocks activation but never destroys the user's draft value.
- A contact point can be marked unreachable with reason and observed time.
- Historical endpoints remain visible to authorized users but are excluded from routine messaging.

## Frappe realization

- **DocTypes:** `OC Patient Contact Point` with system, value, normalized_value, use, rank, verified_on, validity, and unreachable_reason.
- **Workflow:** Draft → Active → Unreachable, Inactive, or Superseded.
- **Roles/permissions:** `OC Registration Clerk` maintains; `OC Patient Portal User` proposes own changes; `OC Privacy Officer` sees restricted endpoints.
- **API/surfaces:** `open_chart.api.v1.registration.upsert_contact_point`; contact grid, verification badge, and unreachable-contact worklist.

## Boundaries

Owns: contact endpoints and operational status. Consumes: patient-provided contact facts. Emits: active qualified endpoints. Does not own: communication consent or campaign delivery.

## Open questions

- Should shared-device warnings automatically restrict message content?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
