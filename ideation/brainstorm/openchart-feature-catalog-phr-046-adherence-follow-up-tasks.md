# Adherence Follow-Up Tasks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates assigned, time-bounded follow-up tasks from documented medication access or taking concerns without inferring nonadherence automatically.
Topics: openchart-feature-catalog, eprescribing, frappe, adherence-follow-up
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-046 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Barrier-specific resource routing** — Reviewed task templates could connect cost, transportation, literacy, or adverse-effect concerns to appropriate staff.

## Focus

This feature isolates operational follow-up after a person or authorized workflow records an adherence concern. Signals remain hypotheses until a patient or clinician supplies evidence.

## Behavior

- A clinician, pharmacist, patient request, or configured workflow can propose a follow-up with source and reason.
- Reasons distinguish access, cost, understanding, side effects, forgetfulness, supply, preference, and unknown barriers.
- A human reviewer confirms task appropriateness, assignee, due date, contact channel, and sensitive-communication constraints.
- The assignee records attempts, patient-reported information, education, escalation, and outcome.
- Missed fill or status data may prompt review but cannot label a patient nonadherent by itself.
- Completion links any accepted medication-statement update through its governed API rather than rewriting source records.

## Frappe realization

- **DocTypes:** `OC Medication Follow-Up` stores source Dynamic Link, reason, hypothesis status, assignment, contacts, outcome, and linked successors.
- **Workflow:** Proposed → Reviewed → Assigned → In Progress → Completed/Unable to Reach/Escalated.
- **Roles:** Pharmacists, clinical support, and care coordinators receive scoped tasks; portal responses remain patient-reported.
- **Surfaces/hooks:** Assignment Rules, Notifications, due-date reports, and patient timeline links expose accountable follow-up.

## Boundaries

Owns: follow-up task lifecycle and documented outcome. Consumes: human concerns and reviewable operational signals. Emits: contact evidence, escalation, and optional reconciliation referrals. Does not own: adherence inference, diagnosis, or autonomous outreach decisions.

## Open questions

- Which operational signals may propose a task without creating stigmatizing or excessive outreach?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Medication Synchronization Programs](openchart-feature-catalog-phr-045-medication-synchronization-programs.md)
