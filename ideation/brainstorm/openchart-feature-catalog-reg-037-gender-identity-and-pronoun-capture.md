# Gender Identity and Pronoun Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records self-described gender identity, pronouns, and display preferences so staff communicate respectfully without altering legal identity facts.
Topics: openchart-feature-catalog, registration, frappe, gender-pronouns
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-037 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Respectful-language cues** — Present concise pronoun and form-of-address guidance on approved care surfaces.

## Focus

Capture current self-identification and communication cues independently from legal name and sex assigned at birth.

## Behavior

- Patients may select coded gender identities, self-describe, list pronouns, or decline.
- Multiple pronoun sets can be ranked or marked context-specific.
- The patient controls whether identity and pronouns appear on routine, portal, label, and restricted surfaces.
- Staff cannot overwrite self-described text with a narrower code; mappings remain separate.
- Changes are effective-dated and preserve prior responses under sensitive-history permissions.
- Missing information never causes legal sex, name, appearance, or title to be used as a substitute.

## Frappe realization

- **DocTypes:** `OC Gender Identity Record` and child `OC Pronoun Preference` with coded value, self_description, display_scope, rank, and validity.
- **Workflow:** Draft → Active → Superseded or Withdrawn.
- **Roles/permissions:** `OC Patient Portal User` and `OC Registration Clerk` maintain; history and restricted scopes use permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.update_gender_profile`; patient-facing form, approved chart cues, and permission-aware print rendering.

## Boundaries

Owns: self-described gender identity and pronoun preferences. Consumes: patient statements. Emits: permission-qualified respectful display guidance. Does not own: legal identity or clinical anatomy.

## Open questions

- Which default surfaces best balance respectful use with patient-controlled privacy?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
