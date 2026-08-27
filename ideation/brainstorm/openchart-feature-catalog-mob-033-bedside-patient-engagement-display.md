# Bedside Patient Engagement Display — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents permission-filtered care information and patient engagement actions on a room-bound bedside tablet or television.
Topics: openchart-feature-catalog, mobile-devices, frappe, bedside-display
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-033 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Room-ready education playlist** — Offer clinician-approved material tied to the current encounter and language.

## Focus

This entry isolates the room display session, patient binding, content release, and automatic unbinding at transfer or discharge.

## Behavior

- Staff bind a managed display to the current room, encounter, and patient using a short-lived verification ceremony.
- The display may show approved care-team names, schedule, goals, education, meal or comfort requests, and portal prompts.
- Sensitive diagnoses, results, notes, and contacts remain hidden unless specifically released for this surface.
- Patient actions create requests or acknowledgements, never direct clinical orders.
- Transfer, discharge, bed change, isolation policy, staff reset, or inactivity removes patient content immediately.
- Visitors and proxy views require explicit patient or policy authorization.
- Network loss shows a neutral unavailable screen rather than stale patient content beyond configured grace.

## Frappe realization

- **DocTypes:** Create `OC Bedside Display Device`, `OC Bedside Display Session`, and `OC Display Content Release` with room, encounter, patient, allowed widgets, language, expiry, and state.
- **Workflow and roles:** Unbound → Bound → Suspended → Ended; `OC Nurse` binds within location permissions and content owners approve releasable templates.
- **API and auth:** Device-bound REST tokens call `open_chart.api.v1.mobile.bedside.bootstrap` and action methods; no generic chart auto-REST is exposed.
- **Realtime and jobs:** Websocket events drive room, content, request, transfer, and immediate-unbind state; server-side RQ jobs expire sessions and prepare safe content projections.
- **Files and surfaces:** Education media uses approved Frappe attachments; patient-specific files remain private and short-lived, with a Desk device/session monitor.

## Boundaries

Owns: bedside display binding and released projection. Consumes: room, encounter, patient, care-team, education, and release policy. Emits: patient requests and acknowledgements. Does not own: room assignment or clinical orders.

## Open questions

- Which content remains appropriate when roommates, visitors, or cameras may be present?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
