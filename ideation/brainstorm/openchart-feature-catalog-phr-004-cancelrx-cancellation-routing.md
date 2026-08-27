# CancelRx Cancellation Routing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Sends a traceable electronic cancellation for a previously transmitted prescription and reconciles the pharmacy response.
Topics: openchart-feature-catalog, eprescribing, frappe, cancelrx
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-004 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Replacement-prescription linkage** — A cancellation could be paired with a clearly related successor prescription while preserving two independent outcomes.

## Focus

This feature isolates cancellation communication after a prescription has left openChart. Local discontinuation and pharmacy cancellation remain distinct facts until an external response confirms the request outcome.

## Behavior

- A prescriber selects an eligible sent prescription and records a cancellation reason.
- The system warns if dispensing may already have occurred and never represents cancellation as guaranteed.
- Prescriber authorization submits an immutable CancelRx request referencing the original network identifiers.
- The request records queued, sent, accepted, denied, unable-to-match, and indeterminate states.
- Denial or timeout creates a follow-up task with pharmacy contact details and permitted fallback actions.
- Any replacement prescription is linked as a successor but is not transmitted until separately reviewed and signed.

## Frappe realization

- **DocTypes:** Submittable `OC Prescription Cancellation` links `OC Prescription` and stores reason, authorization, network correlation, response, and timestamps.
- **Workflow:** Draft → Authorized → Sent → Accepted/Denied/Manual Follow-up; cancellation of the Frappe document does not erase external evidence.
- **Roles/API:** `OC Prescriber` authorizes; `OC Pharmacy Operations` resolves follow-up through `open_chart.api.v1.prescriptions.cancel` and response callbacks.
- **Hooks/surfaces:** `on_submit` queues CancelRx, a Desk worklist shows exceptions, and notifications escalate unresolved requests.

## Boundaries

Owns: cancellation intent, transmission, and response evidence. Consumes: original prescription identity and pharmacy endpoint. Emits: CancelRx messages and follow-up tasks. Does not own: local medication-list status or reversal of completed dispensing.

## Open questions

- When should an unanswered CancelRx require direct telephone confirmation?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescription Status Tracking](openchart-feature-catalog-phr-007-prescription-status-tracking.md)
