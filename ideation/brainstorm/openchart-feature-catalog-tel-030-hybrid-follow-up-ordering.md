# Hybrid Follow-Up Ordering — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians order and coordinate in-person, virtual, asynchronous, or remote-monitoring follow-up from a virtual encounter.
Topics: openchart-feature-catalog, telehealth, frappe, hybrid-follow-up
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-030 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Follow-up pathway bundle** — Combine reviewed modality, timing, prerequisites, and patient instructions into one coordinated plan.

## Focus

This feature isolates modality-aware follow-up intent and handoff after virtual care rather than fulfilling every downstream order.

## Behavior

- During encounter completion, a clinician selects follow-up modality, service, interval, urgency, prerequisites, and clinical rationale.
- The system checks that the selected modality is offered and records any location, device, or testing dependencies.
- The patient sees the intended next step and whether staff will contact them or self-scheduling is allowed.
- A scheduling or clinical task receives the order with encounter provenance and accountable owner.
- Staff may resolve, redirect, decline, or return the request for clarification without altering the signed order.
- Changes after signature use succession or a linked replacement order and notify affected participants.

## Frappe realization

- **DocTypes/workflow:** `OC Hybrid Follow Up Order` stores encounter, modality, service, interval, rationale, prerequisites, destination, owner, and fulfillment state.
- **API/hooks:** encounter completion can create orders through the supported write API; assignment and Notification events route fulfillment without autonomous modality changes.
- **Surfaces/permissions:** Clinician authors, Scheduler fulfills operational requests, Patient sees released instructions, and a Query Report tracks unresolved follow-up.

## Boundaries

Owns: follow-up intent, modality, and handoff state. Consumes: signed virtual encounter and service catalog. Emits: accountable follow-up request. Does not own: appointment booking, device fulfillment, or downstream clinical service.

## Open questions

- Which follow-up orders may permit patient self-scheduling and which require clinical review first?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
