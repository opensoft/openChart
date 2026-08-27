# Transcript And Audio Retention Policy — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies jurisdiction-, consent-, purpose-, and artifact-specific retention rules to ambient audio and transcripts.
Topics: openchart-feature-catalog, clinical-ai, frappe, media-retention
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-035 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Retention impact preview** — Show which evidence links and replay capabilities will change before a policy is published.

## Focus

This feature isolates lifecycle policy for high-risk ambient source media.

## Behavior

- Privacy administrators define retention by jurisdiction, site, consent basis, participant class, media type, purpose, and artifact disposition.
- Capture sessions pin the effective policy version at start and record later legal holds or revocations.
- Scheduled jobs identify due items, verify no hold, and delete or cryptographically quarantine content according to policy.
- Deletion preserves metadata, digest, policy, actor/job, time, and affected provenance links.
- Reviewers see when source evidence will expire and whether an accepted note remains independently authoritative.
- Policy changes do not silently rewrite completed disposal evidence.

## Frappe realization

- **DocTypes:** `OC AI Media Retention Policy`, `OC AI Legal Hold`, and `OC AI Disposal Event` store applicability, durations, action, policy version, object Links, digest, and outcome.
- **Workflow:** policy Draft → Legal Review → Approved → Active → Retired; disposal Planned → Held/Executed/Failed.
- **Roles/permissions:** `OC Privacy Administrator` governs policy; storage workers delete files; clinicians cannot extend retention ad hoc.
- **Jobs/surfaces:** daily scheduler evaluates retention idempotently; failed-disposal Script Report and Notifications; file hooks prevent deletion outside the governed path.

## Boundaries

Owns: ambient media retention, hold, and disposal evidence. Consumes: jurisdiction, consent, purpose, artifact state, and holds. Emits: retained, quarantined, or deleted state. Does not own: signed-note retention or legal interpretation.

## Open questions

- When consent is revoked, which jurisdictions require immediate deletion versus retention for audit defense?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Consent-Gated Ambient Capture](openchart-feature-catalog-aic-003-consent-gated-ambient-capture.md)
