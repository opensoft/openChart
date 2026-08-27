# Order Set Approval And Publishing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces separated clinical review, approval, publication, and retirement authority for organization order sets.
Topics: openchart-feature-catalog, cpoe, frappe, order-set-approval
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-015 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Conditional approval matrix** — Require specialty, pharmacy, or safety approval according to set contents.

## Focus

This feature isolates the governance gates that make an authored order set available for care.

## Behavior

- A draft version enters clinical review only after structural validation succeeds.
- Required reviewers attest to content scope, evidence, and conflicts of interest.
- The author cannot satisfy independent approval requirements for their own version.
- Publication sets effective dates and atomically retires or schedules the predecessor as policy dictates.
- Rejection returns coded and free-text rationale to the author without deleting history.
- Emergency withdrawal immediately prevents new use while preserving prior provenance.

## Frappe realization

- **DocTypes:** `OC Order Set Review` records reviewer, discipline, decision, comments, identity, and timestamp against `OC Order Set`.
- **Workflow:** Draft → Clinical Review → Approved → Published → Retired or Withdrawn with role-gated transitions and Workflow Actions.
- **Roles/permissions:** distinct `OC Order Set Editor`, `OC Clinical Reviewer`, `OC Pharmacy Reviewer`, and `OC Order Set Publisher` roles.
- **Hooks/API/surface:** `validate` enforces reviewer matrix and separation of duties; Notifications and assignments drive reviews; guarded publish method performs atomic state changes.

## Boundaries

Owns: approval evidence and publication authority. Consumes: validated successor versions and governance policy. Emits: published or rejected state. Does not own: content authoring.

## Open questions

- What constitutes emergency withdrawal authority outside normal publisher roles?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Set Review Reminders](openchart-feature-catalog-ord-016-order-set-review-reminders.md)
