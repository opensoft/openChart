# In-App Telehealth Join — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets an authenticated mobile user join an eligible virtual visit through a short-lived, appointment-bound media grant.
Topics: openchart-feature-catalog, mobile-devices, frappe, telehealth-join
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-023 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Peripheral handoff during visit** — Offer governed device readings to the active virtual encounter.

## Focus

This capability isolates native-app arrival and media handoff while preserving virtual-visit authority on the server.

## Behavior

- The app lists only eligible upcoming or active virtual visits for the authenticated user.
- Join rechecks identity, participant role, appointment, patient location, consent, device permissions, and room state.
- A preflight tests camera, microphone, speaker, and network without retaining media.
- The server issues a short-lived, single-room grant that cannot be replayed across visits.
- Waiting, admitted, connected, reconnecting, converted, ended, and denied states are explicit.
- Notifications and lock-screen surfaces reveal no patient or visit details.
- Technical failure offers governed retry or alternative-contact guidance without marking the visit completed.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Telehealth Join` with appointment, participant, location attestation, consent version, preflight, grant hash, room state, and outcome.
- **Roles and permissions:** Patient, proxy, clinician, and interpreter participation use distinct DocPerms and appointment/participant user permissions.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.telehealth.prepare` and `join` issue scoped media-adapter grants; signed callbacks normalize room state.
- **Realtime and jobs:** Websocket events drive waiting and admission states; server-side RQ jobs expire grants, reconcile adapter sessions, and route failures.
- **Files and surfaces:** Routine media is not attached; explicitly governed visit artifacts use private Frappe file attachment APIs, with native join and Desk room views.

## Boundaries

Owns: app join eligibility, grant, and normalized state. Consumes: appointment, identity, consent, location, and media adapter. Emits: participant presence and outcomes. Does not own: media infrastructure or clinical encounter completion.

## Open questions

- Which media adapter contract is required for equivalent waiting-room and audit behavior on both platforms?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
