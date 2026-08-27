# Portal Refill Request Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts patient or proxy refill requests into a permissioned clinical queue without treating the request as a prescription.
Topics: openchart-feature-catalog, eprescribing, frappe, portal-refill
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-006 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Patient-visible requirement checklist** — The portal could show missing visit or monitoring prerequisites selected by staff without exposing sensitive reasoning.

## Focus

This feature isolates patient-initiated refill intake and queue management. A request remains patient-reported intent until a prescriber independently reviews and signs a prescription.

## Behavior

- An authenticated patient or authorized proxy selects a known medication, preferred pharmacy, and optional message.
- The portal displays that submission is a request, not approval, and provides an expected response channel.
- Identity, proxy scope, duplicates, and recent open renewal requests are checked before queue creation.
- Staff triage requests into review, clarification, duplicate, misdirected, or closed states.
- A prescriber may deny with a patient-safe explanation or create a separate draft prescription for review and signature.
- Portal status updates avoid exposing internal notes, sensitive diagnoses, or pharmacy-network payloads.

## Frappe realization

- **DocTypes:** `OC Portal Refill Request` captures requester authority, patient wording, medication reference, pharmacy preference, state, and linked prescription.
- **Workflow:** Submitted → Triage → Clinical Review → Approved/Denied/Needs Information → Closed with Workflow Actions and assignments.
- **Roles/API:** Portal users create/read scoped records through `open_chart.api.v1.refills`; clinical roles use permlevel-separated internal fields.
- **Surfaces:** An authenticated portal form, clinical Desk queue, duplicate warning client script, and patient-safe Notifications expose progress.

## Boundaries

Owns: refill request intake, communication, and triage state. Consumes: portal identity, proxy authority, medication statements, and pharmacy preference. Emits: review tasks and patient-safe outcomes. Does not own: prescription approval or medication adherence conclusions.

## Open questions

- How long should duplicate detection suppress repeat requests before allowing a new concern?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [RxRenewal Pharmacy Request Processing](openchart-feature-catalog-phr-005-rxrenewal-pharmacy-request-processing.md)
