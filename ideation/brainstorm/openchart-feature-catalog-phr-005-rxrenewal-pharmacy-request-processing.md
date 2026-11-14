# RxRenewal Pharmacy Request Processing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Receives pharmacy-originated renewal requests, matches them to the chart, and routes approve, deny, or clarify decisions to an accountable prescriber.
Topics: openchart-feature-catalog, eprescribing, frappe, rxrenewal
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-005 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Renewal protocol checklist** — Sites could attach reviewable monitoring criteria and required evidence without enabling automatic approval.

## Focus

This feature isolates inbound RxRenewal processing from patient-initiated refill requests. It preserves the pharmacy message, matching confidence, clinical review, and outbound response as separate evidence.

## Behavior

- The network adapter receives an RxRenewal request and verifies message identity and replay protection.
- Deterministic matching proposes a patient, prior prescription, medication, prescriber, and pharmacy with confidence explanations.
- Ambiguous or unmatched requests enter a staffed exception queue and never create an order automatically.
- Assigned clinical staff gather due monitoring and route the request to an authorized prescriber.
- The prescriber approves as a new signed prescription, denies with a coded reason, or asks staff to clarify.
- The outbound response and any new prescription retain correlation to the original request and immutable audit history.

## Frappe realization

- **DocTypes:** `OC Prescription Renewal Request` stores raw digest, parsed fields, match candidates, decision, correlation IDs, and linked successor `OC Prescription`.
- **Workflow:** Received → Matching Review → Clinical Review → Prescriber Decision → Responded, with Unmatched and Clarification states.
- **Roles/API:** `OC Pharmacy Operations`, `OC Clinical Support`, and `OC Prescriber` receive state-specific DocPerms; callbacks and decisions use guarded v1 methods.
- **Surfaces/hooks:** Assignment Rules route inbox items, Workflow Actions notify prescribers, and background jobs send idempotent renewal responses.

## Boundaries

Owns: pharmacy-originated request lifecycle and response. Consumes: external message, patient identity, medication history, and prescriber authority. Emits: denial/approval responses and optionally a newly signed prescription. Does not own: autonomous renewal approval.

## Open questions

- Which matching ambiguities require health-information review versus pharmacy-operations review?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Portal Refill Request Queue](openchart-feature-catalog-phr-006-portal-refill-request-queue.md)
