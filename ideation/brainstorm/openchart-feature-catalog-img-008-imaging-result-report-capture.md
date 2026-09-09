# Imaging Result Report Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures a diagnostic imaging report as a provenance-rich clinical result linked to its order, performance, images, and author.
Topics: openchart-feature-catalog, imaging, frappe, result-reporting
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-008 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Radiator-style reading queue** — Organize unreported studies by priority, subspecialty, location, and ownership.

## Focus

This feature isolates report authorship and result capture while keeping image storage external.

## Behavior

- A radiologist opens a report against one verified order and performed study.
- The report supports indication, technique, comparison, findings, impression, recommendations, structured elements, and linked key images.
- Draft autosave does not expose unaccepted text as a clinical result.
- Signature validates author authority, required sections, referenced images, and current study identity.
- Imported reports retain source organization, external identifiers, timestamps, and original attachment.
- Corrections and addenda preserve the accepted report and create an explicit succession chain.

## Frappe realization

- **DocTypes:** submittable `OC Imaging Report` with naming series `IMG-RPT-.YYYY.-`, child structured elements, key-image links, and source provenance.
- **Workflow:** Draft → Ready for Signature → Accepted → Addendum Pending → Superseded.
- **Roles/permissions:** radiologists author and sign; transcription staff edit drafts under assignment; clinicians receive accepted results only.
- **Hooks/API/surfaces:** guarded report methods enforce succession; Jinja Print Format renders the report; report workspace links PACS viewer context.

## Boundaries

Owns: diagnostic report content, state, provenance, and amendment lineage. Consumes: order, performance, viewer references, and templates. Emits: clinical result and communication obligations. Does not own: image pixels or PACS lifecycle.

## Open questions

- Which external report signatures can be trusted directly versus requiring local verification?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
