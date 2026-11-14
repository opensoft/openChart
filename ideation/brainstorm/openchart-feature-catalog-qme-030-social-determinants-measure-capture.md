# Social Determinants Measure Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures and measures social-needs screening, response, intervention, and follow-up with consent, provenance, and anti-stigmatization controls.
Topics: openchart-feature-catalog, quality-reporting, frappe, sdoh-measures
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-030 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Equity completeness lens** — Reveal screening availability and missingness without ranking patients or communities by inferred risk.

## Focus

Measure-ready SDOH evidence that preserves patient wording, instrument provenance, consent, and bounded use.

## Behavior

- Capture records instrument, version, respondent, mode, language, responses, completion status, consent, and source encounter.
- Patient-declined, skipped, not-asked, inaccessible, and positive responses remain separate states.
- Measure logic evaluates screening and documented response according to approved program releases.
- Sensitive responses are purpose-restricted and quality views disclose only required classifications or aggregates.
- External data may supplement context only when its provenance and permitted use are explicit.
- Quality gaps do not infer unmet needs, trigger services, or alter care without authorized human review.
- Amendments preserve original patient-reported assertions and successor history.

## Frappe realization

- **DocTypes:** Add `OC SDOH Measure Evidence` and `OC SDOH Measure Mapping` with instrument, respondent, language, response table, consent purpose, sensitivity, and succession fields.
- **Workflow:** Use draft, submitted, review-required, accepted, declined, and superseded evidence states.
- **Permissions and API:** Guard capture and measure reads through purpose-aware `open_chart.api.v1.quality` methods with field redaction.
- **Surfaces:** Provide portal or Web Form intake where authorized, clinician review queues, aggregate Script Reports, and no small-cell exports.

## Boundaries

Owns: SDOH measurement evidence and privacy-governed quality classification. Consumes: patient-reported screening, consent, encounters, interventions, and rules. Emits: bounded measure results and completeness views. Does not own: inferred social risk, eligibility decisions, or autonomous referrals.

## Open questions

- Which response elements can enter aggregate reporting without creating reidentification or stigmatization risk?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
