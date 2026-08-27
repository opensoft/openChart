# Preventive Care Measure Automation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Reuses governed screening evaluations and completed evidence to automate preventive quality measurement with explainable discrepancies.
Topics: openchart-feature-catalog, quality-reporting, frappe, preventive-measures
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-024 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Rule divergence review** — Show where clinical screening guidance and regulatory measure logic produce different due or met states.

## Focus

Safe reuse of preventive screening data while keeping care-guidance rules and reporting rules independently versioned.

## Behavior

- Approved adapters map screening events, results, refusals, contraindications, and outreach outcomes to measure data elements.
- The adapter records both screening-rule and measure-rule releases when derived states are compared.
- Completed evidence may satisfy a measure only when timing, result, source, and population criteria match.
- A clinical due state does not automatically mean a measure gap, and a met measure does not suppress clinical follow-up.
- Divergent states appear in a review report with the decisive rule and evidence differences.
- New evidence or rule succession triggers affected-result reevaluation.
- Automation creates no autonomous order, diagnosis, outreach, or exclusion.

## Frappe realization

- **DocTypes:** Add `OC Preventive Measure Mapping` with screening type, source event, measure element, timing transform, release links, and approval state.
- **Workflow:** Govern mappings through draft, synthetic-test, review, approved, stale, and retired states.
- **Hooks and jobs:** Enqueue recalculation after accepted screening evidence; run divergence checks in rq against immutable rule releases.
- **Surfaces:** Provide divergence Script Reports, mapping coverage dashboards, and patient-result trace links.

## Boundaries

Owns: preventive evidence mapping into measurement and divergence explanations. Consumes: screening events, accepted results, rule releases, and patient context. Emits: measure inputs and discrepancy findings. Does not own: preventive-care guidance or clinical action.

## Open questions

- Which screening engines expose sufficiently stable, provenance-bearing outputs for direct mapping?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
