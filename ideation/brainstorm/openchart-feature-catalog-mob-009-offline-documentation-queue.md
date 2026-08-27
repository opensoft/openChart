# Offline Documentation Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures permitted clinical documentation offline as encrypted, ordered intents that remain visibly pending until server acceptance.
Topics: openchart-feature-catalog, mobile-devices, frappe, offline-documentation
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-009 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Template-specific offline validation** — Package approved field and terminology rules with each documentation schema.

## Focus

This capability isolates durable offline authorship and never represents a local draft as an accepted chart record.

## Behavior

- A user starts only an offline-enabled form from a server-issued schema and authorized patient context.
- Each saved intent records author, device, patient, encounter, schema version, base record version, local sequence, and client timestamp.
- Drafts and queued submissions are encrypted separately from the read cache and survive app restart.
- The UI labels Draft, Queued, Uploading, Accepted, Needs Review, Rejected, and Cancelled states distinctly.
- Users may edit or cancel an intent before upload while preserving local revision history.
- Sign-out or remote wipe does not silently discard pending work; policy determines escrow, blocked access, and supervisor recovery.
- Server rejection preserves the authored payload locally with a reason and safe correction path.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Documentation Intent` with idempotency key, source version, schema version, payload digest, state, receipt, and encrypted attachment references.
- **Workflow and roles:** Use Draft → Queued → Uploading → Accepted/Needs Review/Rejected/Cancelled; only the author or authorized supervisor may recover pending intents.
- **API and auth:** Submit over TLS token-authenticated `open_chart.api.v1.mobile.documentation.submit`; server validation invokes supported guarded write APIs and never direct DocType inserts.
- **Realtime and jobs:** Websocket receipts update queue state; server-side RQ jobs validate large payloads, scan attachments, and retry post-acceptance projections without changing author intent.
- **Files and surfaces:** Upload media through Frappe private file attachment APIs using staged, digest-checked files linked only after acceptance; Desk reconciliation reports expose no payload by default.

## Boundaries

Owns: offline intent durability, ordering, and receipts. Consumes: approved schemas, patient context, and guarded write APIs. Emits: attributable submission intents. Does not own: final clinical acceptance, merge policy, or source-record amendments.

## Open questions

- How should pending documentation be recovered when a clinician loses the device before synchronization?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
