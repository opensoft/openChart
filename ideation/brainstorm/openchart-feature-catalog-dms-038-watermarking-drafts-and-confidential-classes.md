# Watermarking Drafts and Confidential Classes — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies policy-driven visible and forensic watermarks to previews, downloads, prints, and exports based on state, class, recipient, and purpose.
Topics: openchart-feature-catalog, documents, frappe, document-watermarking
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-038 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Recipient-specific forensic mark** — Encode an opaque disclosure identifier in each released rendition for incident investigation.

## Focus

This feature isolates controlled rendition marking while keeping original accepted files immutable.

## Behavior

- A Privacy Administrator defines watermark policies by document class, state, channel, audience, and purpose.
- Draft previews visibly identify draft status; confidential outputs may include recipient, date, purpose, or disclosure identifier.
- Watermarks are applied to derived renditions at access or packet-build time, never baked into the source original.
- The user previews the marked output before print, portal release, fax, or export when workflow permits.
- Each rendition records source checksum, policy version, render parameters, recipient context, and output checksum.
- Unsupported media, rendering failure, missing recipient context, or policy conflict blocks governed release.
- Superseded policies remain resolvable for historical output verification.

## Frappe realization

- **DocTypes:** `OC Document Watermark Policy` (class, state, channel, audience, content_template, opacity, effective dates) and `OC Watermarked Rendition` (source_version, context JSON, policy_version, File, checksum).
- **Files/jobs:** RQ generates private derived Files for PDF/image media; `open_chart.documents.on_file` validates derivative lineage and prevents attachment as a new original.
- **Roles/permissions:** Privacy Administrator versions policy; releasing role requests renditions; viewers cannot bypass required policy through direct File access.
- **API/surfaces:** Central whitelisted render/stream methods serve portal, print, fax, and ROI; preview shows watermark placement and clipping.
- **Print formats:** Frappe Jinja Print Formats provide cover/page overlays for generated documents and packets.

## Boundaries

Owns: watermark policy, marked rendition, render provenance, and checksum. Consumes: source version, state, audience, recipient, and channel. Emits: governed derived output. Does not own: source content, disclosure authorization, DRM guarantees, or recipient behavior.

## Open questions

- Which confidential classes need recipient-identifying marks versus a generic classification banner?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Patient Portal Document Downloads](openchart-feature-catalog-dms-031-patient-portal-document-downloads.md)
