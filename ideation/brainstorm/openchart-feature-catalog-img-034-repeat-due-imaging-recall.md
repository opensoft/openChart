# Repeat-due Imaging Recall — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates and tracks repeat-imaging recall windows such as annual mammography from accepted recommendations and governed surveillance policies.
Topics: openchart-feature-catalog, imaging, frappe, imaging-recall
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-034 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Recall outreach cadence** — Coordinate consented reminders before and after the due window.

## Focus

This feature isolates recurring preventive or surveillance imaging demand distinct from one-time incidental follow-up.

## Behavior

- An accepted report, clinician decision, or governed screening policy creates a recall with target interval and due window.
- The record identifies the study family, laterality or anatomy, responsible program, patient communication basis, and source.
- New results reconcile against open recalls and require human review when multiple episodes could match.
- Due, overdue, deferred, declined, ineligible, and completed states remain reportable.
- Outreach respects consent, language, proxy, and channel policy and records every outcome.
- A changed interval supersedes the prior recall rather than rewriting its historical basis.

## Frappe realization

- **DocTypes:** `OC Imaging Recall` with source Dynamic Link, due rule, target window, outreach child rows, completion evidence, and succession.
- **Workflow:** Planned → Outreach Due → Scheduled → Completed, with Overdue, Deferred, Declined, and Ineligible states.
- **Roles/permissions:** screening coordinators manage; clinicians approve clinical deferrals; patients may view and request scheduling through the portal.
- **Hooks/API/surfaces:** daily scheduler advances due state; Notifications send consented outreach; Calendar and Query Reports show cohort status.

## Boundaries

Owns: repeat-imaging recall identity, due state, outreach, and completion linkage. Consumes: reports, policies, scheduling, consent, and results. Emits: scheduling demand and recall metrics. Does not own: screening-policy authorship or appointment supply.

## Open questions

- How should policy-driven recalls coexist with patient-specific clinician recommendations when intervals differ?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
