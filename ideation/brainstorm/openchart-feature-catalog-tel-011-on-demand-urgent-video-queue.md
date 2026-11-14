# On-Demand Urgent Video Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes unscheduled virtual-care requests through human clinical triage into an eligible clinician queue.
Topics: openchart-feature-catalog, telehealth, frappe, urgent-video-queue
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-011 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Demand and staffing dashboard** — Compare arrival, triage, abandonment, and clinician pickup intervals by service.

## Focus

This feature isolates request intake, human triage, and queue assignment for on-demand virtual care.

## Behavior

- An authenticated patient submits symptoms, location, callback details, and accessibility needs for urgent virtual review.
- The interface displays emergency warnings and local escalation guidance without attempting autonomous diagnosis.
- A qualified triage role reviews the request and marks emergency redirect, virtual eligible, in-person needed, pending information, or declined.
- Eligible requests enter a service queue ordered by explicit policy with visible reason and manual reprioritization audit.
- An eligible clinician claims one request atomically, creating the virtual visit and preventing duplicate pickup.
- Abandonment, timeout, or failed contact closes the queue item with disposition and follow-up responsibility.

## Frappe realization

- **DocTypes/workflow:** `OC On Demand Care Request` uses Submitted, Triage, Queued, Claimed, Redirected, Abandoned, and Closed states with symptoms, location, urgency rationale, and ownership.
- **Assignment/API:** Assignment Rules and guarded claim methods allocate review work; realtime Kanban and Number Cards show queue age without exposing requests outside service permissions.
- **Roles/safety:** Patient submits and reads own status, Telehealth Triage decides eligibility, Clinician claims, and no scheduler or rule engine performs autonomous clinical disposition.

## Boundaries

Owns: on-demand request and accountable queue state. Consumes: patient input, location eligibility, and staffing. Emits: triage disposition or claimed visit. Does not own: emergency response or clinical diagnosis.

## Open questions

- Which queue policies balance arrival order, clinician judgment, equity, and jurisdiction constraints transparently?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
