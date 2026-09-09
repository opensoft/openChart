# Virtual Waiting Room And Staff Admit — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Holds verified virtual participants outside the clinical room until authorized staff admit them.
Topics: openchart-feature-catalog, telehealth, frappe, virtual-waiting-room
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-005 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Queue visibility policy** — Show privacy-safe approximate position or delay bands by service line.

## Focus

This feature isolates controlled arrival, queue presence, and human admission for a virtual room.

## Behavior

- A participant with a valid grant enters waiting rather than joining clinician media directly.
- Staff see display name, participant role, arrival time, readiness status, and appointment linkage for authorized rooms only.
- Authorized staff may admit, defer, deny with a reason, or request readiness correction.
- Admission is atomic and rejects stale grants, wrong rooms, cancelled visits, or already-ended sessions.
- Late or duplicate arrivals are reconciled to the existing participant record and never bypass the queue.
- Denial or room closure presents the participant with a safe explanation and contact path without exposing staff notes.

## Frappe realization

- **DocTypes/workflow:** `OC Virtual Participant` uses Invited, Waiting, Admitted, Left, Denied, and Expired states with transition actor and reason.
- **API/realtime:** guarded admit and deny methods enforce room-scoped DocPerms; websocket events refresh staff and patient views after accepted server transitions.
- **Surfaces/roles:** a Telehealth Operations Kanban and room console serve Telehealth Staff and Clinician roles; Patient and Proxy roles can read only their own waiting state.

## Boundaries

Owns: virtual queue and admission authority. Consumes: grants, readiness, and room state. Emits: participant transitions. Does not own: appointment scheduling or media mixing.

## Open questions

- Which roles may admit interpreters and family participants before the clinician is present?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
