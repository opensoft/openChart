# CDS Ownership And Review Lifecycle — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assigns accountable owners and independent reviewers to each CDS rule with periodic, event-driven, and emergency review paths.
Topics: openchart-feature-catalog, cpoe, frappe, cds-governance
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-047 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Trigger-based review intake** — Open review tasks when safety reports, formulary changes, or evidence updates affect a rule.

## Focus

This feature isolates accountable stewardship over the active life of a CDS rule.

## Behavior

- Every rule has a named clinical owner, technical steward, review interval, and escalation fallback.
- Review tasks present performance, overrides, incidents, evidence freshness, and pending changes.
- Reviewers record retain, revise, suspend, retire, or investigate dispositions with rationale.
- Authors cannot satisfy independent clinical approval for their own material changes.
- Emergency suspension immediately stops new firing but cannot delete historical evaluations.
- Overdue reviews are visible in governance worklists and escalate without auto-changing rule logic.

## Frappe realization

- **DocTypes:** `OC CDS Review Task` with rule version, owner, reviewers, due_at, trigger, evidence snapshot, and disposition.
- **Workflow:** Due → In Review → Completed or Escalated; emergency action can move rule Active → Suspended.
- **Roles/permissions:** `OC CDS Owner`, independent `OC CDS Reviewer`, and `OC CDS Safety Officer` have distinct transitions.
- **Scheduler/API/surface:** daily scheduler creates periodic tasks; incident hooks create event-driven tasks; REST filters and governance reports expose overdue work.

## Boundaries

Owns: rule stewardship, review tasks, and disposition evidence. Consumes: rule performance and evidence signals. Emits: governance decisions and change requests. Does not own: authoring or runtime override decisions.

## Open questions

- What performance thresholds should force review rather than merely inform it?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Override Analytics](openchart-feature-catalog-ord-055-cds-override-analytics.md)
