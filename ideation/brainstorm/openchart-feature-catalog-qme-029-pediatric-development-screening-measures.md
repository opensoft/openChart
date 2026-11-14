# Pediatric Development Screening Measures — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures age-windowed developmental screening and follow-up using instrument-specific evidence, guardian context, and pediatric privacy controls.
Topics: openchart-feature-catalog, quality-reporting, frappe, pediatric-screening-measures
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-029 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Window opportunity preview** — Show upcoming screening windows for supervised previsit planning without asserting a clinical order.

## Focus

Reliable pediatric screening measurement across age windows, instrument versions, incomplete responses, and follow-up evidence.

## Behavior

- Mappings identify approved instrument version, age basis, completion rules, score semantics, setting, and required follow-up.
- Evaluation uses the child's age at encounter and the measure release's eligible windows.
- Partial, parent-declined, language-mismatched, unscorable, or duplicate instruments remain distinct outcomes.
- Positive screens link to permitted follow-up evidence without exposing restricted notes to quality users.
- Guardian or proxy completion is recorded as provenance, not treated as clinician observation.
- Patient aging, corrected date of birth, or instrument succession marks affected results stale.
- Gaps can enter supervised worklists but never trigger diagnosis, referral, or outreach automatically.

## Frappe realization

- **DocTypes:** Add `OC Pediatric Measure Mapping` with instrument, version, age windows, completion rule, follow-up elements, proxy class, and release.
- **Hooks and jobs:** Reevaluate on accepted instrument, follow-up, or demographic succession; schedule bounded window checks.
- **Permissions:** Apply pediatric, proxy, consent, and sensitive-record rules to traces and exports.
- **Surfaces:** Provide age-window Script Reports, instrument completeness dashboards, and patient measure trace panels.

## Boundaries

Owns: developmental screening measure evaluation and reporting. Consumes: accepted instruments, demographics, encounters, follow-up evidence, proxy context, and rules. Emits: results, gaps, and completeness findings. Does not own: developmental diagnosis, instrument licensing, or referral decisions.

## Open questions

- Which instrument licenses permit storage of item-level responses and scoring logic?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
