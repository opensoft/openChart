# Prior and Current Image Comparison — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Opens a current study beside selected priors with patient and anatomy verification, comparison provenance, and graceful viewer fallback.
Topics: openchart-feature-catalog, imaging, frappe, image-comparison
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-015 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Comparison suggestion queue** — Rank plausible priors for human selection using transparent metadata criteria.

## Focus

This feature isolates the workflow for selecting and launching clinically relevant prior/current comparisons.

## Behavior

- The reporting user sees available priors filtered by verified patient identity, anatomy, modality, and date.
- Suggested priors disclose why they matched and require human confirmation before launch.
- A comparison session records the current study and every selected prior reference.
- Patient mismatch, unavailable series, or unsupported cross-archive comparison blocks launch with an actionable message.
- The report may cite which studies were compared without claiming every launched image was reviewed.
- Reopening a report reconstructs references even when viewer layout preferences are not portable.

## Frappe realization

- **DocTypes:** `OC Imaging Comparison Session` with child study references, match rationale, selected flag, launch outcome, and report Link.
- **Roles/permissions:** radiologists and authorized clinicians select priors; cross-facility user permissions apply to every referenced study.
- **API/surfaces:** a whitelisted comparison-session method validates identifiers then delegates layout to the viewer; report form lists cited comparisons.
- **Hooks/audit:** accepted report submission snapshots cited prior identifiers and provenance; unavailable priors create no silent omissions.

## Boundaries

Owns: comparison selection, validation, and citation evidence. Consumes: external study metadata and viewer capabilities. Emits: multi-study launch context. Does not own: image registration, hanging protocols, or diagnostic conclusions.

## Open questions

- Which prior-match criteria should vary by specialty and study type?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
