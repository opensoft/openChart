# Patient-Friendly Explanation Drafts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Drafts plain-language post-visit explanations from accepted encounter content for clinician review before release.
Topics: openchart-feature-catalog, clinical-ai, frappe, patient-explanations
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-008 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Reading-level variants** — Let reviewers compare approved-language drafts tuned to patient preference without changing clinical meaning.

## Focus

This feature isolates patient-facing explanation drafting and its release gate.

## Behavior

- A clinician selects accepted encounter facts, instructions, and results to include in a patient-friendly draft.
- The draft uses an approved language and reading-level profile and cites its clinical source sections internally.
- Medication, diagnosis, follow-up, and warning-sign statements are highlighted for reviewer confirmation.
- The clinician edits, approves, rejects, or returns the draft for regeneration.
- Only approved text can enter the ordinary patient-release workflow; generation never sends a portal message directly.
- Conflicting or incomplete source instructions block approval and identify the conflict.

## Frappe realization

- **DocTypes:** `OC Patient Explanation Draft` stores encounter Link, audience profile, language, artifact, selected source Links, reviewer edits, and release destination.
- **Workflow:** Draft Requested → Pending Review → Approved/Rejected → Released through destination workflow.
- **Roles/permissions:** treating clinicians review; `OC Patient Communications Reviewer` handles delegated review; patients see only released destination records.
- **Hooks/API/surfaces:** `validate` requires accepted sources; whitelisted generate/approve methods; Desk diff view and portal delivery remain separate surfaces.

## Boundaries

Owns: plain-language draft and approval evidence. Consumes: accepted clinical content and communication preferences. Emits: human-approved text to a release workflow. Does not own: source facts, translations, or autonomous patient advice.

## Open questions

- Which statement classes require verbatim clinician confirmation rather than general draft approval?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Patient-Facing Record Assistant](openchart-feature-catalog-aic-019-patient-facing-record-assistant.md)
