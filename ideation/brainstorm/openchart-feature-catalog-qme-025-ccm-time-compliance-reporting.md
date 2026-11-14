# Chronic Care Management Time Compliance Reporting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Reconciles chronic care management time, activity, consent, care-plan, and practitioner evidence into compliance-ready reports.
Topics: openchart-feature-catalog, quality-reporting, frappe, ccm-compliance
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-025 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Threshold risk forecast** — Identify episodes unlikely to meet documented time requirements before month end.

## Focus

Evidence-backed CCM compliance reporting without independently determining billing eligibility or creating charges.

## Behavior

- Authorized staff review monthly patient episodes with consent, qualifying conditions, care plan, assigned practitioner, and recorded activities.
- Time entries identify performer, date, duration, activity class, patient interaction, source, and concurrent-time policy.
- The report detects overlaps, duplicates, missing signatures, ineligible roles, absent consent, and incomplete care-plan evidence.
- Totals distinguish counted, excluded, disputed, and pending-review minutes with reasons.
- Corrections follow source activity amendment rules and trigger episode recalculation.
- A reviewer approves or withholds a compliance snapshot; approval does not create a claim.
- Reports preserve rule release, source cutoff, review evidence, and as-of status.

## Frappe realization

- **DocTypes:** Add `OC CCM Compliance Episode` and `OC Care Management Time Entry` with patient, month, performer, Duration, activity, source Link, count status, and succession fields.
- **Workflow:** Use collecting, exception, review, compliant, noncompliant, and superseded states with clinician/compliance approval.
- **Hooks and jobs:** Validate overlaps and role eligibility on entry acceptance; schedule monthly reconciliation and stale-state detection.
- **Surfaces:** Provide monthly Script Reports, exception queues, patient timeline links, and compliance Print Formats.

## Boundaries

Owns: CCM evidence aggregation and compliance snapshots. Consumes: consent, conditions, care plans, time activities, practitioner roles, and rule releases. Emits: reviewed compliance reports and exceptions. Does not own: coding, claims, payment, or care delivery.

## Open questions

- Which time-entry sources and concurrency rules should be supported in the first profile?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
