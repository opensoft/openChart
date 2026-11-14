# PHI Boundary Controls — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces capability-specific de-identification, limited-dataset, residency, and external-inference restrictions before context leaves openChart.
Topics: openchart-feature-catalog, clinical-ai, frappe, phi-boundaries
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-034 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Context boundary preview** — Show authorized reviewers exactly which fields would be sent, transformed, withheld, or tokenized.

## Focus

This feature isolates data-boundary enforcement for external and self-hosted inference.

## Behavior

- Each capability policy declares allowed data classes, identifiers, purpose, provider, region, retention mode, and transformation profile.
- Before invocation, the server builds a field-level manifest and applies configured removal, tokenization, date shifting, or limited-dataset rules.
- The effective payload is rejected if required transformation fails or prohibited fields remain.
- Users can see whether external inference is allowed and which mode applies without seeing secrets or hidden data.
- Break-glass clinical access does not automatically authorize external transmission.
- Every boundary decision and transformed-payload digest is auditable.

## Frappe realization

- **DocTypes:** `OC AI Data Boundary Policy` and `OC AI Deidentification Profile` store field rules, purpose, provider/region limits, retention class, version, and test evidence.
- **Workflow:** Draft → Privacy Review → Security Review → Approved → Active → Suspended/Retired.
- **Roles/permissions:** `OC Privacy Reviewer` authors policy; invocation service receives only transformed payload; raw preview requires permlevel 2.
- **Hooks/API:** mandatory server-side context-builder hook precedes adapters; synthetic test cases validate transformations; audit Script Report records policy decisions.

## Boundaries

Owns: outbound inference data minimization and policy decision. Consumes: source fields, capability purpose, provider terms, and jurisdiction. Emits: approved transformed context or denial. Does not own: source consent or provider behavior after receipt.

## Open questions

- Which clinical text transformations preserve enough utility without creating false assurances of de-identification?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Transcript And Audio Retention Policy](openchart-feature-catalog-aic-035-transcript-audio-retention-policy.md)
