# Pre-Visit Chart Summary — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates a cited, time-bounded chart summary for clinician review before a scheduled encounter.
Topics: openchart-feature-catalog, clinical-ai, frappe, previsit-summary
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-007 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Change-since-last-visit view** — Contrast newly documented facts with the prior accepted summary.

## Focus

This feature isolates encounter-preparation summarization while keeping the longitudinal chart authoritative.

## Behavior

- An authorized clinician requests a summary for a patient, appointment, and approved specialty profile.
- The output separates active problems, medications, recent results, care gaps, recent encounters, and unresolved follow-up with source citations.
- Every section displays data-through time and unavailable or excluded source classes.
- Clinicians may refresh, annotate, accept for personal preparation, or discard the artifact.
- The summary never updates problem lists, reconciles medications, or closes care gaps.
- Missing permissions or source failures yield explicit partial-summary notices.

## Frappe realization

- **DocTypes:** `OC Previsit AI Summary` links appointment, patient, profile version, source snapshot, artifact, reviewer, and disposition.
- **Workflow:** Requested → Generating → Ready → Reviewed/Discarded/Expired.
- **Roles/permissions:** care-team user permissions restrict requests and views; service accounts receive no patient-list access outside queued jobs.
- **Jobs/API/surfaces:** rq job assembles permission-filtered context; `open_chart.api.v1.ai.request_previsit_summary`; appointment dashboard shortcut and Desk review page show citations.

## Boundaries

Owns: pre-visit summary request and review experience. Consumes: permissioned chart data and approved profile. Emits: cited, expiring preparation artifact. Does not own: source records, reconciliation, or clinical decisions.

## Open questions

- Should summaries be generated only on demand or precomputed for tomorrow's assigned schedules?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI-Assisted Chart-Prep Checklist](openchart-feature-catalog-aic-016-ai-assisted-chart-prep-checklist.md)
