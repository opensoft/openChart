# On-Call Result Routing Pools — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Resolves result recipients from accountable service pools and effective on-call schedules with explicit fallback ownership.
Topics: openchart-feature-catalog, cpoe, frappe, on-call-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-042 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Coverage-gap forecast** — Warn service owners about future schedule intervals with no eligible recipient.

## Focus

This feature isolates schedule-aware routing while preserving a durable service-level safety net.

## Behavior

- Service pools define members, facilities, result classes, schedule source, and fallback owner.
- At result finalization, routing resolves the qualified on-call recipient effective at that timestamp.
- Schedule gaps route to the fallback pool and create an operational exception.
- Shift changes do not silently remove current responsibility; transfer follows accepted handoff rules.
- Users can see why they received an item and which schedule version was used.
- Routing rules never acknowledge or clinically dispose of results.

## Frappe realization

- **DocTypes:** `OC Result Routing Pool`, child membership/scope rows, and `OC On Call Coverage` with effective interval and provenance.
- **Workflow:** pool Draft → Active → Retired; coverage Published → Completed/Cancelled.
- **Roles/permissions:** `OC Service Owner` manages membership; schedule integrations propose coverage; oversight approves exceptions.
- **Hooks/API/surface:** result `on_submit` resolves routing server-side; scheduler detects gaps; REST filters expose pool queues and coverage exceptions.

## Boundaries

Owns: service-pool and schedule-based recipient resolution. Consumes: result class, facility, schedule, and eligibility. Emits: owner assignment and gap exceptions. Does not own: staffing schedules themselves.

## Open questions

- Should responsibility follow the on-call shift at finalization or at acknowledgment deadline?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Owner Assignment And Transfer](openchart-feature-catalog-ord-036-result-owner-assignment-and-transfer.md)
