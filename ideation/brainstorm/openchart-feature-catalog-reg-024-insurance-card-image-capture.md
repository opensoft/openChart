# Insurance Card Image Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures front and back insurance-card images with quality, consent, provenance, and restricted retention controls.
Topics: openchart-feature-catalog, registration, frappe, insurance-card-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-024 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Card refresh detection** — Prompt for a new image when policy numbers or effective dates change.

## Focus

Manage insurance-card evidence separately from the structured coverage record.

## Behavior

- Staff or self-registering patients capture front and back card images for a selected coverage.
- The interface checks blur, glare, cropping, and unreadable text before upload completes.
- Each side records source device, actor, timestamp, consent, and linked coverage.
- A replacement card supersedes prior images without deleting their provenance.
- Routine clinical users see that evidence exists but cannot open the private files.
- Failed or canceled captures do not create misleading active card records.

## Frappe realization

- **DocTypes:** `OC Coverage Card` linked to `OC Patient Coverage`, with private front/back Attach fields, quality state, consent, active, and supersedes.
- **Workflow:** Draft → Captured → Quality Accepted → Active → Superseded or Rejected.
- **Roles/permissions:** `OC Registration Clerk` captures; `OC Coverage Reviewer` accesses files at permlevel 2; portal owner can upload own draft.
- **API/surfaces:** `open_chart.api.v1.registration.capture_coverage_card`; responsive camera page, coverage evidence tab, and stale-card report.

## Boundaries

Owns: insurance-card image custody and lifecycle. Consumes: coverage link and captured files. Emits: controlled card-evidence reference. Does not own: OCR or eligibility verification.

## Open questions

- How long should superseded card images remain accessible to coverage reviewers?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
