# ROI Fulfillment Packet Assembly — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Builds a reviewed, watermarked release packet from approved record selections with manifest, redaction state, and reproducible output.
Topics: openchart-feature-catalog, documents, frappe, roi-fulfillment
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-015 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Scope completeness assistant** — Compare selected records with the approved request scope and explain likely omissions or excesses.

## Focus

This feature isolates minimum-necessary selection, review, and packet generation after an ROI request is approved.

## Behavior

- A Release Specialist starts fulfillment from the frozen approved request scope.
- Search results are ACL- and scope-filtered; the specialist selects exact immutable document versions and generated chart sections.
- Each inclusion or exclusion records category, date, reason, and reviewer.
- Restricted segments, third-party content, superseded records, and legal-hold material display explicit review warnings.
- Packet generation adds a cover sheet, page numbering, request-specific watermark, and item manifest.
- A second reviewer may approve the sealed output when policy requires; any changed selection invalidates approval.
- Delivery can proceed only from the approved sealed packet and records the exact output checksum.

## Frappe realization

- **DocTypes:** `OC ROI Fulfillment` (request, selection_version, state, packet_file, checksum, approved_by) with child `OC ROI Packet Item` (source Dynamic Link, document_version, inclusion, reason, page_range).
- **Files/jobs:** RQ builds the private PDF from source versions and Frappe Print Formats; `open_chart.documents.on_file` verifies generated checksum and attachment target.
- **Workflow:** Selecting → Review → Packet Building → Approval → Ready for Delivery, with Deficient, Build Failed, and Reopened states.
- **Roles/permissions:** Release Specialist selects; Privacy Reviewer approves restricted content; delivery role sees only approved packet and destination.
- **API/surfaces:** Guarded selection and seal methods; Desk packet builder, source preview, and fulfillment manifest Print Format.

## Boundaries

Owns: selection manifest, inclusion decisions, packet rendering, watermark, and sealed checksum. Consumes: approved ROI scope and immutable source versions. Emits: approved fulfillment packet. Does not own: request authorization, channel delivery, or authoritative source records.

## Open questions

- Which record segments require mandatory second review or redaction tooling before inclusion?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Disclosure Log Per Document](openchart-feature-catalog-dms-016-disclosure-log-per-document.md)
