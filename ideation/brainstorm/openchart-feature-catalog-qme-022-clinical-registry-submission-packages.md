# Clinical Registry Submission Packages — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assembles validated registry packages for diabetes, hypertension, and similar collaboratives using profile-specific data and consent controls.
Topics: openchart-feature-catalog, quality-reporting, frappe, registry-package
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-022 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Registry conformance sandbox** — Test package mappings against synthetic registry fixtures before production release.

## Focus

Reusable, profile-governed package assembly for voluntary or contractual clinical registries.

## Behavior

- A registry manager configures program, cohort, period, data-use purpose, destination profile, and required approvals.
- Cohort selection uses explicit inclusion rules and presents patient-level membership for authorized review.
- Package generation maps approved clinical and measure data to the registry schema with source-field traceability.
- Consent, opt-out, sensitive-data, and minimum-necessary rules suppress unauthorized fields or patients.
- Validation reports required-field, vocabulary, identity, date, and cross-field errors before release.
- Released packages include manifest, profile version, row counts, suppression counts, checksum, and receipt placeholder.
- Corrections create amendment packages linked to the original release.

## Frappe realization

- **DocTypes:** Add `OC Registry Profile`, `OC Registry Submission Package`, and child cohort, mapping, manifest, suppression, and error rows.
- **Workflow:** Use configured, generating, validation-failed, review, approved, released, acknowledged, and amended states.
- **Jobs and API:** Generate in rq through guarded quality APIs; keep destination credentials in site configuration or secret references.
- **Surfaces:** Provide cohort Script Reports, package dashboards, exception queues, and permissioned file downloads.

## Boundaries

Owns: registry profiles, cohort package assembly, validation, and release evidence. Consumes: clinical records, measure results, consent, mappings, and registry requirements. Emits: authorized packages and manifests. Does not own: registry governance, transport acceptance, or clinical interventions.

## Open questions

- Which registries require patient-level consent beyond organizational data-use authority?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
