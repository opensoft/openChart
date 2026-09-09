# Drug-Drug Interaction Checking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates a candidate prescription against current medications using severity-tiered, explainable interaction findings and accountable override handling.
Topics: openchart-feature-catalog, eprescribing, frappe, drug-interactions
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-028 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Patient-specific risk refinement** — Reviewed labs, diagnoses, and treatment duration could refine relevance while preserving base-rule evidence.

## Focus

This feature isolates drug-drug interaction evaluation at prescribing time. Findings support prescriber judgment and never discontinue, substitute, or modify medication autonomously.

## Behavior

- The engine compares candidate ingredients with active, PRN, recently stopped, and clinically selected medication statements.
- Findings show interacting pair, severity tier, mechanism, clinical effect, evidence source/version, and recommended considerations.
- The screen distinguishes contraindicated, major, moderate, minor, duplicate, and informational findings according to configured policy.
- Missing medication coding or stale lists produce data-quality warnings rather than false reassurance.
- Blocking or overridable tiers require a prescriber disposition, rationale, and optionally a monitoring plan.
- The signed snapshot retains evaluated medications, rules release, findings, and decisions.

## Frappe realization

- **DocTypes:** `OC Medication Safety Evaluation` and `OC Prescription Safety Finding` store context digests, ruleset version, severity, evidence, and disposition.
- **Hooks/API:** Server validation calls an allowlisted rules provider; results are cached only for the exact content and medication-list version.
- **Permissions:** Prescribers disposition findings; safety-governance roles configure tier policy but cannot sign prescriptions.
- **Surfaces:** Composer alert panel, full evidence drawer, override dialog, and safety analytics Script Report support use and governance.

## Boundaries

Owns: interaction evaluation evidence and disposition. Consumes: candidate prescription, governed medication list, and rules release. Emits: severity-tiered findings. Does not own: medication-list reconciliation, autonomous therapy changes, or proprietary rule content.

## Open questions

- Which severity policies should be site-configurable without undermining minimum safety controls?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Drug-Allergy Interaction Checking](openchart-feature-catalog-phr-029-drug-allergy-interaction-checking.md)
