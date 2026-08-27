# Radiology Peer Review Sampling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Selects eligible interpreted studies for blinded or identified peer review and records structured agreement, feedback, and resolution evidence.
Topics: openchart-feature-catalog, imaging, frappe, peer-review
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-028 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Calibration sessions** — Aggregate de-identified disagreement patterns for facilitated quality discussion.

## Focus

This feature isolates quality-assurance sampling and review without changing the clinical report automatically.

## Behavior

- A governed sampling policy selects eligible accepted reports by modality, subspecialty, facility, and exclusion criteria.
- Assignment avoids self-review and respects conflict, credential, and blindness rules.
- The reviewer records agreement category, significance, comments, and whether clinical review is recommended.
- A disagreement does not amend the report or contact clinicians without an authorized follow-on decision.
- Escalated cases route to a quality lead for resolution, feedback, and any separately governed clinical correction.
- Aggregate reporting protects reviewer and patient confidentiality according to policy.

## Frappe realization

- **DocTypes:** `OC Imaging Peer Review` plus versioned `OC Peer Review Sampling Policy`, assignment, rating, comments, and resolution.
- **Workflow:** Selected → Assigned → Reviewed → Quality Resolution → Closed.
- **Roles/permissions:** peer radiologists review; quality leads resolve; subject readers receive feedback according to blinded policy; administrators lack clinical override rights.
- **Jobs/surfaces:** scheduler creates samples; Assignment Rules route cases; protected Script Reports show rates and unresolved reviews.

## Boundaries

Owns: sampling, review, disagreement, and quality resolution evidence. Consumes: accepted reports and reader credentials. Emits: feedback and reviewed escalation recommendations. Does not own: report amendment, credentialing sanctions, or autonomous clinical communication.

## Open questions

- Should reviewer identity be hidden from the original reader, the quality lead, or neither?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
