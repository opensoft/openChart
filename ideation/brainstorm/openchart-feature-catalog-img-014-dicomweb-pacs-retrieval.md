# DICOMweb PACS Retrieval — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Retrieves study, series, instance, and rendered-image metadata from external PACS through DICOMweb with scoped authorization and resilient reconciliation.
Topics: openchart-feature-catalog, imaging, frappe, dicomweb-retrieval
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-014 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Federated study locator** — Query multiple approved archives and present deduplicated study availability.

## Focus

This feature isolates standards-based discovery and retrieval orchestration while PACS remains the image authority.

## Behavior

- The server uses configured QIDO-RS queries to locate studies by mapped patient and accession identifiers.
- WADO-RS access is proxied or delegated according to policy, with least-privilege tokens and bounded lifetimes.
- STOW-RS is not implied by retrieval permissions and requires a separately governed import path.
- Returned identifiers and metadata are reconciled against the expected order before presentation.
- Ambiguous matches, duplicate archives, unsupported transfer syntax, and partial series are visible to users.
- Retries are idempotent, rate-limited, and recorded without persisting bulk pixel data in Frappe.

## Frappe realization

- **DocTypes:** `OC DICOMweb Endpoint` and `OC Imaging Study Reference` store scoped configuration, identifiers, metadata cache, and reconciliation state.
- **Roles/permissions:** integration secrets are permlevel 2; clinical users receive only references authorized for the current patient and facility.
- **API/jobs:** whitelisted QIDO methods and RQ jobs perform queries; responses use structured errors and correlation IDs.
- **Surfaces:** study availability appears on reports and timelines; Script Report monitors endpoint latency, failures, and unresolved matches.

## Boundaries

Owns: endpoint configuration, retrieval authorization, study references, and reconciliation state. Consumes: PACS DICOMweb services and patient mappings. Emits: viewer-ready references and availability status. Does not own: PACS archives or pixel persistence.

## Open questions

- How long may metadata caches remain valid across PACS corrections and study merges?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
