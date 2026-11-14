# Behavioral Health Integration Measures — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Calculates behavioral health integration measures with sensitive-data segmentation, instrument provenance, follow-up windows, and minimum-necessary reporting.
Topics: openchart-feature-catalog, quality-reporting, frappe, behavioral-health-measures
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-027 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Measurement-based care trajectory** — Compare instrument change over time when consent and program rules permit.

## Focus

Privacy-governed measurement of screening, follow-up, remission, response, and care integration without broadening access to sensitive records.

## Behavior

- Approved mappings identify instrument version, score, administration mode, encounter context, follow-up interval, and result authority.
- Measure evaluation checks age, diagnosis, screening, treatment, follow-up, remission, and exclusion criteria as specified.
- Restricted behavioral health facts are evaluated in a purpose-bound service and disclosed only as the minimum result needed.
- Drill-down redacts source details for reviewers lacking underlying record permission while retaining trace integrity.
- Missing instrument version, partial responses, or conflicting scores produce indeterminate evidence rather than inferred outcomes.
- Patient consent and applicable sensitive-record policy govern patient-level exports and outreach worklists.
- Calculated gaps do not autonomously recommend treatment or disclose behavioral health status.

## Frappe realization

- **DocTypes:** Add `OC Behavioral Measure Mapping` with instrument, score semantics, follow-up windows, release, sensitivity class, and minimum-output policy.
- **Permissions:** Enforce purpose and sensitive-record checks in server methods, permlevels, User Permissions, reports, and exports.
- **Jobs and API:** Evaluate restricted inputs in rq and return bounded classifications through guarded quality APIs with audited access.
- **Surfaces:** Provide redaction-aware Script Reports, authorized trajectory charts, and restricted exception queues.

## Boundaries

Owns: behavioral-health measure mapping, evaluation, and bounded reporting. Consumes: authorized instruments, encounters, conditions, consent, and measure rules. Emits: privacy-governed results and gaps. Does not own: diagnosis, treatment, psychotherapy records, or consent policy.

## Open questions

- Which aggregate outputs remain safe when patient-level behavioral data is specially protected?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
