# Consented Mobile Ambient Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Runs a visible, consent-bound encounter capture session on a phone and produces source-linked draft artifacts for clinician review.
Topics: openchart-feature-catalog, mobile-devices, frappe, ambient-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-020 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Encounter-mode draft adapters** — Produce specialty-specific draft sections behind the same consent and review contract.

## Focus

This entry isolates mobile ambient-session control, participant consent, visible recording, draft generation, and deletion.

## Behavior

- A clinician starts capture only from an active encounter after confirming participants and current consent.
- The app shows an unmistakable recording indicator and offers pause, resume, participant change, and stop controls.
- A participant withdrawal stops capture and records the boundary without erasing prior evidence improperly.
- The system produces transcript and note suggestions labeled as drafts with source intervals and uncertainty.
- The clinician reviews, edits, rejects, or accepts each artifact; no diagnosis, order, or note is committed autonomously.
- Phone calls, lock events, low battery, backgrounding, and network loss create explicit interruption segments.
- Audio follows a disclosed retention policy and is never copied to the device media library.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Ambient Capture Session`, child `OC Capture Participant`, and `OC Ambient Draft` with encounter, consent, intervals, interruptions, provider, state, and reviewer actions.
- **Workflow and roles:** Prepared → Recording → Paused → Processing → Review → Accepted/Discarded/Failed; only encounter clinicians control capture and accept drafts.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.ambient.start`, `segment`, `stop`, and `review` enforce encounter and consent versions.
- **Realtime and jobs:** Websocket events report processing and interruption state; server-side RQ jobs transcribe, draft, delete retained audio, and never auto-submit clinical records.
- **Files and surfaces:** Segmented audio and drafts use private Frappe file attachment APIs with encryption, retention, and digest provenance; review occurs in permission-filtered mobile and Desk views.

## Boundaries

Owns: capture session, consent boundary, source segments, and draft review. Consumes: encounter, participants, consent, and AI/transcription adapters. Emits: clinician-reviewed draft content. Does not own: final diagnosis, orders, note signature, or covert recording.

## Open questions

- How should the app re-establish participant consent after an interruption or participant change?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
