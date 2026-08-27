# Provider Delegation And Coverage — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records time-bounded provider delegation and out-of-office coverage with scoped authority, acceptance, and revocation.
Topics: openchart-feature-catalog, platform, frappe, provider-delegation
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-044 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Coverage gap calendar** — Identify unaccepted or conflicting coverage periods before an absence begins.

## Focus

This feature isolates operational coverage and bounded delegation without transferring authorship, signature identity, or non-delegable authority.

## Behavior

- Providers or authorized coordinators propose delegate, dates, facilities, task classes, escalation route, and exclusions.
- The delegate must accept coverage before it becomes active, unless an approved emergency assignment policy applies.
- Records move through Draft, Pending Acceptance, Scheduled, Active, Revoked, Expired, Rejected, and Superseded states.
- Validation blocks self-delegation, overlapping incompatible coverage, inactive providers, and authority beyond either party's scope.
- Routed work shows original owner, acting delegate, delegation version, and due-time effects.
- Revocation stops new routing immediately while preserving attribution for actions already taken.

## Frappe realization

- **DocTypes:** `OC Provider Delegation` stores principal, delegate, date range, facility Table MultiSelect, task classes, exclusions, and state.
- **Workflow:** Principal proposes; Delegate accepts; Clinical Operations may approve emergency coverage or revoke unsafe assignments.
- **Hooks/API:** Assignment hooks consult active delegation; guarded methods accept, revoke, and explain routing authority.
- **Surface:** Calendar and Gantt views display coverage, conflicts, pending acceptance, and gaps.

## Boundaries

Owns: time-bounded coverage agreements and routing authority. Consumes: provider status, affiliations, signature policy, and task class. Emits: delegation decisions and attribution context. Does not own: clinical authorship, credentials, or on-call scheduling.

## Open questions

- Which task classes are legally or clinically non-delegable in each jurisdiction?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [E-signature Authority Registry](openchart-feature-catalog-plt-043-e-signature-authority-registry.md) · [Skill-based Task Routing](openchart-feature-catalog-plt-045-skill-based-task-routing.md)
