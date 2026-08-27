# Opt-in Usability Telemetry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Collects consented, minimized interaction metrics and accessibility friction signals to feed a governed UX backlog without capturing clinical content.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, usability-telemetry
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-030 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **UX evidence review board** — Combine telemetry trends, support reports, and accessibility defects into a prioritized human-reviewed backlog.

## Focus

This feature isolates privacy-minimized usability measurement under explicit site and user choice.

## Behavior

- Site administrators enable telemetry only after configuring purpose, retention, allowed event classes, and notice text.
- Users see whether telemetry is active and may opt in or out where policy requires or permits individual choice.
- Events use approved route, component, action, duration bucket, error code, accessibility mode, and outcome fields without free text or clinical values.
- Patient identifiers, record names, search terms, note content, field values, and raw URLs are rejected at ingestion.
- Small cohorts and rare combinations are suppressed in reports to reduce re-identification risk.
- UX reviewers create backlog candidates from trends, recording evidence, owner, decision, and whether a change was accepted.
- Disabling collection stops new events immediately; retention jobs delete expired event detail and preserve only approved aggregates.

## Frappe realization

- **DocTypes:** `OC Usability Telemetry Policy` stores purpose, event allowlist, consent mode, retention, suppression threshold, and state; `OC UX Backlog Candidate` stores reviewed findings.
- **Ingestion:** `open_chart.api.v1.ux.telemetry.record` accepts only a typed allowlist, strips identifiers, rate-limits sessions, and writes through background jobs.
- **Preferences and bootinfo:** Site policy and user opt state resolve into a boolean collection capability in bootinfo; no collection script initializes when false.
- **Reports and jobs:** Aggregated Query/Script Reports expose trends by permitted dimensions; `scheduler_events` enforces retention and minimum-cohort suppression.

## Boundaries

Owns: consented usability events, minimization, retention, aggregation, and UX backlog handoff. Consumes: site policy, user choice, approved component IDs, and non-content outcomes. Emits: suppressed aggregate evidence and backlog candidates. Does not own: clinical surveillance, workforce performance scoring, marketing analytics, or autonomous prioritization.

## Open questions

- Should clinician telemetry require individual opt-in even where organizational policy could legally authorize collection?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Screen-reader Component Conformance](openchart-feature-catalog-iax-008-screen-reader-component-conformance.md)
