# Core Demographic Profile — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures foundational demographic facts with explicit unknown states to support safe identification, reporting, and care workflows.
Topics: openchart-feature-catalog, registration, frappe, core-demographics
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-004 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Demographic completeness score** — Surface policy-relevant gaps without inventing defaults.

## Focus

Define the small current demographic profile shared by registration and downstream chart contexts.

## Behavior

- Staff capture date of birth, place of birth, marital status, and other configured core facts.
- Every coded field supports unknown, declined, and not-applicable where semantically valid.
- Date-of-birth precision distinguishes exact, estimated, month-only, and year-only values.
- Age is derived at use time and never stored as the authoritative fact.
- Implausible combinations warn the user and require correction or documented override.
- Accepted changes retain prior values, author, source, and effective time.

## Frappe realization

- **DocTypes:** `OC Patient Demographic Profile` linked one-to-one with `OC Patient`, plus `OC Demographic Value History` for succession.
- **Workflow:** Draft → Verified → Superseded, with supervisor review for configured sensitive changes.
- **Roles/permissions:** `OC Registration Clerk` edits drafts; `OC Registration Supervisor` overrides warnings; all chart roles read permitted fields.
- **API/surfaces:** `open_chart.api.v1.registration.update_demographics`; patient form section, completeness indicator, and demographic history report.

## Boundaries

Owns: foundational non-contact demographic facts. Consumes: patient assertions and evidence. Emits: normalized current facts and history. Does not own: clinical observations or social screening responses.

## Open questions

- Which demographic changes should always require secondary review?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
