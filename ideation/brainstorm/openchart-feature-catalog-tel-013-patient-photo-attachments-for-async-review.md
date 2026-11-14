# Patient Photo Attachments For Async Review — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients securely attach clinically relevant photos to an asynchronous virtual-care request for clinician review.
Topics: openchart-feature-catalog, telehealth, frappe, async-photo-upload
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-013 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Guided image retake** — Prompt for reviewed framing, scale, and lighting requirements when an image is insufficient.

## Focus

This feature isolates patient-originated image capture, safe attachment, and review disposition for asynchronous care.

## Behavior

- The portal explains acceptable content, privacy risks, file limits, and capture guidance before upload.
- The patient can preview, replace, caption, and explicitly submit each image to the active e-visit or review request.
- The server validates allowed formats, size, malware status, and image decodability before clinical availability.
- Submission records uploader, capture declaration, timestamp, checksum, and linked request without trusting device metadata as fact.
- A clinician marks each image usable, insufficient, duplicate, or inappropriate and may request a replacement.
- Rejected or deleted attachments retain minimum audit evidence under policy without remaining visible as clinical content.

## Frappe realization

- **DocTypes:** `OC Async Clinical Attachment` links a private Frappe File to patient, request, caption, checksum, provenance, scan state, and review disposition.
- **API/jobs:** chunked portal upload finalizes through a guarded method; background scanning and thumbnail jobs quarantine files until accepted.
- **Permissions/surfaces:** Patient accesses own pending files, assigned Clinician accesses released files, and an attachment review panel prevents public File URLs.

## Boundaries

Owns: secure patient image submission and review state. Consumes: authorized async request and file-scanning service. Emits: provenance-bound clinical attachment. Does not own: image diagnosis or general document storage policy.

## Open questions

- What retention and deletion rules apply to quarantined, rejected, and clinically accepted patient images?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
