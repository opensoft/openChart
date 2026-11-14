# Patient Record Correction Requests — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients identify disputed chart content and submit a correction or amendment request without editing the record.
Topics: openchart-feature-catalog, patient-engagement, frappe, record-correction
Repository context: openChart — Frappe v15 native EMR; catalog entry ENG-068 (Patient Portal Engagement Consent And Proxy Access)
Captured: 2026-08-24

## Possible feats

- **Companion capability** — Patients can attach a statement of disagreement to a denied request where policy allows.

## Focus

Lets patients identify disputed chart content and submit a correction or amendment request without editing the record. This feature isolates that portal capability from clinical, financial, identity, and communication systems that remain authoritative for their own records.

## Behavior

- **Actors:** patient, proxy, and health-information staff use an authenticated portal or restricted desk work queue appropriate to their role.
- **Inputs:** The interaction accepts record reference, disputed text or field, requested correction, rationale, and attachments.
- **Outcome:** A successful action produces a submitted, assigned, accepted, denied, amended, or appealed request and a patient-readable receipt or status.
- **States:** The governed lifecycle is Draft, Submitted, Assigned, Review, Accepted, Denied, Amended, Appealed; only server-validated transitions are accepted.
- **Authority:** Patient and Proxy User portal roles are distinct from desk roles, and proxy actions recheck patient, scope, purpose, and effective dates.
- **Safety:** The original accepted record remains intact; approved changes use succession and denial includes a patient-readable reason.
- **Concurrency:** Stale versions, duplicate submissions, revoked authority, or conflicting accepted records return structured errors and never silently overwrite state.
- **Accessibility:** The portal preserves language choice, keyboard access, responsive layout, and equivalent nonvisual status and error text.
- **Audit:** Every protected view, attempted action, transition, notification, override, and denial enters the clinical audit trail with actor capacity, source, policy version, and correlation ID.

## Frappe realization

- **DocTypes:** OC Record Correction Request stores patient, portal_user, actor_capacity, status, policy_version, source, correlation_id, and feature-specific Links, child tables, Attach fields, or JSON only where structured fields cannot represent the payload.
- **Workflow:** A Frappe Workflow enforces the listed lifecycle with explicit patient, staff-review, expiry, denial, and succession transitions; accepted evidence is amended by successor records rather than in-place edits.
- **Roles and permissions:** Patient and Proxy User receive owner or explicitly scoped portal read/write permissions; Engagement Staff, Engagement Manager, and Audit Reviewer are desk-only roles constrained by clinic User Permissions and permlevels 0-2.
- **Surfaces:** A Frappe portal page under www/engagement/patient-record-correction-requests and a task-specific Frappe Web Form provide patient interaction; Website Theme supplies consistent language, responsive, focus, contrast, and error patterns, while a desk workspace exposes only assigned review work.
- **API and identity:** Guarded whitelisted methods under open_chart.api.v1.engagement.patient_record_correction_requests are the supported mutation surface; OAuth2 sessions and scoped app tokens are reauthorized server-side, and direct clinical-record writes are rejected.
- **Automation and messaging:** validate, before_save, on_update, and scheduler_events enforce policy and expiries; RQ jobs, Frappe Email Notifications, SMS Notifications through SMS Settings, Notification Log, and realtime events deliver consent-aware updates idempotently.
- **Evidence and reports:** File attachments use private storage and versioning; a Query Report and document activity feed expose state and audit evidence, and Print Formats or PDFs render only fields authorized at retrieval time.

## Boundaries

Owns: the patient-facing request, projection, preference, or evidence state for Patient Record Correction Requests. Consumes: authoritative patient identity, consent, proxy scope, clinic policy, clinical release state, and external service outcomes as applicable. Emits: a submitted, assigned, accepted, denied, amended, or appealed request, assignments, consent-aware notifications, and immutable audit events. Does not own: source clinical facts, diagnoses, orders, appointment authority, financial ledger, payment processing, legal identity adjudication, or autonomous clinical action.

## Open questions

- Which policy owner approves default rules, retention, exceptions, and patient-facing wording for Patient Record Correction Requests across clinics and jurisdictions?

## Relationships

[Synthesis: Patient Portal Engagement And Proxy Access](openchart-feature-catalog-synthesis-eng.md)
