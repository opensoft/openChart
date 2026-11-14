# Store-And-Forward Specialist Review — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Packages authorized clinical questions and evidence for asynchronous specialist review with a closed-loop response.
Topics: openchart-feature-catalog, telehealth, frappe, store-and-forward
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-014 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Specialty evidence checklist** — Require reviewed artifact sets for dermatology, ophthalmology, or other store-and-forward services.

## Focus

This feature isolates the asynchronous handoff from a requesting clinician to an authorized specialist and back.

## Behavior

- A requester selects a specialty, clinical question, urgency, patient authorization basis, and included chart artifacts.
- The package snapshots references and provenance so later chart changes do not obscure what the specialist reviewed.
- Routing checks specialist assignment, jurisdiction, service eligibility, and declared response target.
- The specialist may accept, request more information, redirect, decline, or submit a signed opinion.
- Additional evidence is appended with source and timestamp; it never replaces the original package silently.
- The final opinion returns to the requester and patient-release workflow with acknowledgment responsibility.

## Frappe realization

- **DocTypes/workflow:** `OC Store Forward Review`, child `OC Review Evidence`, and `OC Specialist Opinion` use Draft, Submitted, Assigned, Needs Information, Responded, Acknowledged, and Closed states.
- **API/permissions:** guarded package and response methods enforce patient and specialty user permissions; Specialist sees only explicitly included records plus minimum context.
- **Surfaces:** requester and specialist Kanban views, SLA Number Cards, Notifications, and a signed Jinja Print Format support the closed loop.

## Boundaries

Owns: review package, routing state, and specialist opinion. Consumes: authorized chart evidence and specialist authority. Emits: signed response and acknowledgment task. Does not own: referral fulfillment or downstream treatment.

## Open questions

- When is a store-and-forward opinion part of the patient's encounter versus a distinct specialist encounter?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
