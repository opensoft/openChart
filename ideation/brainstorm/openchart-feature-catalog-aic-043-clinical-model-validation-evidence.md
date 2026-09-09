# Clinical Model Validation Evidence — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Displays population, setting, endpoints, performance, limitations, approval, and expiry evidence beside every clinical risk model.
Topics: openchart-feature-catalog, clinical-ai, frappe, validation-evidence
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-043 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Local transportability review** — Compare deployment population and workflow with the model's validated population and intended use.

## Focus

This feature isolates validation evidence as a first-class runtime-visible object rather than buried release documentation.

## Behavior

- Validators register study design, population, sites, dates, endpoint definitions, comparators, metrics, calibration, exclusions, limitations, and evidence files.
- Evidence applies to an exact model version, configuration, intended use, and deployment context.
- Clinical users can open a concise evidence panel from a score and see local status and expiry.
- Material drift, workflow change, or evidence expiry marks use Under Review according to policy.
- Conflicting studies remain visible with reviewer interpretation rather than being silently discarded.
- Validation status never converts a prediction into diagnosis or action authority.

## Frappe realization

- **DocTypes:** `OC AI Validation Evidence` links model version, intended use, population, metrics child table, calibration, studies, files, reviewer decision, and expiry.
- **Workflow:** Draft → Methodology Review → Clinical Review → Approved With Limits/Approved/Rejected → Expired.
- **Roles/permissions:** `OC Model Validator` authors; independent `OC Clinical AI Reviewer` approves; clinicians receive read access to concise evidence.
- **Hooks/surfaces:** expiry scheduler opens review; score form links validation panel; print format exports evidence dossier; model activation hook requires current evidence.

## Boundaries

Owns: validation evidence and deployment eligibility status. Consumes: studies, local evaluations, and intended-use definitions. Emits: runtime-visible evidence and restrictions. Does not own: prediction interpretation or release approval alone.

## Open questions

- What constitutes a material local workflow change requiring revalidation?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Fairness Review Release Gate](openchart-feature-catalog-aic-044-fairness-review-release-gate.md)
