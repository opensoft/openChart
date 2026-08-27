# Bring-Your-Own-Model Onboarding — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Guides administrators through endpoint, credential, capability, privacy, and validation checks before a customer-supplied model can be activated.
Topics: openchart-feature-catalog, clinical-ai, frappe, byom-onboarding
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-031 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Onboarding evidence bundle** — Export configuration, validation, privacy, and approval evidence for local governance review.

## Focus

This feature isolates a safe onboarding wizard for externally hosted or organization-managed models.

## Behavior

- An administrator selects provider type, endpoint, authentication method, supported capabilities, data region, and PHI terms.
- Credentials are tested without displaying secrets and endpoint identity is pinned where supported.
- The wizard runs schema, timeout, structured-output, citation, safety, privacy, and synthetic golden-case tests.
- Failures identify the failed control and prohibit activation; partial success cannot be represented as certified.
- Privacy, clinical, security, and operational approvers attest applicable evidence before adapter creation.
- Completion creates a disabled or shadow-ready deployment, never an active clinical capability.

## Frappe realization

- **DocTypes:** `OC AI Model Onboarding` stores endpoint metadata, encrypted credential reference, attestations, validation run Links, data handling, and resulting adapter/deployment.
- **Workflow:** Draft → Connectivity Test → Validation → Security Review → Clinical Review → Approved/Rejected.
- **Roles/permissions:** AI administrator enters configuration; security, privacy, and clinical reviewers have separate transitions and masked secrets.
- **Jobs/surfaces:** multi-step Desk Form; rq validation suite uses synthetic SYN- fixtures; server scripts cannot reveal Password fields; print format produces evidence bundle.

## Boundaries

Owns: onboarding evidence and preactivation checks. Consumes: endpoint configuration, credentials, contracts, and validation cases. Emits: approved disabled deployment. Does not own: vendor certification or capability activation.

## Open questions

- Which controls can be waived locally, and which are nonwaivable baseline safeguards?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Vendor Model Certification Registry](openchart-feature-catalog-aic-033-vendor-model-certification-registry.md)
