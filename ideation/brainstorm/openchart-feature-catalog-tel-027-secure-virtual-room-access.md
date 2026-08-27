# Secure Virtual Room Access — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Prevents waiting-room bypass and link reuse through unique, scoped, short-lived virtual-session credentials.
Topics: openchart-feature-catalog, telehealth, frappe, session-security
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-027 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Session threat dashboard** — Surface repeated invalid, replayed, or cross-room access attempts to security reviewers.

## Focus

This feature isolates access-token lifecycle and server-enforced room entry controls for virtual care.

## Behavior

- Every participant receives a credential bound to one visit, role, participant identity, entry stage, and short expiry.
- Credentials are single-use or safely rotated and never grant direct media-room admission before waiting-room authorization.
- The server rejects replay, wrong-room, wrong-role, expired, revoked, and appointment-state-mismatched attempts.
- Sharing a portal URL alone does not transfer authority because issuance and use revalidate the authenticated or invited subject.
- Staff can revoke one participant, all outstanding grants, or the room without exposing token values.
- Security failures record redacted reason, correlation ID, actor context, and response without logging secrets or clinical content.

## Frappe realization

- **DocTypes:** `OC Session Grant` stores hashed token ID, participant, room, scope, issue, expiry, use, rotation, and revocation metadata; secrets live in an appropriate secret store.
- **API/security:** guarded issue, exchange, rotate, and revoke methods use constant-time verification, rate limits, CSRF controls, secure cookies where applicable, and CSP.
- **Roles/reports:** Security Reviewer sees normalized attempt events; Telehealth Staff can revoke within assigned rooms; no role can retrieve issued plaintext credentials.

## Boundaries

Owns: virtual-room credential and admission-stage enforcement. Consumes: verified participant and visit state. Emits: scoped media credential or denied attempt. Does not own: portal authentication or media encryption implementation.

## Open questions

- What proof must partner platforms expose to demonstrate that their room links cannot bypass openChart admission policy?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
