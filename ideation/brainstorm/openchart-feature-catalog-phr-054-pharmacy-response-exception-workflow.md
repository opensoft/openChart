# Pharmacy Response Exception Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes pharmacy clarification, substitution, change, denial, and unable-to-fill responses to accountable review without silently changing a prescription.
Topics: openchart-feature-catalog, eprescribing, frappe, pharmacy-exceptions
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-054 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Structured clarification threads** — Message exchanges could remain grouped by question while preserving every immutable turn.

## Focus

This feature isolates inbound pharmacy exceptions that require clinical or operational action outside renewal requests. Pharmacy proposals remain external requests until an authorized prescriber accepts them through a new signed record.

## Behavior

- The adapter validates and correlates inbound clarification, substitution, therapeutic change, denial, stock, or unable-to-fill messages.
- Each item shows original prescription, pharmacy wording, structured proposal, urgency, and response deadline.
- Staff triage identity, routing, administrative questions, and clinical questions to permitted roles.
- A prescriber may decline, clarify, or create a successor prescription after full review and safety checks.
- No inbound message edits the original prescription, medication list, or destination automatically.
- Outbound response, successor linkage, contacts, and closure reason remain in one auditable thread.

## Frappe realization

- **DocTypes:** `OC Pharmacy Exception` with immutable message turns, structured proposal, assignments, decision, and successor prescription links.
- **Workflow:** Received → Triage → Operational/Clinical Review → Awaiting Pharmacy → Resolved/Closed.
- **Roles/API:** Pharmacy operations route; prescribers decide clinical changes; authenticated callbacks and v1 response methods preserve correlation.
- **Surfaces:** In Basket-style queue, threaded timeline, due indicators, and unresolved-exception Query Report support resolution.

## Boundaries

Owns: pharmacy exception thread, assignment, response, and closure. Consumes: inbound message, original prescription, pharmacy endpoint, and prescriber decision. Emits: response and optional successor draft. Does not own: automatic substitution or silent prescription mutation.

## Open questions

- Which response categories can support delegated administrative closure without prescriber review?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [NewRx Electronic Prescription Routing](openchart-feature-catalog-phr-001-newrx-electronic-prescription-routing.md)
