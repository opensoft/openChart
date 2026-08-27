# Background Job Operations Console — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives operators a safe console for monitoring queues, inspecting failures, and retrying approved background jobs.
Topics: openchart-feature-catalog, platform, frappe, background-jobs
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-013 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Queue saturation forecast** — Project backlog clearance from recent throughput without inspecting payloads.

## Focus

This feature isolates operational visibility and controlled remediation for Frappe RQ background work.

## Behavior

- Operators view queues, worker heartbeat, waiting and running counts, throughput, age, and failure rate by site.
- Job detail shows allowlisted metadata, correlation ID, attempts, timestamps, and safely redacted exception text.
- Payload values are hidden by default and never reveal clinical data or credentials in the console.
- Retry is available only for jobs declared retry-safe and requires a reason; the original attempt remains immutable.
- Cancellation requests distinguish queued removal from cooperative cancellation of running work.
- Worker loss or repeated failure opens an operational alert with links to related run evidence.

## Frappe realization

- **DocTypes:** `OC Background Job Evidence` projects RQ identifiers, site, method class, state, attempts, timings, and redacted error; `OC Job Retry Request` records authority.
- **Automation:** worker callbacks and scheduled reconciliation update evidence; realtime events refresh queue Number Cards and charts.
- **Permissions:** Job Operator may retry safe classes; Platform Operator may pause queues; Audit Reviewer has read-only access.
- **Surface/API:** a Desk page reads queue telemetry through guarded whitelisted methods and never accepts arbitrary job functions.

## Boundaries

Owns: queue observability, retry authorization, and job evidence. Consumes: RQ metadata and worker health. Emits: approved retry or cancellation requests and alerts. Does not own: business outcomes or raw job payloads.

## Open questions

- What retention period balances forensic usefulness with operational metadata minimization?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Scheduled Job Manager](openchart-feature-catalog-plt-012-scheduled-job-manager.md) · [Capacity And Performance Diagnostics](openchart-feature-catalog-plt-050-capacity-and-performance-diagnostics.md)
