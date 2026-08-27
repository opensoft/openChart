# Technologist Worklist — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents authorized technologists with a prioritized, readiness-aware queue of scheduled and unscheduled imaging work.
Topics: openchart-feature-catalog, imaging, frappe, technologist-worklist
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-006 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Operational delay reasons** — Capture structured causes when a ready study cannot begin.

## Focus

This feature isolates the task surface used to coordinate imaging performance without replacing the modality console.

## Behavior

- Technologists see cases filtered by facility, modality, room, shift, date, and assigned team.
- Each row shows patient safeguards, study, protocol status, preparation, safety blocks, appointment, and priority.
- Starting a case revalidates order, patient, protocol, and blocking safety conditions on the server.
- Users may claim, hand off, defer, or mark a case unable to perform with structured reasons.
- Emergency and add-on cases are visibly distinguished and audited when reprioritized.
- Realtime updates are advisory; accepted server state resolves concurrent claims or stale rows.

## Frappe realization

- **DocTypes:** `OC Imaging Work Item` materializes operational state linked to order, appointment, protocol assignment, and performance record.
- **Workflow:** Ready → Claimed → In Progress → Deferred or Unable to Perform → Completed.
- **Roles/permissions:** `OC Imaging Technologist` acts within facility and modality user permissions; managers may reassign with reason.
- **Surfaces/API:** Query Report plus Desk workspace and websocket updates; guarded start and handoff methods return conflict-safe responses.

## Boundaries

Owns: operational assignment and work state. Consumes: order, protocol, schedule, and safety readiness. Emits: performance start and delay evidence. Does not own: modality-console worklists or image acquisition.

## Open questions

- Should work items be materialized records or projections with event-backed claims?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
