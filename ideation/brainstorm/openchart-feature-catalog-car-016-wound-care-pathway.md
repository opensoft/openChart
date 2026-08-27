# Wound Care Program Pathway — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates wound episodes through staged assessments, treatment tasks, measurements, images, and clinician review milestones.
Topics: openchart-feature-catalog, care-coordination, frappe, wound-care
Repository context: openChart — Frappe v15 native EMR; catalog entry CAR-016 (Care Plans Coordination Referrals And Transitions)
Captured: 2026-08-24

## Possible feats

- **Wound Care Program Pathway quality review** — Add a governed review report that compares timeliness, exceptions, and outcomes without changing clinical decisions automatically.

## Focus

This feature isolates one capability: coordinates wound episodes through staged assessments, treatment tasks, measurements, images, and clinician review milestones. It keeps the accountable workflow independently reviewable rather than hiding it inside a broad coordination record.

## Behavior

- Wound Clinician and Care Coordinator may create or act on the record only within patient, facility, and program user permissions.
- The record captures patient, wound site, pathway, measurements, image consent, review cadence; required inputs are validated before the first accountable transition.
- The supported lifecycle is `Open > Active Treatment > Healing > Healed or Escalated or Discontinued`; invalid or stale transitions return a structured conflict and leave accepted state unchanged.
- Every transition records actor, role, timestamp, source, reason, and predecessor so corrections supersede accepted evidence instead of rewriting it.
- Assignment or notification automation proposes and routes work, but an authorized human remains responsible for clinical interpretation and action.
- Missing consent, identity ambiguity, inaccessible attachments, or an ineligible assignee routes the item to review rather than silently continuing.
- Patients and proxies see only explicitly publishable, minimum-necessary fields under current consent and proxy authority.
- Completion emits an auditable coordination event and leaves downstream systems to accept or reject the handoff under their own authority.

## Frappe realization

- **DocTypes:** `OC Wound Care Episode` uses naming series `OC-CAR-.YYYY.-.#####` with Link fields for patient and source records, explicit state/date fields, child tables where repeated evidence applies, and Attach fields with provenance.
- **Workflow:** a Frappe Workflow enforces `Open > Active Treatment > Healing > Healed or Escalated or Discontinued` with transition conditions, rejection reasons, and succession-based amendments for accepted clinical records.
- **Roles and permissions:** Wound Clinician and Care Coordinator receive least-privilege DocPerms at permlevels 0-2; patient, facility, program, and assignee user permissions constrain rows and sensitive fields.
- **Hooks and automation:** `validate` checks required authority and chronology, `on_update` emits idempotent events, `scheduler_events` opens due review work, and background jobs retry only safe delivery operations.
- **API:** guarded `open_chart.api.v1.care_coordination` whitelisted methods are the supported write surface; `/api/resource/OC%20Wound%20Care%20Episode` remains read-only for integrations without explicit direct-write authority.
- **Surfaces:** Gantt pathway, image-aware form, Assignment Rules, and progress dashboard; comments and the activity feed expose review history without substituting for structured state.

## Boundaries

Owns: the wound care program pathway coordination record, its state, assignments, and evidence. Consumes: authorized patient identity, consent, accepted clinical records, care-team authority, and external acknowledgements. Emits: versioned coordination events, human work items, notifications, and reviewable status. Does not own: diagnosis, prescribing, payer adjudication, appointment capacity, vendor fulfillment, or autonomous clinical action.

## Open questions

- Which transitions and evidence in wound care program pathway require dual review, patient acknowledgement, or an explicitly documented exception?

## Relationships

[Synthesis: Care Plans Coordination Referrals And Transitions](openchart-feature-catalog-synthesis-car.md) · [COPD Management Program](openchart-feature-catalog-car-015-copd-management-program.md) · [Anticoagulation Program INR And Dosing Logs](openchart-feature-catalog-car-017-anticoagulation-program-inr-logs.md)
