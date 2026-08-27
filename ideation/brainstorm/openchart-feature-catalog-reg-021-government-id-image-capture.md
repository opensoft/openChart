# Government ID Image Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Securely captures government identity document images with purpose, consent, retention, and least-privilege access controls.
Topics: openchart-feature-catalog, registration, frappe, government-id-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-021 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Automatic redaction profiles** — Mask document fields not required for the stated verification purpose.

## Focus

Govern acquisition and custody of identity-document images independently from extracted data or verification decisions.

## Behavior

- Staff select document type and state the permitted capture purpose before using camera or upload.
- The patient may consent, decline, or request manual verification when policy allows.
- Front and back images receive quality checks for blur, glare, cropping, and unexpected file type.
- Images are private attachments and never become the patient's general profile image.
- Retention date and legal basis are recorded at capture and reviewed before deletion or extension.
- Failed uploads leave no active evidence record and provide a safe retry path.

## Frappe realization

- **DocTypes:** `OC Identity Document` with type, issuer, masked_number, private attachments, purpose, consent, retention_until, and quality status.
- **Workflow:** Draft → Captured → Quality Accepted → Retained or Rejected → Disposed.
- **Roles/permissions:** `OC Registration Clerk` captures; `OC Identity Reviewer` reads images at permlevel 2; routine chart roles see metadata only.
- **API/surfaces:** `open_chart.api.v1.registration.capture_identity_document`; secure capture page, evidence vault list, and retention report.

## Boundaries

Owns: government-ID image custody and metadata. Consumes: consent and captured files. Emits: controlled evidence reference. Does not own: OCR extraction or identity assurance decision.

## Open questions

- Which document types should be image-free after verification is complete?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
