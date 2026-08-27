# Cumulative Radiation Exposure View — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents a provenance-aware longitudinal view of verified radiation exposure metrics without reducing unlike dose measures to a misleading single number.
Topics: openchart-feature-catalog, imaging, frappe, cumulative-exposure
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-022 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Protocol-family trends** — Compare repeated study dose distributions against local reference ranges.

## Focus

This feature isolates longitudinal exposure visibility for clinicians and quality teams.

## Behavior

- Authorized users view verified dose records chronologically and grouped by modality and metric type.
- The view distinguishes measured, estimated, imported, missing, corrected, and unverified values.
- Metrics with incompatible units or biological meaning are not summed together.
- Date, body region, facility, protocol, age range, and source filters support review.
- External dose records may be included only with clear provenance and confidence labeling.
- Any risk guidance is informational and requires human interpretation; no order is blocked autonomously.

## Frappe realization

- **Model:** a read projection over `OC Imaging Dose Record` avoids duplicating accepted source values.
- **Roles/permissions:** clinicians see their authorized patients; `OC Radiation Safety Reviewer` receives facility-level aggregate access.
- **Surfaces:** Script Report, Dashboard Charts, and patient timeline card show metric-specific trends and missing-data indicators.
- **API:** read-only `open_chart.api.v1.imaging.get_exposure_timeline` applies patient and facility permissions server-side.

## Boundaries

Owns: longitudinal dose projection and explanatory labels. Consumes: verified dose records and external evidence. Emits: patient and quality views. Does not own: risk diagnosis, exposure estimation science, or acquisition settings.

## Open questions

- Which normalized comparisons are clinically responsible enough to display across devices and protocols?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
