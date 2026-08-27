# Sync Status And Retry Transparency — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows clinicians what is synchronized, pending, blocked, or failed and gives safe control over retry without obscuring server acceptance.
Topics: openchart-feature-catalog, mobile-devices, frappe, sync-transparency
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-011 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Support-safe sync bundle** — Export redacted queue metadata and correlation IDs for troubleshooting.

## Focus

This feature isolates user-visible synchronization truth and recovery controls.

## Behavior

- A persistent indicator distinguishes Online, Offline, Syncing, Pending, Needs Review, and Service Unavailable.
- A detail view lists each queued item by safe label, age, state, retry eligibility, and last server receipt.
- Manual retry respects ordering, backoff, connectivity, battery, and idempotency instead of duplicating submissions.
- Authentication, permission, validation, conflict, attachment, and transient-service failures have distinct guidance.
- Accepted means the server returned an authoritative receipt, not merely that bytes left the device.
- Users cannot dismiss unresolved clinical work as synchronized.
- Support identifiers reveal no clinical payload and remain useful across mobile and server logs.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Sync Receipt` with intent key, state, attempt count, response code, correlation ID, accepted source link, and timestamps.
- **Roles and permissions:** Authors read receipts for their own device; `OC Mobile Support` sees redacted metadata, while clinical payload access follows source permissions.
- **API and auth:** Provide token-authenticated `open_chart.api.v1.mobile.sync_status` and `retry`; server receipts are immutable and auto-REST writes are blocked.
- **Realtime and jobs:** Deliver state changes via websocket and process retries, backoff, and dead-letter escalation in server-side RQ jobs.
- **Files and surfaces:** Frappe private file attachment APIs expose attachment upload state and digest only; mobile details and a Desk Script Report share correlation IDs.

## Boundaries

Owns: sync state presentation, receipts, and retry requests. Consumes: queue, network, auth, and server outcomes. Emits: clear status and controlled retry. Does not own: conflict resolution or source-record acceptance.

## Open questions

- When should a prolonged pending item escalate to a supervisor rather than rely on the author?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
