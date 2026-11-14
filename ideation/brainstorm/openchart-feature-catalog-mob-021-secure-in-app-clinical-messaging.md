# Secure In-App Clinical Messaging — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides patient-contextual, role-aware clinical messaging with delivery evidence, attachment controls, and explicit escalation boundaries.
Topics: openchart-feature-catalog, mobile-devices, frappe, secure-messaging
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-021 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Structured handoff message** — Combine message threads with accountable transfer and receipt fields.

## Focus

This feature isolates protected mobile conversations among authorized care participants.

## Behavior

- Users start direct or team threads from an authorized patient, encounter, or operational context.
- Membership is server-derived from roles, care team, facility, and explicit thread invitations.
- Sent, delivered, opened, acknowledged, expired, and failed are distinct message states.
- Edits and withdrawals preserve prior versions and reasons rather than silently rewriting history.
- Offline messages remain encrypted and visibly queued until a server receipt arrives.
- Push previews contain no PHI; opening reauthenticates and rechecks thread membership.
- Messaging is not an emergency channel and displays configured escalation guidance.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Secure Message Thread`, `OC Thread Participant`, and `OC Secure Message` with context Dynamic Link, sender, sequence, state, acknowledgement, expiry, and successor.
- **Roles and permissions:** Clinical and operational roles access threads through context user permissions and participant membership; compliance export is separately restricted.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.messages` methods create and acknowledge messages; block generic auto-REST writes and enumerate safe actions server-side.
- **Realtime and jobs:** Deliver minimum-necessary message IDs through websocket events; server-side RQ jobs handle push fallback, expiry, attachment scanning, and escalation reminders.
- **Files and surfaces:** Attachments use private Frappe file attachment APIs with thread permission checks and malware scanning; mobile threads pair with a Desk inbox.

## Boundaries

Owns: thread membership, messages, delivery evidence, and acknowledgements. Consumes: identity, care-team scope, and notification routing. Emits: secure conversation events. Does not own: emergency dispatch, clinical orders, or telecom delivery guarantees.

## Open questions

- When should patient-context threads close or revalidate membership after care-team changes?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
