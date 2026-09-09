# Clinical Media Library — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Organizes permissioned patient photos, video, and audio with safe previews, player embeds, captions, and encounter provenance.
Topics: openchart-feature-catalog, documents, frappe, clinical-media
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-012 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Longitudinal media comparison** — Place consent-compatible images or clips side by side by body site, encounter, and capture date.

## Focus

This feature isolates clinical media storage and playback while preserving class-specific access and consent boundaries.

## Behavior

- An authorized clinician uploads or captures media against a patient, encounter, purpose, and optional body site.
- The system validates format, size, malware result, capture timestamp, source device, and required consent reference.
- Originals remain private and immutable; derived thumbnails, waveforms, and streaming renditions are separately checksummed.
- Viewers use an embedded player that prevents public URLs and rechecks access at playback time.
- Captions, annotations, and descriptions are versioned metadata and never alter the original media.
- Unsupported codecs or failed derivatives leave the original quarantined with actionable diagnostics.
- Download, playback, and export events are audited for sensitive classes.

## Frappe realization

- **DocTypes:** `OC Clinical Media` (patient, encounter, media_kind, purpose, consent_event, original_file, state) and child `OC Media Rendition` (File, codec, dimensions, checksum, derivative_of).
- **Files/hooks/jobs:** Private Frappe file manager attachments pass `open_chart.documents.on_file`; RQ jobs create thumbnails, captions, and streaming renditions without replacing originals.
- **Roles/permissions:** Clinician contributes; Media Reviewer accepts; Behavioral Health and Sensitive Media roles use permlevel 2 and patient user permissions.
- **API/surfaces:** Time-limited whitelisted streaming method rechecks ACL; patient timeline embeds image/audio/video players and rendition status.
- **Workflow:** Uploaded → Processing → Review → Available, with Quarantined and Superseded states.

## Boundaries

Owns: media metadata, renditions, playback authorization, and capture provenance. Consumes: patient context, File, and consent event. Emits: permissioned media reference. Does not own: diagnostic imaging archives, consent policy definition, or public media hosting.

## Open questions

- Which clinical media classes require explicit consent at capture versus access-time policy alone?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Consent Document Linkage](openchart-feature-catalog-dms-013-consent-document-linkage.md)
