# Opt-in Usage Telemetry Dashboard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives administrators transparent, privacy-minimized product usage telemetry under explicit site opt-in and retention controls.
Topics: openchart-feature-catalog, platform, frappe, usage-telemetry
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-049 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Feature adoption review** — Compare enabled capabilities with aggregate use to guide human-led rollout improvements.

## Focus

This feature isolates administrator-visible operational adoption metrics and excludes clinical content, surveillance, and hidden vendor collection.

## Behavior

- Site administrators review a plain-language event inventory, fields, purpose, destination, retention, and default-off state before opting in.
- Consent may be scoped to local-only dashboards or approved external aggregate reporting and can be revoked prospectively.
- Events use coarse feature keys, role classes, durations, outcomes, and site pseudonyms without patient IDs, free text, or record identifiers.
- Dashboards show collection health, last event, retention, top features, failure funnels, and suppressed-event counts.
- Low-volume groups are thresholded to reduce re-identification risk; exports disclose applied suppression.
- Revocation stops new collection and schedules deletion according to the published retention policy.

## Frappe realization

- **DocTypes:** `OC Telemetry Policy`, `OC Telemetry Event`, and aggregate `OC Usage Metric` store consent scope, event key, coarse dimensions, dates, and retention.
- **Hooks:** registered client/server events pass an allowlist and redaction layer before local append; no arbitrary analytics payload is accepted.
- **Automation:** scheduler jobs aggregate and purge raw events; external export uses signed aggregate batches only when opted in.
- **Surface:** Dashboard Charts, Number Cards, event dictionary, and consent controls make collection visible to Site Administrator.

## Boundaries

Owns: telemetry consent, allowed event schema, collection, aggregation, and display. Consumes: privacy-minimized product events. Emits: local metrics and optional aggregates. Does not own: clinical quality, employee surveillance, or patient analytics.

## Open questions

- What minimum group threshold is appropriate for very small clinic sites?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Feature Flag Gradual Rollout](openchart-feature-catalog-plt-031-feature-flag-gradual-rollout.md) · [Managed-tier Subscription Metering](openchart-feature-catalog-plt-033-managed-tier-subscription-metering.md)
