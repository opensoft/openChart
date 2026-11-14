# Sex Assigned at Birth Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures sex assigned at birth as a provenance-qualified demographic fact distinct from gender identity and clinical sex parameters.
Topics: openchart-feature-catalog, registration, frappe, sex-at-birth
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-036 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Purpose-aware disclosure** — Expose the field only to workflows with a documented clinical or reporting need.

## Focus

Store this sensitive fact using modern distinctions, explicit unknown states, and least-privilege access.

## Behavior

- The intake explains the field's purpose and distinguishes it from current gender identity.
- Patients may answer with supported coded values, unknown, or declined.
- Staff record whether the value is patient-reported, proxy-reported, document-derived, or imported.
- The field is not used alone to infer anatomy, pregnancy capability, or clinical decision parameters.
- Changes preserve prior values and record source, actor, reason, and effective time.
- Unauthorized users see no value and cannot infer it from search filters or exports.

## Frappe realization

- **DocTypes:** `OC Sex Assigned At Birth Record` with coded value, original_text, source, validity, supersedes, and disclosure profile.
- **Workflow:** Draft → Accepted → Superseded or Withdrawn.
- **Roles/permissions:** `OC Registration Clerk` captures; sensitive value uses permlevel 2 and purpose-aware API filtering.
- **API/surfaces:** `open_chart.api.v1.registration.update_sex_at_birth`; respectful intake control, restricted demographic panel, and audit report.

## Boundaries

Owns: sex-assigned-at-birth demographic fact. Consumes: patient or qualified source assertion. Emits: permission-scoped versioned value. Does not own: gender identity, anatomy inventory, or clinical sex parameters.

## Open questions

- Which downstream purposes justify access, and how should they be reviewed?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
