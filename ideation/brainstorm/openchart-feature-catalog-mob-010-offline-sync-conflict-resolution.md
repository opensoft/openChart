# Offline Sync Conflict Resolution — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects concurrent chart changes and routes offline documentation conflicts through field-aware, human-reviewed resolution instead of silent overwrite.
Topics: openchart-feature-catalog, mobile-devices, frappe, sync-conflicts
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-010 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Conflict simulation fixtures** — Test deterministic outcomes against synthetic concurrent-edit scenarios.

## Focus

This entry isolates conflict detection, comparison, and authoritative resolution after offline work returns.

## Behavior

- The server compares the intent's base version with the current authoritative record and schema.
- Nonoverlapping additions may be accepted only under an explicit field policy; destructive or semantically ambiguous changes require review.
- Reviewers see base, current, and authored values with actor, source, and time provenance.
- Choices include accept as new, preserve current, create succession amendment, return to author, or reject with rationale.
- The mobile author receives a reason-coded result and can inspect the safe comparison when permitted.
- No generic last-write-wins behavior is allowed for accepted clinical records.
- Repeated uploads with the same idempotency key return the original conflict or resolution receipt.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Sync Conflict` and child `OC Conflict Field` with intent link, source version, current version, value digests, resolution, reviewer, and rationale.
- **Workflow and roles:** Pending Review → Resolved/Returned/Rejected; `OC Clinical Reviewer` resolves within patient and facility user permissions, with sensitive fields at permlevel 1.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.conflicts.get` and `resolve` call source-specific guarded amendment APIs; direct auto-REST mutation is disabled.
- **Realtime and jobs:** Notify assigned reviewers and authors through minimum-necessary websocket events; server-side RQ jobs prepare diffs and apply approved resolutions transactionally.
- **Files and surfaces:** Attachment conflicts compare Frappe private file digests and metadata, never public URLs; a Desk comparison view and Script Report support review.

## Boundaries

Owns: conflict evidence, resolution workflow, and receipts. Consumes: offline intent, authoritative versions, schema policy, and reviewer authority. Emits: accepted write, succession amendment, return, or rejection. Does not own: source semantics or autonomous clinical reconciliation.

## Open questions

- Which structured field types can be proven safe for automatic nonoverlapping merge?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
