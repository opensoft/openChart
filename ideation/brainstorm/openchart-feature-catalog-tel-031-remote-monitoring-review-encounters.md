# Remote Monitoring Review Encounters — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates accountable clinician review encounters for bounded sets of remote-monitoring observations and resulting actions.
Topics: openchart-feature-catalog, telehealth, frappe, remote-monitoring-review
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-031 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Review workload queue** — Group due monitoring reviews by program, urgency signal, and accountable care team.

## Focus

This feature isolates human review and documentation of remote-monitoring data, not device ingestion or autonomous alerting.

## Behavior

- A program or clinician opens a review window with patient, metric set, time range, reason, and accountable reviewer.
- The encounter snapshots the observation identifiers and data-quality status included in the review.
- The reviewer records trends considered, data limitations, patient contact, assessment, and human-selected next action.
- Missing, stale, implausible, or duplicate data is visibly qualified and never treated as absent clinical risk automatically.
- The reviewer may request contact, order follow-up, continue monitoring, escalate, or close with rationale.
- Corrections preserve the original accepted review through succession and retain observation provenance.

## Frappe realization

- **DocTypes/workflow:** `OC Monitoring Review Encounter` and child `OC Reviewed Observation Reference` use Due, Assigned, In Review, Awaiting Contact, Completed, and Escalated states.
- **Automation:** scheduler events may create due review assignments from governed program cadence; no threshold autonomously completes a clinical disposition.
- **Surfaces/permissions:** Clinician worklist, trend dashboard, and signed Print Format use patient and program user permissions; Patient sees only released review summaries.

## Boundaries

Owns: bounded human review encounter and disposition evidence. Consumes: remote observations and program cadence. Emits: signed review and selected follow-up. Does not own: device ingestion, alert algorithms, or monitoring enrollment.

## Open questions

- What event or cadence should define a billable versus nonbillable monitoring review without placing billing policy in openChart?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
