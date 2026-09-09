# Direct-To-Chart Clinical Photo Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures wound or lesion images directly into an authorized chart record without retaining them in the device photo library.
Topics: openchart-feature-catalog, mobile-devices, frappe, clinical-photo-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-016 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Repeat-view positioning guide** — Help users reproduce distance and orientation without interpreting image content.

## Focus

This entry isolates consent-aware acquisition, protected transfer, provenance, and local non-retention of clinical photography.

## Behavior

- Capture begins from an authorized patient, encounter, body-site, and documentation context.
- The app displays purpose and consent requirements before opening an in-app camera that bypasses the photo library.
- The user reviews, retakes, annotates, or discards the image before upload.
- Metadata records author, patient, encounter, body site, orientation, capture time, consent evidence, and device clock status.
- Images are encrypted in transient app storage and deleted after verified server receipt or explicit discard.
- Offline captures remain encrypted, visibly pending, excluded from backups, and subject to expiry and recovery policy.
- Upload or malware-scan failure never creates a broken chart reference or leaves an untracked gallery copy.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Clinical Image Capture` with patient, encounter, body site, consent link, provenance, state, file digest, and successor links.
- **Workflow and roles:** Draft → Pending Upload → Scanning → Accepted/Rejected/Cancelled; clinical roles capture within patient permissions and privacy roles audit consent exceptions.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.clinical_image.init` and `complete` issue staged upload grants and guarded chart linkage.
- **Realtime and jobs:** Websocket receipts confirm scan and linkage state; server-side RQ jobs perform malware checks, metadata stripping, derivatives, and retention actions.
- **Files and surfaces:** Use Frappe private file attachment APIs only, disable public paths, preserve original digest, and provide permission-filtered chart and Desk views.

## Boundaries

Owns: capture session, transfer, provenance, and chart linkage. Consumes: patient context, consent, body site, and retention policy. Emits: private clinical image reference. Does not own: diagnosis, image interpretation, or device gallery behavior outside the app sandbox.

## Open questions

- Which metadata should be stripped for privacy and which must remain for clinical provenance?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
