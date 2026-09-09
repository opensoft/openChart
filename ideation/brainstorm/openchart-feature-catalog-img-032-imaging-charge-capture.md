# Imaging Charge Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Derives reviewable charge candidates from performed imaging facts and sends accepted evidence to an external billing owner.
Topics: openchart-feature-catalog, imaging, frappe, charge-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-032 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Documentation gap queue** — Identify performed-study facts missing before a charge candidate can be reviewed.

## Focus

This feature isolates clinical-to-financial evidence generation without making openChart a billing or claims system.

## Behavior

- Accepted performance records generate candidates based on study, components, contrast, guidance, laterality, and documented completion.
- Each candidate cites the exact clinical facts and versioned mapping rule that produced it.
- Partial, repeated, cancelled-after-start, and outside studies follow explicit exception rules.
- Authorized staff accept, correct, reject, or hold candidates with a reason.
- Export uses idempotent transaction identifiers and records external acknowledgment or rejection.
- Mapping changes never rewrite previously accepted clinical evidence or transmitted history.

## Frappe realization

- **DocTypes:** `OC Imaging Charge Candidate` with evidence Links, rule version, suggested codes, review decision, and external transaction status.
- **Workflow:** Generated → Review → Accepted → Exported → Acknowledged, with Held, Rejected, and Reconciliation states.
- **Roles/permissions:** imaging coders review; clinicians read source linkage; integration users export only accepted candidates.
- **Hooks/API/surfaces:** performance `on_submit` queues derivation; guarded export adapter sends to openPractice or another billing owner; exception report tracks failures.

## Boundaries

Owns: charge candidate and clinical evidence linkage. Consumes: performed-study facts and governed mappings. Emits: accepted charge evidence. Does not own: fees, claims, coding final authority, payment, or accounts receivable.

## Open questions

- Which coding decisions belong in openChart review versus the external billing system?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
