# Drug-Allergy Interaction Checking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Compares candidate ingredients and classes with accepted allergy and intolerance records and explains each direct or class-mediated match.
Topics: openchart-feature-catalog, eprescribing, frappe, allergy-interactions
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-029 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Cross-reactivity evidence view** — Reviewers could inspect the exact class and relationship path behind a cross-reactivity finding.

## Focus

This feature isolates allergy and intolerance safety checks for prescribing. It preserves assertion type, source, reaction, severity, and uncertainty rather than flattening all entries into one alert.

## Behavior

- Candidate ingredients, excipients when available, and drug classes are compared with effective allergy statements.
- Findings identify direct ingredient, class, ingredient-family, or excipient match and show the relationship path.
- Allergy, intolerance, adverse effect, entered-in-error, and uncertain assertions produce distinct presentation.
- Missing coding, unreconciled allergy status, or unknown reaction severity generates a data-quality warning.
- A permitted override requires prescriber rationale and records whether patient counseling or monitoring is planned.
- Signed evidence retains allergy statement versions, rule release, findings, and dispositions.

## Frappe realization

- **DocTypes:** Reuse `OC Allergy Statement`; `OC Medication Safety Evaluation` stores statement-version links and `OC Prescription Safety Finding` rows.
- **Hooks:** Candidate changes and allergy-list updates invalidate cached evaluations; `before_submit` requires current results.
- **Permissions:** Prescribers disposition alerts; allergy reconciliation remains governed through existing statement APIs.
- **Surfaces:** Alert card displays reaction and criticality with an evidence drawer and missing-data action.

## Boundaries

Owns: candidate-to-allergy matching and prescribing disposition. Consumes: accepted allergy statements, drug composition/class data, and rules release. Emits: explainable findings. Does not own: allergy diagnosis, reconciliation, or autonomous substitution.

## Open questions

- How should uncertain class allergies affect hard-stop policy across care settings?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Drug-Drug Interaction Checking](openchart-feature-catalog-phr-028-drug-drug-interaction-checking.md)
