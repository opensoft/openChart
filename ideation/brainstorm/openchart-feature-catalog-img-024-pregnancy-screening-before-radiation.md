# Pregnancy Screening Before Radiation Imaging — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records policy-governed pregnancy screening, uncertainty, testing evidence, and authorized exceptions before applicable CT, fluoroscopy, or radiographic studies.
Topics: openchart-feature-catalog, imaging, frappe, pregnancy-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-024 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Privacy-preserving intake** — Collect sensitive screening answers through a scoped patient or staff workflow.

## Focus

This feature isolates radiation-related pregnancy readiness while avoiding assumptions based on demographics alone.

## Behavior

- Applicable study policy prompts screening based on clinical context rather than a hard-coded sex or gender field.
- The reviewer records patient response, uncertainty, relevant dates, testing evidence, and source.
- Results are classified as Cleared, Review Required, Test Pending, Declined, or Exception Authorized.
- Sensitive details are minimized in broad worklists while the blocking state remains visible.
- New information or an expired screening window invalidates prior clearance.
- Urgent exceptions require an authorized clinician, reason, and communication evidence; the system does not decide risk autonomously.

## Frappe realization

- **DocTypes:** `OC Imaging Safety Check` subtype Pregnancy with protected fields at permlevel 1, evidence Links, policy version, and expiry.
- **Workflow:** Screening Due → Evidence Pending → Review Required → Cleared, with Declined and Exception Authorized states.
- **Roles/permissions:** trained technologists collect; authorized clinicians approve exceptions; minimum-necessary views hide sensitive answers.
- **Hooks/API/surfaces:** protocol readiness validates current screening; portal Web Form may collect scoped answers; audit records every disclosure and decision.

## Boundaries

Owns: imaging-specific screening evidence and readiness state. Consumes: patient response, testing evidence, study policy, and protocol. Emits: clearance or review requirement. Does not own: reproductive history, diagnosis, or treatment.

## Open questions

- Which screening details belong in the longitudinal chart versus the restricted imaging episode?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
