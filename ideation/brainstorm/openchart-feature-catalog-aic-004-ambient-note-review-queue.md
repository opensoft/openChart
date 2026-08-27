# Ambient Note Review Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts consented encounter transcripts into note drafts that remain blocked in clinician review until explicitly accepted and signed.
Topics: openchart-feature-catalog, clinical-ai, frappe, ambient-notes
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-004 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Section-level reviewer assignment** — Route specialized draft sections to different qualified reviewers before final signature.

## Focus

This feature isolates ambient note drafting and the mandatory review-before-sign queue.

## Behavior

- A stopped, consent-valid capture can be submitted for drafting against an approved note profile.
- The generated note enters Pending Review and is never inserted into a signed note automatically.
- Assigned clinicians compare transcript evidence, edit sections, accept or reject the draft, and record material corrections.
- The sign action remains disabled until required sections, provenance, and reviewer attestations pass server validation.
- Failed generation leaves the encounter unchanged and offers retry or manual-documentation paths.
- Rejected drafts remain auditable but cannot be promoted to clinical documentation.

## Frappe realization

- **DocTypes:** `OC Ambient Note Draft` links `OC AI Artifact`, encounter, note template, assignment, generated sections, edits, and destination note successor.
- **Workflow:** Queued → Generating → Pending Review → Accepted/Rejected → Signed Through Destination.
- **Roles/permissions:** assigned `OC Clinician` edits; `OC Note Signer` accepts and signs; AI service accounts cannot receive submit permission.
- **Hooks/jobs/surfaces:** rq generation job; `validate` blocks acceptance without provenance; Desk Workspace queue, diff view client script, Assignments, and Notifications support review.

## Boundaries

Owns: transcript-to-note drafting and review state. Consumes: consented transcript, template, model, and encounter context. Emits: human-edited draft eligible for ordinary note signature. Does not own: signed-note authority or autonomous diagnosis and ordering.

## Open questions

- Which note types require a second reviewer when generated from ambient capture?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Sentence-Level Transcript Provenance](openchart-feature-catalog-aic-005-sentence-level-transcript-provenance.md)
