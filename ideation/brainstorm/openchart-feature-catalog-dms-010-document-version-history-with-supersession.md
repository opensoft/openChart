# Document Version History With Supersession — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves immutable accepted document versions and explicit successor relationships so corrections never erase prior chart evidence.
Topics: openchart-feature-catalog, documents, frappe, document-supersession
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-010 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Version change summary** — Present metadata and page-level differences between an accepted version and its proposed successor.

## Focus

This feature isolates succession-based amendment of document content and metadata.

## Behavior

- Authorized staff start a correction from the current accepted document version and must state a reason.
- The proposed successor copies references but receives a new immutable file, checksum, metadata set, and version identifier.
- Until accepted, the current version remains authoritative and the proposal is clearly labeled Draft Successor.
- Acceptance marks the predecessor Superseded while preserving its viewability to authorized users.
- Rejection leaves the predecessor current and retains the rejected proposal with decision evidence.
- Open routes, portal releases, retention dates, and exports are re-evaluated against the accepted successor.
- The timeline shows who proposed and accepted each transition without rewriting file history.

## Frappe realization

- **DocTypes:** `OC Patient Document` points to current version; `OC Document File Version` stores version_no, File Link, supersedes, reason, state, accepted_by, and accepted_at.
- **Workflow:** Draft Successor → Review → Accepted, with Rejected and Superseded states; accepted records use succession rather than Frappe cancellation-based amendment.
- **Roles/permissions:** Document Maintainer proposes; Health Information Manager accepts; legal and disclosure roles retain read access to historical versions under policy.
- **Hooks/API:** `validate` prevents cycles and in-place File changes; guarded `open_chart.api.v1.documents.supersede` atomically advances the current pointer and emits an event.
- **Surfaces:** Patient timeline version tree, side-by-side preview, and history Print Format identify current versus superseded content.

## Boundaries

Owns: immutable versions, successor graph, acceptance authority, and current-version pointer. Consumes: corrected file or metadata and reason. Emits: accepted-supersession event. Does not own: duplicate judgment, retention destruction, or clinical fact reconciliation.

## Open questions

- Which metadata-only corrections may use a lighter approval path without weakening provenance?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Duplicate Document Detection](openchart-feature-catalog-dms-009-duplicate-document-detection.md)
