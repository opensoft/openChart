# Capacity And Performance Diagnostics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents safe self-diagnostics for request latency, workers, queues, database pressure, storage, and site capacity with actionable thresholds.
Topics: openchart-feature-catalog, platform, frappe, performance-diagnostics
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-050 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Guided capacity plan** — Translate sustained threshold breaches into a reviewed scaling checklist.

## Focus

This feature isolates platform health diagnosis without exposing raw queries, clinical payloads, secrets, or unsafe tuning controls.

## Behavior

- Platform operators view site and fleet health for web latency, error rate, RQ depth, worker heartbeat, scheduler lag, database connections, disk, and cache.
- Metrics display collection time, sampling window, threshold source, and unknown state when unavailable.
- Operators can run bounded synthetic probes that create no clinical records and have explicit cost and timeout limits.
- Findings classify Healthy, Degraded, Critical, Unknown, or Maintenance with recommended human actions.
- Cross-site views aggregate safely; clinic administrators see only their own site's metrics and incidents.
- Diagnostics never execute arbitrary SQL, shell commands, or configuration changes from the page.

## Frappe realization

- **DocTypes:** `OC Health Check Definition`, `OC Health Check Run`, and `OC Capacity Threshold` store registered probes, measurements, state, scope, and evidence.
- **Automation:** scheduler and RQ jobs collect bounded metrics; realtime events refresh Number Cards and Dashboard Charts.
- **Permissions:** Site Administrator reads local checks; Platform Operator runs fleet probes; threshold changes require Platform Approver.
- **Surface/API:** diagnostics Desk page and guarded health endpoints return redacted metrics and correlation IDs.

## Boundaries

Owns: health checks, capacity thresholds, safe diagnostics, and findings. Consumes: platform metrics and registered probes. Emits: health states and remediation alerts. Does not own: infrastructure scaling, raw database access, or clinical performance measures.

## Open questions

- Which thresholds can be baseline-derived without masking slow degradation?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Background Job Operations Console](openchart-feature-catalog-plt-013-background-job-operations-console.md) · [Redacted Log Viewer](openchart-feature-catalog-plt-051-redacted-log-viewer.md)
