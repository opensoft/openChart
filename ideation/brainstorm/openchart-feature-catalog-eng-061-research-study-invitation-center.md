# Research Study Invitation Center — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents approved study invitations and captures interest or decline without enrolling the patient automatically.
Topics: openchart-feature-catalog, patient-engagement, frappe, research-invitations
Repository context: openChart — Frappe v15 native EMR; catalog entry ENG-061 (Patient Portal Engagement Consent And Proxy Access)
Captured: 2026-08-24

## Possible feats

- **Companion capability** — Patients can maintain broad preferences for future study contact.

## Focus

Presents approved study invitations and captures interest or decline without enrolling the patient automatically. This feature isolates that portal capability from clinical, financial, identity, and communication systems that remain authoritative for their own records.

## Behavior

- **Actors:** patient and research coordinator use an authenticated portal or restricted desk work queue appropriate to their role.
- **Inputs:** The interaction accepts study summary, eligibility source, approval identifier, contact permission, response, and expiry.
- **Outcome:** A successful action produces an interested, declined, expired, withdrawn, or contacted invitation state and a patient-readable receipt or status.
- **States:** The governed lifecycle is Prepared, Published, Viewed, Interested, Declined, Expired, Withdrawn; only server-validated transitions are accepted.
- **Authority:** Patient and Proxy User portal roles are distinct from desk roles, and proxy actions recheck patient, scope, purpose, and effective dates.
- **Safety:** Interest is not consent, eligibility, or enrollment, and care teams cannot see responses unless policy permits.
- **Concurrency:** Stale versions, duplicate submissions, revoked authority, or conflicting accepted records return structured errors and never silently overwrite state.
- **Accessibility:** The portal preserves language choice, keyboard access, responsive layout, and equivalent nonvisual status and error text.
- **Audit:** Every protected view, attempted action, transition, notification, override, and denial enters the clinical audit trail with actor capacity, source, policy version, and correlation ID.

## Frappe realization

- **DocTypes:** OC Research Invitation stores patient, portal_user, actor_capacity, status, policy_version, source, correlation_id, and feature-specific Links, child tables, Attach fields, or JSON only where structured fields cannot represent the payload.
- **Workflow:** A Frappe Workflow enforces the listed lifecycle with explicit patient, staff-review, expiry, denial, and succession transitions; accepted evidence is amended by successor records rather than in-place edits.
- **Roles and permissions:** Patient and Proxy User receive owner or explicitly scoped portal read/write permissions; Engagement Staff, Engagement Manager, and Audit Reviewer are desk-only roles constrained by clinic User Permissions and permlevels 0-2.
- **Surfaces:** A Frappe portal page under www/engagement/research-study-invitation-center and a task-specific Frappe Web Form provide patient interaction; Website Theme supplies consistent language, responsive, focus, contrast, and error patterns, while a desk workspace exposes only assigned review work.
- **API and identity:** Guarded whitelisted methods under open_chart.api.v1.engagement.research_study_invitation_center are the supported mutation surface; OAuth2 sessions and scoped app tokens are reauthorized server-side, and direct clinical-record writes are rejected.
- **Automation and messaging:** validate, before_save, on_update, and scheduler_events enforce policy and expiries; RQ jobs, Frappe Email Notifications, SMS Notifications through SMS Settings, Notification Log, and realtime events deliver consent-aware updates idempotently.
- **Evidence and reports:** File attachments use private storage and versioning; a Query Report and document activity feed expose state and audit evidence, and Print Formats or PDFs render only fields authorized at retrieval time.

## Boundaries

Owns: the patient-facing request, projection, preference, or evidence state for Research Study Invitation Center. Consumes: authoritative patient identity, consent, proxy scope, clinic policy, clinical release state, and external service outcomes as applicable. Emits: an interested, declined, expired, withdrawn, or contacted invitation state, assignments, consent-aware notifications, and immutable audit events. Does not own: source clinical facts, diagnoses, orders, appointment authority, financial ledger, payment processing, legal identity adjudication, or autonomous clinical action.

## Open questions

- Which policy owner approves default rules, retention, exceptions, and patient-facing wording for Research Study Invitation Center across clinics and jurisdictions?

## Relationships

[Synthesis: Patient Portal Engagement And Proxy Access](openchart-feature-catalog-synthesis-eng.md)
