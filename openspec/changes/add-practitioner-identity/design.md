## Context

openChart today models patients, not practitioners. The one promoted capability
(`expanded-patient-intake`) persists patient-reported statements behind the
single guarded write surface `open_chart.api.v1`, whose controller guards in
`open_chart/intake/guarded.py` reject any write that does not carry the API
flag, and whose endpoints refuse a call without subject, tenant, purpose and
role context. That architecture is the hook this change extends: the place where
a write is already refused for missing context is the place where it must also
be refused for missing authority.

The credential half is not being invented. openXwallet is a ratified contract
family in openxFactory (contract-v1.31, 2026-08-07) — schemas, canonical
validator, CI, and one live holder, a council with holder class `agent`. There
is no runtime and no issuance service. Its doctrines are inherited, not
re-argued: identity is composition (a sha256 over `model_version`,
`prompt_contract`, `tool_manifest`, `policy_version`, `parameters`,
`retrieval_corpus`), authority travels as monotonically narrowing grants checked
at exercise with proof of possession, a wallet identifier is never a subject
identifier, and every domain must remain operable with no wallet at all.

What openXwallet's neutral core cannot express is the clinical case: no
expertise attestation, no license field, and closed schemas that refuse
additional properties. The sanctioned route is therefore a **practitioner
profile family** over that core, authored by openChart as the domain that needs
it first and contributed as contracts in openxFactory. The owner of both
repositories confirmed the extension path on 2026-08-26; the contracts
themselves are unauthored, which this design treats as coordinated dependent
work rather than a blocker.

Six design questions were dispositioned `accepted` in the same ruling. They are
settled inputs here, recorded as Decisions 3 through 8, not reopened.

## Goals / Non-Goals

**Goals:**

- Model the practitioner as a first-class clinical actor, human or AI, whose
  authority comes from a credential rather than from species.
- Bind an openXwallet credential optionally and non-identifyingly, keeping the
  domain fully operable wallet-free.
- Make licensed-identity continuity provable retrospectively from the evidence,
  not from a monitoring process.
- Compute distance-to-boundary in openChart from versioned registry data, so a
  jurisdiction correction is a data change and an old zone is reproducible.
- Express supervision and composite (council) practice with one record shape.
- Refuse production clinical authority until a real license number is bound to a
  MedxFactory major release.

**Non-Goals:**

- A credential issuance or wallet runtime service — openXwallet has none, and
  this change does not build one.
- Third-party (court or state board) verification, deferred until openXwallet
  becomes its own repo-level project.
- Any real license number, any production authority flip, or any grant of
  autonomous clinical action in this change.
- Rewriting `expanded-patient-intake` requirements, or deleting any catalog
  governance machinery — the restatement is a restatement.

## Decisions

### 1. openChart owns the practitioner; openxFactory owns the contracts

The split is deliberate and follows the inherited doctrine that a wallet
identifier is never a subject identifier.

Living in openChart: the practitioner record (with a holder class from
openXwallet's vocabulary — person, practitioner, organisation, agent), the
license binding and its pinned composition-hash set, scope-grant and exercise
records, the co-signature record's instances, the AI-treatment consent and
transfer-of-care records, the zone calculator, and both registries. Living in
openxFactory: the four profile-family contracts — specialty/expertise
attestation, state-license-number binding, zone model declaration, co-signature
record kind — layered over the neutral core.

Alternative considered and rejected: forking openXwallet's schemas locally to
add the missing fields. It is faster and it forfeits the ratified validator, CI
and the council-wallet precedent, and it makes every downstream consumer
(MedxFactory, HealthLinc) reconcile two vocabularies. The profile family is the
sanctioned path, and the cost of coordinating it is the price of one vocabulary.

Consequence for sequencing: contract authoring is an early coordinated task, and
openChart's own records are designed to the contract shape but do not wait on
ratification to exist — a practitioner without a wallet binding is a valid,
fully operable practitioner.

### 2. Wallet binding is optional, and the wallet is never the subject key

The practitioner record carries its own openChart identifier. A wallet holder
reference is an optional attribute that strengthens authority; it does not
constitute the practitioner. Every enforcement path must therefore have a
defined answer for an unbound practitioner: a human practitioner with no wallet
signs under the conventional human gate, and an AI practitioner with no valid
binding holds no clinical authority at all. Wallet-free operation is a test
obligation, not a documented aspiration — the same discipline the intake
foundation applied to standalone operation without MedxFactory.

### 3. The major/minor composition line (Q1, accepted)

`model_version` and `policy_version` are **license-relevant and therefore
major**: a change to either revokes and requires re-licensure. `retrieval_corpus`,
`parameters`, `prompt_contract` and `tool_manifest` are **minor**: the strict
any-composition-change-revokes rule still fires, but reissue is automatic and
fast, the license persists, and the wallet re-attests with an attestation record
naming the changed component and the new hash.

The line follows what a state board would recognise as a different practitioner.
`model_version` changes the reasoning substrate and `policy_version` the rules
practiced under; the other four are closer to a physician's reading, tooling and
dictation habits — constantly changing, material to competence, not
re-licensable events. `parameters` is the least comfortable call, since sampling
settings can change clinical behaviour; the mandatory attestation on every minor
reissue keeps that auditable rather than silent, and Decision 5's join makes it
provable afterwards.

### 4. Zones are computed in openChart from a versioned scope registry (Q2, accepted)

The wallet supplies `scope.acts` and `scope.objects`. A **zone calculator** in
openChart's enforcement layer places each intended action at a distance from the
*license* boundary and returns one of four zones:

- **green** — well inside; proceed.
- **yellow** — near the boundary from the inside; soft block with notification
  to the practitioner.
- **red** — near the boundary from the outside; escalation to the supervising or
  treating practitioner.
- **black** — well outside; shutdown of the practitioner's clinical authority.

The calculator reads a **versioned scope registry** mapping act and object
classes to license boundaries, with per-jurisdiction calibration held as
registry data rather than code. One calculator, many registry versions; a
jurisdiction is a row set, and a license level selects a boundary within it —
which is what lets HealthLinc's nurse-level AI use the same calculator at a
different boundary.

Alternative considered and rejected: compiling boundaries into the enforcement
layer. That makes every state a code change and every legal correction a deploy,
guaranteeing drift from the law, and it puts the artifact out of reach of the
people qualified to review it. Versioning is not optional: an action's zone must
be reproducible as of the time it was taken when the record is examined years
later, so the exercise record pins the registry version it was evaluated
against.

### 5. Continuity is evidence, not monitoring (Q3, accepted)

**Every clinical exercise record carries the composition hash**, and the license
record **pins the set of hashes** the license covers. Verifying that the AI we
licensed is the AI that performed a given act is then a **join**: was this act's
hash in this license's covered set at this timestamp?

This makes continuity a property of the evidence rather than of a monitoring
process, which matters because monitoring has gaps and evidence does not.
openXwallet already records the presenting key at exercise, so carrying the
composition hash alongside extends an existing record rather than adding one.
The covered set is held append-only, so a minor reissue adds a hash without
rewriting history and the license's coverage over time is itself reconstructible
— the shape a transparency log would want, and the cheapest artifact to hand a
third party once verification stops being deferred. The cost is record size on
every clinical act, which is the right place to spend it.

### 6. Consent revocation opens transfer of care (Q4, accepted)

Consent to AI treatment is a **one-time, revocable record on the patient**, not
a per-encounter prompt. Revocation **opens a transfer-of-care workflow with
continuity guarantees**: the AI practitioner's authority to initiate new
clinical acts stops immediately, active orders and the treatment plan remain in
force, and a named human practitioner accepts the care, which closes the
transfer.

The failure mode designed against is a revocation that leaves a patient with an
active plan and no practitioner of record — clinically worse than the thing
revoked, and indefensible. Modelling revocation as a transfer rather than a
termination also gives it a completion state, so "consent revoked" is not a
limbo the chart sits in, and it keeps the accountability question answerable:
there is always exactly one accountable practitioner, and the transfer record
says when it changed.

### 7. One exercise, N role-qualified signatures (Q5, accepted)

The co-signature record holds **one exercise and N signatures**, each signature
**role-qualified** as performer, supervisor, council member or dissenting
member.

One record with N signatures keeps the clinical act singular, which is what the
chart, the order and any later legal reconstruction all need; N records
referring to one act invites divergence about which is authoritative. Role
qualification lets one structure serve both supervision and composite practice
without a second design: a pre-licensure order is one performer plus one
supervisor, and a council decision is one gateway performer plus N members, some
recorded as dissenting. Dissent as a signer role rather than a separate object
matches the conference record that already carries dissent.

### 8. One jurisdiction registry, fed by ongoing legal research (Q6, accepted)

A single **jurisdiction registry** carries disclosure obligations, supervision
requirements and license-boundary calibration per state, and the zone calculator
consumes it. It is fed by a **named legal-research work item run as an ongoing
process**, not a one-time survey.

These are the same jurisdictions with the same versioning problem as Decision 4,
and one registry rather than three keeps a state's rules consistent with
themselves. Routing disclosure through the zone calculator puts the check where
the action is already evaluated, so a per-encounter disclosure requirement
becomes a condition on the act rather than a separate compliance surface someone
must remember to consult. The registry deliberately does not assume the
one-time-consent rule survives everywhere: a state that mandates per-encounter
disclosure regardless of obviousness is represented as registry data without
reopening the general rule.

### 9. Enforcement extends the guarded API surface, it does not sit beside it

`open_chart.api.v1` is the one supported write surface, and
`open_chart/intake/guarded.py` already makes every other write path fail loudly.
Exercise-time authority checks join the context check that runs there today:
before a clinical write touches data, the surface resolves the acting
practitioner, validates the credential binding if one is present, checks the
narrowing scope grant with proof of possession, calls the zone calculator, and
records the exercise — composition hash, registry version, zone, and grant
reference — as part of the same guarded write. A guarded controller refuses a
clinical write that carries no exercise record for the same reason it refuses a
write with no API flag.

Two properties are preserved deliberately. Decisions stay in pure functions the
bench-free validator can exercise (the pattern `open_chart/intake/core.py`
established), so zone computation and grant evaluation are testable without a
Frappe site. And the guard is a refusal, not an advisory: a red or black zone
does not annotate the write, it prevents it.

### 10. QA and production are different authority environments

QA runs the `act_unsupervised` tier against **synthetic data only**, with the
practice license **simulated** — no co-signature required, because there is no
patient and no real authority. Production requires a **real license number**
bound to the MedxFactory **major release**, and the environment flip is an
explicit, recorded act rather than a configuration default. A simulated license
must be structurally incapable of authorizing a write against non-synthetic
data, and the pre-licensure tier caps grants at `act` so that an order is staged
and inert until a human medical director or managing physician co-signs.

## Risks / Trade-offs

- **[The profile-family contracts never land, and openChart's records drift from
  a shape openxFactory will not ratify]** → Author the contracts as the first
  coordinated task, design openChart's records to that shape, and keep every
  path operable wallet-free so an unratified contract degrades authority
  strength rather than blocking the capability.
- **[The repository holds two contradictory positions on the human gate until
  the restatement lands]** → The restatement is a named documentation task in
  this change with an explicit entry list, and the inconsistency is stated in
  the proposal rather than hidden. MedxFactory's own restatement is outside this
  repository and is flagged, not assumed.
- **[A registry-driven zone calculator becomes a legal-advice engine]** → The
  registry encodes boundaries and obligations as reviewable data authored by a
  legal-research work item; the calculator computes distance and returns a zone,
  and never infers a boundary that the registry does not state.
- **[Composition hash on every clinical act inflates every record]** → Accepted
  deliberately; it is the cost of continuity being evidence rather than
  monitoring. Storage is bounded by a fixed-width hash plus a registry-version
  reference per act.
- **[`parameters` classified minor lets clinical behaviour change without
  re-licensure]** → Every minor reissue writes an attestation naming the changed
  component and the new hash, and the join in Decision 5 makes the change
  provable against any act performed after it.
- **[A simulated QA license leaks into production authority]** → The license
  record carries its environment, a simulated license cannot authorize a write
  against non-synthetic data, and the production flip is a recorded act
  requiring a real license number tied to a named MedxFactory major release.
- **[Transfer of care stalls and the patient is left without an accountable
  practitioner]** → Revocation opens a transfer with a completion state and a
  named accepting practitioner; active orders and the plan remain in force
  throughout, and an unaccepted transfer is a visible open state, never silent.

## Migration Plan

1. Author the four practitioner profile-family contracts against openXwallet's
   neutral core and open them for openxFactory ratification.
2. Seed the versioned scope registry and the jurisdiction registry with their
   first version and a first jurisdiction, from the legal-research work item.
3. Add the practitioner, credential-binding, license, scope-grant, exercise,
   co-signature, consent and transfer-of-care records with migrations,
   permissions, audit behavior and synthetic fixtures.
4. Add the zone calculator and grant evaluation as pure functions, then wire
   exercise-time enforcement into `open_chart.api.v1` and the controller guards.
5. Run the capability under the pre-licensure tier in QA against synthetic data
   with a simulated license, and publish the wallet-free operation evidence.
6. Restate the human-gate predicate across the named catalog assumptions.

Rollback removes exercise-time enforcement and the practitioner records from
disposable sites; because no real license number and no production authority
exist in this change, rollback forfeits no granted authority. Nothing in this
plan flips an environment to production.

## Open Questions

- Is the companion's own witness credential a **reduced practitioner profile**
  (same family, scope narrowed to `attest`, no license binding) or a **distinct
  witness profile** that never touches the practitioner family? The reduced
  reading inherits zone machinery and revocation for free but invites the
  reading that the companion is a junior practitioner, which the
  reasoning-evidence rule denies.
- What is the escalation contract between HealthLinc's nurse-level AI and the
  treating practitioner in openChart — where advice crosses into practice, and
  which zone transition represents it?
- Which jurisdiction seeds the first registry version, and what cadence does the
  legal-research work item run at once seeded?
- Does the composite (council) practitioner hold one license over the collective
  with a gateway performer, or a license per member rolled up at the gateway?
  The co-signature record supports both; the license binding does not yet
  distinguish them.
