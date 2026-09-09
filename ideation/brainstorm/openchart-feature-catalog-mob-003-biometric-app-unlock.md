# Biometric App Unlock — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Uses device biometrics to release a locally protected app session while preserving server-side authentication, revocation, and reauthentication policy.
Topics: openchart-feature-catalog, mobile-devices, frappe, biometric-unlock
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-003 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Risk-based reauthentication** — Require server step-up for sensitive actions despite a successful local unlock.

## Focus

This entry isolates convenience unlock and explicitly avoids treating a local biometric match as server identity proof.

## Behavior

- An enrolled user may opt in only when the operating system reports secure biometric and passcode protection.
- The app stores no biometric template and asks the OS to release an app-specific encryption key.
- Successful unlock restores only the locally permitted session and displays its user, site, and freshness.
- Repeated failures, biometric-set changes, device restart, or policy expiry require full online reauthentication.
- Offline unlock obeys a server-issued maximum age and cannot extend that age locally.
- Shared-device policy may disable biometrics or require explicit user selection before every unlock.
- All failures return a neutral message that does not disclose patient or account details.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Add biometric policy and last-full-auth fields to `OC Mobile Device Enrollment`; create `OC Mobile Authentication Event` with outcome, reason code, policy version, and no biometric data.
- **Roles and permissions:** `OC Security Administrator` manages policy; users may enable only within their own active enrollment and cannot alter server freshness limits.
- **API and auth:** Provide token-authenticated `open_chart.api.v1.mobile.biometric_policy` and `record_unlock_outcome`; auto-REST is read-only for applicable policy records.
- **Realtime and jobs:** Send policy invalidation by websocket and use server-side RQ jobs to expire stale unlock grants and aggregate non-PHI failure telemetry.
- **Files and surfaces:** Frappe file attachment APIs store no biometric material; support exports are private, scrubbed attachments available only to security roles.

## Boundaries

Owns: unlock policy and audit outcome. Consumes: OS biometric result and server session freshness. Emits: local key release decision and minimum audit evidence. Does not own: biometric capture, matching, templates, or account authentication.

## Open questions

- What is the maximum offline-unlock interval for each mobile role and sensitivity tier?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
