# Organization Order Set Library — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes a searchable organization-owned library of specialty and pathway order sets for controlled reuse.
Topics: openchart-feature-catalog, cpoe, frappe, order-set-library
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-013 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Service-line collections** — Curate role- and location-specific views over the same published library.

## Focus

This feature isolates discovery and use of governed organization order sets.

## Behavior

- Clinicians browse or search published sets by specialty, condition, care setting, owner, and effective date.
- Opening a set shows grouped orders, defaults, optionality, cautions, version, and last review date.
- Applying a set creates editable draft orders and does not submit any item automatically.
- Inapplicable or privilege-restricted items are identified before acceptance.
- Retired sets remain visible in historical provenance but cannot create new drafts.
- Usage records identify the set version without copying patient data into library records.

## Frappe realization

- **DocTypes:** `OC Order Set` with title, specialty, owner, status, version, effective dates, provenance, and child `OC Order Set Item`.
- **Workflow:** Draft → Clinical Review → Approved → Published → Retired.
- **Roles/permissions:** `OC Order Set Editor`, `OC Clinical Reviewer`, and `OC Order Set Publisher` have separated duties; ordering roles read Published only.
- **Hooks/API/surface:** Desk workspace and whitelisted preview/apply methods return current sets; applied `OC Clinical Order` records store source set/version.

## Boundaries

Owns: discoverable organization set catalog. Consumes: governed orderables and publication decisions. Emits: editable order drafts with provenance. Does not own: personal favorites or final signatures.

## Open questions

- Can one published set include another, and how should nested version provenance work?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Set Version Authoring](openchart-feature-catalog-ord-014-order-set-version-authoring.md)
