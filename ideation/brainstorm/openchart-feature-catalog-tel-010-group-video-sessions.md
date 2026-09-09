# Group Video Sessions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Supports clinician-led virtual sessions with multiple patients while preserving individual authority, consent, and documentation.
Topics: openchart-feature-catalog, telehealth, frappe, group-video
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-010 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Breakout consultation** — Move one patient and an authorized clinician into a separately governed private room.

## Focus

This feature isolates multi-patient virtual session controls and privacy boundaries, not ordinary family participation in one patient's care.

## Behavior

- Staff create a group session with capacity, facilitators, eligibility, participant rules, and disclosure version.
- Each patient receives an individual invitation and completes identity and group-specific consent before admission.
- Participants see approved display names and are warned against recording or sharing identities.
- Facilitators may mute, remove, lock admission, and end the room while all actions are audited.
- Clinical documentation is created in each patient's authorized encounter; group notes never expose another patient's chart.
- Withdrawal or removal ends that participant's access without changing other participants' encounter state.

## Frappe realization

- **DocTypes:** `OC Virtual Group Session`, child `OC Group Session Participant`, and per-patient `OC Virtual Visit` links separate shared room operations from individual encounters.
- **API/workflow:** guarded enrollment, consent, admit, remove, and close methods enforce capacity and participant-scoped grants; realtime presence excludes cross-chart identifiers.
- **Permissions:** Group Facilitator manages room controls, Clinician accesses assigned encounters, and Patient reads only their own enrollment and approved room roster projection.

## Boundaries

Owns: shared virtual-room governance and individual enrollment. Consumes: eligibility, identity, and consent. Emits: per-participant attendance. Does not own: clinical program design or cross-patient charting.

## Open questions

- Which group-size and moderation guarantees can a custom WebRTC stack support compared with a partner platform?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
