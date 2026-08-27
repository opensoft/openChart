# Registry Submission Reconciliation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Reconciles reportable local immunization events against sent, acknowledged, rejected, and unsent registry transactions.
Topics: openchart-feature-catalog, public-health, frappe, registry-reconciliation
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-014 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Completeness attestation** — Let program managers sign a bounded reporting-period reconciliation.

## Focus

An operational sent-versus-accepted ledger that exposes registry reporting gaps.

## Behavior

- Program managers select date range, site, registry, vaccine, and event status filters.
- The report groups events as accepted, pending, rejected, excluded-by-policy, or missing submission.
- Every count drills through to clinical event and exchange evidence under permission controls.
- Late acknowledgments update the current result while preserving prior report snapshots.
- Authorized users annotate justified exclusions without changing the administration event.
- Incomplete connector data produces an explicit unknown bucket instead of favorable assumptions.

## Frappe realization

- **DocTypes:** Add immutable `OC Registry Reconciliation Snapshot` with child result rows and filter/evidence digests.
- **Reports:** Build a Script Report joining administration, targets, submissions, and acknowledgments plus dashboard Number Cards.
- **Permissions:** Limit identifiable drill-through to exchange roles and provide aggregate views to `OC Public Health Program Manager`.
- **Jobs and API:** Schedule snapshots after reporting periods and expose read-only export through guarded, audited methods.

## Boundaries

Owns: reconciliation classification and snapshots. Consumes: clinical events and exchange lifecycle evidence. Emits: gap lists and aggregate completeness. Does not own: transport retries or external acceptance criteria.

## Open questions

- Which denominator exclusions must be fixed versus configurable by jurisdiction?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
