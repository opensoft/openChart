# NewRx Electronic Prescription Routing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates, signs, and routes a standards-ready electronic prescription to a selected retail pharmacy with traceable delivery outcomes.
Topics: openchart-feature-catalog, eprescribing, frappe, newrx
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-001 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Network adapter certification kit** — Sites could validate first-party NewRx adapters against synthetic conformance messages before production activation.

## Focus

This feature isolates the prescriber's creation and outbound routing of one electronic prescription. It keeps the accepted prescription as the source of truth while treating network delivery as a separately observed process.

## Behavior

- A licensed prescriber selects a patient, medication, dose, SIG, quantity, refills, indication, and destination pharmacy.
- The composer validates required clinical and routing data before allowing signature.
- Signing submits an immutable prescription and queues one idempotent NewRx transmission.
- The service records queued, sent, accepted, rejected, or indeterminate delivery states with timestamps and network identifiers.
- Rejection shows actionable reasons and permits correction through a successor prescription rather than editing the submitted record.
- Staff may monitor and retry transport failures but may not alter signed clinical content or impersonate the prescriber.

## Frappe realization

- **DocTypes:** Use submittable `OC Prescription` with naming series `OC-RX-.YYYY.-.#####`, child `OC Prescription Line`, and `OC Prescription Transmission` for payload digest, network ID, state, and attempts.
- **Workflow:** Draft → Ready to Sign → Signed → Transmission Queued → Sent, with Failed and Cancelled branches; submission fixes the signed clinical snapshot.
- **Roles/API:** `OC Prescriber` signs through guarded `open_chart.api.v1.prescriptions.create_and_send`; `OC Pharmacy Operations` can retry only the transmission via idempotent whitelisted methods.
- **Surfaces/hooks:** A Desk prescription composer, patient timeline card, `on_submit` enqueue hook, background network adapter, and realtime status updates expose the flow.

## Boundaries

Owns: signed prescription intent and outbound delivery evidence. Consumes: patient identity, medication terminology, prescriber authority, and pharmacy endpoint. Emits: NewRx payloads, acknowledgements, and audit events. Does not own: pharmacy dispensing decisions, claims, or autonomous medication selection.

## Open questions

- Which transport profiles and certification evidence must every network adapter support at launch?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescription Status Tracking](openchart-feature-catalog-phr-007-prescription-status-tracking.md)
