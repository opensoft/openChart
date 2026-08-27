# Chart-Launched Masked Calling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Initiates an outbound call from chart context through a proxy number so personal clinician numbers remain undisclosed.
Topics: openchart-feature-catalog, mobile-devices, frappe, masked-calling
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-022 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Interpreter bridge launch** — Add an approved interpreter leg without exposing personal numbers.

## Focus

This entry isolates call setup, number masking, purpose, and disposition evidence without recording clinical audio by default.

## Behavior

- An authorized user selects a current patient contact and call purpose from chart context.
- The server confirms contact permissions, consent or preference, facility identity, quiet-hours policy, and caller role.
- A telecom adapter bridges clinician and patient through expiring proxy numbers.
- The app shows the called contact label and organizational callback identity before launch.
- Connected, no answer, busy, failed, cancelled, and voicemail outcomes are recorded separately.
- Call content is not recorded; duration and routing metadata are minimized and access-controlled.
- Emergency and prohibited contact flags block ordinary launch and provide the approved alternative.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Masked Call Session` with patient, contact reference, purpose, requester, proxy allocation, provider ID, state, times, and disposition.
- **Roles and permissions:** Clinical and outreach roles call only contacts visible through patient user permissions; `OC Communications Administrator` manages adapter policy without chart content.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.call.prepare` and `launch` create short-lived grants; provider callbacks use signed whitelisted endpoints.
- **Realtime and jobs:** Websocket events update call state; server-side RQ jobs expire proxy allocations, reconcile callbacks, and purge excess telecom metadata.
- **Files and surfaces:** No recording attachment is created by default; authorized call artifacts, if policy permits, use private Frappe file attachment APIs and restricted retention.

## Boundaries

Owns: call authorization, proxy session, and disposition. Consumes: patient contact, consent, role, and telecom adapter. Emits: minimized call event evidence. Does not own: carrier networks, conversation content, or emergency calling.

## Open questions

- Which contact preferences and jurisdiction rules must be evaluated before each call launch?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
