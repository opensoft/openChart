# Occupational Health Screening Program — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates employee screening requirements while enforcing purpose-limited employer reporting and separation from the general clinical chart.
Topics: openchart-feature-catalog, public-health, frappe, occupational-health
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-036 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Employer compliance roster** — Share minimum-necessary completion status through an isolated, audited portal.

## Focus

Employee screening episodes with a hard boundary between clinical findings and employer-facing fitness status.

## Behavior

- Occupational-health staff enroll an employee under a program, job requirement profile, authorization, and effective period.
- Screening milestones link immunizations, TB, respirator, exposure, laboratory, or clearance records as configured.
- Employer recipients see only approved completion, restriction, expiry, or follow-up-needed conclusions.
- Clinical values and diagnoses remain hidden unless separately authorized and legally permissible.
- Changes to employment or program requirements create new effective assignments rather than rewriting history.
- Every employer disclosure records recipient, purpose, fields, authorization, and artifact digest.

## Frappe realization

- **DocTypes:** Add `OC Occupational Screening Episode`, `OC Job Requirement Profile`, and `OC Employer Disclosure` with field-level disclosure snapshots.
- **Workflow:** Use enrolled, in-progress, clinical-review, cleared, restricted, expired, and closed states.
- **Permissions:** Create isolated roles and User Permissions by employer; protect clinical links at permlevel 2 from employer users.
- **Surfaces:** Provide occupational workspace, expiry Query Reports, minimum-necessary Print Formats, and an audited portal endpoint.

## Boundaries

Owns: occupational program coordination and employer disclosure artifacts. Consumes: employment assignment, authorization, and clinical evidence. Emits: bounded fitness/completion status. Does not own: employment decisions, general HR, or unrestricted chart disclosure.

## Open questions

- Should occupational records live in the same site with strict permissions or a separate Frappe tenant?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
