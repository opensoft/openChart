# Consent Document Linkage — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Links stored consent artifacts to the signed consent events they evidence while preserving signer, scope, version, and revocation history.
Topics: openchart-feature-catalog, documents, frappe, consent-linkage
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-013 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Consent evidence completeness check** — Flag signed events missing a required document, witness, representative authority, or translated copy.

## Focus

This feature isolates the evidence relationship between an immutable consent document and a governed consent event.

## Behavior

- Staff attach a consent artifact only to a patient and an existing consent event or pending signature session.
- The linkage records form/template version, scope, signer role, signed time, witness, representative authority, and capture method.
- The displayed consent status comes from the consent event, not from filename or OCR text.
- A revoked or expired consent remains linked and viewable to authorized auditors but is clearly non-current.
- Corrected scans or countersigned copies become successor document versions without rewriting the signed event.
- A scope mismatch, wrong patient, missing signer authority, or invalid signature blocks completion.
- Downstream access checks consume the current consent event and can retrieve the exact evidence version used.

## Frappe realization

- **DocTypes:** `OC Consent Evidence Link` (patient, consent_event Dynamic Link, document_version, template_version, signer_role, scope, evidence_state) plus signer/witness child rows when required.
- **Workflow:** Pending Evidence → Verified → Current, with Deficient, Revoked Evidence, Expired, and Superseded states derived from linked authority.
- **Roles/permissions:** Consent Coordinator links and verifies; Clinician reads in context; Privacy Officer audits; signer identity fields use permlevel 1.
- **Hooks/API:** `validate` enforces patient and scope consistency; `open_chart.api.v1.documents.link_consent_evidence` is the guarded write surface and records provenance.
- **Surfaces:** Consent timeline card, deficiency Query Report, and consent evidence Print Format show status and artifact without conflating them.

## Boundaries

Owns: evidence linkage, form version, and verification state. Consumes: consent authority event, signed File version, and signer context. Emits: resolvable consent evidence reference. Does not own: consent policy, signature ceremony, or access decision itself.

## Open questions

- Which consent events require the original signed binary versus a verified scan?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Clinical Media Library](openchart-feature-catalog-dms-012-clinical-media-library.md)
