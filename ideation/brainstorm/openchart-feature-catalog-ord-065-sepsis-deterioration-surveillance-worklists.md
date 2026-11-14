# Sepsis And Deterioration Surveillance Worklists — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies registered surveillance rules on a schedule and routes reviewable sepsis or deterioration signals to qualified clinical worklists.
Topics: openchart-feature-catalog, cpoe, frappe, clinical-surveillance
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-065 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Signal trajectory view** — Show how contributing observations and rule outputs changed over time for reviewer interpretation.

## Focus

This feature isolates scheduled detection and human review of possible deterioration from registered, provenance-bearing rules.

## Behavior

- Active surveillance rules evaluate eligible patients using authorized recent observations, results, orders, and care-setting context.
- Signals display rule/version, contributing facts and times, severity, missing data, owner, and recommended review steps.
- Qualified clinicians acknowledge, assess, dismiss with reason, escalate, or create separately reviewable draft actions.
- A signal never diagnoses, activates a protocol, places an order, or contacts a patient autonomously.
- Repeated evaluations update a signal trajectory without erasing prior states.
- Rule errors, stale scans, and unroutable signals enter operational exception worklists.

## Frappe realization

- **DocTypes:** `OC Surveillance Signal` with patient, rule version, first/last detected, severity, state, owner pool, contributing-reference table, provenance, and disposition.
- **Workflow:** New → Acknowledged → Assessed → Resolved/Dismissed/Escalated, with Reopened on material recurrence.
- **Roles/permissions:** `OC Surveillance Clinician` reviews scoped services; CDS governance owns rules; integration users cannot clinically acknowledge.
- **Scheduler/API/surface:** `scheduler_events` cron scans enqueue idempotent rule evaluations; REST filters by pool/state/severity/age and a Desk workspace provide worklists; failures surface in a Script Report.

## Boundaries

Owns: surveillance signal lifecycle and review worklist. Consumes: active rules and authorized clinical facts. Emits: human-review signals and draft-action options. Does not own: diagnosis, autonomous treatment, or bedside monitoring.

## Open questions

- Which scan cadence and latency targets are safe for each surveillance rule without implying real-time monitoring?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Rule Testing Sandbox](openchart-feature-catalog-ord-062-cds-rule-testing-sandbox.md)
