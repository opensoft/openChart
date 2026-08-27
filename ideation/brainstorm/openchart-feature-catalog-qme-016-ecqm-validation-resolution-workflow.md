# eCQM Validation Resolution Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes specification, calculation, mapping, and submission validation failures to accountable owners with evidence-backed resolution.
Topics: openchart-feature-catalog, quality-reporting, frappe, validation-resolution
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-016 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Recurring defect clusters** — Group repeated errors by root cause and suggest governed remediation playbooks.

## Focus

A unified exception lifecycle that resolves reporting defects without permitting quality staff to rewrite clinical source data.

## Behavior

- Engines, imports, mappings, and package validators create normalized issues with severity, stage, code, evidence, and affected scope.
- Issues are deduplicated by error fingerprint while retaining every occurrence.
- Triage assigns an owner category: source-data review, identity, terminology, mapping, configuration, specification, or connector.
- Owners can resolve, waive, defer, escalate, or mark false-positive with rationale and evidence.
- Clinical corrections require the normal provenance-preserving amendment path and trigger recalculation afterward.
- Waivers require elevated approval, expiry, and visibility in readiness and evidence packages.
- Repeated or reopened failures retain their full activity history and successor links.

## Frappe realization

- **DocTypes:** Add `OC Quality Validation Issue` and `OC Validation Occurrence` with fingerprint, source Dynamic Link, severity, owner class, disposition, waiver, and evidence.
- **Workflow:** Use new, triaged, assigned, remediating, resolved, waived, deferred, reopened, and superseded states.
- **Hooks and API:** Offer a normalized issue-creation service and guarded disposition methods; enqueue affected recalculation after accepted corrections.
- **Surfaces:** Provide Kanban by owner, SLA Query Reports, Assignment Rules, Notifications, and issue links from package and run forms.

## Boundaries

Owns: quality-validation issue lifecycle and evidence. Consumes: validator outputs, permissions, assignments, and correction events. Emits: dispositions, waivers, escalations, and recalculation requests. Does not own: direct clinical edits or external validator policy.

## Open questions

- Which severity classes may be waived locally without making a package ineligible for release?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
