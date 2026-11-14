# Consent-Gated Ambient Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures encounter audio only after explicit consent and keeps recording state visible and revocable to participants.
Topics: openchart-feature-catalog, clinical-ai, frappe, ambient-consent
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-003 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Participant consent receipt** — Provide a portal-visible record of what was captured, why, and under which retention policy.

## Focus

This feature isolates the client and server gate that must precede ambient conversation recording in an encounter.

## Behavior

- A clinician selects an encounter and requests capture; the client displays purpose, participants, retention, and recording status.
- Capture cannot start until the required consent method and consenting party authority are recorded.
- A visible control lets authorized participants pause, resume, or stop capture immediately.
- Revocation stops new audio transmission and marks already captured segments for policy-directed handling.
- Connection loss shows a prominent interrupted state and never implies that capture continued.
- Encounters with missing authority, prohibited jurisdiction, or disabled site policy cannot record.

## Frappe realization

- **DocTypes:** `OC Ambient Capture Session` links encounter, consent evidence, policy, participants, timestamps, segment files, and interruption reasons.
- **Workflow:** Requested → Consented → Recording/Paused → Stopped → Processing → Closed; Revoked is terminal for capture.
- **Roles/permissions:** clinicians initiate; `OC Consent Reviewer` resolves authority exceptions; audio fields use permlevel 2.
- **Hooks/client/API:** Desk client script maintains recording indicator; whitelisted start/pause/stop methods recheck consent server-side; `on_update` writes audit events.

## Boundaries

Owns: capture state and consent gating. Consumes: encounter, participant authority, site policy, and jurisdiction. Emits: consent-bound audio segments and capture audit events. Does not own: transcription, note acceptance, or consent policy authorship.

## Open questions

- How should multi-party consent be represented when participants join after recording starts?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Ambient Note Review Queue](openchart-feature-catalog-aic-004-ambient-note-review-queue.md)
