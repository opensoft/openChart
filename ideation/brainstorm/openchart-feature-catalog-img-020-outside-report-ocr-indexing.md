# Outside Report OCR-assisted Indexing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Extracts candidate metadata and text from scanned outside imaging reports for human verification, indexing, and provenance-preserving attachment.
Topics: openchart-feature-catalog, imaging, frappe, report-ocr
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-020 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Section confidence review** — Prioritize low-confidence patient, date, impression, and recommendation fields for verification.

## Focus

This feature isolates assistive OCR indexing without treating extracted text as an accepted diagnostic report automatically.

## Behavior

- Staff attach a scanned report to a matched outside-study import or patient document intake.
- OCR proposes patient identifiers, study type, dates, facility, author, findings, impression, and recommendations with confidence evidence.
- A reviewer compares each proposed field with the source image before acceptance.
- Patient or study conflicts block indexing and route back to identity review.
- Accepted text remains linked to the immutable source attachment, OCR engine version, and reviewer.
- Low confidence, unreadable pages, handwriting, and multi-report scans remain explicitly unresolved.

## Frappe realization

- **DocTypes:** `OC Outside Imaging Report` with source File, OCR run, candidate fields, accepted index values, reviewer, and linked study.
- **Workflow:** Uploaded → OCR Processing → Verification → Indexed, with Identity Conflict and Unreadable states.
- **Roles/permissions:** document indexers verify; clinicians read accepted indexes and source; OCR integration users cannot accept content.
- **API/jobs/surfaces:** RQ job calls configured OCR adapter; review form shows source and candidates side by side; search indexes only accepted values.

## Boundaries

Owns: OCR candidates, human verification, searchable index, and source provenance. Consumes: scanned report and identity match. Emits: indexed external report reference. Does not own: diagnostic reinterpretation or autonomous finding registration.

## Open questions

- Which extracted fields may enter clinical search versus remaining document-only metadata?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
