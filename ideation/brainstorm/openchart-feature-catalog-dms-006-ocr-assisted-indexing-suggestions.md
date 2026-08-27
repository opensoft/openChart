# OCR-assisted Indexing Suggestions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Suggests patient, document type, and service date from OCR evidence for explicit human acceptance or rejection.
Topics: openchart-feature-catalog, documents, frappe, assisted-indexing
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-006 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Field evidence highlighting** — Jump reviewers from a proposed value to the exact source-page region that supports it.

## Focus

This feature isolates explainable indexing assistance while preserving human authority over chart association.

## Behavior

- A Document Indexer opens an OCR-complete item and sees ranked patient, class, and date candidates.
- Every suggestion displays confidence, matching factors, source page coordinates, and model or rule version.
- The reviewer accepts, edits, rejects, or marks each field unresolved independently.
- Conflicting identifiers, multiple plausible patients, or low confidence block final indexing.
- Accepted values record the reviewer and evidence; rejected suggestions remain available for quality evaluation.
- No candidate writes demographics, clinical facts, or document classification before confirmation.
- A later OCR or model run never changes previously accepted metadata without a new review decision.

## Frappe realization

- **DocTypes:** `OC Indexing Review` (document_version, OCR_run, state, reviewer) with child `OC Indexing Suggestion` (field_name, proposed_value, confidence, evidence JSON, disposition, accepted_value).
- **Workflow:** Suggested → Human Review → Confirmed, with Identity Conflict and Unresolved states.
- **Roles/permissions:** Document Indexer decides ordinary fields; Patient Identity Reviewer resolves patient candidates; integration roles cannot transition to Confirmed.
- **API/jobs:** RQ suggestion job reads OCR output and permitted patient indexes; guarded `open_chart.api.v1.documents.confirm_indexing` validates all human dispositions.
- **Surfaces:** Desk side-by-side review uses client scripts for evidence highlighting and Assignment Rules for conflicts.

## Boundaries

Owns: candidate values, evidence, reviewer dispositions, and confirmed document index metadata. Consumes: OCR run, patient search projection, and class rules. Emits: confirmed indexing decision. Does not own: patient merge, OCR generation, or autonomous chart attachment.

## Open questions

- Which patient matching factors are safe to expose to document indexers at each facility?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Unmatched-document Resolution Queue](openchart-feature-catalog-dms-008-unmatched-document-resolution-queue.md)
