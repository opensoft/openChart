# Smart Pump Data Hooks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines governed hooks for receiving smart-pump programming and infusion events and reconciling them with authorized orders and administrations.
Topics: openchart-feature-catalog, mobile-devices, frappe, smart-pump-hooks
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-030 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Human-reviewed auto-documentation proposal** — Prepare an infusion record from matched pump events for clinician confirmation.

## Focus

This capability isolates a vendor-neutral event contract and mobile status view, not closed-loop pump control.

## Behavior

- An integration receives device identity, channel, patient association, medication, concentration, rate, volume, times, alarms, and event identifiers.
- The server matches events to current patient, order, administration, device assignment, and location.
- Matched, ambiguous, duplicate, late, cancelled, and unmatched events remain distinct.
- Mobile staff can review pump status and discrepancies only for assigned patients and locations.
- Any proposed chart update requires an authorized human confirmation unless a separately governed policy proves safe automation.
- Delayed or missing events never imply that an infusion stopped or completed.
- The mobile app cannot issue programming commands through this read/reconciliation feature.

## Frappe realization

- **DocTypes:** Create `OC Smart Pump Event Intake`, `OC Pump Device Assignment`, and `OC Pump Reconciliation` with vendor IDs, raw digest, normalized event, matches, state, and reviewer.
- **Workflow and roles:** Received → Matched/Needs Review → Reconciled/Rejected; `OC Infusion Nurse` reviews and integration roles have no broad chart read.
- **API and auth:** Vendor adapters use signed whitelisted `open_chart.api.v1.devices.smart_pump_event`; mobile review uses TLS REST token auth and guarded reconciliation methods.
- **Realtime and jobs:** Websocket events update assigned mobile views; server-side RQ jobs normalize, correlate, deduplicate, retry, and route discrepancies.
- **Files and surfaces:** Raw vendor batches use encrypted private Frappe file attachment APIs with limited retention; mobile status and Desk reconciliation reports are permission-filtered.

## Boundaries

Owns: intake normalization, matching evidence, and reconciliation. Consumes: pump events, device assignment, patient, order, and administration. Emits: reviewable infusion evidence. Does not own: pump programming, drug library, device alarms, or autonomous charting.

## Open questions

- What minimum event and clock-quality contract is required before pump data can support documentation?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
