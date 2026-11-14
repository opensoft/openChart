# Communicable Disease Case Reporting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assembles, reviews, submits, and tracks jurisdiction-specific communicable-disease case reports with legal authority and provenance.
Topics: openchart-feature-catalog, public-health, frappe, disease-case-reporting
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-022 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Supplemental report updates** — Send governed follow-up facts under the original case correlation.

## Focus

Human-governed case-report lifecycle from clinical evidence to public-health acknowledgment.

## Behavior

- Authorized reporters create a candidate from a reportable condition, laboratory result, or clinician concern.
- The packet shows patient facts, condition, dates, evidence, jurisdiction, authority basis, and required gaps.
- States are candidate, under-review, report-ready, submitted, acknowledged, rejected, follow-up, and closed.
- Report release requires a role-authorized user and records the exact version disclosed.
- Conflicting evidence remains visible; the workflow does not autonomously diagnose or suppress a case.
- Connector errors enter a remediation queue while statutory deadlines remain visible.

## Frappe realization

- **DocTypes:** Add submittable `OC Communicable Disease Case Report`, evidence child rows, and protected disclosure artifacts.
- **Workflow:** Require `OC Public Health Reporter` review/release and optionally `OC Clinician` confirmation by condition profile.
- **Permissions:** Apply purpose-based access, patient User Permissions, permlevel protection, and audit to every preview and export.
- **API and surfaces:** Add guarded prepare/submit methods, jurisdiction-aware Print Formats/connectors, and statutory-deadline Query Reports.

## Boundaries

Owns: local case-report packet, disclosure, and delivery state. Consumes: problems, labs, demographics, jurisdiction rules, and legal authority. Emits: authorized reports and acknowledgments. Does not own: diagnosis or authority adjudication by agencies.

## Open questions

- Which report types permit automated candidate creation but still require manual release?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
