# Advanced Imaging Precertification Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records payer precertification requirements, submissions, identifiers, decisions, validity windows, and evidence for advanced imaging readiness.
Topics: openchart-feature-catalog, imaging, frappe, precertification
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-033 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Clinical evidence packet** — Assemble order, question, guideline, and prior-study references for reviewed submission.

## Focus

This feature isolates imaging authorization evidence and operational readiness while payer transactions may remain external.

## Behavior

- Staff record payer, plan, study scope, requirement status, submission date, reference number, decision, and validity period.
- The episode links supporting clinical evidence without duplicating or rewriting source records.
- Approved authorization is checked against scheduled date, facility, modality, body region, and study changes.
- Pending, denied, expired, not-required, and unable-to-determine states remain distinct.
- Overrides to schedule without approval require policy-authorized review and a documented reason.
- External portal or clearinghouse updates are reconciled by transaction identifier and never accepted on patient match alone.

## Frappe realization

- **DocTypes:** `OC Imaging Precertification` with payer references, scope, evidence child table, decision, authorization number, and validity dates.
- **Workflow:** Requirement Review → Evidence Assembly → Submitted → Pending → Approved or Denied, with Expired and Exception Review.
- **Roles/permissions:** authorization staff manage; ordering clinicians respond to evidence requests; patients receive limited status where appropriate.
- **API/surfaces:** guarded update and callback methods; Assignment Rules route pending work; worklist and Script Report show schedule-risk cases.

## Boundaries

Owns: precertification episode, evidence links, decision, and readiness state. Consumes: order, coverage, payer response, and schedule. Emits: authorization status and tasks. Does not own: insurance eligibility, payer policy, billing, or appeals adjudication.

## Open questions

- Which payer exchanges can be automated without making an unverified response authoritative?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
