# Manual Chart Abstraction Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures reviewed quality-reporting facts from source documents when discrete data is unavailable while preserving provenance and limited authority.
Topics: openchart-feature-catalog, quality-reporting, frappe, chart-abstraction
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-018 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Dual abstraction sampling** — Compare independent abstractions to measure reviewer agreement and training needs.

## Focus

Structured abstraction for measurement use that never masquerades as an original clinical observation or diagnosis.

## Behavior

- An abstractor selects patient, measure data element, source document, source page or section, observed value, date, and certainty.
- The entry records whether the fact is absent from discrete data, conflicting, unreadable, or otherwise unsuitable for direct extraction.
- Required evidence includes a permitted source reference and exact location; copied attachments are avoided where possible.
- Entries move through draft, review, accepted-for-measurement, rejected, expired, and superseded states.
- High-risk or exclusion-related abstractions can require a second reviewer.
- Accepted abstractions participate only in configured measure contexts and remain labeled manual.
- Source amendment, access revocation, or period change marks affected abstractions stale for review.

## Frappe realization

- **DocTypes:** Add `OC Measure Abstraction` with patient, measure element, source Dynamic Link, locator, typed value fields, certainty, context, and successor link.
- **Workflow:** Separate `OC Quality Abstractor` entry from `OC Abstraction Reviewer` acceptance; support dual review by policy.
- **Hooks and API:** Validate source access and typed values, guard writes under `open_chart.api.v1.quality.submit_abstraction`, and mark stale on source succession.
- **Surfaces:** Provide Quick Entry, document-side abstraction panel, review queue, and inter-rater Script Report.

## Boundaries

Owns: measurement-only abstracted assertions and review. Consumes: source documents, measure data definitions, patient identity, and permissions. Emits: provenance-labeled measure inputs. Does not own: original clinical documentation, diagnosis, or source-document correction.

## Open questions

- Which measure elements permit abstraction and what dual-review sampling rate is defensible?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
