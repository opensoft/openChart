# Scheduled Job Manager — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides governed scheduling, pausing, manual execution, and run history for approved recurring platform jobs.
Topics: openchart-feature-catalog, platform, frappe, scheduled-jobs
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-012 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Maintenance-window calendar** — Visualize job overlap and block risky execution periods.

## Focus

This feature isolates administrator control over approved scheduler tasks without exposing arbitrary Python execution.

## Behavior

- Platform operators choose an allowlisted job, cron expression, time zone, site scope, parameters, and concurrency policy.
- Validation previews the next runs and rejects malformed schedules or unsupported parameters.
- Jobs move through Draft, Enabled, Paused, Running, Failed, and Retired operational states.
- Manual runs require a reason, use the same policy as scheduled runs, and receive a unique correlation ID.
- Overlap policy may skip, queue, or reject a run; it never starts duplicate work silently.
- Each run records timing, result summary, retry count, and redacted error details without storing sensitive payloads.

## Frappe realization

- **DocTypes:** `OC Scheduled Job Policy` stores allowlisted method, cron, timezone, parameters JSON, scopes, and overlap policy; `OC Scheduled Job Run` stores outcomes.
- **Automation:** `scheduler_events` cron polls due policies and enqueues RQ jobs with distributed locking and idempotency keys.
- **Permissions:** Platform Operator schedules and pauses; Job Operator may trigger approved manual runs; Audit Reviewer reads history.
- **Surface:** Calendar and List views show next runs; Script Report summarizes duration, failures, and skips.

## Boundaries

Owns: approved schedules, invocation policy, and run evidence. Consumes: allowlisted job registrations and site scopes. Emits: RQ jobs and status events. Does not own: worker infrastructure or arbitrary code execution.

## Open questions

- How should daylight-saving transitions affect local-time cron schedules?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Background Job Operations Console](openchart-feature-catalog-plt-013-background-job-operations-console.md)
