# Mandatory Clinical Question — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Requires a concise answerable clinical question on imaging orders so protocoling and interpretation can address the reason for examination.
Topics: openchart-feature-catalog, imaging, frappe, clinical-question
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-002 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Appropriateness evidence prompt** — Surface organization-approved guidance references while preserving clinician judgment.

## Focus

This feature isolates the clinical question as a mandatory, reviewable element distinct from diagnosis codes or copied history.

## Behavior

- The ordering clinician must enter a patient-specific question before signing an imaging order.
- The field rejects whitespace-only text and configurable non-informative phrases.
- Relevant symptoms, diagnoses, prior studies, and rule references may be linked as supporting context.
- Guidance can warn when the selected study appears mismatched, but it cannot place, change, or cancel an order autonomously.
- A radiologist or technologist may request clarification and suspend downstream readiness.
- The signed question remains immutable; corrections use the order's governed succession path.

## Frappe realization

- **DocTypes:** fields `clinical_question`, `supporting_context`, and child `OC Imaging Guidance Evidence` on `OC Imaging Order`.
- **Rules:** mandatory and `depends_on` expressions show study-specific prompts; server `validate` applies versioned policy beyond client checks.
- **Roles/permissions:** ordering clinicians author; imaging staff read and open clarification; policy managers maintain phrase and guidance rules.
- **API/surfaces:** guarded order methods return structured validation errors; the question appears in worklists, requisition Print Formats, and report context.

## Boundaries

Owns: the order's answerable question and validation state. Consumes: clinical context and appropriateness rules. Emits: interpretation context and clarification tasks. Does not own: medical necessity decisions or autonomous study selection.

## Open questions

- Which specialty-specific minimum-content rules should be configurable without encouraging boilerplate?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
