# Outside-record Diff View — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Compares extracted claims from an outside record with current chart data and presents source-grounded differences for explicit reconciliation.
Topics: openchart-feature-catalog, documents, frappe, outside-record-diff
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-036 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Reconciliation work packet** — Bundle selected differences into owner-specific review tasks without writing chart facts automatically.

## Focus

This feature isolates a side-by-side comparison aid; the outside document and current chart remain separate authorities until human reconciliation.

## Behavior

- A clinician opens an accepted outside record and requests comparison for supported fact families such as medications, allergies, problems, or demographics.
- Extraction produces candidate claims with source page, region, text, confidence, and engine or reviewer provenance.
- The view aligns candidates with current chart entries and labels match, possible conflict, outside-only, chart-only, or unresolved.
- Users can filter and annotate differences, but no action silently changes either source.
- Sending a difference to reconciliation creates a typed task or draft through the owning clinical workflow.
- Low confidence, temporal ambiguity, negation, copied history, and patient mismatch remain explicit uncertainty.
- The comparison records source document version and chart snapshot time so later changes do not rewrite prior review evidence.

## Frappe realization

- **DocTypes:** `OC Outside Record Comparison` (document_version, chart_snapshot_at, extractor_version, state) with child `OC Outside Record Difference` (fact_family, source_evidence JSON, chart_reference, category, disposition).
- **Jobs:** RQ extraction/alignment runs are bounded and human-reviewed; model output cannot call clinical write APIs.
- **Roles/permissions:** Clinician reviews; domain-specific Medication/Allergy/Problem Reviewer owns reconciliation; Document Indexer cannot accept clinical facts.
- **API/surfaces:** Guarded comparison request and task-creation methods; Desk split-view links source-page regions and current records.
- **Provenance:** Any reconciliation handoff carries document version, exact excerpt, reviewer, and disposition into the owning workflow.

## Boundaries

Owns: comparison snapshot, candidate alignment, difference classification, and handoff evidence. Consumes: outside document/OCR and current chart read projection. Emits: human-reviewed reconciliation request. Does not own: clinical truth, automatic chart updates, or document import.

## Open questions

- Which fact families have sufficiently clear temporal and negation models for an initial comparison release?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [External Records Import Bundles](openchart-feature-catalog-dms-011-external-records-import-bundles.md)
