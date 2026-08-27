# Therapeutic Alternative Suggestion Hooks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides governed integration hooks for explainable therapeutic alternatives that remain non-autonomous and require prescriber selection.
Topics: openchart-feature-catalog, eprescribing, frappe, therapeutic-alternatives
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-020 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Evidence-cited comparison card** — Alternatives could show formulary, safety, guideline, and cost evidence side by side for human review.

## Focus

This feature isolates a vendor-neutral extension point for alternative suggestions. It enforces provenance, explainability, and explicit human action so no model or rules engine changes therapy by itself.

## Behavior

- A prescriber explicitly requests alternatives for a selected medication and indication context.
- Each suggestion identifies source, rationale, evidence/version, applicability limits, and known missing data.
- Suggestions are ranked only by a declared method and are visually separate from accepted prescriptions.
- Selecting a suggestion creates a new editable candidate and reruns benefit, interaction, dose, and authority checks.
- The prescriber may dismiss, compare, or adopt a suggestion and can record a reason without training hidden models by default.
- Unavailable, untrusted, or stale suggestion services fail closed to ordinary manual prescribing.

## Frappe realization

- **DocTypes:** `OC Therapeutic Suggestion Session` and child candidates store request context digest, source, rationale, evidence references, ranking, and user disposition.
- **API:** A provider interface behind `open_chart.api.v1.prescriptions.suggest_alternatives` applies allowlists, timeouts, and schema validation.
- **Permissions:** Only prescribers can adopt candidates; governance roles configure providers and evidence policies.
- **Surfaces/hooks:** Comparison dialog labels generated content, and draft creation never invokes submit or signing hooks.

## Boundaries

Owns: governed suggestion exchange and disposition evidence. Consumes: prescriber request, medication context, benefit data, and approved providers. Emits: non-binding candidates. Does not own: autonomous therapy changes, diagnosis, or final prescribing judgment.

## Open questions

- What evidence and transparency threshold must a suggestion provider meet before activation?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescriber Formulary Favorites](openchart-feature-catalog-phr-019-prescriber-formulary-favorites.md)
