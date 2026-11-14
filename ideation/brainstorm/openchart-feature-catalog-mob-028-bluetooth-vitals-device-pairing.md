# Bluetooth Vitals Device Pairing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Pairs approved Bluetooth blood-pressure, pulse, oxygen, and glucose devices and imports attributable readings into a reviewable chart intake flow.
Topics: openchart-feature-catalog, mobile-devices, frappe, bluetooth-vitals
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-028 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Device conformance harness** — Test parsing, units, timestamps, and disconnect behavior using synthetic readings.

## Focus

This capability isolates pairing, device identity, measurement transfer, unit normalization, and human confirmation.

## Behavior

- A user selects an approved device profile and initiates pairing from an authorized patient or equipment context.
- The app displays device model, serial alias, measurement types, battery, and current patient association.
- Each reading preserves raw value, unit, device time, phone receive time, device identity, and parser version.
- The user confirms patient and reading set before upload; shared devices require renewed patient association per session.
- Duplicate, implausible, unsupported-unit, stale-time, and partial readings route to review rather than silent correction.
- Offline readings stay encrypted and pending with device provenance.
- Disconnect and permission failures preserve already received complete measurements and explain recovery.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Connected Device`, `OC Device Profile`, and `OC Device Reading Intake` with model, serial hash, protocol, parser, raw/normalized values, times, patient, and state.
- **Workflow and roles:** Captured → Confirmed → Accepted/Needs Review/Rejected; clinical roles confirm and `OC Device Integration Administrator` governs profiles.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.devices.register` and `submit_readings` validate profile and call guarded observation APIs.
- **Realtime and jobs:** Websocket receipts update intake state; server-side RQ jobs deduplicate, normalize configured units, route review, and monitor adapter failures.
- **Files and surfaces:** Device exports or calibration evidence use private Frappe file attachment APIs; mobile pairing and a Desk device/intake report expose permission-filtered metadata.

## Boundaries

Owns: pairing metadata, transfer provenance, and reading intake. Consumes: Bluetooth protocol, approved profile, patient context, and observation schema. Emits: confirmed observation intents. Does not own: device calibration, diagnosis, or treatment decisions.

## Open questions

- Which device standards and model certification evidence are required for initial support?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
