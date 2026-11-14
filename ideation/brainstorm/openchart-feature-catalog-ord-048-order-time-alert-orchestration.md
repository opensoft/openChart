# Order-Time Alert Orchestration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates eligible CDS rules against an order draft and returns deduplicated interruptive alerts and non-interruptive advisories before signature.
Topics: openchart-feature-catalog, cpoe, frappe, alert-orchestration
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-048 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Alert bundling** — Group multiple manifestations of one safety issue while retaining every contributing rule version.

## Focus

This feature isolates deterministic rule firing and presentation at order time.

## Behavior

- Evaluation receives patient, encounter, draft order, active medication, allergy, laboratory, demographic, and care-setting context allowed by consent and permissions.
- Only active, in-scope rule versions execute, and each result includes severity, rationale, evidence, owner, and missing-data status.
- Duplicate alerts are grouped without suppressing distinct clinical concerns.
- Interruptive alerts require resolution before signature; advisories remain visible but do not block.
- Timeouts or rule errors are shown explicitly and follow configured fail-safe policy.
- No rule submits, edits, cancels, or fulfills an order; the clinician remains the approving actor.

## Frappe realization

- **DocTypes:** `OC CDS Evaluation` stores rule version, context digest, outcome, severity, missing inputs, latency, and provenance; no unnecessary clinical snapshot is duplicated.
- **Roles/permissions:** ordering users receive scoped results; `OC CDS Auditor` reads evaluation evidence under audited access.
- **Hooks/API/surface:** `OC Clinical Order` `doc_events.validate/on_submit` invoke the orchestration service; whitelisted preview returns alerts, and server submission reruns blocking checks.
- **Operations:** background-safe telemetry, timeout controls, and a Script Report expose rule failures without permitting bypass.

## Boundaries

Owns: rule selection, evaluation orchestration, grouping, and outcomes. Consumes: active rules and authorized clinical context. Emits: alerts, advisories, and evidence. Does not own: clinician decisions or order placement.

## Open questions

- Which technical failure modes should block signing for each rule severity?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Non-Interruptive CDS Advisory Feed](openchart-feature-catalog-ord-053-non-interruptive-cds-advisory-feed.md)
