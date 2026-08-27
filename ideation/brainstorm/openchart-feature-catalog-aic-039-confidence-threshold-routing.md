# Confidence-Threshold Routing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes low-confidence, out-of-distribution, or incomplete AI outputs to stricter human-only paths under versioned policies.
Topics: openchart-feature-catalog, clinical-ai, frappe, confidence-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-039 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Threshold calibration lab** — Compare routing burden and missed failures across synthetic and shadow datasets.

## Focus

This feature isolates routing decisions based on calibrated uncertainty rather than presenting confidence as clinical truth.

## Behavior

- Governors define capability-specific confidence semantics, calibration version, thresholds, missing-signal behavior, and route destinations.
- Runtime evaluation can allow standard review, require enhanced review, suppress a draft, or escalate to a human-only workflow.
- Missing, invalid, or out-of-range confidence follows the safest configured route.
- Threshold decisions display the policy and reason to reviewers and remain attached to the artifact.
- Threshold changes require evaluation evidence and do not reclassify historical decisions.
- Confidence can never bypass a mandatory human review gate or grant clinical authority.

## Frappe realization

- **DocTypes:** `OC AI Confidence Policy` stores capability, metric definition, calibration Link, threshold bands, routes, effective dates, and evidence; decisions link to artifacts.
- **Workflow:** Draft → Calibration Review → Approved → Active → Retired.
- **Roles/permissions:** `OC AI Evaluator` proposes and `OC AI Governor` approves; clinicians view effective routing reasons.
- **Hooks/API/surfaces:** post-generation server hook resolves route; Assignment Rules receive only approved enhanced-review tasks; Dashboard tracks route volumes and outcomes.

## Boundaries

Owns: confidence interpretation and workflow route. Consumes: calibrated signals, completeness flags, and policy. Emits: standard, enhanced, suppressed, or escalated route. Does not own: clinical confidence or human gate removal.

## Open questions

- Which capabilities have confidence measures calibrated enough for routing rather than display only?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Clinical Risk Model Serving](openchart-feature-catalog-aic-042-clinical-risk-model-serving.md)
