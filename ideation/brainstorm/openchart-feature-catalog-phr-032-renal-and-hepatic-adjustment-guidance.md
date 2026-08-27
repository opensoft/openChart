# Renal And Hepatic Adjustment Guidance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents medication-specific renal and hepatic adjustment guidance keyed to selected accepted labs, calculations, and condition context.
Topics: openchart-feature-catalog, eprescribing, frappe, organ-adjustment
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-032 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Calculation-method comparison** — Prescribers could compare supported renal-function formulas and document which one informed review.

## Focus

This feature isolates organ-function guidance at prescribe time. It shows source labs, calculation method, freshness, and rule evidence while leaving dose choice to the prescriber.

## Behavior

- The engine identifies medications with renal or hepatic guidance and requests the required patient context.
- It proposes eligible accepted laboratory observations and lets the prescriber confirm which values apply.
- Derived renal measures show formula, demographic inputs, units, timestamp, and limitations.
- Hepatic guidance shows applicable laboratory and condition assumptions without inventing a severity class from incomplete data.
- Missing, stale, conflicting, or unit-incompatible evidence produces an unable-to-evaluate or caution state.
- The prescriber reviews guidance, modifies the draft if desired, and records disposition for configured severe findings.

## Frappe realization

- **DocTypes:** `OC Organ Dose Guidance Rule` and `OC Medication Safety Evaluation` link source `OC Observation Statement` versions and calculation metadata.
- **Hooks/API:** Server services normalize units and calculate supported measures; no result writes back into source observations.
- **Permissions:** Prescribers select evidence and disposition findings; rule stewards govern effective releases.
- **Surfaces:** Composer evidence picker, calculation panel, stale-lab warning, and unsupported-rule report support safe review.

## Boundaries

Owns: adjustment guidance, selected evidence links, and disposition. Consumes: candidate medication, accepted labs, demographics, conditions, and rules. Emits: explainable guidance. Does not own: diagnosis, lab correction, or automatic dose change.

## Open questions

- Which renal and hepatic calculation methods should be available for each medication and population?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Dose-Range And Age Checking](openchart-feature-catalog-phr-031-dose-range-and-age-checking.md)
