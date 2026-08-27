# Vendor Model Certification Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lists vendor and model versions with approved uses, certification status, evidence, restrictions, and review dates.
Topics: openchart-feature-catalog, clinical-ai, frappe, model-certification
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-033 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Evidence expiry calendar** — Notify owners before contracts, attestations, evaluations, or security reviews lapse.

## Focus

This feature isolates the catalog of externally supplied models and their evidence-backed eligibility.

## Behavior

- Governors register vendor, model family and exact version, intended capabilities, deployment regions, data terms, certifications, evaluations, and restrictions.
- Status applies to an exact version and use, not to a vendor brand broadly.
- Evidence items record issuer, scope, date, expiry, attachment or URL, reviewer, and verification result.
- Expired or withdrawn evidence creates a review task and may suspend affected use under policy.
- Clinicians can see plain-language certification and restriction status from AI output details.
- Listing never substitutes for local validation, fairness review, or human oversight.

## Frappe realization

- **DocTypes:** `OC AI Vendor`, `OC AI Model Version`, and child `OC AI Certification Evidence` store identity, uses, terms, scopes, dates, files, status, and review owner.
- **Workflow:** Proposed → Evidence Review → Approved With Restrictions/Approved/Rejected → Suspended/Retired.
- **Roles/permissions:** vendors have no direct write role; `OC AI Vendor Reviewer` curates evidence and `OC AI Governor` decides status.
- **Jobs/surfaces:** scheduler_events flags expiries; Workspace list, calendar, Dashboard, and output detail link display current evidence.

## Boundaries

Owns: model/version eligibility evidence and restrictions. Consumes: vendor assertions, independent evidence, and local evaluations. Emits: certification status for policy resolution. Does not own: external certification validity or activation.

## Open questions

- Which evidence types require independent verification rather than document receipt?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Clinical Model Validation Evidence](openchart-feature-catalog-aic-043-clinical-model-validation-evidence.md)
