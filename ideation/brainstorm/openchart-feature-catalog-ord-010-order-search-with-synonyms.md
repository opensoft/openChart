# Order Search With Synonyms — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Finds orderable concepts through governed synonyms, abbreviations, codes, and clinically meaningful terms.
Topics: openchart-feature-catalog, cpoe, frappe, order-search
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-010 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Zero-result stewardship** — Route unresolved search phrases to terminology curators without exposing patient context.

## Focus

This feature isolates fast, governed discovery of orderable items.

## Behavior

- Users search by preferred name, local synonym, abbreviation, external code, specimen, modality, or service term.
- Results identify order class, active status, common name, and organization restrictions.
- Exact and prefix matches rank ahead of fuzzy synonyms; inactive concepts are excluded by default.
- Ambiguous abbreviations display disambiguating context instead of auto-selecting.
- Search telemetry excludes patient identifiers and records only normalized query and selected concept when allowed.
- No-result searches offer a terminology feedback action rather than a free-text order shortcut.

## Frappe realization

- **DocTypes:** `OC Orderable Concept` with class, code system, code, status, and child `OC Order Synonym` with locale, term, type, and provenance.
- **Roles/permissions:** all ordering roles read published concepts; `OC Terminology Curator` manages synonyms and lifecycle.
- **Hooks/API/surface:** global-search integration and `@frappe.whitelist` search method enforce class privileges, pagination, and active filters.
- **Reports:** a privacy-minimized Query Report lists zero-result terms for curator review.

## Boundaries

Owns: orderable discovery vocabulary and ranking. Consumes: concept catalog and privilege context. Emits: selected concept identifiers. Does not own: clinical appropriateness.

## Open questions

- Which fuzzy-match threshold avoids unsafe near-name substitutions?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Personal Order Favorites](openchart-feature-catalog-ord-011-personal-order-favorites.md)
