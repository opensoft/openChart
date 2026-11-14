# Measure Steward Feed Ingestion — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Monitors and ingests authorized measure-steward feeds for specification, status, benchmark, and retirement changes with human approval.
Topics: openchart-feature-catalog, quality-reporting, frappe, steward-feed
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-015 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Change triage digest** — Summarize feed changes by affected periods, mappings, simulations, and submissions.

## Focus

Observable update intake for PQRS-successor and other steward sources without automatic activation of external changes.

## Behavior

- A librarian configures an authorized feed endpoint, authentication reference, schedule, format, and expected publisher identity.
- Polling records retrieval time, response signature or checksum, source version, and parse outcome.
- New, changed, retired, and withdrawn artifacts become review candidates linked to existing local releases.
- Duplicate payloads are idempotent; signature, schema, or publisher failures enter quarantine.
- Impact analysis lists periods, mappings, runs, dashboards, and profiles potentially affected.
- No feed item becomes active until a reviewer approves a local measure-library release.
- Feed history and raw payload retention follow licensing and security policy.

## Frappe realization

- **DocTypes:** Add `OC Measure Steward Feed`, `OC Steward Feed Receipt`, and child change rows with endpoint metadata, secret reference, checksum, payload Attach, and disposition.
- **Jobs:** Poll through scheduler events and rq with bounded retry, dead-letter status, PHI-free logs, and Notifications on failures.
- **Permissions and API:** Restrict configuration to `OC Measure Librarian`; expose guarded test, poll, review, and accept methods.
- **Surfaces:** Provide a feed health dashboard, change-impact Script Report, and quarantine queue.

## Boundaries

Owns: feed retrieval evidence, parsing, quarantine, and review handoff. Consumes: authorized external feeds and local library metadata. Emits: candidate changes and impact notices. Does not own: publisher availability, content rights, or automatic measure activation.

## Open questions

- Which steward feeds provide stable machine-readable interfaces and acceptable redistribution terms?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
