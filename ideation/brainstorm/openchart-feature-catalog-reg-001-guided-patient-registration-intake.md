# Guided Patient Registration Intake — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Guides registration staff through a resumable intake that creates a reviewable patient identity record without bypassing provenance controls.
Topics: openchart-feature-catalog, registration, frappe, guided-intake
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-001 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Adaptive intake paths** — Show only sections required by age, setting, and visit type.

## Focus

Provide one coherent staff-led registration flow from identity search through readiness for care.

## Behavior

- Registration Clerk starts intake only after searching for an existing patient.
- The flow captures identity, demographics, contacts, relationships, coverage, and acknowledgments in ordered sections.
- A draft can be saved and resumed by its owner or reassigned with a reason.
- Required fields vary by configured clinic policy without hiding missing-data indicators.
- Submission validates duplicate candidates, authority, consent, and section completeness.
- Failed validation keeps the draft, identifies actionable errors, and never creates a partial patient silently.

## Frappe realization

- **DocTypes:** `OC Registration Intake` with patient, status, source, current_section, completeness, and child `OC Intake Section Status`; links accepted data to `OC Patient`.
- **Workflow:** Draft → In Progress → Ready for Review → Accepted or Needs Correction; only accepted intake may call patient creation.
- **Roles/permissions:** `OC Registration Clerk` owns drafts; `OC Registration Supervisor` reviews at permlevel 1; clinical roles have read-only access after acceptance.
- **API/surfaces:** guarded `open_chart.api.v1.registration.save_intake` and `.submit_intake`; Desk wizard, registration workspace, and resumable list view.

## Boundaries

Owns: intake orchestration and completeness. Consumes: clinic policy and captured registration facts. Emits: accepted intake provenance and patient-create request. Does not own: clinical assessment or billing adjudication.

## Open questions

- Which minimum identity fields permit an emergency placeholder intake?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
