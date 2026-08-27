# Wearable Data Pipeline Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs wearable-source connections, high-volume data intake, provenance, aggregation, quality, and review without flooding the clinical chart.
Topics: openchart-feature-catalog, mobile-devices, frappe, wearable-pipelines
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-031 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Episode extraction workspace** — Let clinicians select a bounded wearable interval for chart inclusion with source provenance.

## Focus

This entry isolates pipeline operations and governed promotion of wearable data into clinically usable records.

## Behavior

- A connection declares patient, source platform, device classes, authorized data types, date range, and consent.
- Raw samples remain source-labeled and are separated from reviewed chart observations.
- The pipeline records cursor, lag, gaps, duplicates, source corrections, timezone, and quality flags.
- Configured aggregation produces transparent windows and methods while retaining references to source batches.
- Staff can pause, resume, backfill, revoke, or repair a connection without silently deleting accepted records.
- Volume, lag, and error dashboards expose operational metadata without broad clinical-content access.
- Any clinical alert or interpretation remains a separately governed, human-reviewed capability.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Wearable Connection`, `OC Wearable Batch`, and `OC Wearable Aggregate` with source, scopes, cursor, interval, quality, provenance, consent, and state.
- **Workflow and roles:** Pending → Active → Paused/Degraded/Revoked; `OC Device Integration Administrator` operates pipelines and clinicians approve chart promotion.
- **API and auth:** OAuth2/token setup and signed adapter callbacks use `open_chart.api.v1.devices.wearables`; guarded methods enforce patient and consent scope.
- **Realtime and jobs:** Websocket events publish pipeline health and review readiness; server-side RQ jobs ingest, deduplicate, aggregate, backfill, and enforce retention.
- **Files and surfaces:** Raw batches use encrypted private Frappe file attachment APIs with content digests; Desk dashboards and patient review views separate operations from chart facts.

## Boundaries

Owns: connection and pipeline lifecycle, raw provenance, aggregates, and promotion requests. Consumes: wearable APIs, patient link, and consent. Emits: quality-labeled aggregates and review tasks. Does not own: consumer device accuracy or autonomous clinical interpretation.

## Open questions

- Which raw sample classes merit retention after a verified aggregate is produced?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
