# Sentence-Level Transcript Provenance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Links each generated note sentence to supporting transcript spans so reviewers can verify source fidelity before acceptance.
Topics: openchart-feature-catalog, clinical-ai, frappe, sentence-provenance
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-005 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Unsupported-claim heatmap** — Highlight draft sentences with weak, conflicting, or absent transcript support.

## Focus

This feature isolates fine-grained evidence linkage between ambient source material and generated documentation.

## Behavior

- Each generated sentence carries zero or more timestamped transcript span references and a support classification.
- Reviewers select a sentence to view the exact transcript text and, when retained, play the bounded audio segment.
- Sentences with no source are labeled generated inference and cannot masquerade as quoted patient statements.
- Editing a sentence preserves the original mapping and marks whether support needs re-review.
- Missing or deleted source media leaves a visible unavailable-evidence state rather than removing provenance.
- Exported accepted notes may include an internal provenance manifest without exposing audio to unauthorized users.

## Frappe realization

- **DocTypes:** child `OC AI Sentence Evidence` stores sentence ID, transcript segment Link, offsets, timestamps, support class, and reviewer status beneath `OC AI Artifact`.
- **Roles/permissions:** note reviewers read text evidence; audio playback requires `OC Ambient Audio Reviewer` at permlevel 2.
- **Hooks/API/surface:** generation `on_update` validates offsets against immutable transcript versions; whitelisted evidence method returns permission-filtered spans; client script renders sentence popovers.
- **Reports:** Script Report lists unsupported or stale evidence mappings by capability and reviewer.

## Boundaries

Owns: sentence-to-source mappings and support labels. Consumes: versioned transcript and generated draft. Emits: reviewer-verifiable provenance. Does not own: clinical correctness, transcription accuracy, or retention decisions.

## Open questions

- What support taxonomy is understandable to clinicians without overstating model certainty?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Artifact Registry](openchart-feature-catalog-aic-001-ai-artifact-registry.md)
