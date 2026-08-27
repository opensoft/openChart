# Geofenced Field Visit Check-In — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records privacy-minimized arrival and departure evidence for assigned field visits with transparent geofence verification and exception handling.
Topics: openchart-feature-catalog, mobile-devices, frappe, geofence-check-in
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-025 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Safety check timer** — Offer an opt-in, policy-governed missed-checkout escalation for lone workers.

## Focus

This capability isolates check-in and check-out evidence and avoids continuous workforce or patient-location surveillance.

## Behavior

- Location is requested only when staff explicitly check in or out of an assigned visit.
- The app shows why location is requested, the configured radius, accuracy, and whether evidence is retained.
- The server compares captured coordinates, accuracy, time, assignment, and effective geofence policy.
- Verified, outside radius, low accuracy, unavailable, manually attested, and pending offline states are distinct.
- An exception requires reason and may route to supervisor review without blocking urgent care.
- Offline evidence is signed with device/session context and reconciled against assignment and trusted server time.
- Patient address coordinates and worker location are restricted, minimized, and never shown in general analytics.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Field Visit Check Event` and `OC Visit Geofence Policy` with visit, event type, coordinate precision, accuracy, policy version, outcome, reason, and retention.
- **Workflow and roles:** Pending → Verified/Exception Review → Accepted/Rejected; field staff submit and `OC Home Care Supervisor` reviews within facility permissions.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.visit_check` validates assignment and signed device evidence; coordinate reads require permlevel 2.
- **Realtime and jobs:** Websocket events return verification or review state; server-side RQ jobs reconcile offline checks, expire raw coordinates, and retain coarse evidence where approved.
- **Files and surfaces:** No map screenshot is required; approved exception evidence uses private Frappe file attachment APIs, with restricted Desk maps and audit reports.

## Boundaries

Owns: point-in-time visit check evidence and geofence result. Consumes: assignment, geocoded destination, device location, and policy. Emits: check-in/out and exceptions. Does not own: payroll, continuous tracking, or proof that care occurred.

## Open questions

- What location precision and retention are proportionate for operational verification?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
