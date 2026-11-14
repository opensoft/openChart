# Prescription Renewal Request Inbox — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Triages patient and pharmacy renewal requests into a structured inbox with medication context, eligibility checks, and prescriber disposition.
Topics: openchart-feature-catalog, messaging-tasks, frappe, renewal-inbox
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-030 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Renewal readiness summary** — Present due monitoring, recent visits, adherence signals, and policy exceptions without making an autonomous prescribing decision.

## Focus

This feature isolates accountable request intake and review; it does not prescribe, approve, or transmit a medication renewal by itself.

## Behavior

- Requests arrive from portal, SMS, staff entry, pharmacy interface, or phone with source and requester identity evidence.
- Matching links the request to patient, medication statement or prescription, prescriber, pharmacy, and requested quantity when available.
- Ambiguous medication, patient, or pharmacy identity enters a restricted reconciliation queue.
- Configurable checks surface refill timing, remaining refills, monitoring due, recent encounter, duplicate open request, and controlled-substance status.
- Staff may request information, route to covering prescriber, mark duplicate, or submit for prescriber decision.
- Only an authorized prescriber records approve, deny, modify-via-prescribing-workflow, or appointment-required disposition.
- Approval disposition alone does not create or send a prescription; it links to the authoritative prescribing transaction.
- Patient-facing updates use preference, consent, and minimum-necessary channel policy.

## Frappe realization

- **DocTypes:** `OC Renewal Request`, `OC Renewal Review Check`, and `OC Renewal Disposition` hold sources, medication/prescription links, requester, pharmacy, state, checks, and decision evidence.
- **Workflow:** Received → Reconciliation/Triage → Awaiting Information/Prescriber Review → Disposed/Cancelled.
- **Assignment:** Frappe Assignment Rules route by prescriber, patient panel, facility, schedule, and coverage; exception items enter the staff work queue.
- **Notifications:** Notification Log alerts staff; patient responses use approved SMS settings or Email Accounts through the communication gateway.
- **API/permissions:** guarded intake and disposition methods separate staff triage from Prescriber authority; Query Reports expose age and bottlenecks.

## Boundaries

Owns: renewal-request intake, triage, and disposition evidence. Consumes: medication and prescription context, prescriber coverage, monitoring, and patient communications. Emits: reviewed request and linked prescribing work. Does not own: prescription authorization or transmission.

## Open questions

- Which readiness checks are advisory versus mandatory before prescriber review?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Staff Work-queue Inbox](openchart-feature-catalog-msg-001-staff-work-queue-inbox.md)
