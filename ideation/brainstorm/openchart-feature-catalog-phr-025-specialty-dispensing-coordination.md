# Specialty Dispensing Coordination — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates specialty pharmacy routing, onboarding, shipment, receipt, and care-team handoffs without conflating them with clinical administration.
Topics: openchart-feature-catalog, eprescribing, frappe, specialty-dispensing
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-025 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Cold-chain exception routing** — Shipment temperature or delivery failures could create urgent coordination tasks with evidence attachments.

## Focus

This feature isolates post-authorization specialty dispensing coordination across the patient, clinic, and external pharmacy. It maintains explicit handoffs and uncertainty around shipment and receipt.

## Behavior

- A coordinator confirms the mandated or selected specialty pharmacy and prescription routing status.
- Required onboarding, consent, education, financial, and delivery steps receive owners and due dates.
- Shipment details include destination, expected date, tracking reference, handling requirements, and source.
- Patient, clinic, or pharmacy receipt is recorded separately from shipping and separately from administration.
- Delay, failed delivery, cold-chain concern, or unreachable patient creates an exception with escalation.
- Completion preserves the coordination timeline while leaving administration and adherence to their authoritative records.

## Frappe realization

- **DocTypes:** `OC Specialty Dispensing Coordination` with task, contact, shipment, receipt, and exception child tables links prescription and authorization episode.
- **Workflow:** Pharmacy Selected → Onboarding → Ready to Ship → Shipped → Receipt Confirmed → Closed, with Hold and Exception states.
- **Roles/API:** Specialty coordinators maintain cases; external updates enter through authenticated idempotent adapter methods.
- **Surfaces:** Timeline, Kanban, communication log, notifications, and delayed-shipment report expose handoffs.

## Boundaries

Owns: specialty dispensing handoffs, shipment observations, and exceptions. Consumes: prescription status, authorization readiness, pharmacy endpoint, and patient communication preferences. Emits: coordination tasks and receipt evidence. Does not own: medication administration or adherence assessment.

## Open questions

- Which shipment events can be patient-visible without exposing protected logistics data?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Specialty Authorization Tracking](openchart-feature-catalog-phr-024-specialty-authorization-tracking.md)
