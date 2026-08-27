# Order Set Version Authoring — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized editors draft successor versions of order sets with explicit diffs, provenance, and effective dating.
Topics: openchart-feature-catalog, cpoe, frappe, order-set-versioning
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-014 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Semantic change summary** — Generate a reviewer draft of clinically meaningful differences for human correction.

## Focus

This feature isolates safe authoring and succession of order-set content.

## Behavior

- Editors clone a published set into a draft successor rather than editing active content in place.
- Each version records owner, authors, source evidence, rationale, effective dates, and predecessor.
- A structured diff highlights added, removed, reordered, and default-changed items.
- Broken or retired orderable references block review submission.
- Historical patient orders continue to point to the exact originating version.
- Concurrent edits use optimistic conflict detection and never silently overwrite changes.

## Frappe realization

- **DocTypes:** versioned `OC Order Set` with predecessor Link, version, change_reason, evidence Table, and mandatory provenance fields; child items use stable logical identifiers.
- **Workflow:** Draft → Clinical Review; only a successor can advance while predecessor remains Published.
- **Roles/permissions:** `OC Order Set Editor` authors; `OC Clinical Reviewer` comments; permlevel 2 protects approval and provenance metadata.
- **Hooks/API/surface:** `before_save` computes structural diff, `validate` rejects invalid references, and a Script Report renders predecessor comparison.

## Boundaries

Owns: authoring succession and diffs. Consumes: current set and orderable catalogs. Emits: review-ready successor. Does not own: approval authority or clinician application.

## Open questions

- Which changes require a major version and renewed multidisciplinary review?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Set Approval And Publishing](openchart-feature-catalog-ord-015-order-set-approval-and-publishing.md)
