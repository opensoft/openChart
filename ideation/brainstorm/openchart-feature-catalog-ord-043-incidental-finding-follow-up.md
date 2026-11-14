# Incidental Finding Follow-Up — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Registers incidental findings as explicit follow-up obligations with recommendation, owner, deadline, and closure evidence.
Topics: openchart-feature-catalog, cpoe, frappe, incidental-findings
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-043 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Recommendation extraction draft** — Let NLP propose finding text and interval for clinician verification before registration.

## Focus

This feature isolates longitudinal accountability for findings outside the original diagnostic question.

## Behavior

- A clinician or qualified reviewer registers finding text, source result/version, recommendation, urgency, target interval, and owner.
- Machine-extracted candidates remain drafts until a human verifies every field.
- The owner chooses a plan, documents patient communication, and links resulting orders or referrals.
- Deferral, refusal, unreachable status, and transfer require reason and next review date where applicable.
- Completion requires evidence matched to the registered recommendation or a documented clinical disposition.
- Overdue items appear in dedicated worklists and use the result escalation ladder.

## Frappe realization

- **DocTypes:** `OC Incidental Finding` with source result, finding, recommendation, verified_by, owner, due_at, state, provenance, and linked actions.
- **Workflow:** Candidate → Verified → Planned → In Follow-Up → Completed, Deferred, Declined, or Escalated.
- **Roles/permissions:** qualified clinicians verify; assigned owners manage follow-up; draft AI service identity cannot transition Candidate.
- **Hooks/API/surface:** guarded verify/complete methods, scheduler escalation, and REST filters by owner/state/due range provide an incidental-findings worklist.

## Boundaries

Owns: incidental-finding obligation and closure evidence. Consumes: exact result version and human verification. Emits: longitudinal follow-up tasks. Does not own: source interpretation or autonomous extraction acceptance.

## Open questions

- Which roles may verify machine-proposed incidental findings?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Follow-Up Deadline](openchart-feature-catalog-ord-039-result-follow-up-deadline.md)
