# Analytics Row-level Security — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies patient, provider, facility, organization, consent, and purpose restrictions to every analytical dataset and derivative.
Topics: openchart-feature-catalog, analytics, frappe, row-level-security
Repository context: openChart — Frappe v15 native EMR; catalog entry ANL-042 (Analytics Reporting Dashboards)
Captured: 2026-08-24

## Possible feats

- **Policy Simulation Can Show Administrators** — policy simulation can show administrators the rows a test identity would receive.

## Focus

This feature isolates one capability: applies patient, provider, facility, organization, consent, and purpose restrictions to every analytical dataset and derivative. It keeps analytical interpretation explicit so openChart users and pluggable open-source BI tools can share semantics without a proprietary reporting lock-in.

## Behavior

- Security Administrators and Data Consumers start from viewer identity, roles, user permissions, dataset policy, row attributes, and purpose.
- The system resolves the user's current roles, facility and organization user permissions, patient scope where applicable, and purpose before showing a preview.
- Validation displays selected definitions, effective versions, source freshness, grain, denominator, exclusions, and estimated query cost before execution.
- A successful run produces a deterministic allowed row scope carried through query, cache, export, and drill-down.
- Saved or published results retain parameters, metric and dataset versions, source watermarks, actor, timestamp, and permission context.
- Drill-down, sharing, subscriptions, exports, and API reuse re-evaluate row-level authority; a cached result never broadens access.
- Missing policy context denies access and invalidates affected cached results.
- Corrections create a new definition or run linked to the prior record; accepted analytical evidence is not silently overwritten.

## Frappe realization

- **DocTypes:** `OC Dataset Access Policy` uses `OC-ANL-.YYYY.-.#####` naming with owner, status, definition version, JSON parameters, source watermark, permission scope, and lineage Links; child tables hold dimensions, filters, recipients, or result references as appropriate.
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
