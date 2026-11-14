# Amendment And Resubmission Handling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates governed successor submissions for corrected data, scope, mappings, or destination feedback while preserving the original record and rationale.
Topics: openchart-feature-catalog, quality-reporting, frappe, resubmission
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-033 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Amendment impact diff** — Show changed patients, counts, mappings, files, and scores between original and successor packages.

## Focus

Succession-based reporting correction with explicit cause, authority, changed scope, and receipt reconciliation.

## Behavior

- An authorized submitter starts an amendment from a released submission and selects correction reason and affected scope.
- Causes include source-record succession, identity correction, mapping defect, measure release, scope correction, or destination request.
- The system identifies stale calculations and requires recalculation and validation before successor package approval.
- A diff shows changed artifacts, patients, population counts, rates, identifiers, mappings, and disclosure scope.
- Unchanged artifacts may be referenced only when destination rules permit and the manifest remains explicit.
- The original submission and receipts remain immutable and linked to the successor chain.
- Release requires approval, deadline status, destination method, and amendment narrative.

## Frappe realization

- **DocTypes:** Add `OC Quality Submission Amendment` with predecessor/successor Links, reason, affected scope JSON, diff summary, approvals, deadline, and destination instruction.
- **Workflow:** Use initiated, impact-review, recalculating, validating, approval, released, acknowledged, rejected, and superseded states.
- **Jobs and API:** Compute diffs and regenerate affected artifacts in rq through guarded amend and release methods.
- **Surfaces:** Provide side-by-side diff Script Reports, amendment chain timeline, approval form, and revised manifest Print Format.

## Boundaries

Owns: submission succession, impact analysis, and resubmission evidence. Consumes: prior submissions, corrected sources, recalculated results, profiles, and destination requests. Emits: successor packages and amendment narratives. Does not own: clinical amendment authority or destination acceptance.

## Open questions

- Which correction types require full replacement versus delta submission for each destination profile?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
