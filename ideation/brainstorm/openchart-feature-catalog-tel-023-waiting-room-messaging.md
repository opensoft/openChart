# Waiting Room Messaging — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Supports privacy-safe staff-to-participant messages while a person waits for admission to virtual care.
Topics: openchart-feature-catalog, telehealth, frappe, waiting-room-messaging
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-023 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Approved quick replies** — Offer localized delay, readiness, and assistance templates with minimum disclosure.

## Focus

This feature isolates operational messaging before admission and excludes clinical consultation in the waiting channel.

## Behavior

- Staff can send approved or free-text operational messages to one waiting participant in an authorized room.
- The patient can reply, request technical help, or indicate they must leave the queue.
- Messages display sender role, timestamp, delivery state, and whether the participant acknowledged them.
- Clinical content warnings discourage assessment or treatment in the waiting channel and offer the appropriate encounter path.
- Room closure, admission, denial, or grant expiry makes the channel read-only and prevents delayed delivery into another visit.
- Messages follow retention and access policy and never appear to unrelated group or family participants.

## Frappe realization

- **DocTypes:** `OC Waiting Room Message` links visit, participant, direction, template, body, delivery state, actor, and timestamps.
- **API/realtime:** room-scoped whitelisted send and acknowledge methods publish websocket events after permission and state checks.
- **Permissions/surfaces:** Patient reads only their thread; Telehealth Staff and assigned Clinician use a console panel; templates are governed by Telehealth Operations Manager.

## Boundaries

Owns: pre-admission operational conversation. Consumes: waiting participant and room authorization. Emits: delivery and acknowledgment events. Does not own: clinical messaging or emergency advice.

## Open questions

- Should free text be allowed for all staff roles or only approved templates for some services?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
