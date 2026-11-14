# Measure Result Provenance Trace — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves a reproducible trace from each measure classification through logic, terminology, and source-record versions for review and audit.
Topics: openchart-feature-catalog, quality-reporting, frappe, result-provenance
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-005 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Counterfactual trace** — Explain which single missing or changed fact would alter a patient's measure outcome.

## Focus

Immutable calculation evidence that distinguishes derived quality assertions from the clinical records and specifications they reference.

## Behavior

- Every patient evaluation stores the measure release, terminology release, engine version, source cutoff, and input record versions.
- Trace nodes identify evaluated expression, normalized input, outcome, and parent-child rule relationships.
- Sensitive source values are redacted in views when the reviewer lacks underlying record permission.
- Users can compare current and superseded traces to see why a classification changed.
- Missing or deleted dependencies render the trace incomplete and raise an integrity exception.
- Trace evidence is content-hashed and cannot be silently rewritten after run completion.
- A human-readable narrative accompanies machine-readable trace data without replacing it.

## Frappe realization

- **DocTypes:** Add `OC Measure Evaluation Trace` and child `OC Measure Trace Node` with source Dynamic Links, versions, hashes, expression paths, outcomes, and redaction classes.
- **Hooks:** Build and hash traces during execution completion; verify integrity before evidence export and flag stale dependencies on source succession.
- **Permissions and API:** Use source-aware permission checks in `open_chart.api.v1.quality.get_trace`; restrict raw JSON to `OC Measure Auditor`.
- **Surfaces:** Provide a read-only tree view, before/after comparison Script Report, and Jinja evidence Print Format.

## Boundaries

Owns: calculation provenance and integrity evidence. Consumes: engine events, specifications, terminology, and versioned clinical records. Emits: machine and human traces plus integrity exceptions. Does not own: clinical provenance creation or measure interpretation policy.

## Open questions

- How much intermediate expression data can be retained without creating excessive PHI duplication?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
