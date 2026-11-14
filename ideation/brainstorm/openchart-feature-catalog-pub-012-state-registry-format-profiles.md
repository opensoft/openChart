# State Registry Format Profiles — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Manages versioned first-party profiles for state-specific HL7, XML, CSV, transport, validation, and acknowledgment variants.
Topics: openchart-feature-catalog, public-health, frappe, registry-format-profile
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-012 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Connector update channel** — Distribute signed managed-profile releases independently of application upgrades.

## Focus

A governed profile layer that turns state configuration from implementer work into supportable first-party connectors.

## Behavior

- Connector administrators choose jurisdiction, direction, message family, transport adapter, and effective dates.
- Profiles define mappings, required fields, code translations, validation rules, and acknowledgment semantics.
- Draft profiles run only against synthetic fixtures until reviewed and published.
- Activation preserves prior versions for message replay, audit, and historical interpretation.
- Secrets are referenced from protected configuration and never embedded in profile exports.
- Unsupported variants fail closed with a profile-gap status rather than emitting best-effort clinical messages.

## Frappe realization

- **DocTypes:** Add `OC Registry Format Profile`, child mapping and validation-rule DocTypes, plus `OC Connector Endpoint` with secret references.
- **Workflow:** Use draft, test, technical-review, published, active, and retired states with effective-date collision validation.
- **Permissions:** Separate `OC Connector Administrator`, `OC Registry Profile Author`, and `OC Registry Profile Approver` duties.
- **Surfaces:** Provide synthetic conformance Script Reports, profile version comparison, fixtures, patches, and guarded profile export/import APIs.

## Boundaries

Owns: local profile versions and managed mappings. Consumes: jurisdiction specifications and connector adapters. Emits: deterministic validation and serialization rules. Does not own: state specifications, credentials, or clinical records.

## Open questions

- What support policy and signing mechanism should govern first-party profile releases?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
