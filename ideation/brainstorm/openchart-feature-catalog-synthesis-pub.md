# Synthesis: Immunizations Public Health And Registries — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects 40 governed capabilities into a provenance-aware public-health system spanning immunizations, managed registry exchange, screening programs, reporting, and emergency response.
Topics: openchart-feature-catalog, public-health, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB synthesis (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Managed public-health connector program** — Ship signed, tested state-profile releases with observable conformance and bounded support lifecycles.

## Focus

This synthesis relates the PUB catalog as one governed graph while preserving patient identity, consent, clinical authority, source provenance, succession-based amendments, minimum-necessary disclosure, and human control over clinical and external-reporting actions.

## Members and their joints

### Immunization record and clinical interpretation

- [Immunization Administration Record](openchart-feature-catalog-pub-001-immunization-administration-record.md) — Records a coded, attributable local vaccine event.
- [Vaccine Dose Product And Site Capture](openchart-feature-catalog-pub-002-vaccine-dose-product-and-site-capture.md) — Adds product, lot, dose, route, site, and funding snapshots.
- [Immunization Schedule Engine](openchart-feature-catalog-pub-003-immunization-schedule-engine.md) — Evaluates versioned series rules against accepted evidence.
- [Immunization Catch Up Calculation](openchart-feature-catalog-pub-004-immunization-catch-up-calculation.md) — Derives explainable catch-up timing from valid prior doses.
- [Vaccines Due Today Forecast](openchart-feature-catalog-pub-005-vaccines-due-today-forecast.md) — Presents current due states and missing-data conditions.
- [Invalid Immunization Dose Review](openchart-feature-catalog-pub-006-invalid-immunization-dose-review.md) — Routes age, interval, product, and series exceptions to humans.
- [Historical Immunization Entry](openchart-feature-catalog-pub-007-historical-immunization-entry.md) — Preserves sourced prior-dose assertions and verification state.
- [Parent Reported Immunization Dose](openchart-feature-catalog-pub-008-parent-reported-immunization-dose.md) — Retains caregiver reports as explicitly unverified evidence.

Administrations and historical assertions remain separate sources; validity review determines which evidence the schedule engine may count, while forecasts and catch-up plans expose rather than erase uncertainty.

### Registry exchange and connector operations

- [Registry Query At Patient Registration](openchart-feature-catalog-pub-009-registry-query-at-patient-registration.md) — Starts asynchronous, consent-aware history retrieval.
- [VXU Registry Submission](openchart-feature-catalog-pub-010-vxu-registry-submission.md) — Sends accepted immunization events through managed connectors.
- [Registry Acknowledgment And Error Queue](openchart-feature-catalog-pub-011-registry-acknowledgment-error-queue.md) — Correlates responses and owns remediation accountability.
- [State Registry Format Profiles](openchart-feature-catalog-pub-012-state-registry-format-profiles.md) — Versions jurisdiction-specific formats, mappings, validation, and transport.
- [Multi State Registry Targeting](openchart-feature-catalog-pub-013-multi-state-registry-targeting.md) — Selects explainable targets for mobile and cross-state patients.
- [Registry Submission Reconciliation](openchart-feature-catalog-pub-014-registry-submission-reconciliation.md) — Measures sent, accepted, rejected, excluded, and missing events.

Target decisions and immutable clinical events feed profile-versioned messages; acknowledgments close the loop, and reconciliation makes connector quality measurable. First-party managed profiles are the differentiation from implementer-owned state configuration.

### Vaccine program operations and portable evidence

- [Vaccine Declination And Objection Documentation](openchart-feature-catalog-pub-015-vaccine-declination-and-objection.md) — Separates bounded objections from contraindications and due state.
- [Vaccine Lot Inventory And Expiry Quarantine](openchart-feature-catalog-pub-016-vaccine-lot-inventory-and-expiry-quarantine.md) — Controls clinic lot balances and usability.
- [VFC Eligibility Documentation](openchart-feature-catalog-pub-017-vfc-eligibility-documentation.md) — Records program eligibility and administration-time funding snapshots.
- [VIS Distribution And Version Log](openchart-feature-catalog-pub-018-vis-distribution-version-log.md) — Proves edition- and language-specific information delivery.
- [Mass Vaccination Clinic Mode](openchart-feature-catalog-pub-019-mass-vaccination-clinic-mode.md) — Accelerates safe multi-patient entry under session controls.
- [Adverse Event Following Immunization Report](openchart-feature-catalog-pub-020-adverse-event-following-immunization-report.md) — Coordinates suspected-event follow-up without asserting causality.
- [Immunization Clearance Form Generation](openchart-feature-catalog-pub-026-immunization-clearance-form-generation.md) — Issues purpose-bound school, camp, and work clearances.
- [Travel Medicine Consultation](openchart-feature-catalog-pub-027-travel-medicine-consultation.md) — Relates itinerary and reviewed destination guidance.
- [Immunization Certificate Printing](openchart-feature-catalog-pub-040-immunization-certificate-printing.md) — Creates signed as-of portable immunization records.

Inventory, eligibility, disclosure, rapid administration, and adverse-event follow-up form the operational envelope around the clinical dose; clearance and certificate artifacts compose verified history without becoming a second source of truth.

### Public-health reporting and surveillance

- [Communicable Disease Case Reporting](openchart-feature-catalog-pub-022-communicable-disease-case-reporting.md) — Governs case packet review, disclosure, delivery, and follow-up.
- [Syndromic Surveillance Export](openchart-feature-catalog-pub-023-syndromic-surveillance-export.md) — Produces minimized encounter surveillance feeds.
- [Electronic Case Report Trigger Capture](openchart-feature-catalog-pub-024-electronic-case-report-trigger-capture.md) — Captures rule evidence from accepted problem and laboratory context.
- [Reportable Condition Worklist](openchart-feature-catalog-pub-025-reportable-condition-worklist.md) — Joins trigger evidence, deadlines, assignments, and reporting state.

Triggers create candidates rather than diagnoses; accountable reviewers decide whether and what to report, connector evidence tracks disclosure, and the worklist keeps statutory timing visible without bypassing clinical authority.

### Screening programs and accountable follow-up

- [Tuberculosis Screening And Read Tracking](openchart-feature-catalog-pub-021-tuberculosis-screening-and-read-tracking.md) — Coordinates PPD and IGRA milestones and overdue review.
- [Preventive Screening Rule Engine](openchart-feature-catalog-pub-028-preventive-screening-rule-engine.md) — Produces graded, explainable preventive due states.
- [Cancer Screening Outreach Tracking](openchart-feature-catalog-pub-029-cancer-screening-outreach-tracking.md) — Tracks supervised cancer care-gap outreach and responses.
- [FIT Kit Mailing Program](openchart-feature-catalog-pub-030-fit-kit-mailing-program.md) — Closes the loop from mailed kit through result review.
- [STI Screening Program Workflow](openchart-feature-catalog-pub-031-sti-screening-program-workflow.md) — Coordinates confidential screening and follow-up.
- [Prenatal Screening Panel Tracking](openchart-feature-catalog-pub-032-prenatal-screening-panel-tracking.md) — Tracks gestational-window panels and unresolved components.
- [Newborn Screen Coordination](openchart-feature-catalog-pub-033-newborn-screen-coordination.md) — Relates infant tests, results, repeats, and referrals.
- [Pediatric Lead Screening Surveillance](openchart-feature-catalog-pub-034-pediatric-lead-screening-surveillance.md) — Coordinates lead results, confirmation, and reporting candidates.
- [Refugee And Immigrant Intake Screening](openchart-feature-catalog-pub-035-refugee-immigrant-intake-screening.md) — Applies respectful program checklists without origin-based diagnosis.
- [Occupational Health Screening Program](openchart-feature-catalog-pub-036-occupational-health-screening-program.md) — Separates clinical evidence from employer-facing conclusions.

Versioned rules identify reviewable gaps; program episodes coordinate orders, results, outreach, and referrals while consent, confidentiality, proxy rules, and purpose-bound disclosure vary by population and program.

### Emergency response and population accountability

- [Outbreak Response Mode](openchart-feature-catalog-pub-037-outbreak-response-mode.md) — Activates temporary, approved protocols and rapid surfaces.
- [Public Health Emergency Inventory Draw](openchart-feature-catalog-pub-038-public-health-emergency-inventory-draw.md) — Tracks incident stock custody and reconciliation.
- [Population Immunization Coverage Dashboard](openchart-feature-catalog-pub-039-population-immunization-coverage-dashboard.md) — Measures transparent, privacy-protected cohort coverage.

Incident mode binds temporary permissions, protocol versions, rapid records, and inventory movements; stable aggregate definitions then make response and routine coverage visible without weakening small-cell privacy or source-record provenance.

## Frappe realization

- Reuse `OC Patient` and existing provenance-bearing condition, observation, order, result, encounter, and document references; add focused `OC` DocTypes with naming series, child evidence rows, and immutable accepted versions.
- Keep supported writes under guarded `open_chart.api.v1` whitelisted methods; use read-only auto-REST where safe, idempotency keys for exchange, and successor records for accepted clinical amendments.
- Govern schedule, screening, trigger, connector, jurisdiction, template, and incident releases through Frappe Workflows with effective dates, synthetic conformance fixtures, and distinct author/approver roles.
- Run registry, surveillance, evaluation, notification, expiry, aggregate, and deadline work in rq or scheduler jobs with bounded retry, realtime status, and PHI-safe structured logs.
- Apply patient, facility, employer, jurisdiction, and incident User Permissions plus permlevels and purpose/consent checks across Desk, portal, report, print, and API surfaces.
- Deliver Public Health and Immunization Desk workspaces, Query/Script Reports, Kanban queues, Calendar/Gantt milestones, Dashboard Charts, Number Cards, Jinja Print Formats, and permissioned portal pages.

## Boundaries

Owns: public-health clinical records, program coordination, rules/evaluation provenance, managed connector profiles, reporting evidence, vaccine operations, and privacy-governed aggregate views. Consumes: patient identity, encounters, accepted problems/orders/results, consent and authority, terminology, facilities, external specifications, and agency responses. Emits: forecasts, review tasks, portable records, authorized public-health messages, operational exceptions, and aggregate measures. Does not own: autonomous diagnosis or treatment, billing, general ERP inventory, employer decisions, immigration adjudication, regulator authority, or proprietary external content.

## Emergent behavior

Together these members turn isolated doses, tests, results, and encounters into closed-loop public-health operations. Shared provenance and succession let a historical dose inform a schedule without masquerading as local administration; shared connector evidence lets first-party state profiles be tested and reconciled; shared worklists ensure triggers, screening gaps, adverse events, and acknowledgments retain accountable human owners.

## Tensions to hold

- Fast vaccination and emergency throughput must not weaken identity, lot, consent, performer, disclosure, or amendment controls.
- Public-health reporting deadlines and population benefit must coexist with minimum-necessary access, sensitive-program confidentiality, and jurisdiction-specific authority.
- Rule engines need current clinical guidance while preserving release provenance, uncertainty, explainability, and human disposition.
- Managed state connectors offer a strong differentiator but create support, certification, secret-management, and specification-change obligations.
- Aggregate dashboards need useful segmentation while preventing small-cell disclosure and false certainty from incomplete data.

## Recombination opportunities

- Combine registry query, reconciliation, validity review, and schedule forecasting into a previsit immunization-readiness flow.
- Combine mass-clinic sessions, lot inventory, VFC eligibility, VIS evidence, outbound VXU, and acknowledgments into an end-to-end vaccination operation.
- Combine screening evaluations, confidential program episodes, bounded outreach, and result-accountability tasks into supervised prevention programs.
- Combine eCR triggers, condition worklists, case reports, surveillance exports, and connector profiles into one observable reporting control plane.
- Combine outbreak protocols, emergency inventory custody, mass vaccination, and privacy-protected coverage snapshots into an incident closeout packet.

## Open questions

- Which clinical, schedule, screening, and jurisdiction rule sources can openChart legally redistribute and maintain as first-party releases?
- Which state connectors should receive supported-product status first, and what conformance and update service level is sustainable?
- Which sensitive screening programs require separate tenant isolation rather than field- and purpose-level permissions within one site?
- What minimum cell sizes, geography levels, and retention periods should govern public-health aggregate outputs?
- Where must external reporting remain manual-release, and where can explicit site policy authorize automatic transmission after clinical acceptance?

## Relationships

[Catalog anchor: Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
