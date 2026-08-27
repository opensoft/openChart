# Data-driven PDF Form Generation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates patient-specific PDFs from approved form templates and versioned data snapshots with review, provenance, and immutable output.
Topics: openchart-feature-catalog, documents, frappe, pdf-form-generation
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-030 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Fillable field overlays** — Produce standards-compatible interactive fields while preserving a flattened archival rendition.

## Focus

This feature isolates reproducible form rendering from governed chart data without granting templates arbitrary data access.

## Behavior

- An authorized user selects an approved form template, patient context, purpose, and effective date.
- The system resolves only allowlisted fields and freezes a source-value snapshot with provenance.
- Missing required values, conflicting current records, and restricted fields appear before generation.
- The user may correct source records through their owning workflows or enter explicitly permitted form-only values.
- Preview shows all pages, overflow, omitted fields, and signature placeholders.
- Approval produces an immutable private PDF with template version, snapshot checksum, generator version, and actor.
- Regeneration after source changes creates a new output version and never alters a previously signed or disclosed PDF.

## Frappe realization

- **DocTypes:** `OC PDF Form Template` (purpose, source PDF/File, field map JSON, allowed_fields, version, state) and `OC Generated PDF Form` (patient, template_version, snapshot JSON, output_file, checksum, state).
- **Files/jobs:** Private Frappe Files store templates and outputs; `open_chart.documents.on_file` validates MIME and ownership; RQ renders overlays and archival flattening.
- **Workflow:** Requested → Data Review → Preview → Generated, with Deficient, Failed, Signed, and Superseded states.
- **Roles/permissions:** Form Template Author maps fields; Template Approver activates; clinical users generate only allowed purposes and patient scope.
- **API/surfaces:** Guarded generation API, Desk/portal preview where authorized, and Frappe Print Format cover/attestation pages.

## Boundaries

Owns: form template mapping, data snapshot, render attempt, output, and provenance. Consumes: permissioned chart values and approved PDF template. Emits: immutable generated form. Does not own: source clinical facts, signature authority, submission to external agencies, or arbitrary report building.

## Open questions

- Which form-only overrides are safe, and how must they be labeled when they differ from chart data?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Digital Signature Certificate Application](openchart-feature-catalog-dms-039-digital-signature-certificate-application.md)
