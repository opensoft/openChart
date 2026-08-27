# Provider Substitution Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Reassigns affected appointments to an eligible substitute provider with review, patient notice, and preserved lineage.
Topics: openchart-feature-catalog, scheduling, frappe, provider-substitution
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-052 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Coverage roster matching** — Rank approved substitute candidates by credential, location, and availability.

## Focus

This feature isolates provider replacement when an appointment time can remain intact.

## Behavior

- A disruption identifies appointments whose assigned provider is unavailable.
- Candidate substitutes must satisfy specialty, location, appointment type, authority, and schedule constraints.
- Staff preview affected patients, continuity implications supplied by authorized data, and notification consequences.
- Approval changes provider assignment while preserving original provider and reason in history.
- Patients receive identity and choice information and may request rescheduling where policy permits.
- Appointments without a valid substitute remain in the disruption queue and are never reassigned blindly.

## Frappe realization

- **DocTypes:** `OC Provider Substitution` with disruption source, appointment, original_provider, proposed_provider, eligibility evidence, state, and reason.
- **Workflow:** Proposed → Eligibility Checked → Approved/Rejected → Applied; Scheduling Manager or designated clinical operations role approves.
- **Automation:** bulk proposals run in background; Notification doctypes send patient-safe updates only after application.

## Boundaries

Owns: appointment provider-reassignment transition. Consumes: provider eligibility and availability. Emits: revised assignment and notices. Does not own: credentialing authority.

## Open questions

- Which continuity-sensitive visits should prohibit substitution without patient confirmation?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Provider Availability Exceptions](openchart-feature-catalog-sch-022-provider-availability-exceptions.md)
