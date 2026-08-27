# Encounter Interpreter Workflow Flags — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Carries interpreter need, modality, language, and completion evidence through an encounter without claiming the interpreter service itself.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, interpreter-workflow
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-006 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Interpreter delay measure** — Report how often requested support is unavailable or delays care by setting and language.

## Focus

This feature isolates encounter-level interpreter coordination flags and evidence from scheduling and vendor fulfillment.

## Behavior

- Authorized staff set required language, need status, preferred modality, and special communication needs for an encounter.
- Flags move through Not Assessed, Requested, Arranged, Present, Declined, Unavailable, and Completed states.
- The encounter header and relevant worklists show a text-and-icon status that does not rely on color alone.
- Starting documentation with a Required but not Present flag prompts for a safe disposition without blocking emergency care.
- Completion records interpreter identifier or service reference, modality, start/end times, and who attested participation.
- Declined or unavailable outcomes require a reason and may create an assigned follow-up task under site policy.
- Amendments supersede accepted evidence and preserve the original event history.

## Frappe realization

- **DocTypes:** `OC Encounter Interpreter Need` stores encounter, patient, language, modality, status, external reference, timing, attestation, and successor.
- **Workflow:** A Frappe Workflow enforces state transitions; Clinical Staff, Front Desk, Interpreter Coordinator, and Audit Reviewer roles receive scoped DocPerms.
- **Hooks and surfaces:** Encounter `after_insert` seeds an assessment task; client scripts show flags in Desk forms and a Query Report lists unresolved needs.
- **API:** Guarded methods under `open_chart.api.v1.ux.interpreter` accept state transitions and emit realtime worklist updates with audit correlation IDs.

## Boundaries

Owns: encounter interpreter need and participation evidence. Consumes: patient language preference, encounter identity, and external service outcomes. Emits: visible flags, tasks, and audit events. Does not own: interpreter scheduling, contracting, identity proofing, or clinical consent.

## Open questions

- Which encounter types require an explicit interpreter assessment before routine documentation can close?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Patient Language Preference Rendering](openchart-feature-catalog-iax-005-patient-language-preference-rendering.md)
