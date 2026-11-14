# Work School and DME Letters — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates reviewed patient letters from governed templates and encounter facts with purpose-specific disclosure controls.
Topics: openchart-feature-catalog, clinical-documentation, frappe, clinical-letters
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-050 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Verification codes** — Could let recipients validate document authenticity.

## Focus

Generates reviewed patient letters from governed templates and encounter facts with purpose-specific disclosure controls. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician or authorized delegate may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires letter purpose, patient, encounter, template, approved facts, recipient, and expiration.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft record; validation failure creates no accepted clinical content.
- **Transitions:** Draft → Clinician Review → Signed → Released or Revoked. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a signed, versioned letter and printable PDF with disclosure provenance; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Clinical Letter` is a submittable clinical DocType with naming series `OC-.#####`; key fields are patient, encounter, purpose, template_version, recipient, body, signer, expires_on.
- **Workflow:** Frappe Workflow implements Draft → Clinician Review → Signed → Released or Revoked. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Clinical Assistant` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Letter template client script, Letter Head, Jinja Print Format, and portal delivery; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
