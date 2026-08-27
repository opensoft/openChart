# Reminder Effectiveness Analytics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures delivery-to-action conversion for reminder programs with attributable, privacy-aware denominators and uncertainty.
Topics: openchart-feature-catalog, messaging-tasks, frappe, reminder-analytics
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-020 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Cadence comparison workspace** — Compare approved timing variants after accounting for audience and deliverability differences.

## Focus

This feature isolates reminder outcome measurement so delivery, engagement, and the intended patient action remain separate observable stages.

## Behavior

- Analysts select reminder purpose, cohort period, policy versions, facilities, and allowed stratifiers.
- The funnel distinguishes eligible, planned, attempted, delivered, engaged, action completed, and attribution unknown.
- Action linkage uses purpose-specific windows and source-event identifiers rather than temporal coincidence alone.
- Multiple touches receive a documented attribution model and retain uncertainty.
- Opt-outs, unreachable patients, cancellations, and missing outcome feeds remain visible in denominators.
- Small-cell suppression and role-based filters protect sensitive subgroups.
- Dashboards show trends and confidence context without recommending autonomous patient-level action.
- Metric definitions and policy versions accompany exports for reproducibility.

## Frappe realization

- **DocTypes:** `OC Reminder Metric Definition` and `OC Reminder Attribution Snapshot` store funnel rules, windows, dimensions, counts, suppression, and source versions.
- **Automation:** `scheduler_events` runs bounded aggregate refresh jobs; late delivery/action events trigger idempotent recomputation windows.
- **Surfaces:** Script Reports, Dashboard Charts, Number Cards, and downloadable de-identified aggregates.
- **Permissions:** Communications Analyst sees approved aggregates; Privacy Reviewer governs dimensions; patient-level drilldown requires operational authority.
- **Audit:** report parameters and exports are logged with definition version and actor.

## Boundaries

Owns: reminder funnel definitions, attribution, and aggregate reporting. Consumes: reminder, delivery, engagement, and action events. Emits: effectiveness metrics. Does not own: patient eligibility, clinical outcomes, or campaign policy changes.

## Open questions

- Which attribution model is acceptable when several channels precede one action?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Reminder Cadence Engine](openchart-feature-catalog-msg-019-reminder-cadence-engine.md)
