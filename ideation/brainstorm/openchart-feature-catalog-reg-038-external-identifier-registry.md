# External Identifier Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Registers identifiers issued by external systems with authority, type, validity, verification, and uniqueness controls.
Topics: openchart-feature-catalog, registration, frappe, external-identifiers
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-038 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Identifier authority directory** — Govern issuer namespaces, formats, and uniqueness expectations centrally per site.

## Focus

Link a patient to outside identifier namespaces without treating raw values as globally unique.

## Behavior

- Authorized clients register identifier value, type, assigning authority, system URI, use, and effective dates.
- Uniqueness is evaluated within the configured authority and type namespace.
- Exact conflicts route to identity review and never reassign the identifier silently.
- Identifiers can be active, old, temporary, entered in error, or superseded with provenance.
- Sensitive values are masked in lists and require exact guarded lookup.
- Imported identifiers retain source system, transaction, and verification state.

## Frappe realization

- **DocTypes:** existing `OC Patient External Identifier` plus `OC Identifier Authority` with namespace, formats, uniqueness scope, status, and issuer metadata.
- **Workflow:** Proposed → Verified → Active → Superseded, Retired, or Entered in Error.
- **Roles/permissions:** `OC Integration User` registers through API; `OC Identity Reviewer` resolves conflicts; raw values use permlevel 2.
- **API/surfaces:** guarded `open_chart.api.v1.register_external_identifier` and lookup method; registry list, authority workspace, and conflict report.

## Boundaries

Owns: external identifier registration and namespace uniqueness. Consumes: assigning-authority definitions and patient link. Emits: verified identifier mappings. Does not own: external-system record correctness.

## Open questions

- Which authorities permit reuse of retired identifiers, if any?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
