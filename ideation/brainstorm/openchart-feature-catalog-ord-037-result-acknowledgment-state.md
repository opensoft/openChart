# Result Acknowledgment State — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records explicit clinician review and disposition of a result without conflating inbox opening with acknowledgment.
Topics: openchart-feature-catalog, cpoe, frappe, result-acknowledgment
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-037 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Disposition shortcuts** — Offer governed phrases that still require clinician confirmation and editable context.

## Focus

This feature isolates meaningful acknowledgment as a clinical accountability action.

## Behavior

- Opening or previewing a result marks it viewed but never acknowledged.
- An eligible clinician chooses a disposition such as reviewed-no-action, follow-up ordered, patient contact needed, or transferred.
- Required notes or follow-up links vary by result priority and policy.
- Acknowledgment binds identity, timestamp, result version, and displayed abnormality context.
- Corrected results may reopen the state while retaining prior acknowledgment.
- Automated agents and integration users cannot perform clinical acknowledgment.

## Frappe realization

- **DocTypes:** submitted `OC Result Acknowledgment` with accountability, result_version, disposition, note, actor, acknowledged_at, and follow-up links.
- **Workflow:** accountability Assigned → Reviewed → Completed or Follow-Up Pending; corrected results transition to Reopened.
- **Roles/permissions:** accountable clinicians or credentialed covering users acknowledge; service accounts are explicitly denied.
- **Hooks/API/surface:** guarded `acknowledge_result` verifies owner eligibility and current version; filtered REST worklists exclude completed items but preserve audit views.

## Boundaries

Owns: review disposition evidence. Consumes: assigned accountability and exact result version. Emits: acknowledgment and next-step state. Does not own: result viewing telemetry or follow-up execution.

## Open questions

- Which dispositions require a linked follow-up artifact before completion?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Critical Result Acknowledgment Evidence](openchart-feature-catalog-ord-040-critical-result-acknowledgment-evidence.md)
