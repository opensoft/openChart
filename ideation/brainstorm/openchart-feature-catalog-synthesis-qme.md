# Synthesis: Quality Measures And Regulatory Reporting — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects 35 governed capabilities into a reproducible quality-measure lifecycle from specification intake and patient evidence through simulation, submission, reconciliation, and audit.
Topics: openchart-feature-catalog, quality-reporting, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; catalog entry QME synthesis (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Continuous submission rehearsal** — Maintain a non-official, privacy-governed readiness package that exposes calculation, validation, evidence, and deadline defects throughout the year.

## Focus

This synthesis relates the QME catalog as one provenance-first reporting system while keeping derived quality results separate from clinical truth, external program authority, payment adjudication, and autonomous care actions.

## Members and their joints

### Specification, scope, and reproducible calculation

- [eCQM Execution Engine](openchart-feature-catalog-qme-001-ecqm-execution-engine.md) — Executes approved computable logic into versioned patient and aggregate outcomes.
- [Measure Library Version Imports](openchart-feature-catalog-qme-002-measure-library-version-imports.md) — Governs immutable specification releases, dependencies, and conformance cases.
- [Performance Period Configuration](openchart-feature-catalog-qme-003-performance-period-configuration.md) — Locks dates, entities, measures, and source cutoffs into a reusable scope.
- [Measure Population Drill Down](openchart-feature-catalog-qme-004-measure-population-drill-down.md) — Opens aggregate rates into permission-bound population lists and rule explanations.
- [Measure Result Provenance Trace](openchart-feature-catalog-qme-005-measure-result-provenance-trace.md) — Preserves the logic, terminology, input versions, and integrity evidence behind each classification.
- [Measure Steward Feed Ingestion](openchart-feature-catalog-qme-015-measure-steward-feed-ingestion.md) — Brings external changes into quarantine and impact review rather than automatic activation.

Steward receipts become reviewed library releases; approved releases and performance-period fingerprints bind each engine run. Drill-down and provenance then make every aggregate rate explainable without allowing reviewers to rewrite either the specification or clinical source record.

### Gap operations, validation, and evidence completion

- [Patient Measure Gap Worklists](openchart-feature-catalog-qme-006-patient-measure-gap-worklists.md) — Assigns reporting gaps for supervised follow-up without prescribing care.
- [eCQM Validation Resolution Workflow](openchart-feature-catalog-qme-016-ecqm-validation-resolution-workflow.md) — Normalizes errors across calculation, mapping, and package stages into accountable resolution.
- [Reporting Data Completeness Checker](openchart-feature-catalog-qme-017-reporting-data-completeness-checker.md) — Distinguishes missing, late, unmapped, invalid, and inaccessible reporting data before close.
- [Manual Chart Abstraction Entry](openchart-feature-catalog-qme-018-manual-chart-abstraction.md) — Supplies reviewed, measurement-only facts from source documents when discrete evidence is unavailable.
- [Point Of Care Measure Exclusion Capture](openchart-feature-catalog-qme-019-point-of-care-exclusion-capture.md) — Captures clinician-authored exclusion evidence while leaving final classification to measure logic.

Completeness and validation findings become assignments, not hidden coercions. Corrections follow the normal succession path; manual abstraction remains explicitly measurement-only; clinician exclusion evidence is evaluated rather than assumed, and every change drives bounded recalculation and trace succession.

### Program participation, scoring, and organizational views

- [MIPS Participation Tracking](openchart-feature-catalog-qme-007-mips-participation-tracking.md) — Records eligibility, reporting pathway, identifiers, category choices, and readiness.
- [Promoting Interoperability Objectives Status](openchart-feature-catalog-qme-008-promoting-interoperability-status.md) — Combines calculated events, documentary evidence, exclusions, and attestations by objective.
- [Quality Category Score Simulation](openchart-feature-catalog-qme-009-quality-score-simulation.md) — Estimates non-official scores under explicit benchmarks and assumptions before submission.
- [Value Based Attribution Reporting](openchart-feature-catalog-qme-012-value-based-attribution-reporting.md) — Applies versioned CPC+, ACO-style, and similar rosters to quality populations.
- [Provider And Practice Score Views](openchart-feature-catalog-qme-020-provider-practice-score-views.md) — Rolls patient results into provider, facility, TIN, and practice views with suppression.
- [Payment Model Scenario Modeling](openchart-feature-catalog-qme-021-payment-model-scenario-modeling.md) — Explores payment sensitivity without becoming an official payer or accounting calculation.
- [Multi TIN Taxonomy Reporting Splits](openchart-feature-catalog-qme-035-multi-tin-taxonomy-reporting.md) — Resolves effective-dated entity relationships for multi-TIN and taxonomy outputs.

Participation and attribution define who is measured and at which organizational level. Transparent rollups feed score and payment scenarios, while identifier snapshots and uncertainty labels prevent local forecasts from being mistaken for regulator scores or payer settlement.

### Standards, mappings, and submission profiles

- [QRDA I Submission Generation](openchart-feature-catalog-qme-010-qrda-i-submission-generation.md) — Creates validated patient-level reporting documents from locked results and authorized evidence.
- [QRDA III Returned Score Import](openchart-feature-catalog-qme-011-qrda-iii-returned-score-import.md) — Reconciles aggregate external feedback against local submissions without overwriting local results.
- [HEDIS Aligned Measure Mapping Views](openchart-feature-catalog-qme-013-hedis-measure-mapping-views.md) — Describes exact, partial, transformed, and unsupported alignment under licensing constraints.
- [State Quality Program Exports](openchart-feature-catalog-qme-014-state-quality-program-exports.md) — Uses jurisdiction-specific profiles to generate traceable state packages.
- [Clinical Registry Submission Packages](openchart-feature-catalog-qme-022-clinical-registry-submission-packages.md) — Assembles consent-aware diabetes, hypertension, and similar collaborative datasets.

Mappings mediate among clinical data, measure semantics, and destination profiles. QRDA, state, and registry packages share release, manifest, validation, consent, and checksum controls; returned scores become external assertions whose variance can improve mappings without rewriting history.

### Clinical-domain measure adapters

- [Immunization Measure Reporting Hooks](openchart-feature-catalog-qme-023-immunization-measure-reporting-hooks.md) — Reuses dose provenance and validity decisions without duplicating vaccine records.
- [Preventive Care Measure Automation](openchart-feature-catalog-qme-024-preventive-care-measure-automation.md) — Maps screening evidence while exposing divergence between care guidance and reporting rules.
- [Chronic Care Management Time Compliance Reporting](openchart-feature-catalog-qme-025-ccm-time-compliance-reporting.md) — Reconciles monthly CCM activity and time evidence without creating claims.
- [Transitional Care Management Compliance Tracker](openchart-feature-catalog-qme-026-tcm-compliance-tracker.md) — Tracks discharge-to-contact, reconciliation, and visit milestones.
- [Behavioral Health Integration Measures](openchart-feature-catalog-qme-027-behavioral-health-measures.md) — Evaluates sensitive screening and follow-up evidence under bounded disclosure.
- [Maternal Health Measure Bundle](openchart-feature-catalog-qme-028-maternal-health-measure-bundle.md) — Relates prenatal, delivery, outcome, and postpartum evidence through governed episodes.
- [Pediatric Development Screening Measures](openchart-feature-catalog-qme-029-pediatric-development-screening-measures.md) — Handles age windows, instrument versions, proxy provenance, and follow-up.
- [Social Determinants Measure Capture](openchart-feature-catalog-qme-030-social-determinants-measure-capture.md) — Measures social-needs screening and response without inferring risk or broadening sensitive access.

These adapters preserve domain-specific evidence meaning and privacy while presenting a normalized measurement interface. They let shared engines and drill-downs operate consistently, yet prevent regulatory logic from replacing immunization validity, preventive guidance, care management, behavioral health, maternal, pediatric, or SDOH clinical authority.

### Reporting control plane, correction, and audit

- [Annual Reporting Calendar And Deadline Alerts](openchart-feature-catalog-qme-031-reporting-calendar-deadline-alerts.md) — Joins external dates to internal readiness milestones, owners, and escalation.
- [Submission History And Receipts](openchart-feature-catalog-qme-032-submission-history-receipts.md) — Archives released artifacts, transport events, acknowledgments, receipts, and disposition.
- [Amendment And Resubmission Handling](openchart-feature-catalog-qme-033-amendment-resubmission-handling.md) — Produces governed successor submissions with recalculation and impact diffs.
- [Auditor Evidence Package Assembly](openchart-feature-catalog-qme-034-auditor-evidence-package.md) — Builds purpose-bound, integrity-manifested audit evidence under privacy review.

The calendar drives accountable readiness rather than mere reminders. Release creates immutable submission history; destination feedback or corrected evidence starts a successor chain; and the same hashes, approvals, traces, waivers, manifests, and receipts can be recombined into a minimum-necessary auditor package.

## Frappe realization

- Use focused `OC` standard, submittable, and child DocTypes for releases, periods, runs, patient results, traces, issues, packages, submissions, receipts, and evidence; accepted artifacts use successor links rather than in-place mutation.
- Keep supported writes under guarded `open_chart.api.v1.quality` whitelisted methods, with idempotency for imports and transport events and read-only auto-REST only where permission behavior is safe.
- Apply patient, provider, facility, TIN, program, purpose, and sensitive-record User Permissions plus permlevels across Desk, reports, exports, portal surfaces, and background jobs.
- Run calculation, validation, completeness, package generation, reconciliation, deadline, and integrity work in rq or scheduler events with bounded retry, realtime status, and PHI-safe logs.
- Govern measure, terminology, mapping, benchmark, scoring, profile, and program releases with effective dates, synthetic conformance fixtures, author/approver separation, and explicit retirement.
- Deliver a Quality Reporting workspace with Script and Query Reports, Kanban exception queues, Calendar/Gantt milestones, Dashboard Charts, Number Cards, Jinja manifests, and permissioned evidence downloads.

## Boundaries

Owns: quality specification lifecycle, reporting scopes, derived results, provenance, gap and exception operations, simulation, package assembly, submission succession, receipts, and audit evidence. Consumes: accepted clinical records, identity, consent, authority, terminology, provider and organization identifiers, attribution, external program specifications, and destination responses. Emits: explainable measure results, supervised worklists, non-official scenarios, validated packages, submission history, amendments, and evidence manifests. Does not own: clinical diagnosis or treatment, autonomous outreach or orders, claims and accounting, payer settlement, regulator authority, proprietary measure rights, or external acceptance.

## Emergent behavior

Together these members create a continuous evidence chain rather than a year-end export utility. A steward release and performance scope can be traced through every patient classification, gap disposition, rollup, simulation, package field, receipt, correction, and audit item. Because source amendments, mapping changes, and external feedback produce successors and bounded recalculation, openChart can explain not only a submitted rate but why it changed and what evidence authorized the change.

## Tensions to hold

- Regulatory reproducibility requires frozen releases and cutoffs, while patient records and measure guidance continue to change.
- Patient-level drill-down and audit usefulness must coexist with minimum-necessary access, sensitive-domain restrictions, and small-cell suppression.
- Manual abstraction and point-of-care exclusion capture can close real evidence gaps but must not become incentive-driven rewriting of clinical truth.
- First-party destination profiles improve usability but create substantial licensing, conformance, maintenance, and support obligations.
- Score and payment scenarios support planning only if uncertainty and non-official status remain impossible to miss.
- Timely submission pressure must not bypass validation, approval separation, consent, provenance, or amendment controls.

## Recombination opportunities

- Combine steward feeds, library impact analysis, synthetic tests, and continuous rehearsal into a measure-release upgrade program.
- Combine completeness heatmaps, validation ownership, patient drill-down, gap worklists, and exclusion review into a pre-close quality operations cockpit.
- Combine participation, attribution, multi-TIN relationships, rollups, scoring simulation, and payment scenarios into an explainable value-based planning studio.
- Combine clinical-domain adapters, result traces, and privacy-aware drill-down into specialty measure bundles without duplicating source records.
- Combine package manifests, submission receipts, amendment diffs, returned-score variances, and audit assembly into a regulator-ready evidence chain.

## Open questions

- Which computable measure languages, terminology services, and redistribution models can openChart support as first-party capabilities?
- Which destination profiles should receive supported-product status, and what conformance and release service level is sustainable?
- What patient-level retention, redaction, small-cell, and purpose controls should apply across quality operations and audits?
- Which payment and contract assumptions belong in openChart versus a governed openPractice integration?
- Where may site policy authorize automatic package transport after approval, and where must release remain an explicit human action?

## Relationships

[Catalog anchor: Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
