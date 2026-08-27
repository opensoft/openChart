# Promoting Interoperability Objectives Status — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks objective-level evidence, exclusions, numerator and denominator progress, and attestation readiness for Promoting Interoperability reporting.
Topics: openchart-feature-catalog, quality-reporting, frappe, promoting-interoperability
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-008 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Evidence freshness monitor** — Warn when screenshots, logs, or security-analysis evidence no longer cover the attestation period.

## Focus

Explainable objective tracking that combines calculated events with reviewed documentary evidence and explicit exclusions.

## Behavior

- Administrators configure applicable objectives, measures, thresholds, reporting period, and evidence owners.
- Objective status is not-started, collecting, at-risk, met, excluded, failed, or attestation-ready.
- Calculated measures link to event counts and patient-level samples where permission allows.
- Manual evidence requires source, period coverage, attachment hash, reviewer, and approval date.
- Exclusions capture authoritative criterion, rationale, approver, and supporting evidence.
- Threshold or evidence failures identify the unresolved condition and responsible owner.
- Locking an attestation snapshot prevents silent evidence replacement and records successors separately.

## Frappe realization

- **DocTypes:** Add `OC PI Objective Status`, child `OC PI Evidence`, and `OC PI Attestation Snapshot` with objective version, counts, threshold, exclusion, Attach, and hash fields.
- **Workflow:** Use collecting, review, at-risk, met/excluded, approved, and superseded states with `OC Compliance Officer` approval.
- **Jobs and API:** Schedule event aggregation and expose read-only objective detail plus guarded evidence submission methods.
- **Surfaces:** Deliver objective Number Cards, a traffic-light Script Report, evidence Print Format, and due-date Notifications.

## Boundaries

Owns: objective tracking and local attestation evidence. Consumes: approved program rules, system events, security evidence, and participation scope. Emits: readiness snapshots and exceptions. Does not own: legal attestation, external audits, or interoperability event generation.

## Open questions

- Which system events must be retained as patient-level evidence versus aggregate counters?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
