# Scanned-Document Indexing Review — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Extracts and indexes text and metadata from scanned clinical documents through a human-reviewed back-office queue.
Topics: openchart-feature-catalog, clinical-ai, frappe, document-indexing
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-040 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Page-level quality map** — Highlight low-confidence OCR, handwriting, rotation, and missing-page concerns for reviewers.

## Focus

This feature isolates batch AI assistance for scanned-document discoverability without silently creating discrete clinical facts.

## Behavior

- Authorized staff submit existing attachments or bounded batches for OCR, classification, date extraction, and candidate patient linkage.
- Each page retains source file, checksum, extraction coordinates, confidence, and model/version.
- Reviewers correct text, document class, dates, and patient linkage before approving the index.
- Low-confidence or conflicting identity candidates remain unlinked and assigned for manual resolution.
- Approval updates search metadata only; it does not create diagnoses, medications, results, or other discrete facts.
- Failed or malware-quarantined files remain excluded with visible reasons.

## Frappe realization

- **DocTypes:** `OC AI Document Index Job` and `OC Document Index Draft` store files, checksums, page extraction, candidate metadata, artifact, reviewer, and disposition.
- **Workflow:** Queued → Processing → Pending Review → Approved/Rejected/Needs Identity Review.
- **Roles/permissions:** Health Information Management reviewers access assigned files; identity linkage requires `OC Identity Reviewer`.
- **Jobs/surfaces:** rq processes pages in isolated workers; File hooks preserve checksums; Kanban review queue and permission-aware global search consume approved index text.

## Boundaries

Owns: extracted search index and review evidence. Consumes: authorized scanned files. Emits: approved searchable text and metadata. Does not own: source-document alteration, patient merge, or discrete clinical facts.

## Open questions

- Should corrected OCR remain a separate index layer or become an amendment to document metadata?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Imported-Data Normalization Review](openchart-feature-catalog-aic-041-imported-data-normalization-review.md)
