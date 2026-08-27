# Zero-footprint DICOM Viewer Embed — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Launches an external web DICOM viewer inside clinical context using short-lived authorization without storing image pixels in openChart.
Topics: openchart-feature-catalog, imaging, frappe, dicom-viewer
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-013 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Context-preserving viewer return** — Restore the exact chart and report task after the viewer closes.

## Focus

This feature isolates secure contextual viewer launch and embed behavior at the openChart/PACS boundary.

## Behavior

- An authorized user launches the viewer from an order, report, timeline item, or comparison task.
- The server resolves patient and study identifiers only after row-level permission checks.
- Launch credentials are short-lived, audience-bound, single-purpose, and excluded from URLs or logs where feasible.
- The UI clearly identifies the external viewer and handles blocked embedding with a secure new-window fallback.
- Missing studies, identifier conflicts, expired sessions, and PACS outages produce distinct recoverable errors.
- Launch and access outcomes are audited without copying diagnostic images into openChart storage.

## Frappe realization

- **DocTypes:** `OC Imaging Viewer Connection` stores endpoint, authentication mode, facility scope, and identifier mapping policy.
- **Roles/permissions:** clinicians and imaging roles need both chart and study access; connection secrets remain restricted at permlevel 2.
- **API/surfaces:** `open_chart.api.v1.imaging.create_viewer_session` returns a short-lived launch envelope; Desk page embeds via approved CSP origins.
- **Hooks/audit:** launch events record user, patient, study, connection, result, and correlation ID; no pixels are attached to Frappe Files.

## Boundaries

Owns: authorized viewer context and launch audit. Consumes: chart permissions, study identifiers, and viewer capabilities. Emits: short-lived viewer sessions. Does not own: rendering, diagnostic tools, image storage, or PACS availability.

## Open questions

- Which viewer authentication profiles can meet both iframe security and single sign-on requirements?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
