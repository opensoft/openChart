# Audio-Only Visit Fallback — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts an eligible virtual encounter to audio-only care while preserving consent, reason, participants, and modality history.
Topics: openchart-feature-catalog, telehealth, frappe, audio-only-fallback
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-017 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Dial-out bridge** — Let authorized staff connect a patient through a masked, policy-governed telephone bridge.

## Focus

This feature isolates a clinically and operationally governed modality change from video to audio-only.

## Behavior

- A clinician or authorized staff member selects audio-only fallback and records the reason before conversion.
- The system checks service, jurisdiction, consent, and organizational eligibility for audio-only care.
- The patient is told what changes and confirms willingness to continue through the available channel.
- The encounter timeline preserves attempted video, conversion time, audio channel, and participant intervals.
- Ineligible conversion routes to reschedule, in-person, or other human-selected disposition rather than continuing silently.
- Completion prompts for modality-specific documentation fields and exposes coding hints as advisory only.

## Frappe realization

- **DocTypes/workflow:** `OC Visit Modality Transition` links the virtual visit, from/to modality, reason, eligibility policy, patient agreement, actor, and timestamp.
- **API/hooks:** guarded `convert_modality` validates effective policy and appends the transition; encounter completion checks required audio-only documentation.
- **Roles/surfaces:** Clinician and Telehealth Staff can initiate within permlevel limits; a console modal and encounter banner show current and historical modality.

## Boundaries

Owns: approved modality transition and documentation prompts. Consumes: eligibility, consent, and technical state. Emits: modality history and advisory coding context. Does not own: telephone carrier or claims.

## Open questions

- Which service and jurisdiction policies permit audio-only continuation after failed video?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
