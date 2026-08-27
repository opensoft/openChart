# CDS Rule Testing Sandbox — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates draft CDS rules against synthetic patients and curated cases without access to production patients or authority to trigger clinical actions.
Topics: openchart-feature-catalog, cpoe, frappe, cds-sandbox
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-062 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Regression case packs** — Require safety and non-firing cases to pass before rule approval.

## Focus

This feature isolates reproducible pre-activation testing of rule logic and presentation.

## Behavior

- Authors select a draft rule version and synthetic `SYN-` case set.
- Runs show inputs, resolved values, missing data, branch trace, outcome, severity, message, latency, and errors.
- Expected outcomes support pass, fail, and reviewer-explained variance.
- The sandbox cannot query production patients, submit orders, send notifications, or change active rule state.
- Test runs pin rule, value-set, engine, and fixture versions for reproduction.
- Independent reviewers inspect required cases before approval.

## Frappe realization

- **DocTypes:** `OC CDS Synthetic Case`, child expected evaluations, and submitted `OC CDS Test Run` with versions, digest, outcomes, and actor.
- **Workflow:** case Draft → Reviewed → Approved; run Queued → Running → Passed/Failed/Error.
- **Roles/permissions:** `OC CDS Tester` uses synthetic fixtures only; publishers read results; production clinical roles gain no sandbox access by default.
- **Hooks/API/surface:** whitelisted run method enqueues isolated background jobs; server rejects non-`SYN-` identities; Script Report compares expected and actual outcomes.

## Boundaries

Owns: synthetic rule test execution and evidence. Consumes: draft rules, versioned value sets, and synthetic fixtures. Emits: reproducible test results. Does not own: production evaluation or rule approval.

## Open questions

- What minimum regression suite is required for each rule type and severity?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Ownership And Review Lifecycle](openchart-feature-catalog-ord-047-cds-ownership-and-review-lifecycle.md)
