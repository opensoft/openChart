# Mobile Document Scanning — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts camera captures into a cropped, quality-checked, multi-page chart document without retaining source images on the device.
Topics: openchart-feature-catalog, mobile-devices, frappe, document-scanning
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-017 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Assisted document classification** — Suggest a document type while requiring human confirmation before filing.

## Focus

This capability isolates secure page acquisition, edge detection, assembly, and chart filing.

## Behavior

- A user starts scanning from a patient or intake context and selects an approved document type.
- On-device edge detection proposes crop, rotation, glare, blur, and missing-page warnings.
- Users can reorder, retake, or remove pages before finalizing a PDF or image set.
- The app shows patient, document type, page count, and purpose before upload confirmation.
- Source frames stay inside encrypted transient storage and never enter the consumer gallery.
- Offline scans remain pending and cannot appear as filed until server validation succeeds.
- Wrong-patient filing is corrected by a governed supersession or reassignment process, not silent history deletion.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Document Scan` with patient, encounter, type, page count, capture provenance, quality flags, state, digest, and filed document link.
- **Workflow and roles:** Draft → Pending Upload → Quality Review → Filed/Returned/Cancelled; registration and clinical roles receive type-specific permissions.
- **API and auth:** Use TLS token-authenticated `open_chart.api.v1.mobile.document_scan.init` and `file`; guarded methods validate patient and document authority.
- **Realtime and jobs:** Websocket events return conversion and review status; server-side RQ jobs run malware scanning, PDF assembly, OCR adapters, and thumbnail generation.
- **Files and surfaces:** Pages and final documents use private Frappe file attachment APIs with versioning and digest checks; mobile preview and Desk review queue are permission-filtered.

## Boundaries

Owns: mobile scan session, page assembly, and filing request. Consumes: chart context, document taxonomy, and retention policy. Emits: private document attachment and provenance. Does not own: document interpretation or source authenticity.

## Open questions

- Which document classes require a second-person filing review before chart visibility?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
