# Structured Imaging Category Fields — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures governed category systems such as BI-RADS- or LI-RADS-style assessments as discrete, versioned report elements tied to narrative interpretation.
Topics: openchart-feature-catalog, imaging, frappe, structured-reporting
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-037 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Category-consistency review** — Warn when narrative recommendations and selected category appear inconsistent.

## Focus

This feature isolates discrete assessment categories and their controlled semantics within imaging reports.

## Behavior

- Applicable templates present the correct category system, version, allowed values, descriptors, and required companion fields.
- The reporting clinician selects values and reviews generated labels or recommendation prompts.
- Validation blocks impossible combinations defined by the active schema and explains the failed rule.
- Advisory consistency warnings never choose or change a category automatically.
- Signed reports preserve code, display text, schema version, author, and narrative context.
- Addenda or corrected categories follow report succession and trigger any required revised communication.

## Frappe realization

- **DocTypes:** `OC Imaging Reporting Schema` with versioned child fields, value sets, constraints, and recommendation mappings; report child rows store accepted values.
- **Roles/permissions:** clinical schema managers draft; designated radiologists approve; report authors enter values; analysts read permission-filtered discrete data.
- **Hooks/API/surfaces:** report `validate` executes schema rules; form renderer uses metadata rather than custom code per system; Print Format includes labels and versions.
- **Reports:** Query Reports support quality cohorts while preserving row-level patient and facility permissions.

## Boundaries

Owns: category schemas, discrete values, validation, and narrative linkage. Consumes: report context and governed terminology. Emits: coded assessment data and consistency warnings. Does not own: clinical categorization decisions or autonomous recommendations.

## Open questions

- How should licensed or externally governed category definitions be distributed and updated?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
