# Vaccine Declination And Objection Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records a patient or guardian vaccine declination, objection basis, counseling, scope, and effective period without treating it as a permanent contraindication.
Topics: openchart-feature-catalog, public-health, frappe, vaccine-declination
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-015 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Periodic reconsideration prompt** — Surface time-bounded, non-coercive review opportunities.

## Focus

An attributable declination record distinct from clinical contraindications and consent withdrawal.

## Behavior

- Clinicians select vaccine or series scope, declining party, authority relationship, reason category, and effective date.
- Free-text patient wording and counseling details remain alongside coded categories.
- States are active, expired, withdrawn, superseded, and entered-in-error.
- Forecasts may display an active declination but continue showing clinical due status separately.
- A guardian authority failure blocks acceptance for a minor and routes verification.
- Amendments preserve prior objections and never infer refusal for unlisted vaccines.

## Frappe realization

- **DocTypes:** Add submittable `OC Vaccine Declination` with patient, vaccine scope, reporter, authority, counseling, signature/evidence, and predecessor fields.
- **Workflow:** Use draft, accepted, withdrawn, expired, superseded, and entered-in-error states with succession-based amendment.
- **Permissions:** Allow clinician entry, guardian evidence review by `OC Health Information Manager`, and sensitive-reason fields at permlevel 1.
- **Surfaces:** Provide a Jinja declination Print Format, patient-chart badge with expiry, and due-review scheduler notifications.

## Boundaries

Owns: declination assertions and counseling evidence. Consumes: patient, guardian authority, vaccine terminology, and consent context. Emits: reviewable declination status. Does not own: contraindications, schedule eligibility, or coercive outreach.

## Open questions

- Which objection reason details should be hidden from routine aggregate reporting?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
