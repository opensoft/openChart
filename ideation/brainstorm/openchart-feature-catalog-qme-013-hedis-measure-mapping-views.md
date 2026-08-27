# HEDIS Aligned Measure Mapping Views — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows governed mappings between local clinical data, internal measures, and licensed HEDIS-aligned concepts without asserting unsupported equivalence.
Topics: openchart-feature-catalog, quality-reporting, frappe, hedis-mapping
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-013 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Mapping coverage heatmap** — Identify measures and data elements with weak, partial, or unreviewed alignment.

## Focus

Transparent mapping review for HEDIS-aligned reporting while respecting licensing, version, and semantic differences.

## Behavior

- A measure librarian records source and target releases, mapped concepts, relationship type, rationale, and licensing constraint.
- Relationships are exact, broader, narrower, partial, transformed, unsupported, or pending review.
- Mapping views compare populations, data elements, value sets, timing, exclusions, and evidence requirements.
- Version changes mark affected mappings stale and prevent implicit carry-forward.
- Analysts can see where a local rate is comparable, directionally related, or not comparable.
- Export excludes licensed expression content when redistribution is not authorized.
- Approval records reviewer identity and synthetic examples supporting the relationship.

## Frappe realization

- **DocTypes:** Add `OC Measure Mapping` and child `OC Measure Element Mapping` with release Links, relationship, rationale, transformation Code, license class, and status.
- **Workflow:** Use draft, review, approved, stale, rejected, and superseded states with librarian/reviewer separation.
- **Hooks:** Detect source or target release succession and mark mappings stale; validate duplicate active relationships.
- **Surfaces:** Provide side-by-side mapping views, coverage Query Reports, and permission-aware exports.

## Boundaries

Owns: local mapping assertions and review evidence. Consumes: authorized measure metadata, terminology, and local data definitions. Emits: alignment views and mapping gaps. Does not own: HEDIS intellectual property, certification, or official rate submission.

## Open questions

- What licensed content may be stored, displayed, and exported by different deployment models?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
