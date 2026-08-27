# Preliminary-to-Final Report Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs wet reads and resident preliminary reports through attending review, discrepancy handling, final attestation, and visible state transitions.
Topics: openchart-feature-catalog, imaging, frappe, preliminary-reporting
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-009 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Preliminary discrepancy learning** — Aggregate reviewed differences for education without punitive automatic scoring.

## Focus

This feature isolates provisional interpretation and the authority handoff to a final report.

## Behavior

- Authorized readers may issue a wet read or resident preliminary interpretation with explicit provisional labeling.
- Recipients see author, timestamp, scope, and a warning that the interpretation is not final.
- An attending reviews the preliminary text, images, and any documented communication before attestation.
- Material differences require a discrepancy classification and determine whether renewed communication is required.
- Final signature closes the preliminary state but never erases what was previously disclosed.
- Overdue preliminary reviews appear in accountable queues and escalation reports.

## Frappe realization

- **DocTypes:** `OC Imaging Interpretation Version` links one report episode, author, supervision relationship, disclosure recipients, and discrepancy classification.
- **Workflow:** Draft → Preliminary Issued → Attending Review → Final Accepted, with Returned for Revision and Superseded states.
- **Roles/permissions:** `OC Resident Reader` or `OC Wet Reader` issues preliminary text; `OC Attending Radiologist` alone finalizes under configured policy.
- **Hooks/API/surfaces:** workflow actions create immutable disclosure events; Notifications route review; timeline and Print Format label every version state.

## Boundaries

Owns: interpretation states, supervision, attestation, and discrepancy evidence. Consumes: report draft, image context, and staffing authority. Emits: provisional and final result events. Does not own: training program administration.

## Open questions

- Which wet-read scenarios permit non-radiologist authors and what attestation deadline applies?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
