# Refugee And Immigrant Intake Screening — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates configurable refugee and immigrant intake screening checklists with interpretation, consent, provenance, and referral tracking.
Topics: openchart-feature-catalog, public-health, frappe, newcomer-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-035 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Translated intake packets** — Deliver governed language variants with interpreter and literacy accommodations.

## Focus

A respectful program checklist that tracks screening completion without stereotyping or inferring conditions from origin.

## Behavior

- Staff select a jurisdiction/program profile and record arrival context only when relevant and authorized.
- Checklist items may include immunization reconciliation, TB, lead, infection, mental health, and referral milestones.
- Every item states why it applies, required evidence, status, and accountable owner.
- Country or migration history never creates a diagnosis or order automatically.
- Interpreter use, consent, trauma-informed deferral, and declined items retain explicit provenance.
- Profile changes mark open episodes for review without rewriting completed historical items.

## Frappe realization

- **DocTypes:** Add `OC Newcomer Screening Episode`, versioned `OC Newcomer Program Profile`, and child checklist/referral rows.
- **Workflow:** Use intake, in-progress, deferred, awaiting-results, referral-follow-up, complete, and closed-incomplete states.
- **Permissions:** Apply purpose-based roles, sensitive-field permlevels, patient User Permissions, and interpreter-access boundaries.
- **Surfaces:** Provide checklist workspace, multilingual Print Formats, Gantt milestones, and incomplete-item Query Reports.

## Boundaries

Owns: program checklist and coordination state. Consumes: demographics, consent, interpreter needs, immunizations, screenings, and referrals. Emits: accountable milestones. Does not own: immigration status adjudication, diagnosis, or generalized risk inference.

## Open questions

- Which migration-context fields are necessary enough to justify collection and retention?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
