# Coding Distribution Drift Detection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects material changes in diagnosis and procedure coding distributions for review without accusing individual coders.
Topics: openchart-feature-catalog, analytics, frappe, coding-drift
Repository context: openChart — Frappe v15 native EMR; catalog entry ANL-053 (Analytics Reporting Dashboards)
Captured: 2026-08-24

## Possible feats

- **Reviewed Labels Can Separate Policy** — reviewed labels can separate policy changes from possible documentation or coding issues.

## Focus

This feature isolates one capability: detects material changes in diagnosis and procedure coding distributions for review without accusing individual coders. It keeps analytical interpretation explicit so openChart users and pluggable open-source BI tools can share semantics without a proprietary reporting lock-in.

## Behavior

- Coding Quality Analysts start from coded events, service mix, providers, periods, baselines, and drift thresholds.
- The system resolves the user's current roles, facility and organization user permissions, patient scope where applicable, and purpose before showing a preview.
- Validation displays selected definitions, effective versions, source freshness, grain, denominator, exclusions, and estimated query cost before execution.
- A successful run produces explainable drift signals with affected codes, dimensions, and confidence.
- Saved or published results retain parameters, metric and dataset versions, source watermarks, actor, timestamp, and permission context.
- Drill-down, sharing, subscriptions, exports, and API reuse re-evaluate row-level authority; a cached result never broadens access.
- Low volume, service-mix shifts, or mapping changes suppress or qualify alerts.
- Corrections create a new definition or run linked to the prior record; accepted analytical evidence is not silently overwritten.

## Frappe realization

- **DocTypes:** `OC Coding Drift Signal` uses `OC-ANL-.YYYY.-.#####` naming with owner, status, definition version, JSON parameters, source watermark, permission scope, and lineage Links; child tables hold dimensions, filters, recipients, or result references as appropriate.
- **Workflow and permissions:** Draft → In Review → Approved → Published → Retired uses Frappe Workflow where publication is applicable; Analytics Viewer, Report Author, Analytics Steward, Analytics Approver, Privacy Reviewer, and System Manager receive least-privilege DocPerms plus facility and organization user permissions.
- **Reports and dashboards:** a Query Report serves stable relational projections, a Script Report handles permission-aware calculations and suppression, and approved outputs feed Dashboard Chart and Number Card widgets in role-specific Desk workspaces.
- **Aggregates and jobs:** scripted server-side aggregates compile metric semantics and row-level policy; `scheduler_events` and RQ jobs materialize governed aggregate tables, refresh freshness metadata, and execute bounded schedules idempotently.
- **API and hooks:** guarded `open_chart.api.v1.analytics` whitelisted methods create, validate, execute, share, and export records; `validate`, `on_update`, and `on_submit` hooks enforce version, scope, lineage, and approval invariants.
- **Audit and errors:** `OC Report Run`-compatible execution evidence records query hash, cost, row count, definition versions, source watermarks, actor, and structured denial or failure reason; realtime events update progress without making the client authoritative.

## Boundaries

Owns: the governed analytical definition, execution state, presentation, and evidence described here. Consumes: permissioned clinical or operational source records, identity, consent, metric definitions, dataset policy, and source freshness. Emits: scoped aggregates, report artifacts, lineage, quality signals, and audit events. Does not own: source clinical truth, billing or claims transactions, care decisions, identity matching authority, consent capture, or autonomous clinical action.

## Open questions

- Which definition changes require a new public version rather than a corrected draft, and who may approve that distinction?
- What retention and small-cell thresholds should vary by tenant, purpose, or export destination?

## Relationships

[Synthesis: Analytics Reporting And Dashboards](openchart-feature-catalog-synthesis-anl.md)
