# Mobile Voice Dictation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Adds permission-aware voice dictation to approved mobile text fields with transparent transcription, user review, and audio-retention controls.
Topics: openchart-feature-catalog, mobile-devices, frappe, voice-dictation
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-019 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Specialty vocabulary packs** — Apply governed terminology hints without auto-accepting clinical text.

## Focus

This capability isolates deliberate push-to-dictate input and preserves the author as reviewer of resulting text.

## Behavior

- A microphone control appears only on approved fields and displays recording state, duration, language, and destination.
- Recording begins and ends by explicit user action; background or hidden capture is prohibited.
- The user receives a draft transcript and must edit or accept it before it enters the field.
- Uncertain terms are highlighted without silently replacing clinical wording.
- Network, permission, provider, and audio-quality failures preserve the original field content.
- Audio retention defaults to immediate deletion after transcription unless explicit policy and consent require otherwise.
- Accepted text records dictation provenance but remains ordinary authored documentation subject to signature rules.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Dictation Session` with author, document/field context, language, provider, timing, state, transcript digest, retention, and acceptance evidence.
- **Roles and permissions:** Clinical roles dictate only into fields they may edit; `OC Dictation Administrator` manages provider and retention policy without chart access.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.dictation.start`, `upload`, and `accept` use scoped session IDs and guarded field validation.
- **Realtime and jobs:** Websocket events return transcription state; server-side RQ jobs invoke adapters, scrub logs, expire audio, and route provider failures.
- **Files and surfaces:** Audio uses encrypted private Frappe file attachment APIs with short retention; transcripts are not attached until user acceptance, and Desk reports expose operational metadata only.

## Boundaries

Owns: dictation session, transcript draft, and acceptance evidence. Consumes: microphone input, field context, language, and transcription adapter. Emits: user-approved text. Does not own: note signature, clinical correctness, or ambient capture.

## Open questions

- May any audio be retained for correction, and what consent and duration would justify it?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
