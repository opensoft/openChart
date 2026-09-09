# Employer Information Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures current and historical employer details for registration use while minimizing unnecessary employment disclosure.
Topics: openchart-feature-catalog, registration, frappe, employer-data
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-013 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Occupational context handoff** — Offer selected employment facts to clinical workflows only with an explicit purpose and permission.

## Focus

Store employer identity and contact facts as optional registration data with clear purpose limits.

## Behavior

- Staff capture employer name, employment status, occupation label, contact details, and effective dates.
- Patients may decline fields not required by a documented registration purpose.
- Employer address is stored as employer data, not copied into the patient's residence.
- Ending employment closes the record without deleting historical registration context.
- Restricted employer details are excluded from default patient summaries and global search.
- Changes record source and actor and do not overwrite prior accepted values.

## Frappe realization

- **DocTypes:** `OC Patient Employment` with employer_name, status, occupation_text, contact_json, validity, declined, and purpose.
- **Workflow:** Draft → Active → Ended or Superseded.
- **Roles/permissions:** `OC Registration Clerk` edits; `OC Privacy Officer` audits purpose; clinical roles require explicit permlevel 1 access.
- **API/surfaces:** `open_chart.api.v1.registration.upsert_employment`; intake section, patient registration tab, and active-employment report.

## Boundaries

Owns: registration employment facts. Consumes: patient assertions. Emits: purpose-limited employer data. Does not own: occupational health assessment or payroll information.

## Open questions

- Which care settings have a legitimate minimum requirement for employer contact data?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
