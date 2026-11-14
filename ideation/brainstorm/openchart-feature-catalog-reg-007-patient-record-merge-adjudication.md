# Patient Record Merge Adjudication — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives identity reviewers a controlled survivor-and-source decision workflow for confirmed duplicate patient records.
Topics: openchart-feature-catalog, registration, frappe, merge-adjudication
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-007 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Field-level conflict preview** — Compare proposed survivor values and downstream reference impact before approval.

## Focus

Adjudicate whether and how two patient identities may be merged while preserving authority and reversibility planning.

## Behavior

- Identity Reviewer opens a case only from two explicitly selected patient records.
- The case compares identifiers, names, demographics, restrictions, relationships, and linked-record counts.
- Reviewer chooses a survivor and a resolution for every conflicting identity field.
- Active legal holds, incompatible deceased states, or unresolved cross-tenant ownership block approval.
- A second authorized reviewer approves the plan before guarded execution.
- Rejection leaves both records unchanged and records the rationale for future candidate suppression.

## Frappe realization

- **DocTypes:** `OC Patient Merge Case`, child `OC Merge Field Decision`, and `OC Merge Reference Inventory` with survivor and source links.
- **Workflow:** Draft → Identity Review → Secondary Approval → Approved for Execution or Rejected; execution is a background job.
- **Roles/permissions:** `OC Identity Reviewer` prepares; `OC Registration Supervisor` independently approves; `OC Privacy Officer` clears restrictions.
- **API/surfaces:** `open_chart.api.v1.registration.propose_merge` and `.approve_merge`; merge comparison page and blocked-case report.

## Boundaries

Owns: merge decision plan and approvals. Consumes: duplicate evidence and reference inventory. Emits: authorized merge command or rejection. Does not own: audit visualization or facility transfer.

## Open questions

- Which linked clinical records can be reparented versus preserved through an identity-resolution layer?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
