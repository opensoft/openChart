# Telehealth Billing Equivalency Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures encounter facts needed to support human coding of telehealth place-of-service and modality modifiers.
Topics: openchart-feature-catalog, telehealth, frappe, billing-equivalency
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-018 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Coding completeness check** — Flag missing modality facts before a charge handoff without choosing a billable code.

## Focus

This feature isolates factual documentation and explainable suggestions for POS and modifiers such as 95 or GT while leaving billing ownership outside openChart.

## Behavior

- Encounter completion derives candidate documentation needs from service date, modality history, patient location, provider location, and payer policy reference.
- The clinician confirms synchronous video, audio-only, asynchronous, or mixed modality and records required exceptions.
- The system preserves the policy version and evidence behind any suggested place of service or modifier.
- Conflicts between observed session events and clinician attestation require reconciliation rather than silent correction.
- Authorized coding staff may accept, replace, or reject suggestions with rationale.
- The finalized fact package is emitted to the billing boundary; openChart does not submit or adjudicate a claim.

## Frappe realization

- **DocTypes:** `OC Telehealth Billing Facts` and `OC Coding Suggestion` store encounter evidence, policy version, suggested POS/modifier, confidence basis, reviewer decision, and handoff state.
- **Hooks/API:** encounter completion validates required facts; `open_chart.api.v1.telehealth.export_billing_facts` exposes an idempotent, permissioned payload to an external practice system.
- **Permissions/reports:** Clinician confirms clinical facts, Coding Liaison reviews suggestions, and Audit Reviewer sees a read-only rationale report.

## Boundaries

Owns: encounter modality facts and advisory coding evidence. Consumes: visit events and external payer policy. Emits: reviewed billing-fact package. Does not own: fee schedules, claims, payments, or coding authority.

## Open questions

- Which external system is authoritative for payer-specific POS and modifier policy versions?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
