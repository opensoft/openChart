# Patient Portal Document Downloads — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients and authorized proxies preview and download released document versions through the portal with consent, sensitivity, and audit controls.
Topics: openchart-feature-catalog, documents, frappe, portal-downloads
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-031 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Patient-friendly document explanations** — Pair released files with reviewed descriptions of purpose, provenance, and who to contact with questions.

## Focus

This feature isolates safe self-service access to explicitly released documents rather than exposing all chart Files by default.

## Behavior

- A patient or active proxy opens a portal list containing only currently released document versions within their authority scope.
- Each row shows type, service date, source, release date, file size, and whether a newer version exists.
- Preview and download recheck patient/proxy authority, consent, release status, sensitivity, and legal restrictions at request time.
- Time-limited streaming avoids public File URLs and records view/download events.
- Revoked proxy access, withdrawn release, supersession policy, or expired consent removes future access without erasing prior audit.
- Unavailable, corrupt, or quarantined files show a safe error and create support work without leaking storage details.
- Portal access never changes the accepted chart document or count as external disclosure acknowledgment automatically.

## Frappe realization

- **DocTypes:** `OC Portal Document Release` (patient, document_version, audience, proxy_scope, released_at, expires_at, state, reason).
- **Workflow:** Draft → Reviewed → Released, with Withdrawn, Expired, and Superseded states.
- **Roles/permissions:** Patient and Proxy Website Users read scoped releases; Release Coordinator manages; sensitive release decisions use permlevel 2.
- **API/surfaces:** Frappe `www/` portal page and whitelisted streaming method enforce ACL per request; Notification Log may announce new releases.
- **Files/hooks:** Private Frappe File remains attached to its document version; `open_chart.documents.on_file` and integrity state gate portal delivery.

## Boundaries

Owns: portal release decision, audience scope, access-time checks, and download evidence. Consumes: accepted document version, proxy authority, consent, and integrity state. Emits: permissioned stream event. Does not own: proxy enrollment, clinical interpretation, or public sharing.

## Open questions

- Which document classes release immediately, after delay, or only after clinician review?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Watermarking Drafts and Confidential Classes](openchart-feature-catalog-dms-038-watermarking-drafts-and-confidential-classes.md)
