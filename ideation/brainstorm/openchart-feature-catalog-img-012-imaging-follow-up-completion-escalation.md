# Imaging Follow-up Completion and Escalation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks recommended imaging follow-up from due-date calculation through scheduling, completion, exception review, and accountable escalation.
Topics: openchart-feature-catalog, imaging, frappe, follow-up-tracking
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-012 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Barrier coding** — Aggregate patient, access, authorization, and clinical reasons that delay follow-up.

## Focus

This feature isolates the closed-loop operational lifecycle for an accepted imaging recommendation.

## Behavior

- A verified recommendation creates a follow-up episode with target window, responsible owner, and evidence requirements.
- Coordinators can record outreach, patient response, booking, external completion, contraindication, refusal, or clinical deferral.
- Completion requires linkage to an accepted result or reviewed external evidence, not appointment status alone.
- Upcoming, due, and overdue states derive from the accepted due window and configured grace policy.
- Escalations create assignments and notifications while leaving clinical disposition to authorized humans.
- Closure reasons remain reportable and corrections preserve the original timeline.

## Frappe realization

- **DocTypes:** `OC Imaging Follow Up` with child outreach events, due window, completion evidence Links, barrier codes, and closure reason.
- **Workflow:** Open → Outreach → Scheduled → Evidence Review → Completed, with Overdue, Deferred, Refused, and Exception Review states.
- **Roles/permissions:** follow-up coordinators manage operations; responsible clinicians approve clinical deferral or exception closure; patients have scoped portal visibility.
- **Hooks/API/surfaces:** daily scheduler updates due states and assignments; guarded evidence methods close episodes; dashboards show aging and closure quality.

## Boundaries

Owns: follow-up episode, due state, outreach evidence, and closure. Consumes: recommendation, scheduling, result, and external evidence. Emits: tasks, escalations, and completion status. Does not own: clinical treatment decisions.

## Open questions

- How should due windows change when a clinician accepts a revised recommendation?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
