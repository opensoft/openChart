# Multi-reader Imaging Consensus — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates independent or collaborative reads, disagreement reconciliation, consensus authorship, and final attestation for studies requiring multiple readers.
Topics: openchart-feature-catalog, imaging, frappe, reader-consensus
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-040 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Consensus conference queue** — Group unresolved cases by deadline, specialty, and required participants.

## Focus

This feature isolates governed multi-reader interpretation where one preliminary-to-final supervision chain is insufficient.

## Behavior

- A consensus episode defines required reader roles, independence or visibility rules, quorum, deadline, and final authority.
- Each reader submits an interpretation or structured assessment under the configured visibility policy.
- The system identifies differences in designated fields but does not decide which interpretation is correct.
- Disagreement opens a reconciliation task with discussion evidence, participant identities, and outcome.
- Final consensus text identifies contributors, dissent where policy requires, and the authorized attesting reader.
- Missed quorum, conflicts of interest, unavailable readers, and post-final corrections follow explicit exception paths.

## Frappe realization

- **DocTypes:** `OC Imaging Consensus Episode` with child reader assignments, blinded submissions, comparison fields, discussion events, and final attestation.
- **Workflow:** Assigned → Independent Reading → Reconciliation → Consensus Ready → Final Accepted, with Quorum Failed and Exception Review.
- **Roles/permissions:** reader access follows assignment and visibility phase; consensus chair resolves process; only designated authority signs final text.
- **Hooks/API/surfaces:** guarded submission methods prevent premature disclosure; Assignment Rules and Notifications track deadlines; workspace presents differences after unblinding.

## Boundaries

Owns: multi-reader assignments, submissions, reconciliation, consensus, and attestation evidence. Consumes: study, reporting schema, credentials, and reader availability. Emits: final consensus report content. Does not own: credentialing, peer-review sampling, or autonomous adjudication.

## Open questions

- Which workflows require preserved dissent in the final clinical report versus quality-only records?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
