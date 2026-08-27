# CDS Rule Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains the authoritative inventory of clinical decision-support rules with scope, owner, lifecycle, and mandatory provenance.
Topics: openchart-feature-catalog, cpoe, frappe, cds-registry
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-045 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Rule dependency graph** — Visualize shared value sets, data inputs, and downstream surfaces before a change is approved.

## Focus

This feature isolates the governed catalog of decision-support artifacts.

## Behavior

- Governance users search rules by type, clinical scope, owner, status, care setting, trigger, and effective date.
- Every rule records source, authorship, evidence, rationale, version, owner, reviewer, and effective dates.
- Active rules expose human-readable intent, required inputs, outputs, severity, and expected user action.
- Missing provenance or owner blocks review and activation.
- Retired and superseded versions remain available for historical evaluation evidence.
- Registry access never grants authority to activate, override, or execute a rule.

## Frappe realization

- **DocTypes:** `OC CDS Rule` with stable logical ID, type, trigger, scope, expression reference, severity, owner, mandatory provenance fields, evidence Table, and predecessor.
- **Workflow:** Draft → Testing → Clinical Review → Approved → Active → Retired/Withdrawn.
- **Roles/permissions:** `OC CDS Author`, `OC CDS Reviewer`, `OC CDS Publisher`, and read-only `OC CDS Auditor` separate duties.
- **Hooks/API/surface:** `validate` enforces provenance and schema; registry REST filters and a CDS Governance workspace expose lifecycle views.

## Boundaries

Owns: rule identity, metadata, lifecycle, and provenance. Consumes: governance decisions and referenced artifacts. Emits: eligible active rule versions. Does not own: runtime evaluation or clinical action.

## Open questions

- Which rule expression languages may be registered in the first release?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Rule Version And Provenance](openchart-feature-catalog-ord-046-cds-rule-version-and-provenance.md)
