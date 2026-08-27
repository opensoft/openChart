# Parent Reported Immunization Dose — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures a parent or caregiver report of a prior dose as an explicitly unverified assertion pending evidence or registry confirmation.
Topics: openchart-feature-catalog, public-health, frappe, caregiver-reported-dose
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-008 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Portal evidence follow-up** — Request a card image or source details from an authorized proxy.

## Focus

Safe capture of caregiver knowledge without silently elevating it to a verified clinical record.

## Behavior

- Staff record reporter identity and relationship, reported vaccine wording, approximate date, and confidence.
- The saved assertion always displays an unverified patient-source label.
- Approximate dates retain month-only, year-only, or range precision instead of fabricated exact dates.
- The assertion may open a registry query or evidence task but does not become confirmed automatically.
- A reviewer can link later evidence and create a verified successor while preserving the original report.
- Proxy authority or consent failures block portal submission and leave no accepted assertion.

## Frappe realization

- **DocTypes:** Add `OC Reported Immunization Assertion` with Dynamic Link reporter, relationship, original wording, date precision, confidence, and successor fields.
- **Workflow:** Use reported, evidence-requested, verified-by-successor, unable-to-verify, and entered-in-error states.
- **Permissions:** Allow clinical intake roles to create; apply guardian authority and patient User Permissions; reserve verification for `OC Clinician`.
- **Surfaces:** Provide Quick Entry, a permissioned portal Web Form, Notification tasks for evidence, and a clearly labeled history row.

## Boundaries

Owns: the caregiver-reported assertion and follow-up state. Consumes: proxy authority and patient identity. Emits: review tasks and sourced history candidates. Does not own: verification evidence or schedule acceptance policy.

## Open questions

- Should any emergency workflow permit temporary scheduling use of an unverified report?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
