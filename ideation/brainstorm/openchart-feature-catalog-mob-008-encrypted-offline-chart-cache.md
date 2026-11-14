# Encrypted Offline Chart Cache — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Stores a bounded, encrypted, expiring subset of authorized chart data for continuity during network loss.
Topics: openchart-feature-catalog, mobile-devices, frappe, offline-cache
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-008 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Context-aware cache packs** — Prestage minimum-necessary data for an assigned round or field-visit schedule.

## Focus

This feature isolates local read continuity, including its scope, encryption, expiry, and revocation behavior.

## Behavior

- The server issues a cache manifest limited to current assignments, role, facility, purpose, and configured data classes.
- The app encrypts records with an installation key protected by the OS secure store and never writes plaintext exports or thumbnails.
- Every cached item carries source identity, version, scope, fetched time, and expiry.
- Offline views show a persistent offline banner and per-record as-of time.
- Expired, revoked, discharged, or permission-lost records become unreadable and are securely purged at reconciliation.
- Cache capacity pressure evicts least-needed eligible data without removing unsynced authored work.
- Backup, device migration, screen indexing, and consumer cloud synchronization are disabled for protected cache files.

## Frappe realization

- **DocTypes:** Create `OC Mobile Cache Policy` and `OC Mobile Cache Manifest` with subject scope, allowed classes, source versions, expiry, byte budget, and revocation generation.
- **Roles and permissions:** `OC Privacy Officer` and `OC Mobile Administrator` govern policies; manifests are generated from source DocPerms and user permissions.
- **API and auth:** Serve signed manifests and bounded reads through TLS REST token/OAuth2 methods under `open_chart.api.v1.mobile.cache`; deny generic bulk auto-REST access.
- **Realtime and jobs:** Send revocation-generation changes via websocket; server-side RQ jobs assemble manifests, detect stale grants, and record purge acknowledgements.
- **Files and surfaces:** Private clinical attachments use short-lived Frappe file attachment API grants and explicit offline eligibility; policy and purge status appear in Desk reports.

## Boundaries

Owns: offline cache authorization envelopes and lifecycle. Consumes: permissions, assignments, source versions, and device posture. Emits: bounded snapshots and purge directives. Does not own: OS encryption, source records, or unsynced authored changes.

## Open questions

- What evidence is sufficient to show that a revoked device eventually honored purge instructions?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
