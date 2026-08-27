# Staged: Practitioner identity — the accountable credentialed practitioner, held in openXwallet

Status: staged
Kind: capability-proposal
Summary: openChart's catalog encodes `human` as the predicate wherever clinical
authority is exercised, and the clinical-companion vision needs *accountable
credentialed practitioner* instead, with humanity as one way to qualify. This
topic makes practitioner identity a first-class capability: a practitioner —
human or AI — holds an openXwallet-validated credential binding a state license
number to a declared composition, carrying narrowing scope grants checked at
every exercise. openChart drives a new practitioner profile family over
openXwallet's neutral core (specialty attestation, license binding, co-signature,
zones) and computes green/yellow/red/black distance-to-boundary in its own
enforcement layer, keeping the wallet an authority control, not an identity
substrate.
Topics: openchart-clinical-companion, practitioner-identity, openxwallet,
ai-practitioner, credentialing, scope-of-practice, supervision, co-signature
Repository context: openChart — Frappe v15 native EMR; openChart drives the new
openXwallet practitioner profile family whose neutral core contracts live in
openxFactory; MedxFactory and HealthLinc are downstream consumers
Staging ID: openChart:staging:practitioner-identity-openxwallet
Captured: 2026-08-26
Source: owner discussion 2026-08-25/26 recorded in the clinical-companion
phase-decisions document, closing Issue 7 of the clinical-companion feature
review — see [phase decisions](../../brainstorm/openchart-clinical-companion-phase-decisions.md)
and [feature review](../../brainstorm/openchart-clinical-companion-feature-review.md)
Target capabilities: ADDED `practitioner-identity` (AI and human practitioner
identity, openXwallet-validated authority, scope zones, supervision)

## Last proposal attempt (round-trip provenance)

Change ID: none yet
Raised: n/a
Status at demote: n/a
Demoted: n/a
Demote reason: n/a

## Claims

Settled by the owner's 2026-08-25/26 rulings and the openXwallet review recorded
with them. The open questions below iterate against these and do not reopen them.

1. **openXwallet is adopted, not reinvented** — a ratified contract family in
   openxFactory (contract-v1.31, 2026-08-07): schemas, canonical validator, CI,
   one live holder (a council with holder_class `agent`, the council-wallet
   precedent), no runtime or issuance service yet. openChart takes the vocabulary
   as given: holder classes person/practitioner/organisation/agent, authority
   tiers attest/request/act/act_unsupervised, states active/suspended/revoked.
2. **Identity is composition** — a sha256 over declared components
   (model_version, prompt_contract, tool_manifest, policy_version, parameters,
   retrieval_corpus). Authority travels as monotonically narrowing grants
   (scope.acts, scope.objects, expiry, revocation through derivation), checked at
   exercise, proof of possession required.
3. **openChart drives the practitioner profile family.** The neutral core stays
   in openxFactory; openChart authors the extension — specialty/expertise
   attestation, state-license-number binding, the zone model, a co-signature
   record kind. The sanctioned extension path, not a fork.
4. **License-vs-release posture is strict composition-revoke plus fast minor
   reissue.** The any-composition-change-revokes rule is kept intact; *minor*
   changes get fast automatic re-issuance — license persists, wallet re-attests.
   Chosen as maximally defensible to a state board.
5. **Supervision tiers map onto the wallet's own tiers.** Pre-licensure grants
   cap at `act`: a human medical director or managing physician approves before
   an order takes effect, recorded through the profile family's **co-signature
   record kind** rather than an ephemeral workflow state. Post-licensure is
   `act_unsupervised`; QA runs the same tier against synthetic data only,
   pretending to hold the full practice license. The production flip enters a
   real license number for the AI, tied to a MedxFactory serial/release — the
   major release.
6. **Zones live in openChart's enforcement layer, not the wallet.** The wallet
   carries scope; openChart computes distance-to-boundary per intended action —
   **green** well inside, **yellow** near the boundary from inside, **red** near
   it from outside, **black** well outside (shutdown). Enforcement is a soft
   block with notification on entering the grey zone. Zones measure distance from
   the *license* boundary: leaving the AI's *expertise* should be hard or
   impossible, and the state license is the binding edge.
7. **Patient consent to AI treatment is one-time and revocable**, not
   per-encounter — for at least the first year it will be obvious to the patient
   that the practitioner is an AI, so per-visit notification adds nothing.
8. **The composite practitioner is planned for from the start.** MedxFactory as
   a council of AIs — or a gateway AI in front of that council — is itself the
   state-licensed practitioner, so the profile family must express one credential
   over a collective. The council-wallet precedent already exists (Claim 1).
9. **A wallet identifier is never a subject identifier.** The AI physician keeps
   its own practitioner identity in openChart; the wallet is an authority
   control. Inherited doctrine, not a local choice.
10. **The domain must operate with no wallet at all.** Practitioner modelling,
    ordering, and signing must function wallet-free; wallet validation
    strengthens authority, it does not constitute the practitioner.
11. **The gate predicate is restated from `human` to `accountable credentialed
    practitioner`** — the aic-036 reframing, humanity being one way to qualify.
    Not a demolition: the catalog's governance machinery transfers almost intact.
12. **Voice-CPOE inherits the credential.** An AI practitioner's verbal order
    call-out carries intent under its credential; a human confirms by signature.
    The modality is equal; the authority source is not.
13. **Third-party verification is deferred.** Court and state-board verification
    of a credential waits for openXwallet to become its own repo-level project.
14. **HealthLinc's nurse-level AI is the second consumer.** Profile family, zones,
    and supervision tiers must support multiple license levels, with escalation
    to the treating practitioner as the boundary crossing.

## Why

<!-- xspec:candidate target=practitioner-identity -->
Zero of openChart's 1,115 catalogued features mention openXwallet or any
AI-practitioner concept, and roughly 575 carry the boilerplate boundary that the
feature "does not own … autonomous clinical action". aic-036 states the position
sharply — the AI service role has zero submit permission on clinical DocTypes,
and a service-account identity cannot satisfy a human gate. Every signature,
credential, and delegation feature assumes a human underneath it (plt-004,
plt-005, doc-023/027, ord-030–034, phr-011/013).

The vision needs a different predicate. An ungoverned AI acting autonomously is
exactly what aic-036 rightly forbids; a practitioner holding a validated,
scoped, revocable credential and acting inside a verified boundary is a
different object, and the catalog has no name for it. What makes that second
object defensible is already built: aic-033 is a credential registry,
aic-043/044 a scope-of-practice dossier, aic-022/023 competency examination and
recertification, aic-028 license suspension, aic-026/027/050 ongoing practice
monitoring, aic-025 privileging, plt-005/043/044 the authority triad. None of it
is discarded. What has no home is the practitioner itself — an identity that can
hold a state license, present a credential, be scoped, supervised, revoked, and
attributed liability when it errs. The credential half does not need inventing
either: openXwallet's neutral core exists, but has no expertise attestation, no
license field, and closed schemas — precisely why the sanctioned move is a
profile family over that core, driven by the domain that needs it first.
<!-- /xspec:candidate -->

## What changes

<!-- xspec:candidate target=practitioner-identity -->
A new `practitioner-identity` capability makes the practitioner a modelled
clinical actor, human or AI, with authority sourced from a credential rather
than from species. The provider master gains a holder class — person,
practitioner, organisation, agent — drawn from openXwallet's vocabulary rather
than a parallel one, and a practitioner record may bind to a wallet holder
without being defined by it: the wallet identifier stays an authority reference,
never the subject key, and the model remains operable with no wallet present.

openChart authors a **practitioner profile family** over openXwallet's neutral
core, contributed as contracts in openxFactory. Four additions: a
specialty/expertise attestation, a state-license-number binding, a zone model
declaration, and a co-signature record kind carrying one exercise and N
role-qualified signatures. The license binding pins the composition hash set the
license was granted against; any composition change revokes per the existing
rule, and *minor* changes trigger fast automatic reissuance so the license
persists while the wallet re-attests.

Authority is exercised through **scope grants checked at every clinical act**.
Pre-licensure practitioners hold grants capped at `act`, which stages an order
but requires a medical director's or managing physician's co-signature before it
takes effect — recorded, not transient. Post-licensure practitioners hold
`act_unsupervised`; QA runs the same tier against synthetic data only with the
practice license simulated, and the production flip demands a real license
number tied to the MedxFactory major release.

**Zones are computed in openChart, not carried by the wallet.** The wallet
supplies scope.acts and scope.objects; a zone calculator places each intended
action at a distance from the license boundary and returns green, yellow, red,
or black — notification on yellow, escalation on red, shutdown on black —
reading a versioned scope registry rather than compiled rules, so
per-jurisdiction calibration is data.

Consent rides along: consent to AI treatment becomes a one-time revocable record
on the patient rather than a per-encounter prompt, and revocation opens a
transfer-of-care workflow rather than terminating care. Finally, the human-gate
predicate is restated across the affected catalog assumptions — the largest and
least mechanical part of the work, and the one this topic must not pretend is
small.
<!-- /xspec:candidate -->

## Impact

<!-- xspec:candidate target=practitioner-identity -->
- Affected specs: `practitioner-identity` (ADDED — practitioner as a modelled
  clinical actor; credential binding and validation; scope grants and
  exercise-time checks; the zone calculator; supervision tiers and the
  co-signature record; consent to AI treatment).
- Affected catalog assumptions, all requiring restatement rather than deletion:
  aic-036 (the human-gate predicate, the load-bearing one), aic-034 (PHI boundary
  controls treat every inference as egress to an outside party; an AI
  practitioner on the care team accesses PHI under treatment purpose), aic-042
  (blanket "cannot diagnose, order, treat", written actor-independently, so it
  forbids the credentialed case along with the ungoverned one), plt-004 (provider
  master, no non-human provider type), plt-005 (human licenses only),
  plt-043/044 (e-signature authority and delegation registries), phr-011/013
  (credential-bound signing ceremony), ord-030–034 (order signature gates),
  doc-023/027 (documentation signature gates).
- Affected repos: **openChart** — consumer of openXwallet, driver of the profile
  family, owner of the zone calculator and enforcement layer; **openxFactory** —
  host of the neutral core and of the profile-family contracts, and the party
  that must confirm the extension path; **MedxFactory** — the licensed AI
  practitioner itself, whose major release the license binds to and whose wallet
  brainstorms need the same predicate restatement; **HealthLinc** — the
  nurse-level AI as a second consumer at a different license level.
- Blast radius honestly stated: the restatement touches roughly 575 catalog
  entries carrying the autonomous-clinical-action boundary. Most are boilerplate;
  the load-bearing minority is named above.
- Staging this topic changes no authority, grants no credential, licenses nothing.
<!-- /xspec:candidate -->

## Idea notes (pre-document, non-documented)

- The companion signs its own witness record (Issue 2's dual attestation), and it
  is not obvious whether that credential is a *reduced practitioner profile* —
  same family, scope narrowed to `attest`, no license binding — or a *distinct
  witness profile* that never touches the practitioner family. The reduced
  reading gets zone machinery and revocation for free but invites the reading
  that the companion is a junior practitioner, which the reasoning-evidence rule
  (the companion makes no decisions) denies. — Added-by: Claude Fable 5 ·
  2026-08-26
- Strict-revoke plus fast reissue is shaped like a transparency log. If the
  license record held an append-only *set* of composition hashes rather than a
  pointer to one, continuity would become a publicly verifiable artifact — a
  board or a court could check "was this composition licensed at the time of this
  act?" with no issuance service existing yet. Possibly a cheaper answer to Q3
  than a live verification service, and it costs nothing to keep the record in
  that shape now. — Added-by: Claude Fable 5 · 2026-08-26

## Conflicts

- **aic-036 and the ~575-entry human-gate boilerplate are unreconciled today.**
  The catalog states, as promoted policy, that no AI service role receives submit
  authority on consequential clinical DocTypes and that a service-account
  identity cannot satisfy a human gate. Claim 11 contradicts that text directly.
  The restatement is decided in principle and not written, so the repository
  presently holds both positions. — Added-by: Claude Fable 5 · 2026-08-26
- **MedxFactory's wallet brainstorms forbid agent-owned order signing.** The same
  human-gate predicate needing restatement in the openChart catalog is asserted
  there too, and the owner carried the flag forward without restating it. A
  change raised from this topic leaves openChart's position and MedxFactory's
  recorded position inconsistent until MedxFactory's is amended. — Added-by:
  Claude Fable 5 · 2026-08-26
- **openXwallet as it stands cannot express this credential.** No expertise
  attestation, no license field, and closed schemas — additional properties are
  refused, which is what makes a profile family the sanctioned route rather than
  a convenience. That family does not exist yet, so every claim depending on it
  depends on unagreed work in another repo. — Added-by: Claude Fable 5 ·
  2026-08-26

## Open questions

### Q1. Which composition components are license-relevant, and where does the major/minor line sit?

Context: any change to any of the six declared components revokes. Claim 4 keeps
that rule and softens it with automatic reissue for *minor* changes, which only
works once "minor" is defined. The owner named the hard case: does a
retrieval_corpus update — new medical literature — touch the license at all? A
practitioner reading this month's journals is not a different practitioner.
Recommended answer: **model_version and policy_version are license-relevant and
therefore major**; retrieval_corpus, parameters, prompt_contract, and
tool_manifest are **minor** — fast automatic reissue with an attestation
recording the change, license unbroken.
Explanation: the line follows what a state board would recognise as a different
practitioner — model_version changes the reasoning substrate, policy_version the
rules it practices under. The other four are closer to a physician's reading,
tooling, and dictation habits: constantly changing, material to competence, not
re-licensable events. Parameters is the least comfortable call, since sampling
settings can change clinical behaviour; the attestation on every minor reissue
keeps that auditable rather than silent, and Q3's join makes it provable after.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q2. What metric places an intended action in green/yellow/red/black, and who calibrates it per jurisdiction?

Context: Claim 6 requires distance-to-boundary to be computable, which the owner
named as a design problem rather than a detail. Scope arrives from the wallet as
act and object classes; license boundaries are legal text differing by state and
by license level, and HealthLinc's nurse-level AI needs the same calculator at a
different boundary.
Recommended answer: zones are computed from a **versioned scope registry**
mapping act and object classes to license boundaries, with per-jurisdiction
calibration held as **registry data, not code**. One calculator, many registry
versions; a jurisdiction is a row set, a license level selects a boundary in it.
Explanation: encoding boundaries in the enforcement layer makes every state a
code change and every legal correction a deploy, guaranteeing drift from the law.
Data-shaped calibration also makes the artifact reviewable by the people
qualified to review it — a legal researcher can correct a registry version
without reading the enforcement layer. Versioning is not optional: an action's
zone must be reproducible as of the time it was taken when the record is examined
years later. It also makes Q6's per-state matrix an input, not a parallel
structure.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q3. How do we prove the AI we licensed is the AI currently practicing?

Context: the owner's licensed-identity-continuity question. Composition
revocation catches changes prospectively, but the evidentiary question is
retrospective: a board or a court asks, about one clinical act on one date,
whether the practitioner that performed it was the licensed one. Periodic
attestation cannot answer that for the gaps between attestations.
Recommended answer: **every clinical action's exercise record carries the
composition hash**, and the license record **pins the hash set** the license
covers. Verification is then a **join** — is this act's hash in this license's
set at this timestamp — continuous by construction rather than periodic.
Explanation: this makes continuity a property of the evidence rather than of a
monitoring process, which matters because monitoring has gaps and evidence does
not. openXwallet already records the presenting key at exercise, so carrying the
composition hash alongside extends an existing record rather than adding one. The
join is also the cheapest thing to hand a third party once verification stops
being deferred (Claim 13), and what the transparency-log idea note would build
on. The cost is record size on every clinical act — the right place to spend it.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q4. What does revocation of AI-treatment consent trigger operationally?

Context: Claim 7 makes consent one-time and revocable, and the owner attached
the rider that revocation must be defined operationally — handoff to a human
practitioner mid-course of care. A patient may revoke between encounters, during
one, or with orders active and a plan running.
Recommended answer: revocation **opens a transfer-of-care workflow with
continuity guarantees** — the AI practitioner's authority to initiate new
clinical acts stops, active orders and the plan remain in force, and a named
human practitioner accepts the care. Never an immediate abandonment.
Explanation: the failure mode to design against is a revocation leaving a patient
with an active treatment plan and no practitioner of record — clinically worse
than the thing revoked, and indefensible. Modelling revocation as a transfer
rather than a termination also gives it a completion state, so "consent revoked"
is not a limbo the chart sits in. It reuses machinery the vision already needs
for mid-encounter handoff, and keeps accountability answerable: there is always
exactly one accountable practitioner, and the transfer record says when it
changed.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q5. What shape does the co-signature record take?

Context: Claim 5's pre-licensure tier requires a human medical director's signoff
before an order takes effect, and Claim 8's composite practitioner raises the
same question from the other side — whether a gateway signs alone or council
members co-sign, and whether internal dissent is record content. Both need one
exercise to carry more than one signature.
Recommended answer: a **new record kind in the practitioner profile family**,
holding **one exercise and N signatures**, each signature **role-qualified** —
performer, supervisor, council member, dissenting member.
Explanation: one record with N signatures keeps the clinical act singular, which
is what the chart, the order, and any later legal reconstruction all need; N
records referring to one act invites divergence about which is authoritative.
Role qualification lets one structure serve supervision and composite practice
without a second design: a pre-licensure order is one performer plus one
supervisor, a council decision one gateway performer plus N members, some
recorded as dissenting. Dissent as a signer role rather than a separate object
also matches the conference record that already carries dissent (car-054).
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

### Q6. How is the per-state legal matrix for AI disclosure and supervision represented?

Context: the owner attached a legal-research check that no target state mandates
per-encounter AI disclosure regardless of obviousness — which, if any state
does, contradicts Claim 7 there. Supervision requirements for pre-licensure
practice vary the same way, and the P4 privilege matrix is a third axis over the
same jurisdictions.
Recommended answer: a **jurisdiction registry consumed by the zone calculator**,
carrying disclosure obligations, supervision requirements, and license-boundary
calibration per state, fed by a **named legal-research work item** as an ongoing
process — not a one-time survey.
Explanation: these are the same jurisdictions with the same versioning problem as
Q2, and one registry rather than three keeps a state's rules consistent with
themselves. Routing disclosure through the zone calculator puts the check where
the action is already evaluated: a per-encounter disclosure requirement becomes a
condition on the act, not a separate compliance surface someone must remember to
consult. The recommendation deliberately does not assume Claim 7 survives
everywhere — the registry is where a state that mandates per-encounter disclosure
is represented without reopening the general rule.
Disposition status: accepted — owner ruling 2026-08-26 (disposition round 1, recommendation stands)
Added-by: Claude Fable 5 · 2026-08-26

## Exit

The proposal gate is crossed when every open question above carries a disposition
other than `open`, and when the openxFactory side confirms that a practitioner
profile family over the neutral openXwallet core is the accepted extension path —
Conflict 3 is a dependency on another repository's agreement, not something this
topic can resolve alone. The change raised from this fragment carries the
`practitioner-identity` capability together with the restatement plan for the
catalog assumptions named in Impact.

Gate status 2026-08-26: all six questions dispositioned `accepted` (disposition
round 1); the extension path is confirmed by the owner of both repositories
(Issue 7 ruling, phase-decisions record) — the profile-family contracts remain
unauthored in openxFactory, which the raised change must treat as dependent
work, not as a blocker to proposing.
