# Point-Of-Care Quality Gap Prompts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents governed care-gap prompts during an encounter with rationale, evidence, exclusions, and human-approved next actions.
Topics: openchart-feature-catalog, cpoe, frappe, care-gap-prompts
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-063 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Gap resolution bundle** — Offer reviewable documentation, order, and follow-up drafts appropriate to the selected disposition.

## Focus

This feature isolates encounter-time prompts for registered clinical quality gaps.

## Behavior

- Eligible prompts show measure or rule name, missing action, evidence, due context, exclusions, owner, and data freshness.
- Clinicians may address, defer, exclude with reason, mark already satisfied with evidence, or dismiss when permitted.
- Choosing an action creates a draft order or task and never submits it automatically.
- Unknown data and contradictory evidence are visible instead of treated as a confirmed gap.
- Resolved gaps update only after qualifying evidence is accepted.
- Prompt interactions retain rule version and disposition for governance review.

## Frappe realization

- **DocTypes:** `OC Care Gap` with patient, rule version, state, due_at, evidence links, exclusions, provenance, and disposition history.
- **Workflow:** Open → Addressed, Deferred, Excluded, Satisfied, or Needs Review.
- **Roles/permissions:** encounter clinicians act within scope; quality reviewers manage disputed evidence; service accounts cannot approve clinical dispositions.
- **Hooks/API/surface:** encounter load invokes allowlisted evaluation; accepted actions call ordinary draft APIs; REST filters expose unresolved gaps by owner and due date.

## Boundaries

Owns: point-of-care gap presentation and disposition evidence. Consumes: registered rules and authorized patient facts. Emits: human-approved drafts and gap state. Does not own: quality measure certification or autonomous care.

## Open questions

- Which gap dispositions require independent quality review?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Visit-Due Preventive Care Prompts](openchart-feature-catalog-ord-064-visit-due-preventive-care-prompts.md)
