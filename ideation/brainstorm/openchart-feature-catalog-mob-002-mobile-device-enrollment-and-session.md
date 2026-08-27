# Mobile Device Enrollment And Session — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enrolls a mobile installation and issues revocable, device-bound sessions with explicit site and account scope.
Topics: openchart-feature-catalog, mobile-devices, frappe, device-enrollment
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-002 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Hardware attestation policy** — Require stronger platform evidence for selected roles or data scopes.

## Focus

This capability binds authentication to an enrolled app installation while keeping server authorization authoritative.

## Behavior

- A user authenticates through an approved identity flow before requesting device enrollment.
- Enrollment records platform, app build, public-key evidence, site, user, and device label without collecting advertising identifiers.
- Successful enrollment returns a short-lived access token and refresh credential protected by the device key store.
- Token refresh rechecks account status, device state, role scope, minimum version, and remote-wipe status.
- Users and security staff can list and revoke their enrolled installations.
- Clock skew, replay, key replacement, or tenant mismatch denies renewal and preserves a reason-coded audit event.
- Revocation invalidates server sessions immediately and signals the app to clear local protected state.

## Frappe realization

- **DocTypes:** Create `OC Mobile Device Enrollment` and `OC Mobile Session` with installation UUID hash, public-key thumbprint, site, user, platform, state, issued/expiry times, and revocation reason.
- **Workflow and roles:** Use Pending → Active → Suspended → Revoked with `OC Mobile User` owner reads and `OC Security Administrator` review at permlevel 1.
- **API and auth:** Implement `open_chart.api.v1.mobile.enroll`, `refresh`, `list_devices`, and `revoke` using TLS REST token/OAuth2 exchange and signed proof-of-possession; block auto-REST writes.
- **Realtime and jobs:** Emit websocket revocation and posture events containing only enrollment IDs; run server-side RQ jobs to expire sessions and reconcile stale refresh grants.
- **Files and surfaces:** Use private Frappe file attachment APIs only for optional attestation evidence with retention limits; provide user device management and an administrator Query Report.

## Boundaries

Owns: enrollment and mobile session lifecycle. Consumes: identity-provider result, app posture, and authorization policy. Emits: scoped session decisions and revocation events. Does not own: passwords, biometric templates, hardware keys, or clinical permissions.

## Open questions

- Which enrollment actions require step-up authentication for shared versus personally assigned devices?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
