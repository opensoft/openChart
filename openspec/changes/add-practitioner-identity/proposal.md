code_surface: openChart (practitioner and credential DocTypes on the open_chart Frappe application: practitioner record with holder class, optional wallet binding, license binding with a pinned composition-hash set, scope grant and exercise records, the zone calculator and its versioned scope and jurisdiction registries, the co-signature record, the AI-treatment consent and transfer-of-care records, and exercise-time enforcement inside the guarded `open_chart.api.v1` surface; the openXwallet practitioner profile-family contracts themselves live in openxFactory and are coordinated dependent work; no issuance service, no third-party verification service, no real license number, no production authority)
target_release: practitioner identity v1 — lands on a validator-green open_chart application that models a practitioner (human or AI), binds an optional openXwallet credential without making the wallet identifier the subject key, checks narrowing scope grants at every clinical exercise, computes green/yellow/red/black zones from a versioned registry, records N role-qualified signatures against one exercise, and refuses production authority until a real license number is bound to a MedxFactory major release
Status: draft
Source: staged topic `openChart:staging:practitioner-identity-openxwallet`, all six open questions dispositioned accepted by owner ruling 2026-08-26 (disposition round 1). See `supporting-docs/`.

## Why

Zero of openChart's 1,115 catalogued features mention openXwallet or any
AI-practitioner concept, and roughly 575 carry the boilerplate boundary that the
feature "does not own … autonomous clinical action". The catalog encodes `human`
as the predicate wherever clinical authority is exercised (aic-036: the AI
service role holds zero submit permission on clinical DocTypes, and a
service-account identity cannot satisfy a human gate), while the
clinical-companion vision needs *accountable credentialed practitioner*, with
humanity as one way to qualify.

An ungoverned AI acting autonomously is exactly what aic-036 rightly forbids; a
practitioner holding a validated, scoped, revocable credential and acting inside
a verified boundary is a different object, and openChart has no name for it. The
governance machinery already exists — credential registry, scope-of-practice
dossier, competency examination and recertification, license suspension,
practice monitoring, privileging, the authority triad — and none of it is
discarded. What has no home is the practitioner itself: an identity that can
hold a state license, present a credential, be scoped, supervised, revoked, and
attributed liability when it errs. The credential half needs no inventing
either — openXwallet is a ratified contract family, but it has no expertise
attestation, no license field, and closed schemas, which is precisely why the
sanctioned move is a profile family over that neutral core, driven by the domain
that needs it first.

## What Changes

- Add the practitioner as a **modelled clinical actor, human or AI**, with a
  holder class drawn from openXwallet's vocabulary (person, practitioner,
  organisation, agent) rather than a parallel one.
- Make **wallet binding optional and non-identifying**: a practitioner record may
  reference a wallet holder, the wallet identifier is never the subject key, and
  practitioner modelling, ordering and signing remain fully operable with no
  wallet present.
- Bind a **state license to a pinned set of composition hashes**. Any
  composition change revokes per openXwallet's existing rule; `model_version` and
  `policy_version` are **major** (re-licensure), while `retrieval_corpus`,
  `parameters`, `prompt_contract` and `tool_manifest` are **minor** — fast
  automatic reissue carrying an attestation, license unbroken.
- Carry the **composition hash on every clinical exercise record**, so proving
  that the licensed practitioner is the practicing one is a join against the
  license's pinned hash set at the act's timestamp, not a periodic attestation.
- Check **monotonically narrowing scope grants at every clinical act**, with
  proof of possession, inside the existing guarded API surface.
- Add **supervision tiers**: pre-licensure grants cap at `act` and stage an order
  that takes effect only after a human medical director's or managing
  physician's co-signature; post-licensure is `act_unsupervised`; QA runs the
  same tier against synthetic data only with a simulated license; the production
  flip demands a real license number tied to a MedxFactory major release.
- Add a **co-signature record**: one exercise, N role-qualified signatures
  (performer, supervisor, council member, dissenting member), serving both
  supervision and the composite council practitioner with one structure.
- Add a **zone calculator in openChart's enforcement layer, not the wallet**,
  placing each intended action at a distance from the *license* boundary and
  returning green, yellow, red or black — soft block with notification on yellow,
  escalation on red, shutdown on black — reading a **versioned scope registry**
  so per-jurisdiction calibration is data, not code, and a zone is reproducible
  as of the time the action was taken.
- Add one **jurisdiction registry** carrying disclosure obligations, supervision
  requirements and license-boundary calibration per state, consumed by the zone
  calculator and fed by a named ongoing legal-research work item.
- Make **consent to AI treatment one-time and revocable** on the patient rather
  than per-encounter, and make revocation **open a transfer-of-care workflow with
  continuity guarantees** — the AI's authority to initiate new clinical acts
  stops, active orders and the plan remain in force, and a named human
  practitioner accepts the care.
- Restate the **human-gate predicate as `accountable credentialed practitioner`**
  across the affected brainstorm-stage catalog assumptions (aic-036, aic-034,
  aic-042, plt-004, plt-005, plt-043, plt-044, phr-011, phr-013, ord-030–034,
  doc-023, doc-027) — restatement, never deletion, and the largest and least
  mechanical part of the work.
- Excluded: credential issuance service, third-party (court or state board)
  verification, any real license number, any production authority flip, and any
  change to promoted `expanded-patient-intake` requirements.

## Capabilities

### New Capabilities

- `practitioner-identity`: the practitioner as a modelled clinical actor (human
  or AI); optional openXwallet credential binding and validation; license
  binding over a pinned composition-hash set with the major/minor reissue line;
  narrowing scope grants and exercise-time checks; the zone calculator and its
  versioned scope and jurisdiction registries; supervision tiers and the
  co-signature record; one-time revocable consent to AI treatment and the
  transfer-of-care it opens.

### Modified Capabilities

None. `expanded-patient-intake` requirements are unchanged: its
authority boundary governs what an *intake artifact* may become (no intake,
statement, API response or extension event creates a prescription, diagnosis,
order, administration, recommendation or autonomous action), and this change
neither weakens that nor grants intake any new authority. The human-gate
restatement targets brainstorm-stage catalog assumptions, which are not
promoted specs.

## Impact

- **openChart:** new practitioner, credential, license, scope-grant, exercise,
  co-signature, consent and transfer-of-care records; the zone calculator and
  two versioned registries; exercise-time enforcement extending the guarded
  `open_chart.api.v1` write surface and its controller guards; migrations,
  permissions, audit and synthetic fixtures for all of it.
- **openxFactory:** hosts openXwallet's neutral core and must host the four
  practitioner profile-family contracts openChart authors — specialty/expertise
  attestation, state-license-number binding, zone model declaration, co-signature
  record kind. The extension path is confirmed by the owner of both
  repositories; the contracts are unauthored today, so this change treats
  contract authoring as a **coordinated dependency, not a blocker**.
- **MedxFactory:** the licensed AI practitioner itself, whose major release the
  license binds to, and whose wallet brainstorms assert the same human-gate
  predicate and need the same restatement. Until that lands, openChart's
  position and MedxFactory's recorded position are inconsistent — stated, not
  hidden.
- **HealthLinc:** the nurse-level AI is the second consumer, so the profile
  family, zones and supervision tiers must support multiple license levels with
  escalation to the treating practitioner as the boundary crossing.
- **Documentation blast radius:** the predicate restatement touches roughly 575
  brainstorm catalog entries carrying the autonomous-clinical-action boundary.
  Most are boilerplate; the load-bearing minority is named in What Changes.
- **Safety:** this change grants no authority, issues no credential, and licenses
  nothing. QA and production are split, QA is synthetic-only under a simulated
  license, and production authority is refused until a real license number is
  bound to a MedxFactory major release.
