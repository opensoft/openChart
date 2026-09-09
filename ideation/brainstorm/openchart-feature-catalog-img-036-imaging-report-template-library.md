# Imaging Report Template Library — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains versioned report templates by study type, modality, subspecialty, facility, language, and author preference under clinical governance.
Topics: openchart-feature-catalog, imaging, frappe, report-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-036 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Template usage feedback** — Compare completion, edit, and omission patterns for reviewed template improvement.

## Focus

This feature isolates reusable reporting structure without constraining the radiologist to unreviewed boilerplate.

## Behavior

- Template authors define sections, labels, requiredness, defaults, structured fields, conditional visibility, and applicable studies.
- Every published version records owner, approvers, effective dates, evidence references, and superseded version.
- Report creation selects a template using transparent applicability and allows an authorized user to choose another valid template.
- Default text is visibly distinguished until reviewed and cannot imply findings automatically.
- Existing reports retain their template version when the library changes.
- Retired templates remain readable for provenance but cannot seed new reports.

## Frappe realization

- **DocTypes:** `OC Imaging Report Template` and submittable `OC Imaging Report Template Version` with child sections and field definitions.
- **Workflow:** Draft → Clinical Review → Approved → Active → Retired.
- **Roles/permissions:** template editors draft; modality leads approve; radiologists use active versions and may save private preferences separately.
- **Hooks/API/surfaces:** validation detects duplicate field keys and applicability overlap; report form renderer builds sections; Query Report shows adoption and stale drafts.

## Boundaries

Owns: report template content, versioning, applicability, and governance. Consumes: study catalog and structured element definitions. Emits: report draft structure. Does not own: final interpretation or speech-recognition tooling.

## Open questions

- Which template elements may be personalized without forking governed clinical content?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
