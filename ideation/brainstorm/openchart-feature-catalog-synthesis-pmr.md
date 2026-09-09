# Synthesis: Problems Allergies Medication Records And Vitals — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects 50 governed capabilities into a provenance-aware longitudinal record for problems, allergies, medications, vitals, devices, and clinical histories.
Topics: openchart-feature-catalog, medical-records, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR synthesis (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Longitudinal record review program** — Combine reconciliation, immutable succession, terminology, and chart surfaces into staged clinical-record quality releases.

## Focus

This synthesis relates the PMR member features as a longitudinal record graph while preserving the authority of the existing OC statement DocTypes, patient-reported provenance, consent, and guarded `open_chart.api.v1` writes.

## Members and their joints

### Problems

- [Coded Problem List Lifecycle](openchart-feature-catalog-pmr-001-coded-problem-list-lifecycle.md) — Maintains a coded longitudinal problem list from identification through active management and closure.
- [Problem Acuity Classification](openchart-feature-catalog-pmr-002-problem-acuity-classification.md) — Classifies each problem as acute, chronic, recurrent, or undetermined to support appropriate chart views and follow-up.
- [Outside Record Problem Reconciliation](openchart-feature-catalog-pmr-003-outside-record-problem-reconciliation.md) — Lets clinicians compare imported outside problems with the local list and accept, reject, map, or defer each candidate.
- [Problem Resolution And Inactivation Reasons](openchart-feature-catalog-pmr-004-problem-resolution-inactivation-reasons.md) — Records coded reasons and effective dates whenever a problem is resolved, made inactive, or entered in error.
- [Problem To Encounter Linking](openchart-feature-catalog-pmr-005-problem-encounter-linking.md) — Links problems to encounters with role and relevance so users can see where each problem was assessed or managed.
- [Duplicate Problem Detection](openchart-feature-catalog-pmr-006-duplicate-problem-detection.md) — Flags likely duplicate problem entries using codes, wording, dates, and status while keeping merge decisions clinician-controlled.
- [Clinical Terminology Lookup](openchart-feature-catalog-pmr-007-clinical-terminology-lookup.md) — Provides governed ICD-10-CM, SNOMED CT, and RxNorm search for coded clinical entry with version-aware results.
- [Coded Entry Favorites](openchart-feature-catalog-pmr-008-coded-entry-favorites.md) — Lets each user pin frequently used condition, allergy, medication, and observation codes for faster structured entry.
- [Referral Problem List Printing](openchart-feature-catalog-pmr-009-referral-problem-list-printing.md) — Produces a referral-ready problem list with selected active and historical entries, provenance, and as-of timestamp.
- [Problem Driven Care Gap Flags](openchart-feature-catalog-pmr-010-problem-driven-care-gap-flags.md) — Derives reviewable care-gap flags from confirmed problem-list criteria without autonomously placing orders or changing care.

### Allergies

- [Coded Allergy Reaction And Severity](openchart-feature-catalog-pmr-011-coded-allergy-reaction-severity.md) — Captures coded substances, manifestations, severity, criticality, timing, and provenance for each allergy statement.
- [Drug Class Allergies](openchart-feature-catalog-pmr-012-drug-class-allergies.md) — Records allergies against medication classes and evaluates candidate drugs against governed class membership.
- [Allergy Versus Intolerance Distinction](openchart-feature-catalog-pmr-013-allergy-intolerance-distinction.md) — Separates immune-mediated allergy, non-allergic intolerance, adverse effect, and unknown assertions while preserving patient language.
- [Adverse Event Reporting Entries](openchart-feature-catalog-pmr-014-adverse-event-reporting-entries.md) — Documents suspected medication or substance adverse events with timing, outcome, seriousness, and report disposition.
- [Allergy List Reconciliation](openchart-feature-catalog-pmr-015-allergy-list-reconciliation.md) — Guides encounter-based review of current, outside, and patient-reported allergy entries with explicit dispositions.
- [Allergy Alert Review And Overrides](openchart-feature-catalog-pmr-016-allergy-alert-review-overrides.md) — Shows explainable allergy matches during medication review and records reasoned, time-bound clinician overrides.

### Medications

- [Medication List Statuses](openchart-feature-catalog-pmr-017-medication-list-statuses.md) — Maintains active, as-needed, historical, on-hold, completed, and discontinued medication statement states.
- [Medication Reconciliation Workflow](openchart-feature-catalog-pmr-018-medication-reconciliation-workflow.md) — Compares current, patient-reported, outside, and encounter medication lists and records a signed disposition for every item.
- [Home Versus In Clinic Medications](openchart-feature-catalog-pmr-019-home-versus-in-clinic-medications.md) — Distinguishes medications taken at home from products supplied or administered in a clinic while retaining shared ingredient identity.
- [OTC Supplement And Herbal Capture](openchart-feature-catalog-pmr-020-otc-supplement-herbal-capture.md) — Captures over-the-counter products, vitamins, supplements, and herbals with patient-reported provenance and structured ingredients when known.
- [Medication Adherence Capture](openchart-feature-catalog-pmr-021-medication-adherence-capture.md) — Records patient-reported or clinician-assessed medication-taking patterns, barriers, and observation periods without overstating certainty.
- [Structured Medication Dosage](openchart-feature-catalog-pmr-022-structured-medication-dosage.md) — Represents dose amount, unit, frequency, timing, route, method, and free-text directions on medication statements.
- [PRN Medication Indications](openchart-feature-catalog-pmr-023-prn-medication-indications.md) — Captures why and under what limits an as-needed medication is reportedly used.
- [Long Term Medication Monitoring Plans](openchart-feature-catalog-pmr-024-long-term-medication-monitoring-plans.md) — Defines reviewable laboratory and clinical monitoring schedules associated with long-term medication use.
- [Medication Source Provenance](openchart-feature-catalog-pmr-025-medication-source-provenance.md) — Shows who reported, imported, reviewed, or clinically confirmed each medication-list assertion and when.
- [Medication Duplication Review](openchart-feature-catalog-pmr-026-medication-duplication-review.md) — Identifies exact and therapeutic medication-list duplicates and routes them to explainable human review.
- [Medication Discontinuation History](openchart-feature-catalog-pmr-027-medication-discontinuation-history.md) — Records effective date, reason, actor, and source when a medication statement is discontinued or marked completed.
- [Medication List Extracts](openchart-feature-catalog-pmr-028-medication-list-extracts.md) — Generates selected, as-of medication and supplement lists for referrals, transitions, and patient review.

### Vitals

- [Vitals Capture Forms](openchart-feature-catalog-pmr-029-vitals-capture-forms.md) — Provides configurable forms for recording blood pressure, pulse, temperature, respiration, oxygen saturation, height, weight, and related observations.
- [Pediatric Growth Percentiles](openchart-feature-catalog-pmr-030-pediatric-growth-percentiles.md) — Calculates and charts age- and sex-reference percentiles for pediatric height, weight, BMI, and head circumference.
- [Adult Vital Trend Charts With Target Bands](openchart-feature-catalog-pmr-031-adult-vital-trend-target-bands.md) — Charts longitudinal adult vital signs against clinician-defined or policy-derived target bands.
- [Out Of Range Vitals Alerting](openchart-feature-catalog-pmr-032-out-of-range-vitals-alerting.md) — Evaluates accepted vital signs against context-aware thresholds and routes reviewable alerts without autonomous clinical action.
- [Patient Reported Home Vitals](openchart-feature-catalog-pmr-033-patient-reported-home-vitals.md) — Accepts patient or caregiver home vital readings with device, method, timestamp, and patient-reported provenance.
- [Blood Pressure Device Import](openchart-feature-catalog-pmr-034-blood-pressure-device-import.md) — Provides vendor-neutral hooks for importing blood-pressure cuff readings with device identity and transmission provenance.
- [Glucometer Device Import](openchart-feature-catalog-pmr-035-glucometer-device-import.md) — Provides vendor-neutral hooks for importing glucose readings with units, meal context, specimen type, and device provenance.
- [Biometric Baselines](openchart-feature-catalog-pmr-036-biometric-baselines.md) — Lets clinicians define effective-dated baseline ranges from selected observations for individualized comparison.
- [Vital Correction And Versioning](openchart-feature-catalog-pmr-037-vital-correction-versioning.md) — Corrects accepted vital observations through succession-based amendments while preserving the original reading and reason.
- [Orthostatic Vitals Series](openchart-feature-catalog-pmr-038-orthostatic-vitals-series.md) — Captures timed supine, seated, and standing blood pressure and pulse measurements as one interpretable series.

### History

- [Pregnancy Status Tracking](openchart-feature-catalog-pmr-039-pregnancy-status-tracking.md) — Records time-bounded pregnancy status, estimated dates, verification source, and uncertainty for clinical context.
- [Tobacco Use Screening](openchart-feature-catalog-pmr-040-tobacco-use-screening.md) — Captures coded tobacco product use, frequency, quantity, duration, quit history, exposure, and screening provenance.
- [Alcohol Use Screening](openchart-feature-catalog-pmr-041-alcohol-use-screening.md) — Captures coded alcohol use patterns and scored screening responses with instrument version and provenance.
- [Substance Use Screening](openchart-feature-catalog-pmr-042-substance-use-screening.md) — Captures coded non-tobacco substance use, route, frequency, recency, screening responses, and patient-reported provenance.
- [Structured Family History](openchart-feature-catalog-pmr-043-structured-family-history.md) — Records relatives, relationship, conditions, age at onset, age or cause of death, and source provenance.
- [Structured Social History](openchart-feature-catalog-pmr-044-structured-social-history.md) — Captures living situation, occupation, education, relationships, activity, nutrition, safety, and other social context as effective-dated statements.
- [Surgical History](openchart-feature-catalog-pmr-045-surgical-history.md) — Records past procedures with codes, dates or ranges, body sites, facilities, outcomes, complications, and provenance.
- [Hospitalization History](openchart-feature-catalog-pmr-046-hospitalization-history.md) — Records prior hospital stays with reason, facility, date range, discharge disposition, and supporting provenance.
- [Implantable Device UDI Registry](openchart-feature-catalog-pmr-047-implantable-device-udi-registry.md) — Registers implantable devices using UDI components, device type, implant and explant dates, status, site, and provenance.
- [Clinical History Reconciliation](openchart-feature-catalog-pmr-048-clinical-history-reconciliation.md) — Provides a unified review session for family, social, surgical, hospitalization, pregnancy, and implant history candidates.

### Composition

- [Longitudinal Record Timeline](openchart-feature-catalog-pmr-049-longitudinal-record-timeline.md) — Presents problems, allergies, medications, vitals, devices, and histories on a provenance-aware patient timeline.
- [Clinical Record Summary Workspace](openchart-feature-catalog-pmr-050-clinical-record-summary-workspace.md) — Combines current problems, allergies, medications, recent vitals, and key histories into a role-aware review workspace.

Problems and histories establish clinical context; allergies and medication records add safety-sensitive assertions; vitals contribute timestamped observations; reconciliation workflows determine which source assertions become locally accepted successors. The timeline and summary workspace compose these records without becoming a second source of truth.

## Frappe realization

- Reuse `OC Condition Statement`, `OC Allergy Statement`, `OC Medication Statement`, `OC Supplement Statement`, `OC Observation Statement`, and `OC Document Reference Statement` as provenance-bearing foundations.
- Add standard workflow DocTypes for reconciliation, alerts, extracts, histories, devices, and monitoring; use child tables for reactions, dosage, codings, source evidence, reconciliation items, and observation components.
- Link all coded fields to versioned OC code tables and use Fetch From for read-only display, system, and terminology-release snapshots.
- Preserve accepted records through succession-based versioning under `open_chart.api.v1`; reject guarded direct writes and never infer clinical authority from patient-reported content.
- Apply Role Permission Manager, permlevels, User Permissions, and purpose or consent references to list, report, print, portal, and API surfaces.
- Expose read-only auto-REST with patient, state, effective-date, and modified filters; keep supported writes in whitelisted `open_chart.api.v1` methods with idempotency keys.
- Deliver a Medical Records Desk workspace, Query Reports for unresolved reconciliation and due monitoring, Script Reports for longitudinal trends, and Jinja Print Formats for referral extracts.

## Boundaries

Owns: longitudinal clinical assertions, their provenance, effective states, reconciliation, and chart composition. Consumes: patient identity, encounters, terminology releases, consent, external records, and device payloads. Emits: reviewable records, alerts, extracts, trends, and reconciliation outcomes. Does not own: prescriptions, medication administration, billing, supply inventory, autonomous diagnosis, or autonomous clinical action.

## Emergent behavior

Together the members support a chart that can distinguish what a patient reported, what arrived from outside, what a clinician confirmed, what was later amended, and which effective record should drive a view. Shared coding, provenance, and succession let care-gap rules, safety review, trends, referral extracts, and reconciliation reuse evidence without silently rewriting it.

## Tensions to hold

- Fast data entry must not erase code-system release, original wording, uncertainty, or source authority.
- Safety alerts need context and escalation while avoiding autonomous care decisions and alert fatigue.
- Longitudinal summaries need a useful current view while retaining disputed, sensitive, superseded, and entered-in-error history under appropriate permissions.
- External and device data can reduce manual work, but identity ambiguity, unit uncertainty, and duplicate payloads require explicit review paths.

## Recombination opportunities

- Combine problem context, medication monitoring plans, and accepted observations into explainable due-review worklists.
- Combine allergy classification, drug-class membership, and medication reconciliation into evidence-rich safety review.
- Combine home-vital ingestion, individual baselines, target bands, and threshold rules into supervised remote-monitoring workflows.
- Combine structured histories, implant UDI records, and referral extracts into portable transition-of-care packets.

## Open questions

- Which terminology and clinical-rule releases can ship openly, and which must be loaded and governed by each site?
- Which sensitive history elements require additional purpose-based access beyond ordinary patient User Permissions?
- Which reconciliation and alert workflows require a second reviewer, and how should incomplete reviews affect encounter closure?
- What freshness and uncertainty labels must remain mandatory across summary, print, portal, and API surfaces?

## Relationships

[Catalog anchor: Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
