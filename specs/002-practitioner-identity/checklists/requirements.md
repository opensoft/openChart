# Specification Quality Checklist: Practitioner Identity

**Purpose**: Validate specification completeness and quality before proceeding to planning

**Created**: 2026-08-27

**Feature**: [spec.md](../spec.md)

## Content Quality

- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

## Requirement Completeness

- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous
- [x] Success criteria are measurable
- [x] Success criteria are technology-agnostic (no implementation details)
- [x] All acceptance scenarios are defined
- [x] Edge cases are identified
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

## Feature Readiness

- [x] All functional requirements have clear acceptance criteria
- [x] User scenarios cover primary flows
- [x] Feature meets measurable outcomes defined in Success Criteria
- [x] No implementation details leak into specification

## Notes

**Result: all items pass** after two validation iterations.

Iteration 1 findings and fixes:

- *All functional requirements have clear acceptance criteria* — FR-027
  (the zone calculation must never infer a boundary the registry does
  not state) had no acceptance scenario and no success criterion. Fixed
  by adding User Story 3 acceptance scenario 10 (an act class the
  registry does not describe is refused rather than assigned an inferred
  or permissive zone), a matching edge case, SC-013, and the same
  refusal in SC-006's negative-test list.
- *Success criteria are technology-agnostic* — SC-006 said a refusal
  that stops firing "fails the build". Reworded to "is itself a
  failure", removing the delivery-pipeline reference.

Iteration 2: re-validated every item against the amended spec; no
further failures found.

Standing observations (not failures):

- **Domain vocabulary is retained deliberately.** Holder class (person,
  practitioner, organisation, agent), authority tier (attest, request,
  act, act_unsupervised), credential state, composition components and
  the green/yellow/red/black zones are openXwallet contract vocabulary,
  not implementation nouns. They are the terms the clinical and legal
  reviewers of this capability will use, and the governing change treats
  them as given. No product, framework, storage or language name appears
  anywhere in the specification.
- **"Composition hash" is stated as "composition identifier."** The
  governing change names a hash; the specification avoids the hashing
  mechanism and speaks only of an identifier computed over the declared
  composition components, so the requirement stays testable without
  fixing an algorithm.
- **Four decisions are recorded in Assumptions rather than as
  clarification markers**, each marked as made here and not in the
  governing change: the registry-version re-check between order staging
  and co-signature; the effect of a credential moving to suspended or
  revoked mid-course; the default breadth of an AI-treatment consent
  record's scope; and the explicit exclusion of the governing design's
  four open questions from this feature.
- **Scope boundary is asserted, not implied.** FR-044 and SC-009 make
  "no authority granted, no credential issued, no real license number
  bound" a checkable outcome of the feature rather than a caveat.

Coverage at validation time: 5 prioritized user stories, 36 acceptance
scenarios, 44 functional requirements, 14 success criteria, 12 key
entities, 13 edge cases — covering all thirteen requirements and
thirty-four scenarios of the governing change.
