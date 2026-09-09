# Feature Specification: Practitioner Identity — The Accountable Credentialed Practitioner

**Feature Branch**: `002-practitioner-identity`

**Created**: 2026-08-27

**Status**: Draft

**Input**: User description: "Implement OpenSpec change
add-practitioner-identity: practitioner as a modelled clinical actor
(human or AI), openXwallet-validated authority via the practitioner
profile family, license binding over a pinned composition-hash set,
scope grants checked at every clinical exercise, zone calculator over
versioned registries, supervision tiers with co-signature, one-time
revocable AI-treatment consent, accountable-credentialed-practitioner
gate predicate"

## Change Linkage *(immutable)*

- **Governing change**: `add-practitioner-identity` (all six design
  questions dispositioned `accepted` by owner ruling 2026-08-26,
  disposition round 1; thirteen ADDED requirements, thirty-four
  scenarios).
- **This feature**: `specs/002-practitioner-identity/` on branch
  `002-practitioner-identity`.
- The change's proposal, design and capability spec are the settled
  source of truth. This specification translates them into user-facing
  form; it does not reopen a dispositioned decision.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - The practitioner exists, credentialed or not (Priority: P1)

A clinic registers its clinical actors. Some are people; one is an AI
physician. Both are practitioners: each carries a holder class drawn
from the openXwallet vocabulary (person, practitioner, organisation,
agent), a display identity, a declared specialty or expertise
attestation, a lifecycle state and audit provenance. A practitioner may
additionally bind to a credential held in an openXwallet holder record,
which strengthens its authority but never constitutes it — the
practitioner's own identifier stays the subject key, and a clinic that
holds no credentials at all still registers practitioners, places
orders and signs documents exactly as before.

**Why this priority**: Every later slice is a check against this
record. Without a practitioner that can be human or AI without being
two different kinds of thing, there is nothing to license, scope,
supervise or hold accountable. The wallet-free half is what keeps the
capability from becoming a dependency on unauthored contracts in
another repository: it is the fallback that makes the rest safe to
build incrementally.

**Independent Test**: Register human and AI practitioners on a clean
installation with no credential binding anywhere, and exercise
practitioner modelling, ordering and signing end to end under the
conventional human gate. Delivers a practitioner registry that is
immediately useful on its own and proves the wallet-free path before
any authority machinery exists.

**Acceptance Scenarios**:

1. **Given** an operator registering a clinical actor, **When** a
   practitioner is created with holder class `agent` and a declared
   specialty attestation, **Then** the record is a first-class
   practitioner addressable by every clinical surface that accepts a
   human practitioner, with no separate record type for AI.
2. **Given** a holder class outside the openXwallet vocabulary, **When**
   the practitioner is created, **Then** the record is rejected rather
   than stored under a parallel term.
3. **Given** a practitioner with an optional credential binding,
   **When** the binding is recorded, **Then** it carries holder
   identifier, holder class, credential state (active, suspended,
   revoked) and binding provenance, while the practitioner's own
   identifier remains its subject key.
4. **Given** a caller supplying a credential holder identifier where a
   practitioner identifier is expected, **When** the request is made,
   **Then** it is refused and no practitioner is resolved, created or
   merged from that identifier.
5. **Given** an installation with no credential binding on any
   practitioner, **When** practitioners are modelled, orders are placed
   and clinical documents are signed, **Then** every one of those
   operations succeeds under the conventional human gate and no path
   demands a credential identifier.

---

### User Story 2 - Authority is checked at the moment it is exercised (Priority: P2)

A practitioner's authority travels as a scope grant: which act classes,
which object classes, which authority tier (attest, request, act,
act_unsupervised), an expiry, and the lineage of the grant it was
derived from. Every consequential clinical act is checked against that
grant at the moment of the act, with proof of possession, and the check
writes an exercise record that says who acted, on what, under which
grant. A pre-licensure practitioner's grant caps at `act`: the order it
produces is staged and inert until a human medical director or managing
physician co-signs. One clinical act carries one co-signature record
holding as many role-qualified signatures as the act needs — performer,
supervisor, council member, dissenting member — so supervision and a
council of AI practitioners share one structure and dissent is recorded
rather than lost.

**Why this priority**: This is the enforcement that makes the
practitioner record consequential. Registering an AI practitioner
without an exercise-time check would grant authority by omission, which
is precisely the ungoverned case the repository already forbids. The
supervision tier is what makes a pre-licensure AI practitioner safe to
run at all: a human signs before anything reaches a patient.

**Independent Test**: With the P1 registry in place and fixture grants
and licenses supplied, drive authorized and refused acts through the
clinical write path and confirm each authorized act produced exactly
one exercise record and each refusal is recorded. Drive a pre-licensure
order to staged, co-sign it, and confirm it took no effect before the
signature. Delivers the accountability record and the supervision gate
without any zone or registry machinery existing.

**Acceptance Scenarios**:

1. **Given** a practitioner holding a grant that carries the act class
   and object class, **When** it performs the act with proof of
   possession, **Then** the act is authorized and an exercise record
   captures the practitioner, the act and object classes, the
   presenting key, the composition identifier in force, the grant
   reference, the registry versions evaluated, the computed zone and
   the timestamp.
2. **Given** a clinical write that carries no exercise record, **When**
   it reaches the clinical write path, **Then** the write is refused.
3. **Given** a grant derivation that adds an act class, object class,
   authority tier or expiry its parent does not carry, **When**
   derivation is attempted, **Then** it is rejected.
4. **Given** a practitioner attempting an act whose class its grant
   does not carry, **When** the act is exercised, **Then** it is
   refused and the refusal is recorded.
5. **Given** a parent grant that is revoked, **When** any grant derived
   from it is presented, **Then** it authorizes nothing, with no
   individual revocation of the descendants required.
6. **Given** a pre-licensure AI practitioner capped at authority tier
   `act`, **When** it issues an order, **Then** the order is staged,
   takes no effect, and becomes effective only once a medical
   director's or managing physician's co-signature is recorded.
7. **Given** a council of AI practitioners reaching a decision with one
   member dissenting, **When** the decision is signed, **Then** one
   co-signature record against the single exercise carries the gateway
   performer signature, the assenting council-member signatures and the
   dissenting-member signature.
8. **Given** an exercise that already has a co-signature record,
   **When** a second record for the same exercise is attempted,
   **Then** it is rejected and the additional signature is appended to
   the existing record instead.
9. **Given** a service-account or otherwise unattributed identity with
   no practitioner record, **When** it attempts a consequential
   clinical write, **Then** the write is refused.

---

### User Story 3 - Distance from the license boundary decides what proceeds (Priority: P3)

Before a clinical act takes effect, the system places it at a distance
from the practitioner's *license* boundary and returns a zone: green
well inside, yellow near the boundary from the inside, red near it from
the outside, black well outside. Green proceeds. Yellow is a soft block
with notification to the practitioner. Red escalates to the supervising
or treating practitioner. Black shuts the practitioner's clinical
authority down. The boundaries themselves are data: a versioned scope
registry maps act and object classes to license boundaries with
per-jurisdiction and per-license-level calibration, and a single
versioned jurisdiction registry carries each state's AI-disclosure
obligations, pre-licensure supervision requirements and boundary
calibration. A legal correction is a new registry version, authored by
a named ongoing legal-research work item, and every exercise pins the
versions it was evaluated against so a zone can be reproduced years
later exactly as it was computed.

**Why this priority**: Scope grants say what a practitioner was
allowed; zones say how close the intended act sits to the edge of the
license, which is the boundary a state board recognises. Holding that
calibration as reviewable data rather than compiled rules is what lets
a legal researcher correct the law's representation without a code
change, and what lets one calculator serve a nurse-level AI and a
physician-level AI at different boundaries.

**Independent Test**: Seed one scope registry version and one
jurisdiction registry version for a single jurisdiction and two license
levels, then evaluate a fixed set of intended acts and confirm the
returned zone and the enforcement outcome for each of green, yellow,
red and black. Re-evaluate a recorded act against its pinned versions
and confirm the original zone reproduces. Delivers reviewable,
jurisdiction-aware boundary enforcement on top of the P2 check.

**Acceptance Scenarios**:

1. **Given** an intended action computed as `yellow`, **When** the
   practitioner attempts it, **Then** the action is soft-blocked, the
   practitioner is notified, and the zone is recorded on the exercise.
2. **Given** an intended action computed as `red`, **When** the
   practitioner attempts it, **Then** the act does not take effect on
   the practitioner's own authority and the matter escalates to the
   supervising or treating practitioner.
3. **Given** an intended action computed as `black`, **When** the
   practitioner attempts it, **Then** the practitioner's clinical
   authority is shut down and the act does not take effect.
4. **Given** a credential that presents a zone value of its own,
   **When** the action is evaluated, **Then** the presented value is
   ignored and the zone is computed from the registry.
5. **Given** a legal correction to one jurisdiction's boundary for an
   act class, **When** a new scope registry version carries the
   correction, **Then** enforcement changes with no change to the
   enforcement rules themselves.
6. **Given** an act recorded under an earlier registry version, **When**
   it is re-examined later, **Then** the pinned version reproduces the
   zone that was computed at the time.
7. **Given** a nurse-level practitioner and a physician-level
   practitioner attempting the same act class in the same jurisdiction
   under one registry version, **When** each is evaluated, **Then** the
   same calculator returns different zones because the license level
   selects a different boundary.
8. **Given** a jurisdiction whose registry row records a per-encounter
   AI-disclosure obligation, **When** an act is evaluated in that
   jurisdiction, **Then** disclosure becomes a condition on the act
   while the one-time consent rule stands unchanged elsewhere.
9. **Given** two jurisdictions stating different supervision
   requirements for pre-licensure practice, **When** acts are evaluated
   in each, **Then** both requirements apply from rows of the same
   registry version according to the act's jurisdiction.
10. **Given** an act class the registry version does not describe for
    the acting practitioner's jurisdiction and license level, **When**
    the act is evaluated, **Then** no boundary is inferred, no
    permissive zone is returned, and the act is refused pending a
    registry version that states the boundary.

---

### User Story 4 - The licensed practitioner is provably the practicing one (Priority: P4)

A license binding carries the license number, jurisdiction, license
level, environment, effective interval, state and an append-only set of
composition identifiers the license covers, each computed over the
practitioner's declared composition — model version, policy version,
prompt contract, tool manifest, parameters and retrieval corpus. Any
composition change revokes the current binding. A change confined to
retrieval corpus, parameters, prompt contract or tool manifest is
minor: the binding reissues automatically, the new identifier joins the
covered set, an attestation names the changed component with its prior
and new identifier, and the license number is unchanged. A change to
model version or policy version is major: re-licensure, not reissue.
Because every exercise record carries the composition identifier in
force at that moment, an auditor asking whether the practitioner that
performed a recorded act was the licensed one gets the answer as a join
against the covered set at the act's timestamp — no monitoring process,
no periodic attestation, no gaps.

**Why this priority**: Continuity of licensed identity is the question
a state board or a court actually asks, and it is asked retrospectively
about one act on one date. Making it a property of the evidence rather
than of a monitoring process is what makes the record defensible years
after the fact. This slice also holds the QA/production split that
keeps a simulated license from ever touching real data.

**Independent Test**: Bind a synthetic license over a seeded covered
set, drive a minor composition change and a major one, and confirm the
reissue, the attestation and the refusal respectively. Then verify a
recorded act's continuity purely from the act's identifier and the
license's covered set at that timestamp. Delivers retrospective
provability without depending on the zone slice.

**Acceptance Scenarios**:

1. **Given** an AI practitioner whose retrieval corpus changes and
   nothing else, **When** the change is recorded, **Then** the binding
   is automatically reissued, the new composition identifier joins the
   covered set, an attestation records the changed component with prior
   and new identifier, and the license number is unchanged.
2. **Given** an AI practitioner whose model version changes, **When**
   the change is recorded, **Then** the binding is revoked, no
   automatic reissue occurs, and clinical authority is refused until a
   re-licensure binding exists.
3. **Given** a covered set that already contains an identifier, **When**
   a caller attempts to remove or overwrite it, **Then** the operation
   is rejected and the historical coverage remains reconstructible.
4. **Given** an auditor asking whether the practitioner that performed
   a recorded act was the licensed one, **When** the question is put,
   **Then** the answer is computed from the act's composition
   identifier against the license's covered set at that timestamp, with
   no monitoring record required.
5. **Given** an AI practitioner with no valid license binding, **When**
   it attempts a clinical act, **Then** the act is refused regardless
   of its scope grant or computed zone.
6. **Given** a practitioner holding a simulated QA license, **When** it
   attempts a write against non-synthetic data, **Then** the write is
   refused.
7. **Given** an attempt to flip an environment to production authority
   with no real license number bound to a named MedxFactory major
   release, **When** the flip is attempted, **Then** it is refused and
   no production clinical authority is granted.

---

### User Story 5 - Consent is given once, revoked freely, and never abandons the patient (Priority: P5)

A patient consents to treatment by an AI practitioner once. The consent
is a revocable record on the patient carrying the consenting party, the
time, the scope of the consent and its state, and subsequent encounters
proceed without a fresh prompt unless the patient's jurisdiction states
a per-encounter disclosure obligation. An AI practitioner exercises no
clinical authority for a patient with no active consent. When a patient
revokes — including mid-course, with orders active and a plan running —
the AI practitioner's authority to initiate new clinical acts stops
immediately, the active orders and the treatment plan remain in force,
and a transfer of care opens. The transfer completes when a named human
practitioner accepts it, and until then it is a visible open state with
the prior accountable practitioner still of record.

**Why this priority**: It is the patient-facing half, and it depends on
the authority machinery above being in place to have anything to stop.
Its failure mode is the one that must not happen: a revocation that
leaves a patient with an active treatment plan and no practitioner of
record is clinically worse than the thing revoked.

**Independent Test**: Record consent for a synthetic patient, run
encounters without further prompting, revoke mid-course with active
orders, and confirm that new AI acts stop while orders and plan
continue, that a transfer opens, that an unaccepted transfer reads as
open with the prior practitioner still accountable, and that acceptance
by a named human completes it. Delivers the consent lifecycle and the
continuity guarantee as a demonstrable patient-safety property.

**Acceptance Scenarios**:

1. **Given** a patient who has consented to AI treatment, **When**
   later encounters occur while the consent remains active, **Then**
   they proceed with no further consent prompt.
2. **Given** a patient with no active consent record, **When** an AI
   practitioner attempts a clinical act for that patient, **Then** the
   exercise is refused.
3. **Given** a patient who revokes consent while orders are active and
   a plan is running, **When** the revocation is recorded, **Then** the
   AI practitioner initiates no new clinical acts, the active orders
   and the treatment plan remain in force, and a transfer of care
   opens.
4. **Given** an open transfer of care, **When** a named human
   practitioner accepts it, **Then** the transfer reaches its
   completion state and the accepting practitioner is the accountable
   practitioner of record from that time.
5. **Given** a transfer of care that has not yet been accepted,
   **When** the patient's record is examined, **Then** the transfer
   reads as a visible open state with the prior accountable
   practitioner still of record, and care is never silently abandoned.

---

### Edge Cases

- A practitioner's credential binding moves to suspended or revoked
  mid-course of care: authority that depended on the binding stops at
  once and the refusal is recorded, while a human practitioner
  operating under the conventional human gate with no binding required
  is unaffected.
- An act's composition identifier is not in the license's covered set
  at the act's timestamp: the continuity join returns a mismatch, and
  the act is attributable to no valid license.
- An out-of-scope act that also lands in a red or black zone: the
  strictest refusal applies, clinical authority shuts down on black,
  and both the grant miss and the zone are recorded on the refusal.
- A staged pre-licensure order that is never co-signed: it stays inert
  indefinitely and never takes effect by timeout or default.
- A registry version is superseded between an order being staged and
  its co-signature: the authority check re-runs against the version
  current at co-signature time and a blocking zone prevents the order
  taking effect.
- A grant expires between an order being staged and its co-signature:
  the order does not become effective on an expired grant.
- Consent is revoked while an act is already staged awaiting
  co-signature: the staged act does not become effective and the
  transfer of care opens with the active orders and plan intact.
- A patient revokes and then re-consents before a transfer is accepted:
  exactly one accountable practitioner is of record throughout, and the
  transfer's state is explicit rather than implied.
- The whole capability runs with no credential binding anywhere:
  practitioner modelling, ordering and signing operate under the
  conventional human gate and no path demands a credential.
- A simulated QA license is presented against non-synthetic data: the
  write is refused, and no configuration makes it succeed.
- A caller presents a credential holder identifier as a practitioner
  identifier: refused, with no record resolved, created or merged.
- Two jurisdictions disagree about a pre-licensure supervision
  requirement for the same act: each applies within its own
  jurisdiction from the same registry version.
- The registry says nothing about an act class for the practitioner's
  jurisdiction and license level: no boundary is invented, no permissive
  zone is returned, and the act is refused until the registry states the
  boundary.

## Requirements *(mandatory)*

### Functional Requirements

**Practitioner identity and credential binding**

- **FR-001**: The system MUST model a practitioner as a clinical actor
  whose identity is independent of species, carrying a holder class
  drawn from the openXwallet vocabulary (`person`, `practitioner`,
  `organisation`, `agent`), display identity, specialty or expertise
  attestation, lifecycle state and audit provenance.
- **FR-002**: An AI practitioner MUST be representable without a
  separate kind of record, and MUST be addressable by every clinical
  surface that accepts a human practitioner.
- **FR-003**: The system MUST reject a practitioner whose holder class
  falls outside the openXwallet vocabulary rather than storing a
  parallel term.
- **FR-004**: A practitioner MAY carry an optional credential binding
  recording holder identifier, holder class, credential state
  (`active`, `suspended`, `revoked`) and binding provenance.
- **FR-005**: A credential holder identifier MUST NOT be a
  practitioner's subject key and MUST NOT be used to resolve, create or
  merge practitioner records; a request presenting one where a
  practitioner identifier is expected MUST be refused.
- **FR-006**: Practitioner modelling, ordering and signing MUST remain
  fully operable with no credential binding present anywhere, under the
  conventional human gate, with no path requiring a credential
  identifier.

**License binding and composition continuity**

- **FR-007**: A license binding MUST carry license number,
  jurisdiction, license level, environment, effective interval, state,
  and an append-only set of composition identifiers the license covers,
  each computed over the declared composition components: model
  version, policy version, prompt contract, tool manifest, parameters
  and retrieval corpus.
- **FR-008**: Any change to the declared composition MUST revoke the
  current license binding.
- **FR-009**: A change confined to retrieval corpus, parameters, prompt
  contract or tool manifest MUST be classified minor and MUST trigger
  automatic reissue that adds the new composition identifier to the
  covered set and writes an attestation naming the changed component,
  the prior identifier and the new one, leaving the license number
  unchanged.
- **FR-010**: A change to model version or policy version MUST be
  classified major, MUST NOT trigger automatic reissue, and MUST refuse
  clinical authority until a re-licensure binding exists.
- **FR-011**: The covered set MUST be append-only: removal or in-place
  overwrite MUST be rejected, and a license's coverage over time MUST
  remain reconstructible.
- **FR-012**: Verification that the licensed practitioner performed a
  given act MUST be answerable as a join — the act's composition
  identifier present in the license's covered set at the act's
  timestamp — with no periodic attestation or monitoring process
  required.

**Exercise records**

- **FR-013**: Every exercise of clinical authority MUST write an
  exercise record carrying the acting practitioner, the act and object
  classes, the presenting key, the composition identifier in force at
  that moment, the scope-grant reference, the scope-registry and
  jurisdiction-registry versions evaluated, the computed zone and the
  timestamp.
- **FR-014**: A clinical write that carries no exercise record MUST be
  refused.
- **FR-015**: Every refusal of a clinical act MUST be recorded with the
  reason it was refused.

**Scope grants**

- **FR-016**: Authority MUST travel as scope grants carrying act
  classes, object classes, authority tier (`attest`, `request`, `act`,
  `act_unsupervised`), expiry and derivation lineage.
- **FR-017**: A derived grant MUST NOT widen act classes, object
  classes, authority tier or expiry beyond its parent, and a widening
  derivation MUST be rejected.
- **FR-018**: Every clinical act MUST be checked against the acting
  practitioner's grant at the moment of exercise, with proof of
  possession, and an act outside the granted classes MUST be refused.
- **FR-019**: Revocation of a parent grant MUST invalidate every grant
  derived from it without requiring individual revocation of the
  descendants.

**Zones and registries**

- **FR-020**: The system MUST compute the zone of each intended action
  in its own enforcement, never reading it from a credential, returning
  `green` (well inside), `yellow` (near the boundary from inside),
  `red` (near the boundary from outside) or `black` (well outside),
  with distance measured from the license boundary.
- **FR-021**: Enforcement MUST be a soft block with notification to the
  practitioner on `yellow`, escalation to the supervising or treating
  practitioner on `red`, and shutdown of clinical authority on `black`;
  in every blocking case the computed zone MUST prevent the write
  rather than annotate it.
- **FR-022**: The zone calculation MUST read a scope registry mapping
  act and object classes to license boundaries, versioned as a whole,
  with per-jurisdiction and per-license-level calibration held as
  registry data rather than as rules.
- **FR-023**: One calculation MUST serve every jurisdiction and license
  level, such that the same act class in the same jurisdiction under
  one registry version can return different zones for different license
  levels.
- **FR-024**: Each exercise MUST pin the registry versions it was
  evaluated against, so a past action's zone is reproducible exactly as
  computed at the time it was taken.
- **FR-025**: A jurisdictional correction MUST be deliverable as a new
  registry version with no change to the enforcement rules.
- **FR-026**: The system MUST maintain a single versioned jurisdiction
  registry carrying, per jurisdiction, AI-disclosure obligations,
  supervision requirements for pre-licensure practice, and
  license-boundary calibration, consumed through the zone calculation
  rather than through a separate compliance surface.
- **FR-027**: The jurisdiction registry MUST be maintained by a named
  ongoing legal-research work item with a recorded owner and cadence,
  and the zone calculation MUST NOT infer a boundary the registry does
  not state.
- **FR-028**: A jurisdiction requiring per-encounter AI disclosure MUST
  be representable as registry data that makes disclosure a condition
  on acts in that jurisdiction, without changing the general one-time
  consent rule elsewhere.

**Supervision, co-signature and authority environments**

- **FR-029**: A pre-licensure practitioner's grants MUST cap at
  authority tier `act`, and an order it produces MUST be staged and
  take no effect until a human medical director or managing physician
  records a co-signature; a post-licensure practitioner MAY hold
  `act_unsupervised`.
- **FR-030**: In QA the same tier MUST run against synthetic data only
  under a simulated license requiring no co-signature, and a simulated
  license MUST NOT authorize any write against non-synthetic data.
- **FR-031**: The flip to production authority MUST require a real
  license number bound to a named MedxFactory major release and MUST be
  a recorded act rather than a configuration default.
- **FR-032**: A co-signature record MUST hold exactly one exercise and
  one or more signatures, each qualified by role as `performer`,
  `supervisor`, `council member` or `dissenting member`, and each
  carrying signer identity, credential reference where present, and
  signing time.
- **FR-033**: A clinical act MUST NOT be represented by several
  competing signature records: a second co-signature record for an
  exercise that already has one MUST be rejected and the additional
  signature appended to the existing record.
- **FR-034**: Dissent MUST be recorded as a signer role on the same
  co-signature record rather than as a separate object.

**Consent and transfer of care**

- **FR-035**: Consent to treatment by an AI practitioner MUST be
  recorded as a one-time, revocable record on the patient carrying
  consenting party, time, scope and state, and MUST NOT require a
  per-encounter consent prompt unless the jurisdiction registry states
  a per-encounter disclosure obligation.
- **FR-036**: An AI practitioner MUST NOT exercise clinical authority
  for a patient with no active consent record.
- **FR-037**: Revocation of consent MUST immediately stop the AI
  practitioner's authority to initiate new clinical acts while leaving
  active orders and the treatment plan in force, and MUST open a
  transfer-of-care record.
- **FR-038**: A transfer of care MUST complete by a named human
  practitioner accepting it, MUST carry a completion state so
  revocation is never an open-ended limbo, and an unaccepted transfer
  MUST be a visible open state with the prior accountable practitioner
  still of record.
- **FR-039**: Exactly one accountable practitioner of record MUST exist
  at every moment across consent, revocation and transfer.

**The gate predicate**

- **FR-040**: The gate on every consequential clinical act MUST be that
  an accountable credentialed practitioner exercises it: a practitioner
  of any holder class with an active credential binding where one is
  required, a valid license binding covering its current composition, a
  scope grant carrying the act, a non-blocking zone, and the
  co-signature its supervision tier demands. Humanity MUST be one way
  to qualify, not the predicate.
- **FR-041**: A service-account or otherwise unattributed identity MUST
  NOT satisfy the gate, and an AI practitioner with no valid license
  binding MUST hold no clinical authority regardless of grant or zone.
- **FR-042**: The catalog assumptions that encode `human` as the gate
  predicate — aic-036, aic-034, aic-042, plt-004, plt-005, plt-043,
  plt-044, phr-011, phr-013, ord-030 through ord-034, doc-023 and
  doc-027 — MUST be restated in terms of the accountable credentialed
  practitioner, never deleted, keeping the prohibition on ungoverned
  autonomous clinical action intact.
- **FR-043**: The remaining boilerplate catalog entries carrying the
  autonomous-clinical-action boundary MUST be swept, with each entry
  either restated or recorded as left unchanged with its reason, and
  the cross-repository inconsistency with MedxFactory's own recorded
  position MUST be flagged rather than assumed resolved.
- **FR-044**: This feature MUST grant no clinical authority, issue no
  credential and bind no real license number; its evidence MUST show
  synthetic-only fixtures, the simulated-license boundary and
  wallet-free operation.

### Key Entities

- **Practitioner** — a clinical actor, human or AI, with a holder class
  from the openXwallet vocabulary, display identity, specialty or
  expertise attestation, lifecycle state and provenance. The subject of
  accountability, and the thing every authority check resolves to.
- **Credential Binding** — an optional reference from a practitioner to
  an openXwallet holder, carrying holder identifier, holder class,
  credential state and binding provenance. Strengthens authority;
  never constitutes identity.
- **License Binding** — a license number in a jurisdiction at a license
  level, for an environment, over an effective interval, with a state
  and an append-only set of composition identifiers it covers.
- **Composition Attestation** — the record written on every minor
  reissue naming the changed component, the prior composition
  identifier and the new one.
- **Scope Grant** — act classes, object classes, authority tier,
  expiry and derivation lineage; narrows monotonically from its parent
  and is revoked through derivation.
- **Exercise Record** — one exercise of clinical authority: acting
  practitioner, act and object classes, presenting key, composition
  identifier, grant reference, registry versions, computed zone,
  timestamp. The unit the co-signature, the zone and the continuity
  join all attach to.
- **Zone Determination** — the placement of an intended act at a
  distance from the license boundary, as green, yellow, red or black,
  with the registry versions it was computed from.
- **Scope Registry** — versioned mapping of act and object classes to
  license boundaries, calibrated per jurisdiction and per license
  level, held as reviewable data.
- **Jurisdiction Registry** — one versioned registry of per-state
  AI-disclosure obligations, pre-licensure supervision requirements and
  license-boundary calibration, authored by the legal-research work
  item.
- **Co-Signature Record** — one exercise and N role-qualified
  signatures (performer, supervisor, council member, dissenting
  member), each with signer identity, credential reference where
  present and signing time.
- **AI-Treatment Consent Record** — a one-time, revocable record on the
  patient with consenting party, time, scope and state.
- **Transfer of Care Record** — opened by consent revocation, naming
  the accepting human practitioner, carrying a completion state, and
  holding the accountability line unbroken while active orders and the
  plan remain in force.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Every clinical action by an AI practitioner is
  attributable to a verified credential and a license binding covering
  the composition in force at the moment of the act; zero acts in the
  evidence set are unattributable.
- **SC-002**: An unsupervised order from a pre-licensure practitioner
  is impossible: 100% of orders produced at authority tier `act` remain
  without effect until a medical director's or managing physician's
  co-signature is recorded, verified by test.
- **SC-003**: A zone determination for any past action is reproducible
  as of its timestamp: 100% of sampled historical exercises reproduce
  their recorded zone from their pinned registry versions.
- **SC-004**: Continuity of licensed identity is answerable from the
  evidence alone for every recorded act, with no monitoring record and
  no periodic attestation anywhere in the answer.
- **SC-005**: The capability operates wallet-free: the practitioner,
  ordering and signing suites pass with zero credential bindings
  present, and no path demands a credential identifier.
- **SC-006**: Every refusal named in this specification has a negative
  test that fires — credential identifier as subject key, unrecognised
  holder class, widened derivation, act outside grant, black zone,
  simulated license against non-synthetic data, production flip without
  a real license, act without consent, second co-signature record,
  service-account clinical write, clinical write with no exercise
  record, act class the registry does not describe — and a refusal that
  stops firing is itself a failure.
- **SC-007**: A jurisdictional legal correction ships entirely as a new
  registry version: zero changes to enforcement rules are required to
  deliver it.
- **SC-008**: One calculation serves at least two license levels: a
  nurse-level and a physician-level practitioner receive different
  zones for the same act class in the same jurisdiction under the same
  registry version.
- **SC-009**: No production authority exists at the end of this
  feature: zero real license numbers are bound, zero production flips
  occur, and an attempted flip without a real license number bound to a
  named MedxFactory major release is refused.
- **SC-010**: A simulated QA license authorizes zero writes against
  non-synthetic data.
- **SC-011**: Exactly one accountable practitioner of record exists at
  every moment across consent, revocation and transfer of care: no
  interval has zero and none has two.
- **SC-012**: Every named catalog assumption reads in terms of the
  accountable credentialed practitioner with the prohibition on
  ungoverned autonomous clinical action intact, and every remaining
  boilerplate entry is either restated or recorded with a reason for
  being left unchanged — zero entries silently untouched.
- **SC-013**: No zone determination is ever produced from an inferred
  boundary: for every act class the registry does not describe, the act
  is refused rather than assigned a permissive zone.
- **SC-014**: A clinician or reviewer can answer, for any recorded
  clinical act, who acted, under what license and scope, in which zone,
  and who co-signed, from the act's own records without consulting a
  separate system.

## Assumptions

- The openXwallet neutral core is a ratified contract family and its
  vocabulary is taken as given: holder classes, authority tiers and
  credential states are inherited rather than redefined.
- The four practitioner profile-family contracts (specialty attestation,
  state-license-number binding, zone model declaration, co-signature
  record kind) are unauthored. This feature designs its records to that
  shape and keeps every path operable wallet-free, so an unratified
  contract weakens authority strength rather than blocking the
  capability.
- QA and production are different authority environments. QA runs
  synthetic data only under a simulated license; production requires a
  real license number. Neither a real license number nor a production
  flip is created in this feature.
- No credential issuance service, no credential runtime, and no
  third-party (court or state board) verification exists or is built
  here; third-party verification is deferred.
- The restatement of the catalog human-gate predicate is documentation
  work inside this feature's scope. MedxFactory's own restatement is
  outside this repository and is flagged, not assumed.
- The promoted `expanded-patient-intake` requirements are unchanged and
  this feature grants intake artifacts no new authority.
- The legal-research work item is the sole author of registry data; the
  first registry version seeds one jurisdiction and at least two license
  levels, and which jurisdiction is seeded first is the work item's
  determination rather than a decision of this specification.
- *(Decision made here, not in the governing change)* Where a registry
  version is superseded between an order being staged and its
  co-signature, the authority check re-runs against the version current
  at co-signature time; a blocking zone or an expired grant prevents the
  staged order taking effect. The exercise record retains the versions
  pinned at staging and records the co-signature-time re-check outcome.
- *(Decision made here, not in the governing change)* A credential
  binding moving to `suspended` or `revoked` withdraws only the
  authority that binding conferred: a practitioner whose authority
  depended on it is refused from that moment, while a human practitioner
  operating under the conventional human gate with no binding required
  is unaffected. The refusal is recorded either way.
- *(Decision made here, not in the governing change)* An AI-treatment
  consent record's scope names the practitioner classes it covers, and a
  consent with no narrower scope covers treatment by AI practitioners
  generally rather than one named practitioner.
- *(Scope boundary)* The governing design's four open questions are out
  of scope for this feature: whether the companion's witness credential
  is a reduced practitioner profile or a distinct one; the escalation
  contract between a nurse-level AI and the treating practitioner;
  which jurisdiction seeds the first registry version and at what
  cadence; and whether a council practitioner holds one license over the
  collective or one per member. The co-signature record supports both
  council readings, and this feature chooses neither.

### Dependencies

- **openxFactory** — hosts the openXwallet neutral core and must host
  the four practitioner profile-family contracts. Contract authoring is
  coordinated dependent work with a recorded coordination state, not a
  blocker.
- **MedxFactory** — the licensed AI practitioner whose major release a
  production license would bind to, and the repository whose recorded
  human-gate position stays inconsistent with openChart's until it is
  restated there.
- **HealthLinc** — the nurse-level AI as the second consumer, requiring
  the same registries and calculation to serve multiple license levels
  with escalation to the treating practitioner at the boundary.
- **Legal-research work item** — a named ongoing process with an owner
  and a cadence, supplying and correcting all jurisdiction and scope
  registry data.
