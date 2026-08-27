# Imported-Data Normalization Review — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Proposes normalized codes, units, dates, and record classes for imported data through an accountable review queue.
Topics: openchart-feature-catalog, clinical-ai, frappe, data-normalization
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-041 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Mapping promotion workflow** — Convert repeatedly approved normalization pairs into governed deterministic mappings.

## Focus

This feature isolates AI-assisted cleanup of imported records without overwriting source data or silently asserting clinical equivalence.

## Behavior

- Data stewards submit an import batch for candidate terminology, unit, date, duplicate, and record-class normalization.
- Every proposal retains raw value, source file and row, candidate normalized value, confidence, rationale, and mapping evidence.
- Reviewers accept, modify, reject, or defer each proposal individually or in an evidence-consistent batch.
- Accepted proposals create reviewed normalized projections or successor records; raw imports remain immutable.
- Ambiguous patient identity, incompatible units, or clinically meaningful text differences route to specialized review.
- No normalization can create an order, diagnosis, or result interpretation autonomously.

## Frappe realization

- **DocTypes:** `OC AI Normalization Job` and child `OC Normalization Proposal` store batch, raw source pointers, candidates, terminology, reviewer, disposition, and projection Links.
- **Workflow:** Queued → Processing → Data Review → Clinical Review if needed → Applied/Rejected/Partial.
- **Roles/permissions:** `OC Data Steward` reviews technical mappings; qualified clinical reviewers resolve clinical equivalence; identity reviewers handle linkage.
- **Jobs/API/surfaces:** rq generates candidates; guarded apply method writes succession-based projections; Data Import integration and Script Report show exceptions.

## Boundaries

Owns: normalization candidates and reviewed projection evidence. Consumes: immutable imported data and terminology. Emits: human-approved normalized representations. Does not own: source alteration, identity merge, or autonomous clinical assertion.

## Open questions

- Which normalization classes are safe for evidence-consistent batch approval?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Scanned-Document Indexing Review](openchart-feature-catalog-aic-040-scanned-document-indexing-review.md)
