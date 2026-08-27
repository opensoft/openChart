# Interpreter-Inclusive Video — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Adds an authorized interpreter as a distinct, privacy-governed participant in a virtual visit.
Topics: openchart-feature-catalog, telehealth, frappe, video-interpretation
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-009 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Interpreter service handoff** — Request and connect an external language-service interpreter through a governed adapter.

## Focus

This feature isolates three-way virtual participation and interpreter-specific authority, presence, and documentation.

## Behavior

- Staff invite a qualified interpreter for the requested language and visit interval.
- The interpreter receives a role-specific, single-use link that reveals only minimum scheduling and identity information.
- Patient admission and interpreter admission are independent so staff can stage introductions appropriately.
- The console identifies the interpreter visibly and supports leave, remove, and reconnect without ending the visit.
- The encounter records language, interpreter identity or service identifier, modality, and participation interval.
- An unavailable interpreter routes to staff escalation or rescheduling policy; it never silently substitutes an unqualified participant.

## Frappe realization

- **DocTypes:** `OC Interpreter Participation` links the virtual visit, language, interpreter or vendor reference, qualification evidence, invitation, and presence intervals.
- **Workflow/API:** Requested, Confirmed, Waiting, Admitted, Completed, and Unavailable states use guarded invite and admit methods plus Notification delivery.
- **Roles/permissions:** Interpreter can access only their assigned room and no chart by default; Clinician documents service use; Language Access Coordinator manages assignments.

## Boundaries

Owns: interpreter invitation and session participation. Consumes: language need and qualification source. Emits: participation evidence. Does not own: interpreter credentialing or translation of the clinical record.

## Open questions

- Must custom WebRTC and partner embeds support the same interpreter controls before either is considered equivalent?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
