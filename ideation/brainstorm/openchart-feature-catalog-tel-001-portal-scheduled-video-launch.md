# Portal Scheduled Video Launch — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets an authorized patient launch a scheduled virtual visit from the portal at the permitted arrival time.
Topics: openchart-feature-catalog, telehealth, frappe, portal-video-launch
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-001 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Calendar deep link** — Open the governed portal arrival page from a privacy-minimized calendar reminder.

## Focus

This feature isolates the patient-facing transition from a confirmed appointment into its authorized virtual-care arrival flow.

## Behavior

- The portal shows Join only to the patient or validated proxy attached to a confirmed virtual appointment.
- Join remains disabled before the configured early-arrival window and explains when access opens.
- Selecting Join revalidates appointment state, participant authority, consent prerequisites, and room readiness server-side.
- A valid request creates a short-lived participant grant and routes the user to device checks or the waiting room.
- Cancelled, completed, expired, or modality-changed appointments never mint a room grant and show safe next steps.
- Repeated selections reuse or rotate the active grant without creating duplicate attendance events.

## Frappe realization

- **DocTypes:** `OC Virtual Visit` links the appointment, patient, room, modality, join window, and current arrival state; `OC Session Grant` stores only hashed token identity, participant role, issue time, and expiry.
- **API/hooks:** `open_chart.api.v1.telehealth.issue_join_grant` performs guarded authorization and records an append-only `OC Telehealth Event`; appointment updates revoke incompatible grants.
- **Surfaces/permissions:** a `www/telehealth/join` portal page is available to Patient and authorized Proxy roles, while Telehealth Staff can inspect grant status but never reveal token material.

## Boundaries

Owns: authorized portal launch and grant issuance. Consumes: appointment, identity, proxy, consent, and room state. Emits: an arrival event and short-lived grant. Does not own: media transport or scheduling.

## Open questions

- Should the first release use a custom WebRTC join client or a partner embed behind the same grant contract?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
