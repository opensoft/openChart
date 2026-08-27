# Template Letter Library — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides versioned clinical and administrative letter templates with governed merge fields, approval, preview, and Letter Head support.
Topics: openchart-feature-catalog, documents, frappe, letter-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-021 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Multilingual template variants** — Maintain translation-linked versions with independent review and locale-aware fallback.

## Focus

This feature isolates reusable letter authoring and governance before patient-specific rendering.

## Behavior

- A Template Author creates a named template for a purpose, audience, facility, locale, and Letter Head.
- Authors insert only allowlisted merge fields grouped by patient, clinician, encounter, appointment, or organization context.
- Preview uses synthetic `SYN-` data and identifies missing, unauthorized, or ambiguous fields.
- A Template Approver reviews wording, field exposure, layout, and effective dates before activation.
- Active versions are immutable; editing creates a draft successor with its own approval.
- Retiring a template prevents new use while preserving letters rendered from prior versions.
- Rendering records exact template version and source-value snapshot for reproducibility.

## Frappe realization

- **DocTypes:** `OC Letter Template` (purpose, locale, facility, letter_head, state, current_version) and `OC Letter Template Version` (Jinja body, allowed_fields, effective dates, supersedes).
- **Workflow:** Draft → Review → Active, with Rejected, Retired, and Superseded states.
- **Roles/permissions:** Template Author drafts; Template Approver activates; field groups enforce role-aware merge access at render time.
- **Print formats:** Build governed Jinja Print Formats and Frappe Letter Heads; server-side sandbox validation rejects unsafe expressions and undeclared fields.
- **API/surfaces:** `open_chart.api.v1.documents.preview_letter_template`; Desk editor, synthetic preview, and template-usage Query Report.

## Boundaries

Owns: template text, allowlisted fields, versions, approval, and layout selection. Consumes: Letter Head and synthetic preview context. Emits: approved render definition. Does not own: cohort selection, recipient identity, mail delivery, or source clinical facts.

## Open questions

- Which merge-field groups may expose sensitive clinical data in externally addressed letters?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Cohort Mail-merge Batch Letters](openchart-feature-catalog-dms-022-cohort-mail-merge-batch-letters.md)
