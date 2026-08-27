# Adverse Event Following Immunization Report — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents suspected adverse events after immunization and assembles a reviewable reporting packet without asserting causality.
Topics: openchart-feature-catalog, public-health, frappe, immunization-adverse-event
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-020 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **External report connector** — Submit approved packets to an authorized adverse-event reporting service.

## Focus

Attributed adverse-event documentation, clinical follow-up, and report preparation explicitly separated from causal determination.

## Behavior

- Clinicians link one or more administrations and record onset, manifestations, seriousness, outcome, and reporter observations.
- The interface labels the relationship as suspected and never infers vaccine causality.
- States are draft, clinical-review, report-ready, submitted, follow-up-needed, closed, and entered-in-error.
- Seriousness criteria or missing follow-up create visible tasks but no autonomous external submission.
- Reporters review the exact outbound fields and authorization basis before release.
- Amendments preserve original observations, report versions, external identifiers, and response evidence.

## Frappe realization

- **DocTypes:** Add submittable `OC Immunization Adverse Event` with administration Links, symptom rows, outcome, follow-up, and report artifacts.
- **Workflow:** Require `OC Clinician` review and `OC Public Health Reporter` release; use Assignments for follow-up.
- **Permissions:** Protect sensitive narrative at permlevel 1 and apply patient User Permissions to every view and export.
- **API and surfaces:** Add guarded report preparation/submission hooks, a follow-up Query Report, and Jinja preview with explicit non-causality language.

## Boundaries

Owns: suspected-event record and reporting workflow. Consumes: immunizations, observations, consent or legal authority, and connector profile. Emits: approved report packets and follow-up tasks. Does not own: causality assessment, treatment, or regulator adjudication.

## Open questions

- Which seriousness criteria should trigger mandatory assignment versus advisory display?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
