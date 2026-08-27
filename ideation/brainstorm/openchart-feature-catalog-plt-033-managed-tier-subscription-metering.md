# Managed-tier Subscription Metering — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows transparent, site-attributed managed-service usage and entitlement measurements without turning openChart core features into hidden locks.
Topics: openchart-feature-catalog, platform, frappe, subscription-metering
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-033 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Usage budget alerts** — Notify administrators before a managed-service threshold is reached.

## Focus

This feature isolates optional managed-tier metering while preserving independent open-source operation and clear measurement provenance.

## Behavior

- Managed-service administrators register entitlement plans, meters, units, collection cadence, and effective site subscriptions.
- Site administrators see current entitlements, measured usage, included amounts, estimates, and source timestamps.
- Meter events carry site, meter key, quantity, period, source, and idempotency key without clinical payloads.
- Corrections append adjustment events rather than rewriting prior measurements.
- Delayed or unavailable metering shows stale status and does not silently disable clinical functionality.
- Exportable statements explain each aggregate and separate operational limits from commercial estimates.

## Frappe realization

- **DocTypes:** `OC Managed Entitlement`, `OC Usage Meter Definition`, and append-only `OC Usage Meter Event` store plan, site, unit, quantity, period, and provenance.
- **Automation:** `scheduler_events` aggregate events into monthly summaries; external billing handoff uses a guarded, signed export.
- **Permissions:** Managed Service Administrator configures plans; Site Administrator reads local usage; finance integration receives aggregates only.
- **Surface:** Number Cards and Dashboard Charts show entitlement, usage trend, stale meters, and projected threshold dates.

## Boundaries

Owns: managed-tier entitlement and usage evidence. Consumes: privacy-minimized operational meter events. Emits: transparent aggregates and alerts. Does not own: invoicing, payment collection, core open-source licensing, or clinical access.

## Open questions

- Which managed services have fair, comprehensible units that cannot incentivize unsafe behavior?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Opt-in Usage Telemetry Dashboard](openchart-feature-catalog-plt-049-opt-in-usage-telemetry-dashboard.md)
