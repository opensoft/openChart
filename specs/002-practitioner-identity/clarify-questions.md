# Clarify Round 1 — 002-practitioner-identity

Session: 2026-08-27. Source: the four assumptions the spec added beyond the
OpenSpec artifacts (spec.md `## Assumptions`). Structured ambiguity scan found
no other material ambiguity — the 12-question disposition round settled the
major decisions, so this round only ratifies or modifies these defaults.
Answer format per question: option letter, "recommended"/"yes", or a short
answer (≤5 words). E.g. `Q1: A, Q2: recommended, Q3: B, Q4: A`.

## Q1. When a staged order awaits co-signature and the scope/jurisdiction registry version changes in between, which registry version governs the order taking effect?

**Recommended:** Option A — re-check at co-signature against the then-current
version; a blocking outcome stops the order; the exercise record pins both the
staging-time versions and the re-check outcome. Authority should be true at the
moment care is actually initiated, and the dual pin keeps both moments
reconstructable.

| Option | Description |
|--------|-------------|
| A | Re-check at co-signature against the current registry version; blocking zone or expired grant stops the staged order; record pins staging-time versions plus re-check outcome |
| B | The staging-time registry version governs; co-signature applies the order without re-check |
| C | Re-check, but only a black-zone outcome stops the order; yellow/red proceed with notification |

## Q2. When a practitioner's credential moves to suspended/revoked mid-course, what exactly is withdrawn?

**Recommended:** Option A — only the authority that binding conferred: a
practitioner whose authority depends on the credential is refused from that
moment; a human practicing under the conventional human gate with no binding
required is unaffected; every refusal is recorded. This keeps wallet-free
operation intact (inherited doctrine) while making credential loss immediate
for those who need it.

| Option | Description |
|--------|-------------|
| A | Withdraw only credential-conferred authority; wallet-free human practice unaffected; refusals recorded |
| B | Suspend all clinical activity of the affected practitioner record until reviewed, credential-dependent or not |

## Q3. What does an AI-treatment consent cover when the patient gives it without narrower scope?

**Recommended:** Option A — the consent record names the practitioner classes
it covers, and an unscoped consent covers AI practitioners generally rather
than one named practitioner. Matches the owner's one-time-revocable ruling;
per-practitioner consent would silently reintroduce per-encounter friction as
staff and AI practitioners rotate.

| Option | Description |
|--------|-------------|
| A | Unscoped consent covers AI practitioners generally; scope field allows narrowing when the patient asks |
| B | Consent is always to a named AI practitioner; a new AI practitioner requires new consent |
| C | Consent is per license level (e.g., covers physician-level AI but nurse-level separately) |

## Q4. What happens when an intended act's class is absent from the scope registry?

**Recommended:** Option A — no inferred or permissive zone; the act is refused
pending a registry version that states the boundary (fail-closed). This turns
the design's "never infer a boundary the registry does not state" risk note
into an enforceable refusal, consistent with the repo's fail-closed posture
everywhere else.

| Option | Description |
|--------|-------------|
| A | Fail closed: unlisted act class → refusal, logged, until a registry version states the boundary |
| B | Fail open with escalation: unlisted act class → treated as yellow zone, proceeds with loud notification |
| C | Fail closed for AI practitioners only; human practitioners proceed under the conventional gate |
