# Population Immunization Coverage Dashboard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures immunization coverage by governed cohort, vaccine series, site, geography, and as-of date with transparent denominators.
Topics: openchart-feature-catalog, public-health, frappe, immunization-coverage
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-039 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Equity review lens** — Compare authorized aggregate cohorts with suppression and small-cell safeguards.

## Focus

Reproducible aggregate coverage metrics that retain cohort, rule-release, and data-freshness provenance.

## Behavior

- Program managers define cohort, denominator eligibility, vaccine/series, completion rule, exclusions, and as-of date.
- Results show numerator, denominator, percentage, unknown-data count, and rule/data freshness.
- Users drill from aggregates only when role, purpose, and minimum-cell policy permit.
- Historical snapshots remain stable when records or schedule releases later change.
- Small cells are suppressed in exports and unauthorized segment combinations are blocked.
- Dashboard errors or incomplete sites display coverage unknown rather than zero.

## Frappe realization

- **DocTypes:** Add `OC Coverage Measure Definition` and immutable `OC Coverage Snapshot` with filter digest, release links, counts, and suppression state.
- **Jobs:** Calculate snapshots in background workers from permissioned reporting tables and effective accepted records.
- **Permissions:** Give aggregate access to `OC Public Health Program Manager`; identifiable drill-through requires an additional clinical role and purpose audit.
- **Surfaces:** Build Dashboard Charts, Number Cards, cohort Query Reports, and suppressed CSV export via whitelisted method.

## Boundaries

Owns: coverage definitions, calculations, and snapshots. Consumes: patient cohorts, accepted doses, schedule releases, sites, and geography. Emits: governed aggregate metrics. Does not own: outreach, external population denominators, or causal interpretation.

## Open questions

- Which geographic granularity and cell-size thresholds adequately protect privacy?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
