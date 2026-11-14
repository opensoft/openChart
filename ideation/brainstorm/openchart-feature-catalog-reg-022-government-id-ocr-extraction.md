# Government ID OCR Extraction — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Extracts candidate identity fields from captured government IDs for human confirmation without silently updating the patient record.
Topics: openchart-feature-catalog, registration, frappe, government-id-ocr
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-022 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Document-layout adapters** — Add jurisdiction-specific parsers with measurable field confidence.

## Focus

Turn an identity-document image into reviewable candidate data while keeping humans authoritative.

## Behavior

- OCR runs only on an authorized retained identity-document image.
- Extracted name, birth date, address, document number, expiry, and issuer are stored as candidates with confidence.
- The reviewer compares image, extracted value, and current patient value field by field.
- Low-confidence or conflicting values require manual entry or rejection and cannot auto-accept.
- Confirmed candidates call the same guarded demographic-change APIs as manual updates.
- Provider errors record a retryable result and never expose document images in logs.

## Frappe realization

- **DocTypes:** `OC Identity Document Extraction` and child `OC Extracted Identity Field` with candidate, confidence, disposition, and target field.
- **Workflow:** Queued → Extracted → Human Review → Accepted, Partially Accepted, Rejected, or Failed.
- **Roles/permissions:** `OC Identity Reviewer` confirms; background integration role reads the minimum private file; other users see outcome only.
- **API/surfaces:** queued `open_chart.api.v1.registration.extract_identity_document` and `.apply_extracted_identity`; side-by-side review page and failure report.

## Boundaries

Owns: OCR candidates and human dispositions. Consumes: controlled ID image. Emits: confirmed change requests with extraction provenance. Does not own: patient update approval or document retention.

## Open questions

- What confidence floor should suppress a field rather than present a misleading candidate?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
