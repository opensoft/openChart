# Preferred Language Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records spoken, written, and preferred care languages with proficiency and provenance to support understandable interactions.
Topics: openchart-feature-catalog, registration, frappe, preferred-language
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-034 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Language-aware document routing** — Prefer available translated forms without claiming equivalence automatically.

## Focus

Represent language needs as more than one preferred-language dropdown.

## Behavior

- Patients may list multiple spoken, written, signed, or other communication languages.
- Each entry records use, proficiency, preference rank, source, and effective dates.
- The preferred language for care may differ from the preferred language for written materials.
- Unknown and declined are explicit states and never default to the site's primary language.
- Staff can search a configured terminology while retaining a patient-stated language label.
- Changes notify dependent accommodation review without autonomously booking an interpreter.

## Frappe realization

- **DocTypes:** `OC Patient Language` with code, display, patient_wording, modality, proficiency, rank, preferred_for, and validity.
- **Workflow:** Draft → Active → Superseded or Inactive.
- **Roles/permissions:** `OC Registration Clerk` and `OC Patient Portal User` maintain; all care roles read active language needs.
- **API/surfaces:** `open_chart.api.v1.registration.update_languages`; registration multi-select, patient banner, portal profile, and language-needs report.

## Boundaries

Owns: patient language facts and preferences. Consumes: terminology and patient statements. Emits: modality-specific language needs. Does not own: translation content or interpreter scheduling.

## Open questions

- Which proficiency scale is understandable enough for patient self-report?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
