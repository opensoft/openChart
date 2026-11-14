# Order Duration And Auto-Stop — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts explicit duration policy into visible stop times, advance review tasks, and auditable automatic status closure.
Topics: openchart-feature-catalog, cpoe, frappe, order-auto-stop
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-022 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Stop-time conflict preview** — Warn when a proposed duration outlasts the encounter or care setting.

## Focus

This feature isolates duration and auto-stop lifecycle behavior for accepted orders.

## Behavior

- The signer enters duration or stop time, or explicitly accepts a displayed organization default.
- The final stop timestamp and source policy are visible before signature.
- Responsible clinicians receive review reminders before high-risk orders stop.
- At expiry, the system changes fulfillment eligibility to stopped and records the scheduler action and policy source.
- Auto-stop never creates a renewal; a clinician must explicitly renew or reorder.
- Failed scheduler processing retries idempotently and appears on an operational exception report.

## Frappe realization

- **DocTypes:** `OC Clinical Order` stores starts_at, stops_at, duration_source, auto_stop_policy, and stopped_at; `OC Order Lifecycle Event` records evidence.
- **Workflow:** Active → Expiring → Stopped, with Renew creating a successor; scheduler transitions are allowed only for due submitted orders.
- **Roles/permissions:** ordering clinicians choose allowed durations; `OC Order Manager` reviews exceptions; lifecycle fields are system-write only.
- **Scheduler/API/surface:** hourly `scheduler_events` performs idempotent stops and advance Notifications; REST filters on status/stops_at feed expiring-order worklists.

## Boundaries

Owns: order stop timing and status transition. Consumes: signed duration and policy. Emits: reminders and stopped state. Does not own: renewal decisions or fulfillment cleanup.

## Open questions

- Which order classes permit auto-stop without human acknowledgment?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Renewal And Reorder](openchart-feature-catalog-ord-023-order-renewal-and-reorder.md)
