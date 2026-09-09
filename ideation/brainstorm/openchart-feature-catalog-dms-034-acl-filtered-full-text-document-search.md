# ACL-filtered Full-text Document Search — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Searches accepted document metadata and approved OCR text while enforcing patient, class, consent, and role access before result disclosure.
Topics: openchart-feature-catalog, documents, frappe, full-text-search
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-034 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Page-region result highlighting** — Open a permitted source page at the coordinates supporting a matched OCR phrase.

## Focus

This feature isolates secure retrieval across indexed documents; relevance must never outrun authorization.

## Behavior

- An authorized user enters terms and optional patient, class, tag, date, source, or facility filters.
- Server-side authorization derives the set of accessible patients and document classes before querying indexed content.
- Results show only permitted metadata, snippets, and current-version indicators; inaccessible matches contribute no counts or timing hints.
- Opening a hit rechecks source document access, consent, hold restrictions, and integrity status.
- OCR snippets are labeled machine-extracted and link to source-page evidence rather than asserting clinical truth.
- Superseded versions are excluded by default but available to roles with historical-record permission.
- Search queries, result access, export, timeout, and index-staleness conditions are auditable and explainable.

## Frappe realization

- **DocTypes:** `OC Document Search Index State` tracks document_version, OCR_run, indexed_at, index_version, and eligibility; no PHI search text is copied to broadly readable DocTypes.
- **Jobs/hooks:** Accepted-version and OCR `on_update` events enqueue index/upsert or tombstone jobs; failures enter a reconciliation queue.
- **Roles/permissions:** Search endpoint composes Frappe DocPerm, patient User Permission, document-class policy, and consent checks before backend query.
- **API/surfaces:** Whitelisted `open_chart.api.v1.documents.search` returns bounded results and opaque cursors; Desk and patient timeline search use the same service.
- **Security:** Snippet generation occurs only after ACL filtering; logs hash query correlation where raw search terms would expose PHI.

## Boundaries

Owns: searchable projection, ACL-aware query, snippets, and index reconciliation. Consumes: accepted metadata, approved OCR runs, tags, and access policy. Emits: authorized result references. Does not own: OCR generation, patient access policy, or autonomous clinical summarization.

## Open questions

- Which search backend best supports per-document ACL filters, deletion guarantees, and Frappe v15 operations?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Document Tagging and Saved Searches](openchart-feature-catalog-dms-033-document-tagging-and-saved-searches.md)
