# Abnormal Results Narrative — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Drafts a cited narrative of abnormal panel findings for qualified clinician interpretation and approval.
Topics: openchart-feature-catalog, clinical-ai, frappe, results-narrative
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-010 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Longitudinal trend paragraph** — Add a reviewer-selectable description of materially changing values across prior panels.

## Focus

This feature isolates narrative drafting from discrete abnormal results without allowing the model to diagnose or notify patients.

## Behavior

- A clinician selects one or more finalized panels and requests a narrative against a governed profile.
- The draft names abnormal values, units, reference ranges, trend context, and source timestamps with direct citations.
- It distinguishes laboratory flags from clinician interpretation and labels unavailable comparisons.
- Critical values retain their existing acknowledgment workflow and are never downgraded by prose.
- The reviewer edits, accepts, or rejects the draft; acceptance creates only candidate documentation.
- Corrected or amended results mark prior narratives stale and require fresh human review.

## Frappe realization

- **DocTypes:** `OC AI Result Narrative` links result versions, artifact, profile, reviewer, staleness state, and destination note/message draft.
- **Workflow:** Requested → Ready → Pending Interpretation → Accepted/Rejected/Stale.
- **Roles/permissions:** `OC Result Reviewer` or qualified clinician may accept; result access controls carry into source citations.
- **Hooks/jobs/surfaces:** result `on_update` stales affected drafts; rq generates narratives; Script Report lists unreviewed and stale drafts; client view renders value citations.

## Boundaries

Owns: abnormal-result narrative draft and staleness. Consumes: finalized result versions and reference metadata. Emits: human-review candidate prose. Does not own: result interpretation, critical-result routing, diagnosis, or patient notification.

## Open questions

- Which corrected-result events should retract versus merely stale an accepted narrative?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Explainability And Input Panel](openchart-feature-catalog-aic-038-explainability-and-input-panel.md)
