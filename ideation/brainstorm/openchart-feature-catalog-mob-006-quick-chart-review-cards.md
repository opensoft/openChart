# Quick Chart Review Cards — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Delivers compact, source-linked chart cards for rapid mobile review without flattening provenance or replacing the longitudinal record.
Topics: openchart-feature-catalog, mobile-devices, frappe, chart-review-cards
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-006 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Specialty card packs** — Offer governed card sets for service-specific review while retaining source links.

## Focus

This capability isolates small-screen review of high-value chart facts and their freshness.

## Behavior

- Cards may cover identity, allergies, medications, problems, recent vitals, results, notes, and care-team context.
- Every fact displays source type, recorded or effective time, status, and a route to the authoritative record.
- Cards distinguish absent data, unavailable data, pending data, and permission-hidden data without leaking restricted content.
- Users choose among approved card packs but cannot expand their underlying data scope.
- Offline cards show snapshot time and suppress actions requiring current state.
- Corrected or superseded facts are replaced on sync while succession provenance remains accessible.
- Card rendering never claims to be a diagnostic summary or make autonomous recommendations.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Review Card Profile` with child card definitions; cache only signed snapshot envelopes keyed to source names and modified versions.
- **Roles and permissions:** Profiles map to roles, while each source read uses Frappe DocPerms, permission query conditions, and patient user permissions.
- **API and auth:** `open_chart.api.v1.mobile.review_cards` accepts token-authenticated patient context and returns normalized cards from guarded reads; arbitrary fields are rejected.
- **Realtime and jobs:** Publish source-version invalidations via websocket; use server-side RQ jobs for expensive card assembly, never for autonomous clinical interpretation.
- **Files and surfaces:** Card attachments are short-lived references served through Frappe private file attachment APIs after permission checks; Desk previews support profile governance.

## Boundaries

Owns: card composition and snapshot metadata. Consumes: authoritative clinical records and permissions. Emits: concise source-linked views. Does not own: source records, diagnosis, alerting, or clinical decisions.

## Open questions

- Which cards may be cached offline for each role and encounter context?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
