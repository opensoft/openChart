# Teaching File Flagging — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Nominates imaging cases for education with consent, privacy, attribution, review, and de-identification status kept separate from clinical records.
Topics: openchart-feature-catalog, imaging, frappe, teaching-files
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-029 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Curriculum collections** — Curate approved cases by diagnosis, modality, difficulty, and learning objective.

## Focus

This feature isolates case nomination and governance before any educational publication or export.

## Behavior

- An authorized clinician flags a study or report and records educational rationale and proposed audience.
- The nomination references source records without altering their clinical state.
- A reviewer verifies consent or approved use basis, privacy requirements, attribution, and de-identification plan.
- Restricted cases cannot be exported or broadly searched until approval conditions are met.
- Revocation or changed consent suspends future educational use while preserving audit evidence.
- Approval does not imply that openChart stores or publishes image pixels.

## Frappe realization

- **DocTypes:** `OC Teaching File Nomination` with source Links, learning tags, use basis, de-identification status, reviewer, and restrictions.
- **Workflow:** Nominated → Privacy Review → Approved → Published Reference, with Rejected, Suspended, and Retired states.
- **Roles/permissions:** clinicians nominate; privacy and education reviewers approve; learners access only approved scoped references.
- **API/surfaces:** guarded export manifest method; Desk workspace for review; tags and filtered search exclude unapproved cases.

## Boundaries

Owns: teaching nomination, governance, and approved reference metadata. Consumes: study, report, consent, and privacy decisions. Emits: controlled educational manifest. Does not own: learning platform, publication, or image de-identification engine.

## Open questions

- Which educational uses require patient consent versus another documented legal or institutional basis?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
