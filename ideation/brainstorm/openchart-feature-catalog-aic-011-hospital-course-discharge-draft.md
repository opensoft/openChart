# Hospital Course And Discharge Draft — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assembles a source-cited hospital-course and discharge-summary draft from accepted structured records for clinician completion.
Topics: openchart-feature-catalog, clinical-ai, frappe, discharge-drafting
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-011 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Unresolved-discharge checklist** — Surface missing reconciliation, follow-up, and pending-result inputs beside the draft.

## Focus

This feature isolates inpatient course synthesis and discharge drafting while preserving accountable authorship.

## Behavior

- A qualified clinician requests a draft for one admission using selected accepted notes, orders, administrations, results, procedures, and disposition data.
- The output separates admission reason, major events, procedures, response, complications, pending items, and follow-up with citations.
- Conflicting dates, medication lists, or disposition instructions appear as unresolved issues rather than reconciled guesses.
- The clinician edits and attests each required section before the draft can enter the ordinary discharge-note signature path.
- Generation cannot discharge a patient, place orders, reconcile medications, or send instructions.
- New material events mark an unaccepted draft stale.

## Frappe realization

- **DocTypes:** `OC AI Discharge Draft` links admission, source snapshot, artifact, section attestations, unresolved-item child table, and destination note.
- **Workflow:** Requested → Generating → Pending Review → Ready For Signature/Rejected/Stale.
- **Roles/permissions:** assigned inpatient clinicians review; discharge authority remains on the destination workflow.
- **Hooks/jobs/surfaces:** rq assembly job; admission-record hooks stale drafts; Desk discharge workspace presents citations, conflicts, and required attestations.

## Boundaries

Owns: hospital-course draft assembly and review evidence. Consumes: accepted admission records. Emits: clinician-completed note candidate. Does not own: discharge authority, medication reconciliation, orders, or patient communication.

## Open questions

- Which events should immediately stale a draft versus append a visible post-generation update?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Documentation-Gap Nudges](openchart-feature-catalog-aic-015-documentation-gap-nudges.md)
