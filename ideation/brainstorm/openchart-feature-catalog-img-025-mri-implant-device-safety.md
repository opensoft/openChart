# MRI Implant and Device Safety — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Verifies implanted-device and foreign-body MRI conditions against source evidence, scanner parameters, and human safety approval.
Topics: openchart-feature-catalog, imaging, frappe, mri-safety
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-025 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Device evidence packet** — Assemble manufacturer documents and prior safety decisions for review.

## Focus

This feature isolates MRI compatibility assessment for implants, devices, and retained foreign bodies.

## Behavior

- Screening captures device type, manufacturer, model, identifier, implant site, date, and source evidence when available.
- The reviewer classifies each item as MR Safe, MR Conditional, MR Unsafe, Unknown, or Not Applicable.
- Conditional items require explicit scanner field strength, coil, positioning, timing, and operating constraints.
- Unknown or conflicting evidence blocks routine readiness and creates a safety-review assignment.
- An authorized MRI safety role documents the final episode-specific decision and any required monitoring.
- A new device record, changed scanner, or revised evidence invalidates incompatible prior clearance.

## Frappe realization

- **DocTypes:** `OC MRI Safety Assessment` with child `OC MRI Device Review`, evidence Files, conditions, scanner Link, policy version, and expiry.
- **Workflow:** Screening → Evidence Review → Conditional Plan → Cleared or Not Cleared, with Exception Review.
- **Roles/permissions:** technologists collect; `OC MRI Safety Officer` approves; device evidence is readable by the care team under patient permissions.
- **Hooks/API/surfaces:** readiness hook checks all device rows; Desk form exposes conditional checklist; API returns conditions without exposing restricted attachments broadly.

## Boundaries

Owns: episode-specific MRI safety review and conditions. Consumes: implant records, patient answers, manufacturer evidence, and scanner data. Emits: MRI readiness plan. Does not own: device registry truth or autonomous compatibility determination.

## Open questions

- What source hierarchy resolves conflicts between patient reports, implant records, and manufacturer labeling?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
