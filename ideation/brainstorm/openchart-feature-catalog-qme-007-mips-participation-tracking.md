# MIPS Participation Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks clinician eligibility, reporting choices, category obligations, and submission readiness across a MIPS performance year.
Topics: openchart-feature-catalog, quality-reporting, frappe, mips-participation
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-007 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Participation option comparison** — Compare individual, group, subgroup, and alternative payment model reporting paths.

## Focus

An operational register of who participates, under which identifiers and pathway, and which obligations remain unresolved.

## Behavior

- A quality administrator records clinician, NPI, TIN, participation pathway, eligibility source, and attestation evidence.
- The register distinguishes individual, group, subgroup, virtual group, and alternative payment model participation.
- Eligibility evidence can be pending, confirmed, disputed, exempt, or superseded.
- Category and measure selections carry effective dates, owners, reporting methods, and completeness status.
- Identifier conflicts or missing eligibility evidence block readiness rather than guessing participation.
- Dashboards show coverage, unresolved decisions, data sufficiency, and approaching milestones.
- Changes after lock require approval and invalidate affected simulations or packages.

## Frappe realization

- **DocTypes:** Add `OC MIPS Participation` with child category, clinician, identifier, measure-selection, and evidence rows.
- **Workflow:** Use draft, eligibility-review, configured, locked, submitted, and superseded states with dual approval for late changes.
- **Permissions and API:** Scope `OC Quality Administrator` by TIN User Permission and expose guarded participation read/update methods.
- **Surfaces:** Provide a MIPS workspace, readiness Script Report, Dashboard Charts, and deadline Notifications.

## Boundaries

Owns: local participation configuration and evidence. Consumes: clinician identities, organization identifiers, program rules, and measure selections. Emits: readiness state and reporting scope. Does not own: CMS eligibility determinations, payment calculations, or credentialing.

## Open questions

- Which external eligibility sources can be imported with durable provenance?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
