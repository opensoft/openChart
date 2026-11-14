# Outside DICOM Upload — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Ingests patient-supplied or referring-facility DICOM media into a quarantined import workflow with manifest, malware, format, and completeness checks.
Topics: openchart-feature-catalog, imaging, frappe, outside-imaging-upload
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-018 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Import receipt** — Give staff and patients a traceable receipt for accepted media and unresolved issues.

## Focus

This feature isolates safe intake of outside imaging packages before patient matching or PACS acceptance.

## Behavior

- Authorized staff upload a DICOM archive or initiate a managed media-ingestion session.
- Files remain quarantined while malware, archive, DICOM conformance, size, and duplicate checks run.
- The system creates a manifest of studies, series, instances, source labels, and detected patient demographics.
- Non-DICOM files and embedded reports are classified separately and never treated as images silently.
- Partial, encrypted, corrupt, or oversized packages enter an exception queue with preserved evidence.
- Release to the external archive requires completed patient matching and an explicit authorized action.

## Frappe realization

- **DocTypes:** `OC Outside Imaging Import` with manifest child rows, quarantine location reference, checks, source, uploader, and disposition.
- **Workflow:** Received → Scanning → Manifest Ready → Matching → Approved for Archive → Transferred, with Rejected and Exception states.
- **Roles/permissions:** imaging import staff create; identity reviewers match; PACS integration users transfer; raw packages are not broadly downloadable.
- **API/jobs/surfaces:** chunked upload method and RQ scanning jobs; realtime progress; Script Report lists aging quarantine items.

## Boundaries

Owns: import intake, quarantine, manifest, validation, and transfer authorization. Consumes: uploaded media and archive endpoint. Emits: vetted package and import evidence. Does not own: long-term image storage or patient matching decision.

## Open questions

- Where should quarantined binaries live when Frappe File storage is unsuitable for large DICOM packages?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
