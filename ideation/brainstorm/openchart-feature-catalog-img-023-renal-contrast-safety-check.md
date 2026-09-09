# Renal Contrast Safety Check — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates contrast readiness against current renal laboratory evidence, protocol policy, allergy context, and documented human override.
Topics: openchart-feature-catalog, imaging, frappe, contrast-safety
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-023 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Lab refresh task** — Generate accountable collection work when renal evidence is missing or stale.

## Focus

This feature isolates nephrotoxicity-related readiness for contrast imaging without making a diagnosis or autonomous protocol decision.

## Behavior

- The check selects qualifying creatinine or eGFR evidence by patient, specimen time, method, and configured validity window.
- It displays the selected value, trend, age, provenance, and relevant risk answers to the reviewer.
- Versioned policy returns Ready, Review Required, Missing Evidence, or Contraindicated by Policy.
- Authorized clinicians may document a reasoned override where policy permits, with approver and timestamp.
- A changed protocol, new laboratory result, or expired validity window invalidates the prior readiness decision.
- The system never orders hydration, laboratory tests, medication changes, or alternative studies autonomously.

## Frappe realization

- **DocTypes:** `OC Imaging Safety Check` subtype Renal Contrast with evidence Links, policy version, outcome, override, and expiry.
- **Workflow:** Pending Evidence → Review Required → Cleared or Blocked, with Override Review and Expired states.
- **Roles/permissions:** technologists initiate; radiologists or designated contrast clinicians approve overrides; policy managers version thresholds.
- **Hooks/API/surfaces:** server validation recalculates on readiness transitions; API returns explainable rule results; worklist displays blocking state.

## Boundaries

Owns: renal evidence selection, policy evaluation, and clearance record. Consumes: labs, protocol, allergies, and risk answers. Emits: contrast readiness and tasks. Does not own: diagnosis, lab ordering, treatment, or autonomous study substitution.

## Open questions

- How should policies account for differing eGFR equations and urgent-study exceptions?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
