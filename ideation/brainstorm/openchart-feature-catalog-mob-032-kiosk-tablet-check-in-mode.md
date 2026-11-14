# Kiosk Tablet Check-In Mode — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Locks a managed tablet into a privacy-preserving patient check-in flow with session isolation, identity verification, and rapid reset.
Topics: openchart-feature-catalog, mobile-devices, frappe, kiosk-mode
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-032 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Assisted check-in handoff** — Transfer a stuck kiosk session to authorized staff without exposing prior patient data.

## Focus

This capability isolates shared tablet check-in and privacy reset rather than general patient portal use.

## Behavior

- The tablet boots into an organization-branded, accessibility-ready check-in surface with no chart navigation.
- A patient begins with an appointment token or approved identity checks and receives a short-lived kiosk session.
- Demographic confirmation, forms, consent, signature, and arrival status are shown only when configured and authorized.
- Inactivity, completion, cancellation, staff reset, app restart, or policy change destroys session-local content.
- The next user cannot navigate back, view autofill, inspect downloads, or recover previous attachments.
- Offline mode may queue an arrival only under explicit policy and clearly labels it unconfirmed.
- Repeated identity failure routes to staff assistance without revealing whether a patient record exists.

## Frappe realization

- **DocTypes:** Create `OC Kiosk Device`, `OC Kiosk Session`, and `OC Kiosk Policy` with device enrollment, facility, allowed flows, expiry, state, and reset evidence.
- **Roles and permissions:** Kiosk service identities receive least-privilege whitelisted methods, no Desk access, and facility-scoped user permissions; staff assistance uses named users.
- **API and auth:** Device-bound TLS REST tokens call `open_chart.api.v1.mobile.kiosk.start`, `submit`, and `reset`; generic auto-REST and unrestricted patient search are disabled.
- **Realtime and jobs:** Websocket events signal staff assistance and policy reset; server-side RQ jobs expire sessions, reconcile offline arrivals, and monitor reset acknowledgements.
- **Files and surfaces:** Captured files use staged private Frappe attachment APIs and are purged from the kiosk after receipt; Web View and Desk reports expose no prior-session cache.

## Boundaries

Owns: kiosk device/session, allowed flow, and reset evidence. Consumes: appointment, identity verification, intake, and facility policy. Emits: check-in submissions and staff-assistance signals. Does not own: device MDM or full portal access.

## Open questions

- Which check-in steps remain usable during a site outage without creating duplicate arrivals?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
