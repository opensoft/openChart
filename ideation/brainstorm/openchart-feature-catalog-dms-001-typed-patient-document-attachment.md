# Typed Patient Document Attachment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized staff attach a file to a patient or encounter under a required document class with provenance and review state.
Topics: openchart-feature-catalog, documents, frappe, typed-attachment
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-001 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Class-specific intake cards** — Tailor required metadata and preview controls to each governed document class.

## Focus

This feature isolates safe, typed attachment of one patient document rather than generic file upload.

## Behavior

- A Medical Records Clerk or Clinician selects a patient, optional encounter, document class, service date, source, and file.
- The system validates allowed media type, size, malware-scan result, and class-specific required fields before acceptance.
- A newly uploaded item remains Draft until the uploader confirms the preview and patient context.
- Submitting creates an immutable accepted document version and records uploader, time, source, and checksum.
- A patient mismatch or unreadable file blocks submission and routes the item to correction without chart visibility.
- View and download permissions follow patient access plus document-class restrictions.
- Replacing accepted content creates a successor version; it never overwrites the accepted attachment.

## Frappe realization

- **DocTypes:** `OC Patient Document` (naming series `OCDOC-.YYYY.-.#####`, patient, encounter, document_class, service_date, source, current_version) and child `OC Document File Version` (File Link, checksum, media_type, supersedes, accepted_by).
- **Files/hooks:** Use the private Frappe file manager `File`/attachment pattern; `hooks.py` routes File `after_insert` and `on_update` to `open_chart.documents.on_file` for validation, checksum capture, and quarantine release.
- **Workflow:** Draft → Previewed → Accepted, with Correction Required and Superseded states.
- **Roles/permissions:** Medical Records Clerk creates; Clinician may quick-attach; Health Information Manager accepts restricted classes; permlevel 1 protects source and review fields.
- **API/surfaces:** Guarded `open_chart.api.v1.documents.attach` plus auto-REST read; patient timeline card, document preview dialog, and Desk list filters expose accepted records.

## Boundaries

Owns: typed attachment identity, metadata, acceptance state, and version pointer. Consumes: patient and encounter identity, class policy, and private File. Emits: accepted patient-document event. Does not own: OCR interpretation, retention policy, or disclosure authorization.

## Open questions

- Which document classes require second-person review before chart visibility?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Clinician Quick-attach From Encounter](openchart-feature-catalog-dms-032-clinician-quick-attach-from-encounter.md)
