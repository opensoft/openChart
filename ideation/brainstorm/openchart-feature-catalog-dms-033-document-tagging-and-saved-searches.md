# Document Tagging and Saved Searches — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies governed document taxonomy terms and lets users save permission-filtered queries without turning free-form tags into clinical facts.
Topics: openchart-feature-catalog, documents, frappe, document-taxonomy
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-033 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Taxonomy stewardship queue** — Review proposed synonyms, unused terms, and ambiguous mappings before changing active vocabulary.

## Focus

This feature isolates reusable descriptive organization and personal/team retrieval views for documents.

## Behavior

- A Taxonomy Steward creates hierarchical or faceted terms with definitions, synonyms, effective dates, and class constraints.
- Authorized users add allowed terms to accepted documents with actor and source provenance.
- Tags describe retrieval facets and never overwrite document class, diagnosis, author, or service date.
- Retiring or merging a term preserves historical assignments and maps future search through a successor.
- A user builds a saved search from filters such as class, tag, source, date, author, department, or state.
- Personal searches remain private; shared searches require explicit audience and are evaluated against each viewer's current ACL.
- Empty, invalid, or newly unauthorized results fail safely without revealing hidden document counts.

## Frappe realization

- **DocTypes:** `OC Document Taxonomy Term` (parent, code, label, definition, synonyms, state, successor) and `OC Document Saved Search` (owner, audience, filters JSON, sort, columns).
- **Tag pattern:** Link child `OC Document Tag Assignment` to document/version and governed term rather than relying solely on free-form `_user_tags`.
- **Workflow/permissions:** Draft → Approved → Active → Retired for terms; Taxonomy Steward governs, Document User assigns permitted terms, shared-search audiences use User Permissions.
- **API/surfaces:** Guarded tag assignment and saved-search methods; Desk list-view filters, shortcuts, and workspace cards compile filters server-side.
- **Reports:** Taxonomy usage Query Report exposes only aggregate counts permitted to the viewer.

## Boundaries

Owns: taxonomy terms, assignments, saved-query definitions, and audience. Consumes: document metadata and viewer ACL. Emits: retrieval facets and filtered result requests. Does not own: document class authority, OCR text, clinical coding, or search-index implementation.

## Open questions

- Which taxonomy facets are organization-wide versus facility-owned, and who may publish shared searches?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [ACL-filtered Full-text Document Search](openchart-feature-catalog-dms-034-acl-filtered-full-text-document-search.md)
