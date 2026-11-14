# Referral Directory With Specialty And Insurance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains searchable referral destinations with specialties, locations, accepted coverage, access notes, and verification dates.
Topics: openchart-feature-catalog, care-coordination, frappe, referral-directory
Repository context: openChart — Frappe v15 native EMR; catalog entry CAR-025 (Care Plans Coordination Referrals And Transitions)
Captured: 2026-08-24

## Possible feats

- **Referral Directory With Specialty And Insurance quality review** — Add a governed review report that compares timeliness, exceptions, and outcomes without changing clinical decisions automatically.

## Focus

This feature isolates one capability: maintains searchable referral destinations with specialties, locations, accepted coverage, access notes, and verification dates. It keeps the accountable workflow independently reviewable rather than hiding it inside a broad coordination record.

## Behavior

- Referral Coordinator and Directory Steward may create or act on the record only within patient, facility, and program user permissions.
- The record captures organization, services, specialties, locations, coverage claims, verification date; required inputs are validated before the first accountable transition.
- The supported lifecycle is `Draft > Verified > Active > Needs Reverification > Inactive`; invalid or stale transitions return a structured conflict and leave accepted state unchanged.
- Every transition records actor, role, timestamp, source, reason, and predecessor so corrections supersede accepted evidence instead of rewriting it.
- Assignment or notification automation proposes and routes work, but an authorized human remains responsible for clinical interpretation and action.
- Missing consent, identity ambiguity, inaccessible attachments, or an ineligible assignee routes the item to review rather than silently continuing.
- Patients and proxies see only explicitly publishable, minimum-necessary fields under current consent and proxy authority.
- Completion emits an auditable coordination event and leaves downstream systems to accept or reject the handoff under their own authority.

## Frappe realization

- **DocTypes:** `OC Referral Destination` uses naming series `OC-CAR-.YYYY.-.#####` with Link fields for patient and source records, explicit state/date fields, child tables where repeated evidence applies, and Attach fields with provenance.
- **Workflow:** a Frappe Workflow enforces `Draft > Verified > Active > Needs Reverification > Inactive` with transition conditions, rejection reasons, and succession-based amendments for accepted clinical records.
- **Roles and permissions:** Referral Coordinator and Directory Steward receive least-privilege DocPerms at permlevels 0-2; patient, facility, program, and assignee user permissions constrain rows and sensitive fields.
- **Hooks and automation:** `validate` checks required authority and chronology, `on_update` emits idempotent events, `scheduler_events` opens due review work, and background jobs retry only safe delivery operations.
- **API:** guarded `open_chart.api.v1.care_coordination` whitelisted methods are the supported write surface; `/api/resource/OC%20Referral%20Destination` remains read-only for integrations without explicit direct-write authority.
- **Surfaces:** Desk directory, portal-safe search method, auto-repeat verification tasks, and Query Report; comments and the activity feed expose review history without substituting for structured state.

## Boundaries

Owns: the referral directory with specialty and insurance coordination record, its state, assignments, and evidence. Consumes: authorized patient identity, consent, accepted clinical records, care-team authority, and external acknowledgements. Emits: versioned coordination events, human work items, notifications, and reviewable status. Does not own: diagnosis, prescribing, payer adjudication, appointment capacity, vendor fulfillment, or autonomous clinical action.

## Open questions

- Which transitions and evidence in referral directory with specialty and insurance require dual review, patient acknowledgement, or an explicitly documented exception?

## Relationships

[Synthesis: Care Plans Coordination Referrals And Transitions](openchart-feature-catalog-synthesis-car.md) · [Internal And External Referral Routing](openchart-feature-catalog-car-024-internal-external-referral-routing.md) · [Referral Status Lifecycle](openchart-feature-catalog-car-026-referral-status-lifecycle.md)
