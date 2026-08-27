## ADDED Requirements

### Requirement: The practitioner is a modelled clinical actor, human or AI
openChart SHALL define a Practitioner record whose identity is independent of species, carrying a holder class drawn from the openXwallet vocabulary (`person`, `practitioner`, `organisation`, `agent`), display identity, specialty or expertise attestation, lifecycle state and audit provenance. The holder class MUST come from that vocabulary rather than a parallel one, and an AI practitioner MUST be representable without a separate record type.

#### Scenario: An AI practitioner is registered
- **WHEN** a practitioner is created with holder class `agent` and a declared specialty attestation
- **THEN** the record is a first-class practitioner addressable by every clinical surface that accepts a human practitioner

#### Scenario: An unrecognised holder class is supplied
- **WHEN** a practitioner is created with a holder class outside the openXwallet vocabulary
- **THEN** validation rejects the record rather than storing a parallel term

### Requirement: Wallet binding is optional and never the subject identifier
A Practitioner MAY bind to an openXwallet holder through an optional credential-binding reference carrying holder identifier, holder class, wallet state (`active`, `suspended`, `revoked`) and binding provenance. The wallet identifier MUST NOT be the practitioner's subject key, MUST NOT be used to resolve or merge practitioner records, and practitioner modelling, ordering and signing SHALL remain operable with no wallet present.

#### Scenario: Wallet-free practitioner operates
- **WHEN** the capability runs with no wallet binding on any practitioner
- **THEN** practitioner records, orders and signatures function under the conventional human gate and no code path requires a wallet identifier

#### Scenario: Wallet identifier is used as a subject key
- **WHEN** a caller supplies a wallet holder identifier where a practitioner identifier is expected
- **THEN** the request is refused and no practitioner is resolved or created from that identifier

### Requirement: A license binds a pinned set of composition hashes
A License Binding SHALL carry the license number, jurisdiction, license level, environment, effective interval, state, and an append-only set of composition hashes the license covers, each hash computed over the declared components `model_version`, `prompt_contract`, `tool_manifest`, `policy_version`, `parameters` and `retrieval_corpus`. A composition change MUST revoke the current binding; a change confined to `retrieval_corpus`, `parameters`, `prompt_contract` or `tool_manifest` is **minor** and SHALL trigger automatic reissue that adds the new hash to the covered set and writes an attestation naming the changed component, the prior hash and the new hash, while a change to `model_version` or `policy_version` is **major** and MUST require re-licensure rather than reissue. The covered set MUST NOT be rewritten or pruned.

#### Scenario: Retrieval corpus is updated
- **WHEN** an AI practitioner's `retrieval_corpus` changes and nothing else does
- **THEN** the binding is automatically reissued, the new hash joins the covered set, an attestation records the change, and the license number is unchanged

#### Scenario: Model version is updated
- **WHEN** an AI practitioner's `model_version` changes
- **THEN** the binding is revoked, no automatic reissue occurs, and clinical authority is refused until a re-licensure binding exists

#### Scenario: Covered set is edited in place
- **WHEN** a caller attempts to remove or overwrite a hash already in a covered set
- **THEN** the operation is rejected and the historical coverage remains reconstructible

### Requirement: Every clinical exercise record carries its composition hash
Every exercise of clinical authority SHALL write an Exercise record carrying the acting practitioner, the act and object classes, the presenting key, the composition hash in force at that moment, the scope-grant reference, the scope-registry and jurisdiction-registry versions evaluated, the computed zone and the timestamp. Verification that the licensed practitioner performed a given act MUST be answerable as a join — the act's composition hash present in the license's covered set at the act's timestamp — without any periodic attestation process.

#### Scenario: Continuity is verified after the fact
- **WHEN** an auditor asks whether the practitioner that performed a recorded act was the licensed one
- **THEN** the answer is computed from the act's composition hash against the license's covered set at that timestamp, with no monitoring record required

#### Scenario: Clinical write without an exercise record
- **WHEN** a clinical write reaches the guarded surface with no exercise record
- **THEN** the write is refused

### Requirement: Scope grants are monotonically narrowing and checked at every clinical act
Authority SHALL travel as scope grants carrying act classes, object classes, authority tier (`attest`, `request`, `act`, `act_unsupervised`), expiry and derivation lineage. A derived grant MUST NOT widen act classes, object classes, tier or expiry beyond its parent. Every clinical act MUST be checked against the acting practitioner's grant at exercise time with proof of possession, and revocation of a parent grant MUST invalidate its derivations.

#### Scenario: Derived grant attempts to widen scope
- **WHEN** a grant is derived with an act class its parent does not carry
- **THEN** derivation is rejected

#### Scenario: Act outside the granted classes
- **WHEN** a practitioner attempts an act whose class its grant does not carry
- **THEN** the exercise is refused and the refusal is recorded

#### Scenario: Parent grant is revoked
- **WHEN** a parent grant is revoked
- **THEN** every grant derived from it stops authorizing acts without requiring individual revocation

### Requirement: A zone calculator places every intended action relative to the license boundary
openChart SHALL compute the zone of each intended action in its own enforcement layer, never reading it from the wallet, returning `green` (well inside), `yellow` (near the boundary from inside), `red` (near the boundary from outside) or `black` (well outside). Enforcement SHALL be a soft block with notification to the practitioner on `yellow`, escalation to the supervising or treating practitioner on `red`, and shutdown of clinical authority on `black`. Distance MUST be measured from the license boundary, and the computed zone MUST prevent the write rather than annotate it.

#### Scenario: Action near the boundary from inside
- **WHEN** an intended action is computed as `yellow`
- **THEN** the action is soft-blocked, the practitioner is notified, and the zone is recorded on the exercise

#### Scenario: Action well outside the boundary
- **WHEN** an intended action is computed as `black`
- **THEN** the practitioner's clinical authority is shut down and the act does not take effect

#### Scenario: Zone is sourced from the wallet
- **WHEN** a credential presents a zone value
- **THEN** the calculator ignores it and computes the zone from the registry

### Requirement: Zones are computed from a versioned scope registry
The zone calculator SHALL read a Scope Registry mapping act and object classes to license boundaries, versioned as a whole, with per-jurisdiction and per-license-level calibration held as registry data rather than compiled rules. One calculator SHALL serve every jurisdiction and license level. Each exercise MUST pin the registry version it was evaluated against so a past action's zone is reproducible as of the time it was taken.

#### Scenario: A jurisdiction boundary is corrected
- **WHEN** a legal correction changes one state's boundary for an act class
- **THEN** a new registry version carries the correction with no change to the enforcement layer

#### Scenario: Past zone is recomputed
- **WHEN** an act recorded under an earlier registry version is re-examined
- **THEN** the pinned registry version reproduces the zone that was computed at the time

#### Scenario: Nurse-level license evaluates the same act
- **WHEN** a nurse-level practitioner and a physician-level practitioner attempt the same act class in the same jurisdiction
- **THEN** the same calculator returns different zones because the license level selects a different boundary in the same registry version

### Requirement: One jurisdiction registry carries disclosure, supervision and boundary calibration
openChart SHALL maintain a single versioned Jurisdiction Registry carrying, per jurisdiction, AI-disclosure obligations, supervision requirements for pre-licensure practice, and license-boundary calibration, consumed by the zone calculator rather than by a separate compliance surface. The registry SHALL be maintained by a named ongoing legal-research work item, and a jurisdiction requiring per-encounter AI disclosure MUST be representable as registry data without changing the general consent rule.

#### Scenario: A state mandates per-encounter disclosure
- **WHEN** the registry records a per-encounter disclosure obligation for a jurisdiction
- **THEN** the zone calculator makes disclosure a condition on acts in that jurisdiction while the one-time consent rule stands elsewhere

#### Scenario: Supervision requirement differs by jurisdiction
- **WHEN** two jurisdictions state different supervision requirements for pre-licensure practice
- **THEN** both are held as rows in the same registry version and applied per the act's jurisdiction

### Requirement: Supervision tiers gate clinical authority by licensure state
A pre-licensure practitioner's grants SHALL cap at authority tier `act`, and an order it produces MUST be staged and take no effect until a human medical director or managing physician records a co-signature. A post-licensure practitioner MAY hold `act_unsupervised`. In QA the same tier SHALL run against synthetic data only under a simulated license requiring no co-signature, and a simulated license MUST NOT authorize any write against non-synthetic data. The flip to production authority MUST require a real license number bound to a named MedxFactory major release and MUST be a recorded act rather than a configuration default.

#### Scenario: Pre-licensure order awaits co-signature
- **WHEN** a pre-licensure AI practitioner issues an order
- **THEN** the order is staged, takes no effect, and becomes effective only when a medical director's or managing physician's co-signature is recorded

#### Scenario: Simulated license reaches real data
- **WHEN** a practitioner holding a simulated QA license attempts a write against non-synthetic data
- **THEN** the write is refused

#### Scenario: Production flip without a real license
- **WHEN** an environment flip to production is attempted with no real license number bound to a MedxFactory major release
- **THEN** the flip is refused and no production clinical authority is granted

### Requirement: One exercise carries N role-qualified signatures
A Co-Signature record SHALL hold exactly one exercise and one or more signatures, each signature qualified by role as `performer`, `supervisor`, `council member` or `dissenting member`, and each carrying signer identity, credential reference where present, and signing time. A clinical act MUST NOT be represented by several competing signature records, and dissent MUST be recorded as a signer role on the same record rather than as a separate object.

#### Scenario: Supervised order is co-signed
- **WHEN** a pre-licensure order is approved by a medical director
- **THEN** one co-signature record carries one `performer` and one `supervisor` signature against the single exercise

#### Scenario: Council decision records dissent
- **WHEN** a council of AI practitioners reaches a decision with one member dissenting
- **THEN** one co-signature record carries the gateway `performer`, the assenting `council member` signatures and the `dissenting member` signature against the same exercise

#### Scenario: Second signature record for the same act
- **WHEN** a caller attempts to create a second co-signature record for an exercise that already has one
- **THEN** the operation is rejected and the additional signature is added to the existing record instead

### Requirement: Consent to AI treatment is one-time and revocable
openChart SHALL record consent to treatment by an AI practitioner as a one-time, revocable record on the patient carrying consenting party, time, scope and state, and MUST NOT require a per-encounter consent prompt unless the jurisdiction registry states a per-encounter disclosure obligation. An AI practitioner MUST NOT exercise clinical authority for a patient with no active consent record.

#### Scenario: Consent is given once
- **WHEN** a patient consents to AI treatment
- **THEN** subsequent encounters proceed without a further consent prompt while the consent remains active

#### Scenario: AI acts without consent
- **WHEN** an AI practitioner attempts a clinical act for a patient with no active consent
- **THEN** the exercise is refused

### Requirement: Consent revocation opens transfer of care with continuity guarantees
Revocation of AI-treatment consent SHALL immediately stop the AI practitioner's authority to initiate new clinical acts and SHALL open a Transfer of Care record, while active orders and the treatment plan remain in force. The transfer MUST complete by a named human practitioner accepting the care, MUST carry a completion state so revocation is never an open-ended limbo, and MUST leave exactly one accountable practitioner of record at every moment.

#### Scenario: Patient revokes mid-course of care
- **WHEN** a patient revokes consent while orders are active and a plan is running
- **THEN** the AI practitioner initiates no new acts, the active orders and plan remain in force, and a transfer of care opens

#### Scenario: Human practitioner accepts the transfer
- **WHEN** a named human practitioner accepts an open transfer of care
- **THEN** the transfer reaches its completion state and the accepting practitioner is the accountable practitioner of record from that time

#### Scenario: Transfer is not yet accepted
- **WHEN** a transfer of care remains unaccepted
- **THEN** it is a visible open state with the prior accountable practitioner still of record, and care is never silently abandoned

### Requirement: Clinical authority requires an accountable credentialed practitioner
The gate on every consequential clinical act SHALL be that an accountable credentialed practitioner exercises it — a practitioner of any holder class with an active credential binding where one is required, a valid license binding covering its current composition, a scope grant carrying the act, a non-blocking zone, and the co-signature its supervision tier demands. Humanity SHALL be one way to qualify, not the predicate. A service-account or unattributed identity MUST NOT satisfy this gate, and an AI practitioner with no valid license binding MUST hold no clinical authority.

#### Scenario: Credentialed AI practitioner acts within scope
- **WHEN** a licensed AI practitioner performs an act inside its granted scope in a `green` zone with consent active
- **THEN** the act is authorized, and the exercise records the practitioner, composition hash, grant, registry versions and zone

#### Scenario: Service account attempts a clinical write
- **WHEN** a service-account identity with no practitioner record attempts a consequential clinical write
- **THEN** the write is refused

#### Scenario: AI practitioner without a license binding
- **WHEN** an AI practitioner with no valid license binding attempts a clinical act
- **THEN** the act is refused regardless of its scope grant or zone
