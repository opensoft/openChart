# Disposition Round 1 — R1 and R2 Staged Topics

Status: record
Kind: report
Summary: the twelve open questions from the practitioner-identity-openxwallet and live-visit-companion staged topics, each with its recommended answer, presented for owner disposition before the proposal gate.
Topics: openchart-clinical-companion, staging, disposition-round
Repository context: openChart — Frappe v15 native EMR; disposition round for the two staged topics
Captured: 2026-08-26

**OUTCOME (2026-08-26): the owner accepted all twelve recommendations as
written** ("accept all 12"). Every question below is dispositioned `accepted`
in its staged outline; this file is the immutable record of the round.

Answer each with **accept** (the recommendation stands), **modify** (say how),
or **defer** (stays open; blocks the proposal gate for its topic). Full
Context/Explanation for every question lives in the staged outlines:
`practitioner-identity-openxwallet/outline.md` and
`live-visit-companion/outline.md`.

## Topic R1 — practitioner-identity-openxwallet

**R1-Q1. Which composition components are license-relevant (the major/minor line)?**
Recommended: `model_version` and `policy_version` are major (re-license);
`retrieval_corpus`, `parameters`, `prompt_contract`, `tool_manifest` are minor
(fast auto-reissue with attestation). New literature = a doctor reading
journals, not a new doctor.

**R1-Q2. How are the green/yellow/red/black zones computed and calibrated?**
Recommended: a versioned scope registry maps act/object classes to license
boundaries; per-jurisdiction calibration is registry data, not code. One
calculator, many registry versions; a zone must be reproducible as-of the time
an action was taken.

**R1-Q3. How do we prove the licensed AI is the practicing AI?**
Recommended: every clinical action's exercise record carries the composition
hash; the license record pins the covered hash set; verification is a join
(act hash ∈ license set at timestamp) — continuous by construction, not
periodic attestation.

**R1-Q4. What does revoking AI-treatment consent trigger?**
Recommended: a transfer-of-care workflow with continuity guarantees — the AI
stops initiating new acts, active orders/plan stay in force, a named human
practitioner accepts the care. Never immediate abandonment.

**R1-Q5. What shape is the co-signature record?**
Recommended: one new record kind in the profile family: one exercise, N
role-qualified signatures (performer, supervisor, council member, dissenting
member). Serves both pre-licensure signoff and council/gateway signing with
one structure.

**R1-Q6. How is the per-state legal matrix represented?**
Recommended: one jurisdiction registry consumed by the zone calculator —
disclosure obligations, supervision requirements, boundary calibration per
state — fed by an ongoing legal-research work item, not a one-time survey.

## Topic R2 — live-visit-companion

**R2-Q1. Practitioner vs companion record disagreement — who adjudicates; does it block signing?**
Recommended: never blocks. Both records file; the discrepancy becomes a
flagged reconciliation item the practitioner reviews post-visit. A witness
with a veto would be a second decision-maker nobody credentialed.

**R2-Q2. Record class / retention / discoverability of the unspoken portions?**
Recommended: part of the record in a distinct provenance class; retention and
patient visibility deferred to the Issue-4 legal research; exposure and
reliance tags captured from day one (they cannot be reconstructed later).

**R2-Q3. Does ask-and-correct agency extend into patient visits?**
Recommended: yes, but through the private channel by default — corrections
reach the room through the practitioner's own voice; audible companion speech
is for conferences or when the practitioner explicitly invites it.

**R2-Q4. Mid-encounter consent revocation semantics?**
Recommended: consent is live; revocation stops capture forward only; content
already captured is retained under the consent that covered it; the
transition is logged as a session event (same pattern as legal off-record).

**R2-Q5. Where does the streaming session runtime live? (shapes requirements — named in Exit)**
Recommended: a dedicated streaming session service beside bench, holding the
live session/transcript/inference, writing into openChart only through
guarded api.v1-style surfaces; rq keeps post-visit jobs.

**R2-Q6. Are private-channel prompts part of the encounter record?**
Recommended: yes — same class as the unspoken portions, with exposure and
reliance tags; an unrecorded influence channel is exactly where
failure-to-heed arguments concentrate.
