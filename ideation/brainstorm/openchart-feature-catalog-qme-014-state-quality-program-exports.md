# State Quality Program Exports — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates jurisdiction-specific quality program files from governed profiles while preserving validation, disclosure, and release evidence.
Topics: openchart-feature-catalog, quality-reporting, frappe, state-quality-export
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-014 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Managed profile releases** — Distribute signed state-profile updates with synthetic conformance fixtures and support windows.

## Focus

Reusable export orchestration around state-specific fields, code sets, formats, and deadlines.

## Behavior

- An administrator selects jurisdiction, program, period, organization scope, and an approved export profile.
- Profiles define required fields, mappings, format, validation rules, minimum-cell policy, and transport handoff metadata.
- Generation reports included, excluded, suppressed, and error records before release.
- Missing jurisdiction identifiers or required values block only affected records when the profile permits partial packages.
- Reviewers can trace every output field to a result, source record, or approved constant.
- Released packages are immutable and carry profile version, manifest, checksum, approver, and disclosure purpose.
- Specification changes create successor profiles and never silently alter prior packages.

## Frappe realization

- **DocTypes:** Add `OC Quality Export Profile`, `OC State Quality Package`, and child mapping, validation, manifest, and exception rows.
- **Workflow:** Govern profiles through draft/review/approved/retired and packages through generating/failed/review/approved/released/superseded.
- **Jobs and API:** Generate in rq through guarded `open_chart.api.v1.quality.create_state_export`; store secrets outside profile records.
- **Surfaces:** Provide package dashboards, exception Script Reports, Jinja manifests, and permissioned downloads.

## Boundaries

Owns: state export profiles, package creation, validation, and release evidence. Consumes: quality results, identifiers, jurisdiction rules, and disclosure authority. Emits: authorized state-program packages. Does not own: regulator transport, acceptance, or source specification authority.

## Open questions

- Which states and programs justify first-party maintained profiles and conformance service levels?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
