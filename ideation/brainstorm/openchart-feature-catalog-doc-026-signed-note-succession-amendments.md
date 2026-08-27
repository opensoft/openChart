# Signed Note Succession Amendments — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Corrects an accepted note by creating a traceable successor rather than editing the signed record in place.
Topics: openchart-feature-catalog, clinical-documentation, frappe, note-amendment
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-026 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **A correction notice** — Could route to prior recipients of the superseded note.

## Focus

Corrects an accepted note by creating a traceable successor rather than editing the signed record in place. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Authorized amending clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires accepted note, amendment reason, copied source content, and corrected content.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable accepted original record; validation failure creates no accepted clinical content.
- **Transitions:** Accepted Original → Superseded; Successor Draft → Review → Accepted. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a newly accepted successor linked bidirectionally to the superseded note; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Clinical Note` is a submittable clinical DocType with naming series `OC-.#####`; key fields are supersedes, amendment_reason, source_hash, accepted_at, author, content.
- **Workflow:** Frappe Workflow implements Accepted Original → Superseded; Successor Draft → Review → Accepted. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Clinical Supervisor`, `OC Health Information Manager` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Amend API in open_chart.api.v1, compare view, and succession-aware print format; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
