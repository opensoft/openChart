# Specialty Summarization Profiles — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs specialty-specific summary structures, source scopes, terminology, and exclusions as versioned clinical content.
Topics: openchart-feature-catalog, clinical-ai, frappe, summary-profiles
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-006 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Profile comparison sandbox** — Run two approved profiles against the same synthetic chart and compare omissions and emphasis.

## Focus

This feature isolates the reusable profile that shapes summaries without embedding specialty policy inside model prompts or vendor adapters.

## Behavior

- Clinical content authors define intended specialty, audience, section order, allowed source classes, lookback windows, exclusions, and citation requirements.
- Profiles move through clinical review and are immutable after activation; changes create successors.
- A generation request pins the exact active profile version and rejects incompatible capabilities.
- Clinicians can see which profile shaped a summary and report missing or overemphasized content.
- Retired profiles remain available for replay but cannot start new generations.
- No profile may authorize diagnosis, ordering, or other consequential action.

## Frappe realization

- **DocTypes:** `OC AI Summary Profile` with specialty, audience, JSON section schema, source policy child table, prompt fragment, owner, evidence, and successor Link.
- **Workflow:** Draft → Clinical Review → Approved → Active → Retired.
- **Roles/permissions:** `OC AI Content Author` drafts and `OC Clinical AI Reviewer` approves; site administrators assign active profiles.
- **Hooks/surfaces:** `validate` checks schema and prohibited actions; fixtures seed baseline profile types; Desk Form, version comparison, and review Notifications support governance.

## Boundaries

Owns: summary structure and source-scope policy. Consumes: specialty governance and capability schemas. Emits: versioned profile identifiers for generation. Does not own: model deployments or patient-specific outputs.

## Open questions

- Which profile elements should be locally configurable versus centrally locked for safety?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Pre-Visit Chart Summary](openchart-feature-catalog-aic-007-pre-visit-chart-summary.md)
