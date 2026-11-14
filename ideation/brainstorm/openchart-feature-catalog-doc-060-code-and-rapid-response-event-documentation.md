# Code and Rapid Response Event Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures a synchronized timeline of emergency response participants, interventions, observations, and outcomes.
Topics: openchart-feature-catalog, clinical-documentation, frappe, emergency-event
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-060 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Role-specific timers** — Could improve completeness during active response.

## Focus

Captures a synchronized timeline of emergency response participants, interventions, observations, and outcomes. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Designated recorder and response team may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires event type, onset, responders, timestamped actions, medications, rhythms, and outcome.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable active recording record; validation failure creates no accepted clinical content.
- **Transitions:** Active Recording → Team Review → Signed; late entries remain explicitly labeled. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a locked event record with late-entry and correction provenance; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Clinical Emergency Event` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, event_type, activated_at, recorder, timeline_table, outcome, ended_at.
- **Workflow:** Frappe Workflow implements Active Recording → Team Review → Signed; late entries remain explicitly labeled. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Emergency Recorder`, `OC Clinician`, `OC Nurse` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Realtime event client, websocket updates, event Print Format, and review queue; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
