# Agent Warranty Protocol — GenLayer Single-Repository Intelligent Contract Master Prompt

> **Updated benchmark edition:** incorporates lessons from the accepted/high-scoring AuditLot design: evidence-class-specific verification, exact artifact pinning where appropriate, substantive independent validators, narrow security claims, live payable-behavior testing, and a full Studionet acceptance matrix.

## Project-specific operating prompt built on the supplied GenLayer single-repository template

> **Purpose:** Build **Agent Warranty Protocol** as one standalone, reusable GenLayer Intelligent Contract primitive.
>
> **Only required input:** replace `<REPO_URL>` below.
>
> **Important:** The project-specific rules in this section **override any conflicting generic instruction later in this document**. In particular:
>
> - the primitive is already selected — **do not replace it during idea scouting**;
> - this is **not a frontend/product build**;
> - the coding agent performs the **canonical Studionet deployment itself** after all local gates are green;
> - the coding agent must **continue end-to-end without stopping at the deployment gate**: deploy, verify source parity, execute live tests, document transaction evidence, perform the steward audit, and freeze only when all applicable gates are green;
> - **evidence integrity appropriate to each evidence class**, escrow, cure, delegation, and substantive consensus are **submission-critical**, not optional decoration;
- do **not** force every web-backed obligation through browser rendering: immutable byte-pinned text/JSON may use independently fetched exact-byte verification, dynamic/rendered state must use a real render path, and visual claims must use an actual image/screenshot path;
- use **AuditLot-level rigor as the quality benchmark**: narrow claims, immutable commitments, independently reproduced validator work, deterministic protocol mechanics, adversarial Direct Mode tests, and a live Studionet acceptance matrix.

---

# PROJECT-SPECIFIC MASTER INPUT

```text
REPOSITORY: <REPO_URL>
PRIMITIVE: Agent Warranty Protocol
NETWORK: GenLayer Studionet
SUBMISSION CATEGORY: Standalone Intelligent Contract
CANONICAL DEPLOYMENT: CODING AGENT DEPLOYS AND VERIFIES END-TO-END
```

The contract must be production-scale and fully auditable. It may naturally exceed 1,000 lines if the architecture requires it, but never pad code simply to hit a line count.

The final contract must avoid schema-loading failures. Verify the actual schema repeatedly during development instead of assuming normal Python syntax is sufficient.

Consult the **current** official GenLayer docs and `skills.genlayer.com` before relying on exact SDK, GenVM, consensus, web-render, multimodal, payable, or transfer APIs. Runtime behavior wins over memory or old examples.

---

# A. FIXED THESIS

Agent Warranty Protocol is:

> **A reusable GenLayer primitive for enforceable performance guarantees between autonomous agents, combining dependency-aware obligations, evidence-class-specific independent verification, cure rights, delegated liability, portable warranty receipts, and deterministic escrow settlement.**

It is **not**:

- an agent marketplace;
- a frontend app;
- a generic task manager;
- simple milestone escrow;
- a thin LLM wrapper;
- a generic "AI decides who wins" contract;
- a reputation system;
- a chatbot;
- a one-off dispute demo.

The load-bearing trust question is:

> Given an immutable warranty specification, a dependency-aware set of obligations, and independently observable evidence, which obligations were fulfilled, partially fulfilled, failed, blocked, or left inconclusive — and what deterministic contract state and escrow consequence follows?

Without GenLayer, one requester, provider, operator, API, or model would become the authority that reads/interprets evidence and authors the verdict that can move money.

With GenLayer, multiple validators must independently observe and interpret decision-critical evidence before deterministic contract logic is allowed to settle.

---

# A2. QUALITY BENCHMARK — AUDITLOT-LEVEL RIGOR, NOT AUDITLOT COPYING

Use the accepted/high-scoring AuditLot repository as a **quality and protocol-discipline benchmark**, not as a concept to clone.

The Agent Warranty contract must demonstrate the same kinds of strengths:

1. **One-sentence primitive clarity**
   - A reviewer should understand what this contract does immediately.
   - Suggested concise framing:
     > Enforceable performance warranties for autonomous agents: GenLayer validators independently establish whether frozen obligations were satisfied from verifiable evidence; deterministic contract logic controls cure, liability, escrow, and certification.

2. **Immutable commitments before semantic judgment**
   - Freeze settlement-critical terms before evidence is judged.
   - Freeze obligation graph, evidence policy, thresholds, severity, cure rules, deadlines, bond rules, delegation permissions, and settlement mapping.
   - Do not permit post-result parameter shopping.

3. **Evidence identity before interpretation**
   - Independently obtain the evidence.
   - Verify the evidence identity appropriate to its class.
   - Only then ask an LLM to make the bounded semantic judgment.

4. **Substantive validator reproduction**
   - A validator must independently reproduce decision-critical evidence work.
   - A well-formed but false leader result must be rejectable.
   - Shape-only validation is forbidden.

5. **LLM has the smallest possible job**
   - The model only classifies irreducibly semantic satisfaction for one already-frozen obligation/evidence set.
   - The model never chooses money, recipients, cure windows, liability allocation, graph transitions, thresholds, or final warranty settlement.

6. **Deterministic final consequence**
   - Obligation aggregation, graph propagation, cure eligibility, severity mapping, liability propagation, escrow accounting, settlement, timeout recovery, and certificate hashing are deterministic.

7. **INCONCLUSIVE is a real state**
   - Missing, changed, unavailable, malformed, ambiguous, or non-reproducible evidence must not silently become FULFILLED or FAILED.
   - If the evidence cannot support a safe semantic finding, return a typed inconclusive/external-failure result.

8. **Security claims must be narrow and honest**
   - Explicitly document what the primitive proves and what it does not prove.
   - If a known limitation cannot be removed with currently available GenLayer primitives, bound it, price it where applicable, test it, and state it plainly.
   - Never market a conditional property as unconditional.

9. **Live network behavior outranks assumptions**
   - If Studionet behavior contradicts local assumptions, redesign around observed behavior.
   - Record the failed design and why it was superseded.
   - Do not hide live-discovered bugs.

10. **Live acceptance matrix, not one happy path**
    - Prove fulfilled, partial/failed, inconclusive, timeout/recovery, cure, challenge, delegation, payout, refund, replay protection, and at least one adversarial evidence case live where feasible.

Do **not** copy AuditLot's blind sampling, commit/reveal protocol, or assessment model into Agent Warranty unless a warranty requirement independently needs such a mechanism.


# B. REQUIRED DIFFERENTIATORS

These features must be real and load-bearing.

## B1. Warranty Graph

A warranty is not a flat pass/fail task.

It contains bounded obligations connected by dependency edges.

Required v1 dependency edge:

```text
REQUIRES
```

Example:

```text
O1 — produce candidate supplier set
 |
 +--> O2 — verify business existence
       |
       +--> O3 — verify contact data
               |
               +--> O4 — produce final artifact
```

The graph must be a DAG.

Reject cycles deterministically.

If a prerequisite makes a downstream obligation impossible, deterministic code may propagate:

```text
BLOCKED
```

Do not spend LLM/validator work on consequences that the graph already proves.

## B2. Cure / Self-Healing Warranty

A remediable defect must not always cause immediate breach.

Required flow:

```text
DELIVERED
   ↓
DEFECT_FOUND
   ↓
CURE_REQUIRED
   ↓
corrected evidence
   ├─ success → FULFILLED
   └─ deadline/max-rounds → BREACHED
```

Cure must be:

- bounded by count;
- bounded by time;
- unable to rewrite original accepted terms;
- fully lineage-preserving.

## B3. Delegated Warranties

A provider may subcontract a bounded obligation when the parent warranty allows it.

Child record binds:

```text
parent_warranty_id
parent_obligation_id
delegated_scope_hash
delegator
delegate_provider
liability_cap_wei
depth
```

The child may itself be a warranty.

## B4. Cascading Liability

GenLayer determines **what happened** to the delegated obligation.

Deterministic code determines **how that result propagates**.

Never ask the model:

```text
"Who is legally/economically liable?"
```

Instead:

```text
"What did the evidence establish about obligation X?"
```

The parent graph + frozen delegation mapping determines liability/state consequences.

## B5. Multi-Modal Evidence

Support real evidence classes such as:

```text
WEB_RENDER
VISUAL_IMAGE
STRUCTURED_ARTIFACT
HASH_COMMITMENT
PUBLIC_DOCUMENT
API/WEB_RESPONSE where independently verifiable
```

Visual support is not allowed to be a dead schema field. If README/SUBMISSION claims image interpretation, prove an actual current GenLayer multimodal path before submission.


## B5A. Canonical Warranty Assessment Identity / No Result Shopping

Define a deterministic identity for the exact warranty being adjudicated.

The identity must bind the terms that determine what is being judged, for example:

```text
chain_id
contract_address
requester
provider
spec_hash
obligation_graph_hash
evidence_policy_digest
settlement_policy_hash
```

Once a warranty version reaches a real terminal adjudicated outcome, the same immutable warranty identity must not be silently recreated with friendlier thresholds, evidence rules, or severity weights merely to obtain a better result.

If retries are allowed for operational failure, distinguish:

```text
same warranty identity
same locked parameters
new bounded attempt
```

from:

```text
new contractual warranty
```

Do not let retry mechanics become result-shopping mechanics.


## B6. Portable Warranty Certificate

A finalized warranty must expose a compact machine-readable certificate that unrelated contracts can consume without understanding internal storage layout.

At minimum bind:

```text
warranty_id
spec_hash
obligation_graph_hash
requester
provider
delegation_root
evidence_digest
consensus_digest
obligation_result_digest
final_state
settlement_digest
completed_at
```

---

# C. THREE-CONSUMER PROOF

The same contract must work unchanged for at least:

1. **Agent procurement**
   - "Deliver 100 verified suppliers satisfying spec S."

2. **Research/data agents**
   - "Deliver a provenance-backed dataset with required coverage/freshness."

3. **Autonomous software operations**
   - "Complete migration/deployment/monitoring obligations and prove them."

Document these in `docs/INTEGRATION.md`.

If core source must change for each consumer, the primitive is too app-specific.

---

# D. PROTOCOL OBJECTS

## D1. Warranty Specification

Immutable after acceptance.

Bind at least:

```text
warranty_id
requester
provider
spec_version
spec_hash
task_summary
created_at
accepted_at
delivery_deadline
cure_window
challenge_window
max_cure_rounds
max_challenge_rounds
delegation_allowed
max_delegation_depth
reward_terms_wei
provider_bond_terms_wei
settlement_policy_hash
status
```

The spec hash must include every settlement-critical term.

## D2. Obligation

Each obligation must have an addressable ID and frozen evaluation rules.

Suggested fields:

```text
obligation_id
warranty_id
criterion_type
criterion_spec
severity
evaluation_mode
required_evidence_kinds
status
attempt
evidence_digest
finding_digest
```

Severity:

```text
CRITICAL
MAJOR
MINOR
INFORMATIONAL
```

Evaluation mode:

```text
DETERMINISTIC
WEB_SEMANTIC
VISUAL
STRUCTURED_ARTIFACT
MIXED
```

## D3. Evidence Receipt

Every settlement-relevant evidence item must have deterministic identity.

Bind:

```text
evidence_id
warranty_id
obligation_id
evidence_kind
source_url_or_pointer
submitted_artifact_hash
render_hash
content_hash
normalization_version
retrieval_kind
submitter
submitted_at
```

Model rationale must never enter evidence identity.

## D4. Typed Finding

The model/validator layer returns typed observation fields, not settlement.

Result enum:

```text
FULFILLED
PARTIAL
FAILED
BLOCKED
INCONCLUSIVE
EXTERNAL_FAILURE
```

Possible critical fields:

```text
obligation_id
result
critical_failure
evidence_sufficient
external_failure
confidence_band
rationale_codes
```

Prose/excerpts are diagnostic only.

## D5. Delegation Link

Bind parent-child scope and liability.

## D6. Warranty Certificate

Portable downstream receipt described above.

---

# E. STATE MACHINE

Write and freeze the exact state machine before coding.

Recommended shape:

```text
DRAFT
  ├─ fund/offer → OPEN
  └─ cancel → CANCELLED

OPEN
  ├─ accept + bond → ACCEPTED
  └─ requester cancel → CANCELLED

ACCEPTED
  ├─ work begins → IN_PROGRESS
  └─ delivery deadline → DELIVERY_TIMEOUT

IN_PROGRESS
  ├─ evidence submitted → DELIVERED
  └─ deadline → DELIVERY_TIMEOUT

DELIVERED
  └─ evaluate → EVALUATING

EVALUATING
  ├─ satisfied → FULFILLED
  ├─ remediable defect → CURE_REQUIRED
  ├─ weighted partial → PARTIAL
  ├─ decisive failure → BREACHED
  ├─ unclear evidence → INCONCLUSIVE
  └─ network/source failure → EXTERNAL_FAILURE

CURE_REQUIRED
  ├─ corrected evidence → EVALUATING
  └─ timeout/max rounds → BREACHED

FULFILLED / PARTIAL / BREACHED
  ├─ challenge window → CHALLENGEABLE
  └─ finality → READY_TO_SETTLE

INCONCLUSIVE / EXTERNAL_FAILURE
  ├─ bounded retry
  ├─ evidence resubmission
  └─ timeout → neutral recovery

READY_TO_SETTLE
  └─ settle → SETTLED
```

No funded state may become an irreversible fund trap.

---

# F. DETERMINISTIC VS NONDETERMINISTIC BOUNDARY

This boundary is submission-critical.

## Deterministic code handles:

- IDs;
- hashing;
- authorization;
- state transitions;
- DAG validation;
- dependency propagation;
- exact counts;
- exact deadlines;
- numeric thresholds;
- settlement arithmetic;
- recipient selection;
- payout basis points;
- bond rules;
- retry counts;
- cure limits;
- challenge limits;
- liability caps;
- escrow conservation.

## GenLayer nondeterminism handles only:

- live web observation;
- interpreting public evidence;
- semantic satisfaction of fuzzy criteria;
- visual interpretation;
- materiality where irreducibly semantic;
- independence/corroboration reasoning where needed.

The model must never directly output:

```text
winner
recipient
payout_bps
slash_bps
refund_amount
bond_amount
settlement state
final contract status
```

Use the principle:

```text
MODEL / WEB / VISION:
"What did we observe?"

DETERMINISTIC CONTRACT:
"What is that observation allowed to do?"
```

---

# G. EVIDENCE POLICY — SUBMISSION-CRITICAL

Do **not** use one retrieval primitive for every obligation.

Each obligation must freeze an `evidence_policy` before provider acceptance. The policy says what evidence class is acceptable and what independent verification is required.

At minimum support only evidence classes that are genuinely implemented and tested.

Recommended v1 evidence classes:

```text
PINNED_TEXT
PINNED_JSON
RENDERED_WEB
VISUAL
```

Optional classes may be added only if they have real semantics and tests.

The core rule is:

> Use the evidence primitive that actually proves the thing the warranty claims to prove.

## G1. PINNED_TEXT

Use when the obligation is about the exact bytes/text of an immutable or content-pinned artefact.

Expected flow:

```text
frozen URL/pointer + expected SHA-256
        ↓
leader independently web.get(...)
        ↓
exact response bytes
        ↓
size bound
        ↓
SHA-256 must match frozen digest
        ↓
UTF-8 decode / deterministic normalization
        ↓
semantic interpretation
```

Validator repeats the same work independently.

A hash mismatch, unavailable source, oversized body, or decode failure becomes:

```text
INCONCLUSIVE or EXTERNAL_FAILURE
```

Never silently PASS/FAIL.

For this evidence class, a browser render is **not automatically required**. Exact-byte identity is the security property.

## G2. PINNED_JSON

Use when the obligation depends on structured JSON/API evidence.

Expected flow:

```text
frozen URL/pointer + expected digest/schema
        ↓
independent fetch
        ↓
exact-byte or canonical-JSON verification
        ↓
strict parse/schema validation
        ↓
bounded semantic interpretation only if needed
```

If deterministic JSON checks can decide the criterion, do not call the LLM.

Document whether the identity is:

```text
hash(exact response bytes)
```

or:

```text
hash(canonical JSON)
```

Never switch between them implicitly.

## G3. RENDERED_WEB

Use when the warranty depends on **rendered webpage state**, client-side DOM, displayed content, or another property that raw response bytes do not faithfully represent.

Before coding, verify the current official GenLayer render API.

Conceptually:

```python
gl.nondet.web.render(
    url,
    mode="html",
    wait_after_loaded="2s",
)
```

but do not trust this remembered signature; use the current supported equivalent.

Expected flow:

```text
frozen URL
   ↓
leader independently renders
   ↓
validator independently renders
   ↓
bounded rendered artifact
   ↓
render_hash = hash(actual rendered artifact)
   ↓
canonical content extraction
   ↓
content_hash
   ↓
semantic interpretation
```

Neither `render_hash` nor `content_hash` may be trusted merely because the caller supplied them.

A caller-supplied expected digest may be treated as an assertion, but the independently observed artifact is authoritative.

## G4. VISUAL

Use only when the obligation actually depends on visual evidence.

See Section H.

## G5. Evidence Receipt

Every accepted evidence observation must produce a deterministic evidence receipt appropriate to its class.

Suggested common fields:

```text
evidence_schema_version
warranty_id
obligation_id
evidence_class
source_url_or_pointer
expected_digest_if_any
observed_artifact_digest
content_digest
normalization_version
retrieval_status
observed_at
```

Canonical `evidence_id` must be independently reproducible and must bind the authoritative observed identity.

Example domain-separated construction:

```text
evidence_id =
sha256(
  "AGENT_WARRANTY_EVIDENCE_V1|"
  + warranty_id
  + "|"
  + obligation_id
  + "|"
  + evidence_class
  + "|"
  + source_url_or_pointer
  + "|"
  + observed_artifact_digest
  + "|"
  + content_digest
  + "|"
  + normalization_version
)
```

Use the exact stable encoding documented by the contract.

Model reasoning must never enter `evidence_id`.

## G6. Submitted evidence is a reference/assertion, not truth

The provider may submit:

- URL;
- pointer;
- expected artifact digest;
- expected relationship;
- metadata.

Those values are untrusted assertions until independently checked.

The provider must not be able to manufacture a trusted evidence receipt by supplying plausible hashes.

## G7. Hostile-data framing

All fetched/rendered/visual material is untrusted DATA.

Prompt instructions must explicitly reject instructions embedded in evidence.

Test prompt injection.

## G8. URL admission

Use deterministic defense-in-depth appropriate to current GenVM constraints.

Prefer HTTPS.

Reject or safely handle:

- empty/malformed authority;
- embedded credentials;
- obvious localhost/internal hosts;
- `.local` / `.internal`;
- raw IP literals if appropriate;
- unsupported ports;
- whitespace/control characters.

Do not claim DNS-level SSRF protection unless the runtime actually documents/proves it.

## G9. Evidence policy must affect code

Do not define enums like `PINNED_TEXT`, `RENDERED_WEB`, `VISUAL` if every branch eventually executes the same generic fetch.

The evidence class must select a real verification path.

## G10. Positive-assurance rule

A positive obligation finding is only as strong as the frozen evidence class.

Examples:

```text
PINNED_TEXT:
exact bytes matched + semantic criterion satisfied

RENDERED_WEB:
actual rendered artifact independently obtained + semantic criterion satisfied

VISUAL:
actual image/screenshot independently bound + multimodal criterion satisfied
```

Do not pretend one evidence class proves the guarantees of another.

---

# H. VISUAL EVIDENCE — BLOCKER IF CLAIMED

Before coding visual logic:

1. verify exact current GenLayer multimodal/image API;
2. verify supported input representation;
3. test the runtime;
4. document exact behavior.

Visual result enum may include:

```text
VISUAL_MATCH
VISUAL_CONFLICT
VISUAL_INSUFFICIENT
```

Bind visual evidence to:

```text
artifact_hash
context_url_or_pointer
render_hash if web-derived
obligation_id
```

The model may say what the image depicts.

The model may not author the artifact hash or settlement.

If visual interpretation cannot be proven live, do not claim it in final submission until fixed.

---

# I. CONSENSUS DESIGN — MINIMIZE FALSE UNDETERMINED

No design can honestly guarantee that the GenLayer protocol can never produce a protocol-level `UNDETERMINED`.

The goal is to **avoid unnecessary disagreement** while remaining safe.

Do not compare raw LLM prose.

Do not require byte-identical explanations.

For semantic obligations, prefer a substantive validator/custom nondeterministic pattern supported by the current SDK.

Leader:

```text
independently observe evidence
classify obligation
return bounded typed proposal
```

Validator:

```text
validate types/schema
independently observe same class of evidence
independently classify
reject fabricated evidence identity
compare settlement-critical fields
accept/reject
```

Settlement-critical fields may include:

```text
obligation_id
result
critical_failure
evidence_sufficient
external_failure
decision-critical evidence identity
```

Safe differences may include:

```text
reasoning prose
excerpt choice
ordering
noncritical rationale code ordering
adjacent confidence band only when it cannot alter settlement
```

The validator must reject a well-formed but substantively false leader result.

For every evidence class, validator reproduction must include the identity checks that make that class trustworthy.

Examples:

```text
PINNED_TEXT:
validator refetches exact bytes and recomputes SHA-256

PINNED_JSON:
validator refetches and independently verifies exact/canonical JSON identity

RENDERED_WEB:
validator independently renders and recomputes render/content identity

VISUAL:
validator independently binds the image/screenshot identity and independently evaluates the visual criterion
```

Where supported by the current SDK, prefer a substantive pattern equivalent to:

```python
gl.vm.run_nondet_unsafe(leader_fn, validator_fn)
```

The leader result should be treated as adversarial input.

Format-only validation is not acceptable.

---

# J. ESCROW — LOAD-BEARING

Use current supported GenLayer payable/EVM transfer APIs verified from docs/runtime.

The intended reusable pattern is:

```python
@gl.evm.contract_interface
class _Recipient:
    class View:
        pass

    class Write:
        pass


def _send_gen(to_address: str, amount: u256) -> None:
    if not to_address:
        raise gl.vm.UserError("Missing recipient address")
    if amount <= u256(0):
        raise gl.vm.UserError("Transfer amount must be positive")
    _Recipient(Address(to_address)).emit_transfer(value=amount)
```

Confirm exact current syntax before using it.

## J0. Payable failure semantics must be verified live

Do not assume EVM-style atomic value rollback.

AuditLot-level rigor means this must be empirically tested against the current Studionet/runtime.

Before finalizing any payable entry point, deliberately test an invalid payable call with a tiny development amount and determine:

```text
Does gl.message.value remain credited if the method reverts?
Does a refund scheduled before a re-raise actually commit?
Does EVM-style emit_transfer reach a plain wallet?
```

If current Studionet reproduces the known behavior where attached value is credited even when the method later reverts, then **payable methods that can reject after value delivery must not strand funds**.

In that environment, use a safe pattern such as:

```text
payable wrapper
  ↓
try internal validation/creation
  ├─ success → return success value
  └─ failure
       ↓
       schedule full refund of gl.message.value
       ↓
       emit rejection event/reason
       ↓
       RETURN NORMALLY with explicit sentinel
```

Do not refund and then re-raise if live testing proves the refund is rolled back by the reverting call.

Integrators must have an unambiguous return value/event for rejected payable calls.

If current runtime behavior has changed, document the observed behavior and use the safe current semantics instead.

## J1. Custody

Any GEN-receiving function must be payable.

Trust only:

```python
gl.message.value
```

Keep economic terms separate from deposited ledger:

```text
reward_terms_wei
reward_deposited_wei

provider_bond_terms_wei
provider_bond_deposited_wei
```

The ledger fields are authoritative for payout.

## J2. Exact bond

If the provider bond is fixed:

```text
gl.message.value == provider_bond_terms_wei
```

Reject underpayment and overpayment.

## J3. One emission point

Every GEN payout goes through `_send_gen`.

No scattered transfer code.

## J4. Mandatory payout order

Every payout path:

1. read ledger;
2. validate nonzero;
3. calculate deterministic split;
4. zero ledger;
5. persist/save state;
6. only then call `_send_gen`.

Never transfer first.

## J5. Closed exit set

Account for every terminal economic path before coding:

| Outcome | Reward | Provider bond | Can funds remain stuck? |
|---|---|---|---|
| FULFILLED | provider | returned to provider | no |
| PARTIAL | deterministic split | policy-defined | no |
| BREACHED | requester refund / policy compensation | policy-defined | no |
| INCONCLUSIVE | no manufactured winner; retry/recovery | neutral policy | no |
| EXTERNAL_FAILURE | retry/recovery | neutral policy | no |
| DELIVERY_TIMEOUT | frozen policy | frozen policy | no |
| CANCELLED pre-acceptance | requester refund | none | no |

No `TBD`.

## J6. Double payout

A second settlement must find zero ledger / terminal state and reject.

## J7. Model never chooses money

Settlement percentages come from frozen deterministic policy.

Use integer basis points, not floats.

---

# K. DELEGATION CONSERVATION

Child warranties cannot create unlimited liability.

Enforce:

```text
sum(child allocated liability) <= parent delegated liability budget
```

Also enforce:

```text
child scope ⊆ delegated parent obligation scope
child depth <= max_delegation_depth
```

A child failure creates a typed child result.

Deterministic parent logic decides whether/how it affects the parent.

Do not ask the model who owes whom.

---

# L. CHALLENGE / APPEAL

A challenge must not mean:

```text
"ask the same AI again"
```

Require:

```text
challenged_obligation_id
challenge_reason_code
new evidence or explicit new ground
```

Use fresh independent consensus.

Bound challenge rounds.

Possible typed challenge outcomes:

```text
UPHELD
MODIFIED
OVERTURNED
INCONCLUSIVE
```

No infinite appeal loop.

---

# M. PROTOCOL INVARIANTS

Freeze and test at least these invariants.

### W1 — Specification Immutability
Settlement-critical terms cannot change after acceptance.

### W2 — Evidence Independence
Validators independently observe decision-critical external evidence.

### W3 — Model Boundary
Model output is typed observation/interpretation only.

### W4 — Deterministic Settlement
Money/state consequences derive from frozen policy + validated findings.

### W5 — Escrow Conservation
Every deposited unit has exactly one eventual accounting path.

### W6 — Checks-Effects-Interactions
Ledger zero/save precedes transfer.

### W7 — Delegation Conservation
Child scope/liability cannot exceed parent allocation.

### W8 — Disagreement Safety
Uncertainty, parse failure, or validator disagreement cannot manufacture a winner.

### W9 — Evidence Authenticity
Settlement-relevant evidence binds to independently verifiable identity.

### W10 — Evidence/Interpretation Separation
Model rationale cannot alter evidence identity.

### W11 — Cure Boundedness
Cure cannot loop forever or rewrite accepted terms.

### W12 — Terminal Immutability
Final settlement cannot be replayed.

For each invariant document:

```text
statement
enforcement point
failure mode
Direct Mode test
live test where feasible
```

---

# N. SCHEMA-SAFETY

Avoid `could not load contract schema`.

Before every candidate deployment:

- parse source;
- run current GenVM lint/check;
- generate/inspect schema;
- use only supported public types;
- keep constructor/schema signatures conservative;
- avoid unsupported nested public types;
- verify current dependency/runner;
- verify current `gl.message.sender` / time / storage APIs;
- use `gl.vm.UserError` for expected validation errors;
- test exact runtime response object shapes;
- keep source ASCII-safe if the current toolchain requires it.

Do not treat ordinary Python success as schema proof.

---

# O. BUILD PHASES

Do not jump straight into a giant contract.

## Stage 0 — Architecture only

Create:

```text
DECISION.md
docs/ARCHITECTURE.md
docs/INVARIANTS.md
docs/ESCROW.md
docs/EVIDENCE.md
```

Freeze:

- state machine;
- obligation graph;
- evidence schema;
- consensus schema;
- escrow table;
- cure rules;
- delegation rules;
- bounds;
- W1-W12.

Do not write nondeterministic production code until architecture is approved.

## Stage 1 — Deterministic skeleton

Implement:

- warranty IDs;
- specification freeze;
- obligations;
- DAG validation;
- graph propagation;
- bounded storage;
- public views;
- state machine.

No web.
No model.
No payout.

## Stage 2 — Escrow

Implement:

- requester reward custody;
- provider bond custody;
- cancellation/refund;
- timeout recovery;
- deterministic settlement preview;
- single emission helper;
- zero-save-transfer invariant.

## Stage 3 — Evidence identity

Implement:

- evidence registration;
- deterministic IDs;
- web evidence metadata;
- visual artifact metadata;
- evidence lineage;
- URL admission.

Still no model-controlled state.

## Stage 4 — Real GenLayer consensus

Implement:

- verified current web-render API;
- semantic finding schema;
- substantive custom validator/equivalence;
- parser hardening;
- typed failure semantics.

## Stage 5 — Cure + challenge

Implement bounded cure and bounded challenge.

## Stage 6 — Delegated warranties

Implement child scope, depth, liability conservation, and propagation.

## Stage 7 — Warranty Certificate

Expose compact machine-readable final receipt.

## Stage 8 — Adversarial hardening

Run full Direct Mode, forged-leader, evidence, parser, graph, delegation, and escrow attacks.

## Stage 9 — Candidate source freeze

Commit and push the locally green candidate source.

Record the exact commit SHA and deployable contract blob/source hash.

Do **not** stop.

## Stage 10 — Canonical Studionet deployment by the coding agent

The coding agent must deploy the committed candidate itself using the current supported GenLayer CLI or Studio Mode/SDK route available in the environment.

Before deployment:
- confirm current network/RPC;
- confirm signer public address;
- confirm signer can sign;
- confirm sufficient Studionet funding or use the current official development funding route;
- never print or commit private keys, mnemonics, keystore passwords, or tokens.

Deploy the exact committed source.

Capture:
- deployer public address;
- deployment transaction hash;
- contract address;
- transaction status/finality;
- deployed source;
- schema;
- Explorer URL.

Then immediately continue to live verification.

## Stage 11 — Live verification + steward pre-submission audit

Do not recommend submission until all four gates below are green.

---

# P. DIRECT MODE / ADVERSARIAL TEST MATRIX

Test the real contract logic.

Mock nondeterminism, not the public method under test.

Required categories:

## Warranty lifecycle
- create;
- accept;
- unauthorized calls;
- cancel;
- delivery;
- deadlines;
- terminal replay.

## Graph
- valid DAG;
- cycle;
- missing node;
- duplicate edge;
- max bounds;
- transitive BLOCKED propagation.

## Evidence
- valid render identity;
- render changed;
- forged evidence ID;
- prompt injection;
- source unavailable;
- malformed URL;
- plain-text fallback;
- visual artifact mismatch.

## Model output
- malformed JSON;
- fenced JSON;
- missing fields;
- extra settlement fields;
- wrong enum;
- bool-as-int;
- float-as-int;
- numeric string;
- oversized output;
- invented obligation/evidence ID.

## Forged leader
Leader attempts to:
- claim FULFILLED on contradictory evidence;
- invent render success;
- alter evidence identity;
- smuggle payout;
- smuggle state;
- omit critical field.

Substantive validator must reject.

## Cure
- correct cure;
- failed cure;
- max rounds;
- timeout;
- old evidence preserved.

## Challenge
- valid new evidence;
- no new evidence;
- upheld;
- modified;
- overturned;
- max rounds.

## Delegation
- valid child;
- excessive depth;
- scope expansion;
- liability overflow;
- child success;
- child breach propagation;
- unrelated child isolation.

## Escrow
- zero reward;
- valid reward;
- exact bond;
- underpay;
- overpay;
- fulfilled payout;
- partial split;
- breach refund/compensation;
- inconclusive recovery;
- external failure recovery;
- delivery timeout;
- cancellation;
- unauthorized settlement;
- double settlement.

Every setup write must be asserted successful before testing downstream behavior.

---

# Q. AUTONOMOUS CANONICAL DEPLOYMENT

This section overrides any instruction that would make the coding agent stop and wait for the user to deploy.

The coding agent must perform the canonical Studionet deployment itself once all local candidate gates are green.

Before deployment, create/update:

```text
docs/DEPLOYMENT.md
docs/LIVE_SMOKE_TEST.md
docs/RELEASE_CANDIDATE_VERIFICATION.md
```

Record before deployment:

```text
candidate commit SHA
contract blob/source hash
exact contract path
constructor args
expected ABI/method count
expected schema version
verified SDK/runner/tool versions
network/RPC
deployer public address
```

Deployment rules:

1. Use the exact committed candidate source.
2. Use the current official GenLayer CLI or supported Studio Mode/SDK route.
3. Verify the network is Studionet.
4. Verify the signer can sign.
5. Never expose private keys, mnemonics, wallet passwords, keystore contents, or tokens.
6. If an existing authorized local account is available, use it.
7. If a dedicated development signer is required, create/use it through the normal supported GenLayer account flow without leaking secrets.
8. If Studionet funding is required, use the current official development/faucet route.
9. Do not call a deployment successful merely because the command returned; inspect receipt/status/finality.
10. After deployment, do not stop. Continue directly into source-parity and live integration verification.

Capture:

```text
canonical contract address
deployment tx hash
deployer public address
initial status
final status when available
Explorer URL
deployed source/code
schema result
```

The coding agent is responsible for carrying this repository from green local candidate through canonical deployment and live verification.

---

# R. LIVE VERIFICATION AFTER AGENT DEPLOYS


Using the canonical address returned by the coding agent's own deployment, verify:

1. schema loads;
2. expected ABI/methods visible;
3. deployed source matches committed candidate;
4. deterministic warranty lifecycle;
5. real semantic GenLayer consensus;
6. real web render-backed evidence;
7. real visual path if claimed;
8. payable requester reward custody;
9. exact provider bond custody;
10. actual settlement payout;
11. ledger zeroed before/at settlement;
12. duplicate settlement rejected;
13. timeout/recovery;
14. cure path;
15. challenge path;
16. one delegated child warranty;
17. liability conservation;
18. portable certificate.

Never describe `ACCEPTED` transaction status as `FINALIZED`.

Do not claim wallet payout merely because internal ledger changed; verify actual transfer evidence/balance when tooling permits.

---

# S. FOUR SUBMISSION GATES

No submission slot may be used until every gate is green.

## Gate 1 — Contract / Schema

```text
schema loads
ABI sane
GenVM lint/check green
Direct Mode green
bounded storage
W1-W12 mapped
escrow conservation proven
```

## Gate 2 — Real Consensus

```text
real Studionet nondeterministic execution
substantive validator
positive case
negative case
disagreement/fail-closed case
no format-only validator
```

## Gate 3 — Real Evidence

```text
real web render
render/content identity
independent validator retrieval
real visual interpretation if claimed
prompt-injection resistance
unavailable-source semantics
```

## Gate 4 — Steward Fit

```text
standalone primitive
not marketplace/app
not generic dispute contract
not simple milestone escrow
not thin LLM wrapper
not AI-controlled payout
three unrelated consumers
Warranty Graph load-bearing
cure load-bearing
delegation/liability load-bearing
README claims backed by live evidence
```

If any gate is not green:

```text
DO NOT SUBMIT.
```

---

# T. STEWARD RED-TEAM REVIEW

Before `SUBMISSION.md` is finalized, act like a skeptical reviewer and try to reject the work.

Ask:

- Is this actually reusable?
- Is it secretly a project?
- Could a normal backend replace GenLayer without materially changing the trust model?
- Is consensus load-bearing?
- Does the validator independently inspect evidence?
- Is it more than format checking?
- Is web evidence a real render or merely text handed to an LLM?
- Is visual evidence actually proven live?
- Can prompt injection influence the judgment?
- Can unavailable evidence become a false breach?
- Can a model choose payout indirectly?
- Can a child warranty create excess liability?
- Can cure loop forever?
- Can funds become stuck?
- Can settlement replay?
- Can harmless model wording variation trigger unnecessary protocol disagreement?
- Are docs overstating transaction finality?
- Does the deployed source exactly match the repo?

Any serious rejection reason must be fixed before spending a slot.

---

# U. REQUIRED DOCUMENTATION

At minimum:

```text
contracts/agent_warranty_protocol.py

tests/direct/
tests/integration/

docs/ARCHITECTURE.md
docs/INVARIANTS.md
docs/CONSENSUS.md
docs/SECURITY.md
docs/ESCROW.md
docs/EVIDENCE.md
docs/DELEGATION.md
docs/INTEGRATION.md
docs/DEPLOYMENT.md
docs/RELEASE_CANDIDATE_VERIFICATION.md

DECISION.md
README.md
SUBMISSION.md
MANUAL_DEPLOYMENT.md
MANUAL_SMOKE_TEST.md
```

Do not create empty decorative files.

---

# V. CANONICAL REVIEWER DEMO

Use one compact end-to-end demo that proves the primitive without turning it into an app:

> A buyer agent funds a warranty for a provider agent to deliver a bounded supplier dataset. The provider posts a bond. One obligation is deterministic (count/uniqueness), one uses real web-render verification, and one visual obligation is included only if the current runtime supports and proves the image path. The first delivery contains a remediable defect, triggering `CURE_REQUIRED`. The provider cures it. One sub-obligation is delegated through a child warranty. Final typed findings deterministically settle escrow and emit a portable Warranty Certificate.

The demo should prove:

```text
mixed deterministic + semantic obligations
Warranty Graph
real web evidence
real GenLayer consensus
visual evidence if supported/claimed
cure
delegation
escrow custody
real payout
replay prevention
portable certificate
```

---

# W. FREEZE STANDARD

Once:

```text
idea/collision position defensible
three-consumer proof complete
delete-GenLayer test passes
W1-W12 proven

schema loads
Direct Mode green
GenVM lint green
forged-leader tests green

real web evidence proven
real visual evidence proven if claimed
real consensus proven

reward custody proven
provider bond proven
zero-save-transfer proven
double settlement rejected
recovery proven

cure proven
challenge proven
delegation proven
liability conservation proven
certificate proven

canonical deployment performed by coding agent from the frozen committed source
source parity verified
Explorer/transaction evidence recorded

README accurate
CONSENSUS docs accurate
SECURITY docs accurate
ESCROW docs accurate
INTEGRATION docs accurate
SUBMISSION copy-ready
working tree clean
```

freeze the contract.

Do not add another feature pass.

Do not make cosmetic source changes that invalidate canonical deployment parity.

If nothing meaningful remains, end with exactly:

```text
NOTHING MEANINGFUL REMAINS BEFORE SUBMISSION.
```

---

# X. FINAL POSITIONING

The finished repository must make this statement true:

> **Agent Warranty Protocol is a reusable GenLayer warranty and liability primitive in which autonomous parties freeze performance obligations, validators independently inspect real external evidence and agree on typed obligation findings, and deterministic contract logic controls dependency propagation, cure, delegated liability, escrow, settlement, recovery, and portable warranty certification.**

Now follow the generic single-repository execution framework below, subject to all Agent Warranty Protocol overrides above.

---

# MASTER AGENT INSTRUCTION

## INPUT

```text
REPOSITORY: <REPO_URL>
```

That is the only required user-supplied parameter.

Everything else must be discovered from:

1. the repository;
2. its Git history;
3. the repository owner's other relevant repositories;
4. the current official GenLayer documentation/tooling;
5. current GenLayer ecosystem examples and contribution requirements;
6. actual test/runtime results.

Do not ask the user to repeat information that can be discovered.

If the repository is empty or contains no meaningful contract concept, scout and select a strong new primitive before building.

If the repository already contains a meaningful concept or partial implementation, understand it first and **finish it rather than casually replacing it**.

---

# 0. NORTH STAR

The final repository must contain a standalone Intelligent Contract primitive that is:

- useful, reusable, or genuinely educational to other GenLayer builders;
- based on a real trust/judgment problem;
- materially dependent on GenLayer rather than merely storing an off-chain AI answer;
- backed by independently checkable evidence where evidence is required;
- explicit about what validators must agree on;
- explicit about what happens when validators cannot safely agree;
- deterministic everywhere deterministic code can safely do the job;
- nondeterministic only where live observation or semantic judgment truly requires it;
- fail-closed where a false positive could create an unsafe state transition;
- bounded in state, history, inputs, model output, and expensive work;
- composable through a small machine-readable interface;
- tested in Direct Mode;
- validated by the GenVM linter/SDK;
- exercised on a real GenLayer network, normally Studionet;
- backed by reproducible committed integration tests;
- documented well enough that a reviewer can understand the trust model without reverse-engineering the source;
- deployed from an identifiable source commit;
- backed by exact transaction evidence;
- linked through the GenLayer Explorer;
- cleanly pushed to the provided repository;
- frozen once all meaningful gates are green.

The goal is **not** maximum code, maximum LLM usage, maximum features, maximum test count, or maximum repository size.

The goal is a **small, defensible piece of GenLayer infrastructure whose consensus is load-bearing**.

---

# 1. NON-NEGOTIABLE RULES

## 1.1 One project, one repository

This task is tied to exactly the supplied repository.

Do not create unrelated sibling projects.

Do not spread critical code/evidence across private scratch repositories.

A separate public verification repository or submodule is acceptable only if there is a compelling tooling reason and the main repository remains self-explanatory. Prefer keeping verification in the main repository.

## 1.2 Preserve before changing

If the repository already has commits:

```bash
git fetch --all --prune
git status --short
git rev-parse HEAD
git branch --show-current
```

Record the starting HEAD.

Before substantive edits, create a rollback branch:

```bash
git branch backup/pre-finalisation-<short-starting-sha>
git push origin backup/pre-finalisation-<short-starting-sha>
```

If push is not yet authenticated, create the branch locally first and push it immediately after GitHub authentication succeeds.

Never force-push unless the user explicitly instructs you to rewrite history.

## 1.3 Never fabricate verification

Never write:

- PASS when a command was not run;
- FINALIZED when a transaction is only ACCEPTED;
- MAJORITY_AGREE when the receipt does not show it;
- “deployed source matches” without comparing source;
- a transaction hash that was not returned by the network;
- a test count copied from an earlier commit;
- a balance, contract address, signer address, or explorer URL you did not verify.

If a test cannot be run, say so.

If a network call is blocked before a transaction is submitted, that is **not** a deployment failure and not a contract failure. Diagnose the transport layer.

## 1.4 No secret leakage

Never:

- print a private key;
- print a mnemonic;
- commit a keystore password;
- put a wallet password into README/docs;
- paste an auth token into a command that will be recorded in shell history unless the user explicitly accepts that risk;
- add `.env` containing secrets to Git;
- expose `GH_TOKEN`, `GITHUB_TOKEN`, private account keys, or GenLayer keystore contents.

Prefer browser/device authentication, OS credential stores, encrypted keystores, interactive password prompts, environment variables already provisioned by the user, and Studio Mode generated accounts.

## 1.5 Contract-only by default

For a standalone Intelligent Contract contribution, do **not** add:

- a dashboard;
- a landing page;
- wallet UI;
- a backend server;
- an indexer;
- a database;
- unrelated agents;
- marketing assets.

A frontend can turn a strong contract primitive into the wrong submission category.

Supporting material should normally be:

```text
contracts/
tests/direct/
tests/integration/
fixtures/
scripts/
docs/
README.md
DECISION.md
SUBMISSION.md
gltest.config.yaml
requirements*.txt
.gitignore
LICENSE
```

## 1.6 Prefer one canonical deployable contract

Prefer exactly one canonical submission contract under `contracts/`.

A consumer example is optional. Add an executable second `gl.Contract` only if it proves an important composition property that cannot be communicated adequately through an interface and `docs/INTEGRATION.md`.

Do not add extra contracts merely to make the repository look substantial.

## 1.7 Current official tooling wins

GenLayer evolves.

Before relying on an exact package version, CLI flag, SDK header, transaction status name, or test helper:

- inspect the contract's current dependency header;
- inspect `requirements*.txt`;
- run `--version` / `--help`;
- consult the current official GenLayer docs.

Do not blindly copy a package version from an older repository.

---

# 2. BOOTSTRAP THE MACHINE AND REPOSITORY

## 2.1 Parse the repository URL

Extract:

```text
OWNER
REPO
HOST
```

Confirm the repository:

```bash
gh repo view OWNER/REPO
```

If the repository exists, clone or enter it.

```bash
gh repo clone OWNER/REPO
cd REPO
```

If it is already cloned:

```bash
git remote -v
git status --short
git rev-parse --show-toplevel
```

Confirm that `origin` points to the supplied repository.

Do not silently work in another clone.

## 2.2 Inspect the development environment

Record at least:

```bash
git --version
gh --version
python --version
python3 --version
node --version
npm --version
genlayer --version
```

On Windows also inspect available Python installations:

```powershell
py -0p
where.exe python
where.exe py
where.exe genlayer
where.exe gh
```

On POSIX:

```bash
which python3
which genlayer
which gh
uname -a
```

The current GenLayer test tooling expects Python 3.12+; still confirm the current official requirement rather than assuming.

Record the actual versions used for the successful final run in deployment/testing docs.

---

# 3. GITHUB AUTHENTICATION AND PUSH ACCESS

The agent is responsible for establishing a normal authenticated Git/GitHub path if possible.

## 3.1 Check GitHub CLI authentication

```bash
gh auth status
```

If the wrong authenticated account is active:

```bash
gh auth status
gh auth switch --hostname github.com --user <correct-user>
```

If the required account is not authenticated, trigger GitHub's browser flow:

```bash
gh auth login --hostname github.com --web --git-protocol https
```

Then:

```bash
gh auth status
gh auth setup-git
```

`gh auth setup-git` configures Git to use the authenticated GitHub CLI credential helper.

Do not ask the user to paste a PAT unless browser/device authentication is genuinely impossible.

If a secure token already exists in the environment, GitHub CLI may use `GH_TOKEN`/`GITHUB_TOKEN`; never print it.

## 3.2 Verify repository permission

```bash
gh repo view OWNER/REPO
git ls-remote origin
```

If the active account lacks push rights, do not fork automatically unless the user requested a fork. Authenticate the correct authorized account.

## 3.3 If the supplied repository does not exist

If the URL clearly identifies an owner/repo and the authenticated user has permission to create it:

```bash
gh repo create OWNER/REPO --public
```

Then initialize the local repository:

```bash
git init
git branch -M main
git remote add origin https://github.com/OWNER/REPO.git
```

If visibility is already implied by the user's environment, preserve it.

## 3.4 Git identity

Check:

```bash
git config user.name
git config user.email
```

If missing, configure a reasonable **repository-local** identity rather than overwriting the user's global identity without permission:

```bash
git config user.name "<authenticated GitHub username>"
git config user.email "<verified/noreply address if discoverable>"
```

Do not invent a personal email address.

---

# 4. CLASSIFY THE CURRENT REPOSITORY BEFORE BUILDING

Determine which state the repository is in.

## STATE A — empty/new

No meaningful contract, no real thesis.

→ Run the full idea-scouting process.

## STATE B — concept only

README/spec/notes exist, contract absent or toy.

→ Audit the concept, collision-check it, then design and build.

## STATE C — partial contract

Meaningful contract exists but tests/deployment/docs are incomplete.

→ Preserve concept, audit source deeply, harden and finish.

## STATE D — apparently complete

Contract/tests/docs/deployment claims exist.

→ Do not trust claims. Reproduce, audit, repair inconsistencies, and obtain current evidence.

Document the classification in your work log.

---

# 5. IDEA SCOUTING: FIND A PRIMITIVE, NOT AN APP

Run this phase only when the repository lacks a strong existing thesis or when the existing concept clearly fails the GenLayer fit test.

## 5.1 Start with the repeated trust question

The best reusable primitives usually begin with:

> “What judgment do multiple applications repeatedly need, where nobody should be able to author the answer alone?”

Strong raw material includes:

- live facts that require corroboration;
- semantic changes in public rules or commitments;
- whether an external dependency is still safe to rely on;
- whether a service is behaviorally healthy rather than merely reachable;
- whether an autonomous agent still conforms to a published behavioral specification;
- whether a live artifact satisfies an immutable acceptance specification;
- whether public evidence supports one side of a dispute;
- whether an appeal warrants a fresh independent ruling;
- whether an external page is safe to feed into another reasoning system;
- whether independent sources are actually independent rather than syndicated;
- whether a policy clearly permits, forbids, or conditions an action;
- whether a prior commitment has materially drifted;
- whether evidence establishes causal responsibility rather than simple correlation;
- whether a submitted object is derivative, duplicate, compliant, complete, or trustworthy under explicit criteria;
- whether a previously accepted state is now stale.

Do not treat those examples as a list to copy. Use them to identify the **shape** of a reusable trust problem.

## 5.2 Search the repository owner's complete portfolio

Do not compare only against repository names that contain “GenLayer”.

Use:

```bash
gh repo list OWNER --limit 200
```

For likely relevant repos inspect:

- README;
- `contracts/`;
- `docs/`;
- submission notes;
- public methods;
- exact verdict/state model.

Build a collision matrix.

Suggested columns:

| Repo | Core trust question | Evidence | Consensus decision | Stateful primitive | Consumer surface | Same lane? |
|---|---|---|---|---|---|---|

Do not decide collision from branding.

Two repos with different names can be the same primitive if they use the same evidence to reach the same decision with essentially the same state model.

Two repos in the same domain can still be distinct if their trust questions and state guarantees are orthogonal.

## 5.3 Search the GenLayer ecosystem

Check current:

- official “Build With GenLayer” ideas;
- “When to Use GenLayer” guidance;
- typical use cases;
- official examples;
- recent community submissions if discoverable;
- the target contribution mission/category.

Use official idea lists as **domains to explore**, not concepts to clone.

## 5.4 Negative-space method

Map what already exists along semantic axes.

Examples of orthogonal axes:

```text
truth/corroboration
        vs
source safety

change detection
        vs
dependency reliance

availability
        vs
behavioral conformance

policy interpretation
        vs
policy drift

one-shot adjudication
        vs
appeal/re-examination

artifact acceptance
        vs
causal responsibility

identity
        vs
reputation
        vs
authorization

observation
        vs
interpretation
        vs
settlement
        vs
recovery
```

Ask:

> What trust boundary is still being repeatedly reimplemented by downstream contracts?

That is often a stronger idea source than “invent another AI contract”.

## 5.5 Generate a serious candidate set

Generate at least 10 genuinely different primitive candidates.

For each record:

```text
Name / working label
One-sentence primitive thesis
Exact trust question
Who uses it
Public evidence
Why a deterministic contract cannot answer it
Why one LLM/API/operator is insufficient
What validators independently do
Stable typed output
State that accumulates
At least three distinct downstream consumers
Nearest existing repo
Why it is not the same primitive
Major risk / hardest technical part
Live testability
```

Do not select the first plausible idea.

## 5.6 Candidate scoring

Score each candidate 0–10 on:

1. **GenLayer necessity**
2. **novelty against owner portfolio**
3. **novelty against ecosystem**
4. **reuse across unrelated consumers**
5. **clarity of independently verifiable evidence**
6. **clarity of equivalence/validator rule**
7. **state design**
8. **deterministic safety constraints**
9. **adversarial depth**
10. **live Studionet testability**
11. **impact/usefulness**
12. **standalone-contract category fit**

Reject weak candidates even if they sound impressive.

Immediately reject a candidate whose load-bearing evidence is private or unavailable to validators unless the design first turns that evidence into something independently checkable, such as a public artifact, a committed hash plus revealed artifact, or a verifiable signed attestation. A private backend database that only one party can query is not a strong GenLayer evidence source.

Also reject a candidate whose primary value is open-ended content generation. GenLayer should adjudicate a shared decision or state transition, not act as a generic on-chain chatbot.

## 5.7 The delete-GenLayer test

For every finalist answer:

> If GenLayer is removed, what exact trust property disappears?

Reject the idea if a normal backend or single off-chain LLM can provide essentially the same security model.

A good answer sounds like:

> “Without GenLayer, one party/operator becomes the authority that chooses/reads/interprets the evidence and authors the verdict.”

A weak answer sounds like:

> “GenLayer makes it more decentralized.”

## 5.8 The three-consumer test

Name three materially different downstream contracts that could use the primitive **without changing its core contract**.

If the only consumer is the app you imagined, it is probably a Project, not a reusable primitive.

## 5.9 The machine-readable-output test

The primary result should normally be something like:

```text
status enum
verdict enum
severity integer
bounded score/band
boolean gate
structured criterion results
freshness status
typed evidence receipt
```

—not an essay a human must read before deciding what to do.

## 5.10 The “model is not the contract” test

Reject designs where the architecture is merely:

```text
caller text -> LLM -> store LLM answer
```

A strong architecture looks more like:

```text
immutable/bounded inputs
    ↓
deterministic admission
    ↓
live/semantic consensus observation
    ↓
substantive equivalence or independent validator
    ↓
deterministic normalization/gates
    ↓
typed state transition
    ↓
small downstream interface
```

## 5.11 Record the decision

Create:

```text
DECISION.md
```

Include:

- portfolio collision map;
- ecosystem collision map;
- candidates considered;
- scoring;
- rejected candidates and reasons;
- selected primitive;
- delete-GenLayer answer;
- three-consumer proof;
- hardest technical risk;
- why it belongs in standalone Intelligent Contracts.

Do not hide overlap analysis. It strengthens the submission.

---

# 6. WRITE THE CONTRACT SPECIFICATION BEFORE THE CONTRACT

Before coding, define the protocol.

## 6.1 One-sentence thesis

Use this structure:

> `<Name>` is a reusable GenLayer primitive that `<does exact judgment>` from `<independently observable evidence>` and exposes `<typed result>` for `<downstream consumers>`.

## 6.2 Define the exact decision

Bad:

> “AI checks the deliverable.”

Good:

> “Given an immutable acceptance specification and a live public artifact, return ACCEPTED, REJECTED, or UNDECIDED; only ACCEPTED authorizes release.”

## 6.3 Define evidence ownership

For every fact used in consensus, ask:

- who selected the source?
- who controls the source?
- can validators fetch it independently?
- can a party edit it after committing?
- do we need a hash/digest?
- do we need multiple independent sources?
- do we need to distinguish same-owner/syndicated sources?
- what happens if the source disappears?

## 6.4 Define state objects

For every record specify:

- immutable fields;
- mutable fields;
- owner/requester/provider/counterparty;
- status;
- timestamps;
- version/fingerprint;
- latest receipt pointer;
- bounded history;
- counters;
- failure state;
- retry count;
- finality state.

## 6.5 State machine

Write the state machine before implementation.

Example shape:

```text
PENDING
 ├─ resolve → SUCCESS
 ├─ resolve → NEGATIVE
 ├─ resolve → INCONCLUSIVE
 ├─ resolve → UNAVAILABLE
 └─ cancel  → CANCELLED
```

For money-moving primitives account for every unit of value in every terminal state.

Never leave “uncertain” as a permanent fund trap.

If uncertainty can strand value, design:

- bounded retries;
- resubmission;
- appeal;
- timeout;
- neutral refund;
- explicit application handoff.

## 6.6 Immutable evidence vs evolving configuration

When old decisions must remain interpretable:

- do not silently mutate their baseline/specification;
- version it;
- compute a definition fingerprint;
- or create a successor record with lineage.

A downstream consumer should be able to answer:

> “Was this receipt produced against the exact policy/specification I expected?”

For mutable profiles, consider:

```text
spec_version
definition_hash
audited_definition_hash
is_current_spec
freshness
```

## 6.7 Freshness

If a verdict can become stale, make freshness explicit.

Do not make downstream applications guess from timestamps.

Possible machine-readable states:

```text
RELIABLE
STALE
BLOCKED
UNKNOWN
```

or equivalent.

## 6.8 Bound everything

Set explicit maxima for:

- URLs;
- strings;
- source bytes/chars;
- model output;
- criteria;
- probes;
- subscribers;
- history length;
- retry count;
- evidence excerpts;
- rounds;
- indexes.

Use ring buffers or capped histories where appropriate.

Unbounded state is not “more complete”; it is a denial-of-service and cost problem.

---

# 7. DESIGN THE DETERMINISTIC / NONDETERMINISTIC BOUNDARY

This is one of the most important parts of the submission.

## 7.1 Nondeterminism is for irreducible uncertainty

Use GenLayer nondeterminism for things such as:

- live network/web observation;
- interpreting natural-language evidence;
- semantic equivalence;
- fuzzy classification;
- materiality;
- causal reasoning;
- independence/syndication reasoning;
- behavior interpretation.

Do **not** use an LLM for:

- integer thresholds;
- access control;
- URL count;
- string length;
- exact deadlines;
- cooldowns;
- payouts;
- simple hashes;
- enum conversion;
- state transitions;
- ring-buffer indexes;
- exact arithmetic;
- ownership;
- quorum counts once consensus-agreed inputs exist.

## 7.2 The strongest recurring pattern

```text
MODEL / WEB:
“What did we observe?”

DETERMINISTIC CONTRACT:
“What is that observation allowed to do?”
```

The model should not be asked:

> “Should we pay?”

It should be asked:

> “Which criteria did this artifact satisfy?”

Then deterministic code maps criteria/verdict to payment.

## 7.3 Deterministic gates around consensus

Run cheap guards before expensive rounds:

```text
exists?
correct state?
authorized?
not expired?
cooldown elapsed?
input can possibly satisfy minimum?
```

After consensus run deterministic gates again:

```text
known enum?
within range?
minimum evidence count?
quorum floor?
critical failure?
freshness?
settlement invariant?
```

## 7.4 Deterministic heuristic as triage, never false authority

If deterministic similarity, hashing, status codes, or thresholds can cheaply narrow candidates, use them as **triage**.

Do not let a noisy heuristic become the semantic verdict.

Example principle:

```text
cheap deterministic distance -> "worth reviewing"
consensus semantic judgment   -> actual originality verdict
```

If empirical testing shows a heuristic ranks obvious examples incorrectly, that is evidence the heuristic must remain a trigger rather than settlement.

---

# 8. SELECT THE RIGHT CONSENSUS / EQUIVALENCE MECHANISM

Do not use one mechanism everywhere.

## 8.1 `strict_eq`

Appropriate only when the returned value is genuinely stable after normalization.

Possible cases:

- canonical integer derived from deterministic data;
- boolean comparison result;
- sorted/canonical structure whose production is stable.

Do **not** wrap raw LLM prose or raw web responses in strict equality.

## 8.2 Comparative semantic equivalence

Use a comparative principle when independent validators may phrase things differently but must agree on a stable semantic decision.

The principle must state:

1. exact shared task;
2. fields that must agree;
3. allowed differences;
4. differences that are **not** equivalent;
5. how reachability/failure affects equivalence.

Example structure:

```text
Equivalent iff:
- same source reachability class;
- same final verdict enum;
- same decision-critical criterion results;
- same confidence band if the band affects downstream behavior.

Ignore:
- reasoning prose;
- excerpt choice where excerpts are only explanatory;
- whitespace/order/capitalization.

Not equivalent:
- ALLOW vs DENY;
- reachable vs unreachable;
- one validator sees a critical failure and another does not.
```

## 8.3 Multiple rounds

Split rounds when they answer different questions.

Good examples:

```text
ROUND 1: What does each source say?
DETERMINISTIC GATE: Is enough evidence reachable?
ROUND 2: Which sources are independent and what is the result?
```

or:

```text
ROUND 1: Extract canonical semantic snapshot
DETERMINISTIC DIGEST: Did meaning-relevant snapshot change?
ROUND 2: If changed, how material is it?
```

Benefits:

- different equivalence rules per question;
- less cross-contamination;
- early deterministic exits;
- easier reviewer reasoning;
- cheaper unchanged/unreachable paths.

## 8.4 Custom `run_nondet_unsafe`

Use a custom validator when the leader result itself must be treated as adversarial.

Leader:

```text
fetch / observe
classify
return bounded proposal
```

Validator:

```text
verify leader result type
independently fetch / observe
independently classify
check typed fields
reject unknown enum/bit values
compare stable security/decision dimensions
independently ground evidence
return accept/reject
```

The validator must be able to reject a **perfectly well-formed but substantively false leader result**.

If it only checks JSON shape, it is not a meaningful validator.

## 8.5 Same-snapshot discipline

If validators both classify a source and verify excerpts/evidence grounding, use the same independently fetched snapshot for both steps when practical.

Avoid:

```text
fetch A -> classify
fetch B -> verify excerpt
```

where the source may change between A and B.

## 8.6 Leader-result type hardening

For custom validators explicitly reject malformed types.

Common adversarial values:

```text
True where integer expected
1.0 where integer expected
"0x100" where decimal integer expected
unknown enum
unknown bit
negative value
oversized string
missing field
extra security-critical field
list instead of dict
truthy string "true" instead of bool
```

In Python, remember:

```python
isinstance(True, int) == True
```

So use exact/type-aware checks where a boolean must not pass as an integer.

---

# 9. FAILURE SEMANTICS

Failure behavior is part of the protocol, not an afterthought.

## 9.1 Distinguish categories

At minimum distinguish conceptually:

```text
EXPECTED user/state error
EXTERNAL evidence/network failure
TRANSIENT infrastructure failure
LLM/PARSE failure
CONSENSUS disagreement
```

Use deterministic error prefixes/classes if useful to downstream tooling.

## 9.2 Fail closed where positive state is dangerous

Examples:

- unreadable policy → `UNKNOWN`, not `ALLOW`;
- unparseable safety analysis → unsafe/quarantined, not safe;
- unreachable dependency → `UNKNOWN`/`UNAVAILABLE`, not reliable;
- insufficient evidence → `INSUFFICIENT`, not resolved;
- unclear dispute → `UNCLEAR`, not a manufactured winner.

## 9.3 Failed observation must not masquerade as world change

Examples:

- HTTP 503 does not mean a clause was deleted;
- fetch failure does not mean a dependency materially drifted;
- unavailable agent does not mean a behavioral probe semantically failed;
- model parse failure does not imply derivative/plagiarized/noncompliant.

## 9.4 Do not advance snapshots on unsafe classification

If new evidence was observed but the materiality/classification stage failed, consider preserving the old trusted snapshot so the change is not silently swallowed.

## 9.5 GenLayer transaction `UNDETERMINED` vs contract-level `UNDECIDED`

Do not confuse:

- **protocol transaction outcome**: validator consensus could not determine the transaction;
- **contract result enum**: the contract intentionally recorded `UNDECIDED` or `INCONCLUSIVE`.

They are not the same thing.

A protocol-level undetermined transaction normally should not mutate application state as though a contract-level outcome was finalized.

---

# 10. WEB AND EXTERNAL EVIDENCE SECURITY

## 10.1 Treat source content as hostile data

A public web page can contain:

- “ignore previous instructions”;
- fake system/developer messages;
- secret requests;
- tool/action commands;
- encoded instructions;
- invisible/obfuscated content;
- links that ask the model to continue instructions elsewhere.

Never treat fetched text as governing instructions.

## 10.2 Prompt/data framing

Prefer structured framing such as JSON:

```python
payload = json.dumps({
    "task": bounded_task,
    "source": bounded_source,
})
```

Prompt instructions should say that source text is evidence/data and any instructions inside it must not be followed.

Do not interpolate attacker-controlled text into a position that can plausibly become system control.

## 10.3 Bound source content

Cap fetched text before sending it to a model.

Document truncation behavior.

If truncation can hide a decisive fact, design the source-selection/section strategy explicitly.

## 10.4 URL admission

Where the contract accepts arbitrary URLs, consider deterministic rejection of:

- non-HTTPS URLs;
- embedded credentials;
- unexpected ports;
- localhost;
- `.localhost`;
- `.local`;
- `.internal`;
- loopback IPv4;
- private IPv4;
- link-local IPs;
- raw/numeric IP encodings;
- ambiguous leading-zero/legacy IP spellings;
- malformed DNS labels;
- unsupported IPv6/colon hosts if you cannot safely classify them.

These are defense-in-depth. Do not claim a small contract helper provides perfect SSRF prevention; validator/runtime egress policy also matters.

## 10.5 Relative paths for registered origins

For agent/service probes:

- store a validated HTTPS origin;
- require probe paths to be relative;
- reject cross-origin absolute paths.

## 10.6 Multi-source independence

If multiple sources are supposed to corroborate a fact, raw URL count is not independence.

Consider:

- registrable-domain ownership;
- subdomain grouping;
- syndicated/copy relationships;
- one source citing another;
- shared wire copy.

If the independence judgment is semantic, let consensus propose clusters and then deterministically enforce the minimum cluster count.

---

# 11. MODEL OUTPUT HARDENING

## 11.1 Request structured output

Prefer:

```python
gl.nondet.exec_prompt(..., response_format="json")
```

when compatible with the SDK version.

## 11.2 Parse defensively

Use `json.loads`.

Never `eval`.

If model output may contain markdown fences, perform bounded/reasonable fence recovery.

## 11.3 Normalize only what is safe to normalize

Examples:

- enum casing;
- whitespace;
- decimal integer strings;
- bounded notes;
- canonical ordering.

Do not “repair” a semantically invalid verdict into a positive result.

## 11.4 Unknown values fail closed

If the valid verdicts are:

```text
PASS
FAIL
INCONCLUSIVE
```

then:

```text
MAYBE_SUPER_PASS
```

must not accidentally map to PASS.

## 11.5 Diagnostic vs settlement fields

Fine-grained semantic labels may vary honestly between validators.

If downstream security only depends on:

```text
hard-risk present?
literal deterministic floor present?
parser failure?
terminal status?
```

make those the consensus-critical dimensions.

Do not force identical diagnostic prose/categories when it would create unnecessary nondeterminism.

---

# 12. STATE AND STORAGE ENGINEERING

## 12.1 Immutable commitments

Fields that define what is being judged should usually become immutable once the commitment starts.

Examples:

- acceptance specification;
- evidence URL set;
- dispute question;
- initial dependency baseline;
- watch target URL;
- challenge prior-entry reference.

## 12.2 Version mutable definitions

If an owner can update:

- endpoint;
- policy;
- probe set;
- thresholds;
- active state;
- audit interval;

increment a version/fingerprint so old receipts cannot silently validate the new definition.

## 12.3 Bounded histories

Prefer:

- ring buffers;
- capped arrays;
- capped mappings with monotonic IDs;
- pagination/range views.

Never let a single view loop over an unbounded history.

## 12.4 Stable external IDs

Do not expose internal database/vector indexes as long-lived public identity if the underlying storage can reuse indexes.

Maintain your own monotonic protocol IDs.

## 12.5 Copy storage-backed objects before nondeterministic closures

If the SDK requires storage objects to be moved/copied to ordinary memory before nondeterministic execution, do that explicitly using the current supported API.

Do not capture unsupported storage references into a pickled nondeterministic closure.

---

# 13. ECONOMIC / PAYABLE PRIMITIVES

Only include money movement when it is part of the primitive's real value proposition.

Do not add token movement merely to make the contract seem important.

When value is present:

## 13.1 Every terminal state accounts for funds

Write a table:

| Terminal state | Who receives principal | Who receives bonds | Can funds remain stuck? |
|---|---|---|---|

No “TBD”.

## 13.2 Uncertainty cannot manufacture a winner

If evidence is genuinely unclear, the neutral outcome may be:

- retry;
- refund own contributions;
- recover after timeout;
- bounded appeal;
- application-specific escalation.

Do not give money to one party because the model failed to parse.

## 13.3 Checks-effects-interactions

Where transfers/messages occur:

1. validate;
2. update state to prevent replay;
3. then transfer/emit/call.

Never leave a double-settlement window.

## 13.4 Verify `gl.message.value`

Test:

- zero;
- exact minimum;
- underpayment;
- overpayment if exact amount required;
- refunds;
- repeated claim;
- unauthorized sender.

## 13.5 Address types on real network

Do not assume a value that looked like an `Address` in a hand-built unit test will be the exact runtime type on real calldata.

Run real-network payable and recipient paths.

Normalize/coerce only through SDK-supported address handling.

## 13.6 Cross-contract writes may be asynchronous

Do not assume a cross-contract write returns a synchronously usable ID unless the GenLayer message model explicitly guarantees it.

For composition, often:

```text
emit/write to shared primitive
then later read/bind the created record
```

is safer than pretending an asynchronous write returned a synchronous local result.

---

# 14. IMPLEMENTATION REPOSITORY SHAPE

A strong default:

```text
contracts/
  <primitive>.py

tests/
  direct/
    test_<primitive>.py
    test_<primitive>_hardening.py
  integration/
    test_<primitive>_studionet.py

fixtures/
  <only if live public fixtures are useful>

scripts/
  preflight.py                 # optional
  deploy_studionet.py          # optional

docs/
  CONSENSUS.md
  SECURITY.md
  INTEGRATION.md
  DEPLOYMENT.md

DECISION.md
SUBMISSION.md
README.md
gltest.config.yaml
requirements-test.txt
requirements.txt
.gitignore
LICENSE
```

Do not create empty directories/files merely to match this layout.

---

# 15. WRITE THE CONTRACT

## 15.1 Start from the current SDK generation

Inspect current official starter contracts and the repository's dependency header.

Do not blindly copy an old `py-genlayer`/GenVM version.

## 15.2 Type public interfaces

Type:

- write arguments;
- view arguments;
- return values;
- storage fields.

Use SDK-supported primitive/collection types.

## 15.3 No normal Python nondeterminism

Do not use ordinary:

```python
time.time()
random.random()
requests.get()
os.urandom()
```

inside contract logic.

Use GenLayer's supported transaction context and nondeterministic APIs.

The linter should catch forbidden patterns, but design correctly first.

## 15.4 Keep helpers auditable

Good helper categories:

```text
_validate_*
_parse_*
_normalize_*
_derive_*
_bound_*
_digest_*
_classify_*
_consensus_*
```

Avoid one 800-line public write method.

## 15.5 Public views are part of the product

A reusable primitive needs downstream-friendly views such as:

```text
get_record
latest_verdict
is_consumable
is_allowed
get_reliance_status
verdict
definition_hash
is_fresh
```

Do not force consumers to reimplement protocol semantics from raw storage fields.

---

# 16. DIRECT MODE TESTING

Direct Mode is the fast adversarial development loop.

## 16.1 Environment

Create a clean Python 3.12+ virtual environment using the platform's correct command.

Windows example:

```powershell
py -3.12 -m venv .venv-test
.\.venv-test\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-test.txt
```

POSIX example:

```bash
python3.12 -m venv .venv-test
source .venv-test/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-test.txt
```

If dependency pins conflict, inspect:

- contract SDK header;
- `genlayer-test` requirements;
- currently installed `genlayer-py`;
- official compatibility guidance.

Do not force an old `genlayer-py` pin just because another repository used it.

## 16.2 Turn on pickling checks

Where supported:

```python
direct_vm.check_pickling = True
```

This catches closures/state that work in ordinary Python but fail under GenVM serialization.

## 16.3 Test the public surface

At minimum:

- constructor;
- every public write;
- every public view;
- ownership;
- state transitions;
- terminal-state replay;
- IDs/counters;
- independent records;
- invalid record IDs;
- boundaries;
- max lengths/counts;
- cooldown/deadline boundaries;
- cancellation;
- retries;
- activation/deactivation;
- stale/fresh;
- version/fingerprint behavior.

## 16.4 Test every contract-level verdict

If statuses include:

```text
SUCCESS
NEGATIVE
INCONCLUSIVE
UNAVAILABLE
CANCELLED
```

test every one.

## 16.5 Mock nondeterminism, not the contract itself

Use Direct Mode web/LLM mocks to exercise the real resolution code.

Do not monkeypatch `resolve()` to return the answer you wanted.

## 16.6 Adversarial output parsing

Inject:

- malformed JSON;
- fenced JSON;
- missing keys;
- extra keys;
- wrong enum;
- empty string;
- oversized reason;
- negative number;
- float;
- boolean-as-integer;
- hex integer;
- unknown mask bit;
- duplicated criterion;
- reordered source list;
- invented URL;
- missing requested URL.

Assert fail-closed behavior and state integrity.

## 16.7 Custom validator: forged-leader testing

If using `run_nondet_unsafe`, use Direct Mode's validator-running helper when supported:

```text
direct_vm.run_validator(...)
```

Feed a forged leader result directly.

Test cases should prove a leader cannot:

- claim SAFE when validator sees risk;
- claim reachable when validator cannot fetch;
- invent an excerpt;
- alter an ID;
- smuggle unknown enum values;
- use truthy strings instead of booleans;
- use float where integer is required;
- claim a passing criterion the validator independently sees failing;
- omit a critical field and still pass.

This is one of the strongest pieces of evidence that the validator is substantive.

## 16.8 No test-order dependence

Each test must be runnable alone.

Never rely on:

```python
capsule_id = 3
```

because test 1 and test 2 happened to create IDs 1 and 2.

Use:

- fresh/function-scoped deployment;
- returned IDs;
- state-derived IDs;
- explicit fixtures that guarantee state.

## 16.9 Test false-positive prevention

Always assert setup transactions/actions actually succeeded.

A test can “pass” for the wrong reason if:

- registration reverted;
- state was never created;
- later view returned a default that happened to satisfy the assertion.

For every load-bearing setup write:

```text
assert transaction succeeded
then assert state was created
then test the target property
```

## 16.10 Final Direct Mode command

Use the command appropriate to the repository, normally:

```bash
pytest tests/direct/ -v -s
```

Record:

```text
collected
passed
failed
skipped
duration
Python version
genlayer-test version
```

---

# 17. WINDOWS DIRECT MODE: KNOWN TEMPFILE/UNLINK FAILURE PATH

This deserves a dedicated diagnostic because it can fail **before the contract executes**.

A known historical environment:

```text
Windows
Python 3.12.13
genlayer-test 0.29.2
```

produced a Windows tempfile cleanup/unlink error similar to:

```text
PermissionError: [WinError 32]
The process cannot access the file because it is being used by another process
```

inside the Direct Mode loader, before the contract loaded.

A successful historical route used an **external, uncommitted pytest runtime plugin** and invoked:

```bash
pytest tests/direct/ -v -s -p runtime_plugin
```

The plugin deferred the offending Windows fd/tempfile unlink cleanup.

Important:

- this was a harness workaround;
- the contract was not modified;
- Python was not changed to “fix” the contract;
- the `genlayer-test` package was not committed as a patched fork;
- the local shim was not committed;
- the literal historical plugin source was not preserved.

Therefore, if the **same** failure appears:

1. prove it occurs before contract execution;
2. inspect the currently installed `genlayer-test` loader source;
3. check whether a newer compatible official release already fixes it;
4. if current compatibility requires the affected version, implement the narrowest test-runtime/local workaround that defers the invalid cleanup;
5. do **not** globally monkeypatch all file deletion;
6. do **not** change contract logic to fix an OS cleanup bug;
7. keep the workaround external/uncommitted unless a clean scoped test-only compatibility hook is genuinely worth sharing;
8. report normal tests separately from the host workaround.

Do not claim “Direct Mode passed natively without workaround” if it did not.

---

# 18. OPTIONAL ZERO-DEPENDENCY PREFLIGHT

A small `scripts/preflight.py` can be useful if it verifies source invariants without requiring GenLayer packages.

It must not replace Direct Mode or the GenVM linter.

Possible checks:

- one canonical deployable contract;
- dependency header present;
- expected public methods;
- no forbidden imports;
- nondeterminism only in intended methods;
- known enum values;
- validator function exists;
- source bounds;
- deterministic status derivation helper;
- no obvious side effects inside nondeterministic closure.

Output a real count:

```text
74/74 PASS
```

only if exactly 74 assertions ran and passed.

---

# 19. GENVM LINTER AND SDK VALIDATION

## 19.1 Use a separate clean linter environment when useful

Windows:

```powershell
py -3.12 -m venv .venv-lint
.\.venv-lint\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install genvm-linter
genvm-lint --version
```

POSIX:

```bash
python3.12 -m venv .venv-lint
source .venv-lint/bin/activate
python -m pip install --upgrade pip
python -m pip install genvm-linter
genvm-lint --version
```

If the repository has a verified compatible linter pin, use it.

Otherwise check the current published version/current docs.

## 19.2 Run AST lint

```bash
genvm-lint lint contracts/<primitive>.py
```

## 19.3 Run full SDK validation

```bash
genvm-lint check contracts/<primitive>.py
genvm-lint check contracts/<primitive>.py --json
```

Useful auxiliary commands when needed:

```bash
genvm-lint validate contracts/<primitive>.py
genvm-lint setup --contract contracts/<primitive>.py
genvm-lint download
genvm-lint schema contracts/<primitive>.py
genvm-lint typecheck contracts/<primitive>.py
```

## 19.4 Interpret exit codes correctly

Current documented semantics should be checked, but historically/currently:

```text
0 success
1 lint or validation failure
2 contract file not found
3 SDK download failure
```

An SDK download error is not evidence that the contract is invalid.

A genuine AST/SDK contract error **is** a contract issue.

## 19.5 If linter requires contract changes

Record the pre-lint source commit.

Make the minimum correct code fix.

Then rerun:

1. preflight;
2. Direct Mode;
3. pickling;
4. linter;
5. any deterministic compilation checks.

Any previous network deployment now corresponds to old source and cannot be presented as current-source runtime proof.

Plan a fresh canonical deployment after local gates are green.

## 19.6 Typecheck is supplemental

Fix genuine type problems.

Do not block a valid submission indefinitely because an optional Pyright pass cannot resolve GenLayer SDK stubs while primary `lint` and `validate` are green.

Document that distinction accurately.

---

# 20. COMMIT THE GREEN CONTRACT SOURCE BEFORE CANONICAL DEPLOYMENT

Once the **contract code** is locally green:

```bash
git status --short
git diff
git add contracts tests scripts requirements*.txt gltest.config.yaml docs README.md DECISION.md SUBMISSION.md
git commit -m "feat: complete reusable GenLayer primitive"
git push origin <default-branch>
```

Use smaller commits if work naturally separates.

Record:

```bash
git rev-parse HEAD
git rev-parse HEAD:contracts/<primitive>.py
```

The second command gives the Git blob SHA of the deployable contract at that commit.

This commit becomes the candidate deployment-source commit.

---

# 21. GENLAYER CLI SETUP

## 21.1 Install/verify CLI

Current general route:

```bash
npm install -g genlayer
genlayer --version
genlayer --help
```

Record the actual version.

Do not assume an older repository's CLI syntax if `--help` differs.

## 21.2 Select/check Studionet

Current Studionet:

```text
GenLayer RPC: https://studio.genlayer.com/api
Chain ID: 61999
Currency: GEN
Explorer: https://explorer-studio.genlayer.com
```

Depending on the installed CLI generation, use its current documented network selector, for example:

```bash
genlayer network studionet
```

or the current `network set` form if shown by:

```bash
genlayer network --help
```

Then inspect:

```bash
genlayer config get
```

or the current equivalent.

---

# 22. GENLAYER CLI ACCOUNT / WALLET ROUTES

The agent must not get stuck just because one old encrypted account is unusable.

## 22.1 Inspect existing accounts

Run:

```bash
genlayer account --help
genlayer account list
```

For each candidate account, inspect only public information:

```bash
genlayer account show --account <name> --rpc https://studio.genlayer.com/api
```

## 22.2 Use an existing account whose password is known interactively

Select it using the current CLI syntax, commonly:

```bash
genlayer account use <name>
```

Unlock:

```bash
genlayer account unlock --account <name>
```

Enter the password interactively.

Unlock caches the private key in the OS keychain where supported.

Do not include `--password <plaintext>` in scripts/logged commands unless the user explicitly provisioned a secure noninteractive mechanism.

## 22.3 Existing encrypted account but password unavailable

Do **not**:

- guess indefinitely;
- extract private key by bypassing encryption;
- ask the user to paste secrets into chat;
- commit the keystore.

Instead choose one of:

### Route A — create a fresh dedicated signer

```bash
genlayer account create --name <project>-deployer
```

Let the CLI prompt interactively for a keystore password.

Then:

```bash
genlayer account use <project>-deployer
genlayer account unlock --account <project>-deployer
genlayer account show --account <project>-deployer --rpc https://studio.genlayer.com/api
```

Store only the **public address** in deployment docs.

### Route B — Studio Mode default/generated Studionet account

For test/development deployment, use:

```python
from gltest import get_contract_factory, get_default_account

factory = get_contract_factory(
    contract_file_path="contracts/<primitive>.py"
)

contract = factory.deploy(
    account=get_default_account(),
    consensus_max_rotations=3,
)
```

Studionet test configuration can provide generated/default accounts.

This avoids dependency on a forgotten CLI-keystore password.

It does **not** bypass a machine/network socket block.

## 22.4 Import an existing wallet only if legitimately available

Current CLI supports importing from a keystore or private key.

Prefer keystore file:

```bash
genlayer account import --name <name> --keystore <secure-path>
```

Let source/new passwords be entered interactively where possible.

Avoid:

```text
--private-key <secret>
--password <secret>
--source-password <secret>
```

in logged commands.

Use a direct private-key import only if the user has explicitly and securely provisioned the key locally and accepts the risk.

Never echo it.

## 22.5 Funding

Check public balance:

```bash
genlayer account show --account <name> --rpc https://studio.genlayer.com/api
```

If the network requires funds, use the official Studionet faucet/current funding mechanism.

Do not fabricate a balance requirement.

Do not claim deployment is impossible solely because a local CLI account shows zero until you test the current Studionet development flow.

---

# 23. STUDIONET CONNECTIVITY PRECHECK

Before debugging contract deployment, prove the process can open a TLS connection to:

```text
https://studio.genlayer.com/api
```

## 23.1 Windows

```powershell
Test-NetConnection studio.genlayer.com -Port 443
curl.exe -I https://studio.genlayer.com/api
```

A 400/404/405 HTTP response can still prove the socket/TLS path works; the goal here is transport, not a valid RPC call.

Test the relevant runtimes separately if needed:

```powershell
python -c "import socket; s=socket.create_connection(('studio.genlayer.com',443),10); print(s.getpeername()); s.close()"
```

```powershell
node -e "fetch('https://studio.genlayer.com/api').then(r=>console.log(r.status)).catch(e=>{console.error(e);process.exit(1)})"
```

Check proxy configuration if relevant:

```powershell
netsh winhttp show proxy
```

## 23.2 `WinError 10013`

If Python/CLI reports:

```text
WinError 10013
```

at socket creation **before a transaction hash exists**, classify it as an OS/network/process-access problem, not a contract error.

Determine:

- Does `Test-NetConnection` pass?
- Does `curl.exe` pass?
- Does Node pass?
- Does Python fail only?
- Does `genlayer` CLI pass?
- Is a proxy configured?
- Is antivirus/application control blocking one executable?
- Is Windows Firewall blocking that process?
- Is the environment sandbox itself denying outbound sockets?

Do not disable Windows Firewall globally.

Do not weaken endpoint security broadly.

If one official process is allowed and another is blocked, use the working official route for the tasks it can perform while seeking a narrow, legitimate process/network fix for the blocked test route.

If **all** processes are blocked by system policy, report the exact connectivity evidence. There is no contract-code change that can fix a socket ACL.

## 23.3 Do not confuse transport with signing

These are separate:

```text
Can process reach RPC?
Can account sign?
Does account have needed funds?
Does deployment transaction execute?
Does consensus finalize?
```

Diagnose them in that order.

---

# 24. CANONICAL STUDIONET DEPLOYMENT

Deploy only after the contract source is locally green and committed.

Two valid routes exist.

## 24.1 Route A — GenLayer CLI

Verify account/network:

```bash
genlayer account list
genlayer account show --account <deployer> --rpc https://studio.genlayer.com/api
```

Deploy:

```bash
genlayer deploy --contract contracts/<primitive>.py --rpc https://studio.genlayer.com/api
```

Add constructor arguments only if actually required and use current CLI syntax.

Capture:

```text
deployer public address
deployment transaction hash
contract address
initial transaction status
```

Inspect:

```bash
genlayer receipt <deploy-tx>
genlayer trace <deploy-tx>
genlayer schema <contract-address>
genlayer code <contract-address>
```

Use the exact options shown by current CLI `--help`.

## 24.2 Route B — `genlayer-test` Studio Mode

Create a small deployment/evidence script or integration fixture using:

```python
from gltest import get_contract_factory, get_default_account

factory = get_contract_factory(
    contract_file_path="contracts/<primitive>.py"
)

contract = factory.deploy(
    args=[...],                         # only if constructor needs args
    account=get_default_account(),
    consensus_max_rotations=3,
    wait_interval=10000,
    wait_retries=20,
)
```

Use the exact API supported by the installed version.

Capture:

```text
generated/default deployer public address
contract address
deployment receipt/transaction
```

Do not expose generated private keys.

## 24.3 Canonical vs disposable deployments

Integration tests may create many disposable contracts.

Pick one canonical deployment for the contribution and document it.

Do not replace the canonical address every time an integration test runs.

## 24.4 Finality language

Understand transaction lifecycle.

Do not write:

```text
FINALIZED / MAJORITY_AGREE
```

because deployment returned without raising.

Inspect the receipt/status.

If only ACCEPTED, document ACCEPTED.

If it later becomes FINALIZED, update the evidence.

Use protocol finalization commands only when they are appropriate for the actual transaction state; do not blindly “force finalization”.

---

# 25. PAYABLE WRITE TOOLING

Before scripting native-value writes, inspect current CLI:

```bash
genlayer write --help
```

Historically, at least one CLI generation exposed gas/fee value but did not provide the needed native `gl.message.value` path for a payable contract write.

If the current CLI still lacks a correct native-value option, use a supported SDK route:

## Studio Mode / genlayer-test

```python
receipt = contract.some_payable_write(args=[...]).transact(
    value=<amount>,
    account=<account>,
    consensus_max_rotations=3,
)
```

## GenLayerJS

Use the current `writeContract` API with its native `value` parameter.

Never fake a payable path by directly mutating balance/storage in the live evidence script.

---

# 26. LIVE RUNTIME SMOKE EVIDENCE

Deployment alone is not enough.

Exercise the primitive's meaningful behavior on the canonical deployment.

Choose scenarios that actually prove the thesis.

At minimum:

## Case A — normal/success path

Examples:

```text
SAFE
ALLOW
UP
UNCHANGED
CONFORMANT
ACCEPTED
RESOLVED
ORIGINAL
```

depending on primitive.

## Case B — adversarial/negative/fail-closed path

Examples:

```text
QUARANTINED
DENY
DOWN
MATERIAL_DRIFT
BREACHED
REJECTED
CONTRADICTED
DERIVATIVE
```

## Case C — lifecycle/recovery path

Examples:

```text
cancel
retry
UNAVAILABLE
UNDECIDED
fallback refund
appeal
deactivate/reactivate
successor
stale result
transfer ownership
```

Pick what is native to the primitive.

## 26.1 Assert state, not just receipt status

For every smoke transaction:

1. assert receipt succeeded;
2. read the relevant view;
3. assert the expected stored state;
4. assert the downstream convenience gate;
5. record transaction hash.

## 26.2 Stable assertions

Do not assert exact LLM prose unless exact prose is genuinely a contract invariant.

Prefer:

```text
status
verdict
critical bit
criterion result
risk present
is_consumable
is_allowed
is_fresh
balance/payout
```

## 26.3 Public fixtures

If a deterministic hostile/material/negative public source is needed, add a small fixture under `fixtures/` and expose it through raw GitHub.

Be careful with timing:

A fixture committed locally is not available at the `raw.githubusercontent.com/.../main/...` URL until it is pushed.

If integration tests depend on it:

1. commit/push fixture first;
2. verify URL;
3. then execute live tests.

## 26.4 Web instability

For safe cases, choose stable public sources.

Do not use a page whose content constantly changes if your test expects a stable semantic result.

## 26.5 Consensus variability

If an honest validator can vary on diagnostic categories, assert only settlement-critical dimensions.

Do not weaken the test so much that anything passes; assert the primitive's actual guarantee.

---

# 27. COMMITTED STUDIONET INTEGRATION TESTS

The final repository should contain a small real-network suite.

Suggested path:

```text
tests/integration/test_<primitive>_studionet.py
```

## 27.1 What integration proves

Direct Mode proves logic under controlled nondeterminism.

Studionet integration should prove:

- real contract deployment;
- real RPC path;
- real validators;
- real consensus;
- real web/model execution where relevant;
- persistent state;
- live success path;
- live negative path;
- meaningful lifecycle behavior.

## 27.2 Use official Studio Mode helpers

Typical pattern:

```python
from gltest import get_contract_factory, get_default_account
from gltest.assertions import tx_execution_succeeded

factory = get_contract_factory(
    contract_file_path="contracts/<primitive>.py"
)

contract = factory.deploy(
    account=get_default_account(),
    consensus_max_rotations=3,
)
```

Use current API signatures.

## 27.3 Keep the integration suite small

Aim for roughly 3–5 high-signal tests, not the full Direct Mode matrix.

Possible structure:

```text
test_deploy_and_public_surface
test_success_path
test_negative_fail_closed_path
test_cancel_or_recovery_path
```

## 27.4 Tests must be independently runnable

Prefer a fresh/function-scoped deployment for each behavioral test if that makes state isolation reliable.

Do not rely on pytest ordering.

Run the whole suite:

```bash
gltest tests/integration/ -v -s --network studionet
```

Then run important behavioral tests individually.

Record both results.

## 27.5 Do not use leader-only for final consensus proof

`--leader-only` can be useful for debugging/speed.

It is **not** equivalent to proving validator consensus.

The final contribution evidence must include real consensus execution.

---

# 28. SOURCE PARITY: PROVE THE DEPLOYED CONTRACT IS THE CONTRACT IN `main`

This is mandatory for credible deployment evidence.

Record:

```text
DEPLOYMENT_SOURCE_COMMIT
CONTRACT_PATH
DEPLOYMENT_CONTRACT_BLOB_SHA
CANONICAL_ADDRESS
DEPLOY_TX
```

Get the deployment-source blob:

```bash
git rev-parse <deployment-source-sha>:contracts/<primitive>.py
```

Get current-main blob:

```bash
git rev-parse HEAD:contracts/<primitive>.py
```

If the SHAs match:

> The deployable contract is byte-identical to the canonical deployment source.

Later commits may safely change:

- tests;
- tooling dependencies;
- fixtures;
- docs;

without requiring redeployment **if the contract blob remains identical**.

Use accurate wording:

> `contracts/<primitive>.py` has not changed since the deployment source commit. Subsequent commits affect only tests, tooling dependencies, fixtures, and documentation; the deployable contract source remains byte-identical.

Do not write “later commits are docs only” if you also changed tests or requirements.

## 28.1 If contract bytes change after deployment

Immediately mark old deployment evidence historical.

Rerun:

- preflight;
- Direct Mode;
- pickling;
- linter;
- canonical deployment;
- live smoke;
- source parity.

Old transactions can remain documented as history, but must not be described as runtime proof for the current source.

---

# 29. POST-DEPLOYMENT COLD TEST

After all contract-changing fixes are over, run the entire applicable gate set one more time.

Example matrix:

```text
source preflight             PASS
Python compile               PASS
Direct Mode                  N/N
pickling                     PASS
GenVM AST lint               PASS
GenVM SDK validate           PASS
integration suite            N/N
individual integration       N/N
canonical deployment         FINALIZED / actual consensus
success live path            verified
negative live path           verified
recovery/lifecycle path      verified
contract blob parity         MATCH
```

If a row cannot be truthfully filled, it is not green.

---

# 30. README: THE 30-SECOND REVIEWER TEST

The top of README should answer, quickly:

1. What is this primitive?
2. Who calls it?
3. What does it decide?
4. Why does GenLayer need to decide it?
5. What is the live contract address?
6. What tests are green?

Then explain deeply.

Recommended content:

## Thesis

One sentence.

## Canonical deployment

Table:

```text
Network
Contract
Explorer
Deployment tx
Finality/status
Consensus result
Deployment source commit
Current source parity
```

## Problem

The repeated trust problem.

## Why GenLayer

Counterfactual table:

```text
off-chain operator -> trusted authority
single LLM -> trusted reporter
deterministic parser -> cannot answer semantic question
normal oracle -> wrong data type/problem
```

## Delete GenLayer: what breaks?

One explicit paragraph/table.

## Why this is not a rejected pattern

Address:

- thin LLM wrapper;
- generic AI app;
- format-only validator;
- caller-authored evidence;
- toy storage;
- full application.

## State machine

## Contract surface

## Nondeterministic operations

For each:

```text
call
where
why irreducibly nondeterministic
```

## Deterministic responsibilities

List the much larger deterministic surface.

## Equivalence/validator design

Exact stable fields.

## Safety/failure semantics

## Reuse surface

Show smallest possible consumer interface.

## Limitations

Be explicit.

Examples:

- not legal advice;
- not proof of absolute truth;
- honest-majority/validator assumptions;
- web availability;
- semantic labels may vary;
- bounded history;
- no perfect SSRF/prompt-injection guarantee;
- testnet/Studionet deployment, not production audit.

## Verification

Exact commands and results.

## Reviewer fast path

Commands a reviewer can copy.

---

# 31. `docs/CONSENSUS.md`

This document must answer:

## 31.1 Exact nondeterministic calls

For each call:

- what data enters;
- what output comes back;
- why deterministic code cannot replace it.

## 31.2 Leader behavior

Exact steps.

## 31.3 Validator behavior

Exact independent steps.

## 31.4 Equivalence

What must match?

What may differ?

Why?

## 31.5 Forged-leader defense

If custom validator:

- type checks;
- independent recomputation;
- source grounding;
- stable dimensions;
- malformed result rejection.

## 31.6 Failure

How are:

- unreachable source;
- parse failure;
- model failure;
- validator disagreement;
- protocol undetermined;

handled?

## 31.7 Why consensus is load-bearing

State precisely:

> Remove consensus → what input/state does deterministic code no longer have?

---

# 32. `docs/SECURITY.md`

Include a threat model.

## Assets

What is protected?

Examples:

- funds;
- permission verdict;
- trusted evidence;
- reputation;
- audit receipt;
- change event;
- challenge result.

## Actors

- caller;
- owner;
- provider;
- counterparty;
- source owner;
- malicious web page;
- malicious leader;
- honest validator;
- malicious validator minority;
- downstream consumer.

## Trust assumptions

List them.

## Input attacks

- malformed URL;
- oversized text;
- prompt injection;
- forged semantic output;
- reentrancy/message ordering if relevant;
- state replay;
- stale evidence;
- duplicated source;
- ambiguous address.

## Fail-open/fail-closed policy

State every safety-critical default.

## Limitations

Do not promise perfect security.

---

# 33. `docs/INTEGRATION.md`

Show how another Intelligent Contract uses the primitive.

Prefer:

```python
@gl.contract_interface
class IPrimitive:
    class View:
        def latest_verdict(...): ...
        # or is_allowed/is_consumable/etc.
```

Then:

```python
result = IPrimitive(address).view().latest_verdict(id)

if not result["safe_condition"]:
    raise gl.vm.UserError("EXPECTED: primitive gate not satisfied")
```

The consumer should not need:

- web access;
- LLM prompts;
- equivalence principles;
- internal risk parsing.

That is how you prove reuse.

Do not add a second executable contract unless the composition behavior itself needs real runtime proof.

---

# 34. `docs/DEPLOYMENT.md`

Record exact canonical evidence:

```text
Date
Network
RPC
Chain ID
CLI/test SDK versions
Python version
Deployment method
Deployer public address
Deployment source commit
Contract blob SHA
Canonical contract address
Explorer URL
Deployment tx
Deployment lifecycle/finality
Consensus result
```

Then a transaction table:

| Scenario | Action | Tx | Stored result |
|---|---|---|---|
| success | ... | ... | ... |
| negative | ... | ... | ... |
| lifecycle | ... | ... | ... |

Also record:

- integration suite result;
- source parity;
- disposable test deployments are not the canonical deployment.

---

# 35. `SUBMISSION.md`

Make this copy-ready.

Include:

```text
Category
Title
One-line thesis
Repository
Canonical Studionet address
Explorer URL
Deployment tx
Deployment source
Why GenLayer is required
Consensus mechanism
Deterministic responsibilities
Failure policy
Reuse surface
Test results
Live evidence
Limitations
Reviewer fast path
```

Also produce a portal-length description under the current character limit.

If the portal currently permits 1000 characters, keep a verified version under 1000.

Example structure:

> `<Name>` is a standalone GenLayer Intelligent Contract that `<exact primitive>`. Validators independently `<fetch/observe/judge>`, while deterministic contract logic `<derive/gate/store>`. It exposes `<stable interface>` for downstream contracts. Verified with `<Direct count>` Direct Mode tests, GenVM lint/SDK validation, `<integration count>` live Studionet integration tests, and a `<finalized status>` Studionet deployment.

Only include counts/statuses actually verified.

---

# 36. EXPLORER EVIDENCE FOR THE CONTRIBUTION PORTAL

The contribution portal may require a URL it recognizes specifically as:

```text
genlayer-explorer-contract
```

For a Studionet contract use:

```text
https://explorer-studio.genlayer.com/address/<CANONICAL_CONTRACT_ADDRESS>
```

This is different from:

- GitHub repository URL;
- Studio import URL;
- transaction URL;
- README deployment section.

If the form says:

```text
Missing required evidence. Provide a URL for:
(genlayer-explorer-contract)
```

supply the **contract-address Explorer URL**.

Add the GitHub repository and deployment document as additional evidence when the portal allows multiple links.

---

# 37. GIT COMMIT AND PUSH DISCIPLINE

Use commits that say what changed.

Examples:

```text
feat: implement consensus-backed primitive
fix: fail closed on malformed consensus output
test: add forged-leader validation coverage
test: add reproducible Studionet integration coverage
docs: record canonical deployment evidence
docs: finalize reviewer submission notes
chore: pin verified GenLayer tooling dependencies
```

Before every push:

```bash
git status --short
git diff --check
```

Push normally:

```bash
git push origin <default-branch>
```

Never force-push by default.

At the end:

```bash
git status --short
git rev-parse HEAD
git log -1 --oneline
git remote -v
```

Working tree must be clean.

---

# 38. DEPENDENCY HYGIENE

Use separate dependency intent where helpful:

```text
requirements-test.txt
requirements.txt
```

Do not pin unnecessary packages.

Do not pin `genlayer-py` to an incompatible version when `genlayer-test` already resolves a compatible range.

Pin a verified `genvm-linter` version only after it has actually passed for this contract/environment.

If current official tooling changed, update to the currently compatible path and document the actual version.

Do not leave a stale Git dependency if the successful verification used a published package instead.

---

# 39. `.gitignore` / SECRET SCAN

At minimum consider:

```text
.venv/
.venv-*/
__pycache__/
.pytest_cache/
*.pyc
.env
.env.*
!.env.example
artifacts/
dist/
build/
coverage/
.DS_Store
```

Do not ignore files that the reviewer actually needs.

Search before final push:

```bash
git grep -n -i "private.key\|mnemonic\|seed phrase\|password\|gh_token\|github_token"
```

Inspect hits manually; docs may legitimately contain the word “password”.

Also inspect:

```bash
git status --ignored
```

Never commit GenLayer keystore directories or OS-keychain exports.

---

# 40. DO NOT ADD CI FOR DECORATION

CI is optional.

For this submission, a real local test matrix plus committed Studionet integration tests and live transaction proof can be stronger than a decorative workflow that cannot run GenVM correctly.

If CI already exists:

- keep it if it is meaningful and green;
- fix genuine problems;
- remove it only if it is unsupported noise and its removal is justified.

Do not add GitHub Actions merely to get a badge.

---

# 41. REVIEWER-QUALITY DESIGN LESSONS TO APPLY

These are reusable engineering lessons, not code templates.

## 41.1 Corroboration

Multiple URLs are not necessarily multiple sources.

Separate:

```text
what each source says
```

from:

```text
which sources are actually independent
```

Then apply a deterministic quorum floor to consensus-agreed clusters.

## 41.2 Semantic watching

Byte changes are not material changes.

Canonicalize meaning, stabilize it against prior agreed state, and test the canonical **digest**, not only the absence of false events.

If keys are stable but values paraphrase every round, the digest gate is still broken.

## 41.3 Policy gates

Positive permission should require strong evidence.

Ambiguity/low confidence can safely downgrade:

```text
ALLOW -> REVIEW
```

rather than silently grant permission.

## 41.4 Uptime/service health

HTTP `200` is not necessarily healthy.

Deterministically verify status expectations, then use semantic judgment only where body meaning matters.

## 41.5 Dependency safety

If a baseline changes legitimately, do not rewrite history.

Create a version/successor so old reviews retain meaning.

Expose freshness-aware reliance, not only a raw last verdict.

## 41.6 Acceptance escrow

`UNDECIDED` is a valid protocol state.

A robust reusable primitive gives it bounded recovery rather than stranding funds.

## 41.7 Appeals

Appeals should have:

- who may appeal;
- cost;
- window;
- maximum rounds;
- terminal handling of ambiguity.

Otherwise an appeal mechanism can become infinite griefing.

## 41.8 Originality/similarity

Cheap deterministic similarity may be useful to triage.

Do not confuse similarity distance with semantic derivation.

Empirically test heuristics before trusting thresholds.

## 41.9 Evidence firewall

A source can contain both useful evidence and instructions aimed at the model.

Independently re-observe, classify, and ground released excerpts.

## 41.10 Behavioral conformance

Being online is not the same as behaving according to specification.

Bind audit receipts to the exact version/fingerprint of the behavior definition so an owner cannot weaken the policy after a trusted audit and still satisfy consumers expecting the original policy.

---

# 42. COMMON BLOCKERS AND EXACT DIAGNOSTIC ORDER

## 42.1 Direct Mode fails before contract load

Symptoms:

```text
Windows tempfile unlink
WinError 32
loader stack
no contract frame
```

Action:

1. classify as host harness;
2. reproduce minimal;
3. inspect installed test package;
4. check compatible current release;
5. use narrow test-only/runtime shim if needed;
6. keep contract unchanged;
7. rerun actual tests;
8. record workaround honestly.

## 42.2 Direct tests fail inside contract

Action:

1. identify exact invariant;
2. fix contract/test;
3. rerun focused test;
4. rerun whole Direct suite;
5. rerun pickling;
6. rerun linter.

## 42.3 GenVM lint exit 3

SDK download/tooling problem.

Do not edit working contract logic randomly.

Check:

- network;
- SDK header;
- linter cache;
- `genvm-lint download`;
- `genvm-lint setup --contract`.

## 42.4 Studionet `WinError 10013`

Socket/policy denial before transaction.

Run process-specific connectivity matrix.

Do not edit contract.

Do not call it a failed deployment until a transaction was submitted.

## 42.5 CLI account locked and password unavailable

Do not extract secret.

Use:

```text
new encrypted dedicated signer
```

or:

```text
Studio Mode get_default_account()
```

for development deployment.

## 42.6 CLI account balance zero

Inspect current Studionet/faucet behavior.

Do not assume zero balance blocks all development operations without testing current network behavior.

## 42.7 Transaction stays ACCEPTED

Inspect receipt and consensus lifecycle.

Do not rewrite docs to FINALIZED.

Wait/poll/finalize only through supported protocol behavior.

## 42.8 `UNDETERMINED`

Determine whether:

- honest model disagreement;
- unstable source;
- brittle equivalence;
- validator/network issue.

Do not widen equivalence until unsafe answers “agree”.

Retry when retry is safe and normal.

## 42.9 Exact prose makes live test flaky

Assert stable semantic fields.

Do not assert identical LLM sentences.

## 42.10 Raw GitHub fixture returns 404

Confirm fixture is pushed to the branch referenced by the URL.

## 42.11 Payable write silently reverts

Assert the write receipt before continuing.

Confirm native `value` was actually sent.

Never treat a later default view as proof setup succeeded.

## 42.12 Cross-contract call behaves differently live

Inspect asynchronous message semantics and address types.

Do not assume synchronous EVM-style returns.

## 42.13 Deployed source mismatch

Stop.

Identify the exact commit that deployed.

If current contract differs, redeploy current source and refresh evidence.

---

# 43. FINAL COLD AUDIT

Pretend you are a skeptical GenLayer reviewer.

Ask:

## Idea

- Is this actually new?
- Is it a primitive or a one-off app?
- Can three unrelated consumers use it?
- Does it overlap the owner's existing submissions?

## GenLayer fit

- What exact decision needs judgment?
- Can validators independently verify the evidence?
- What does GenLayer add beyond one trusted backend?
- What breaks if GenLayer is removed?

## Consensus

- What does the leader do?
- What do validators independently do?
- Can a well-formed wrong leader result be rejected?
- Is equivalence about substance, not JSON shape?
- Is strict equality being used on unstable nondeterminism?
- Are multiple rounds separated when they answer different questions?

## Deterministic safety

- Does the model ever directly choose money movement?
- Are all thresholds/permissions/state transitions deterministic?
- Are critical floors rechecked after consensus?
- Are failures fail-closed?

## State

- Are commitments immutable where needed?
- Are mutable specs versioned?
- Are histories bounded?
- Can stale evidence be distinguished?
- Can terminal states replay?

## Security

- Are web inputs hostile?
- Are URLs constrained?
- Are prompts framed?
- Is output strictly parsed?
- Are bool/int and enum/mask edge cases covered?
- Can unknown values create a positive result?

## Money

- Does every terminal state account for funds?
- Can ambiguity steal funds?
- Can a user settle twice?
- Are payable writes proven live?

## Tests

- Were setup writes asserted?
- Are tests independent?
- Is pickling enabled?
- Are forged leader results tested if applicable?
- Is integration real consensus, not leader-only?

## Runtime

- Does canonical deployment correspond to current contract?
- Are transaction hashes current?
- Is finality language correct?
- Are safe/negative/recovery paths proven?
- Is Explorer URL valid?

## Repository

- one canonical deployable contract?
- no unnecessary frontend?
- no secret?
- docs internally consistent?
- working tree clean?

Fix only real defects found here.

Do not invent another feature pass.

---

# 44. FREEZE RULE

Once all applicable conditions are true:

```text
idea novelty defensible
GenLayer necessity explicit
one reusable primitive
contract source complete
preflight green
Direct Mode green
pickling green
GenVM lint green
SDK validation green
committed Studionet integration green
individual integration tests independent
canonical deployment verified
finality/consensus verified
live success path verified
live negative path verified
recovery/lifecycle verified
source blob parity verified
Explorer contract URL valid
README accurate
CONSENSUS docs accurate
SECURITY docs accurate
INTEGRATION docs accurate
DEPLOYMENT docs accurate
SUBMISSION copy ready
no secrets
main pushed
working tree clean
```

**STOP.**

Do not:

- refactor for aesthetics;
- add a frontend;
- add CI for a badge;
- add another contract;
- change prompts casually;
- change package versions casually;
- redeploy for no reason;
- chase optional tooling noise that does not affect GenLayer validity.

After this point, only reopen the contract for a specific demonstrated defect or reviewer request.

---

# 45. REQUIRED FINAL AGENT REPORT

Return this exact information when finished.

```text
PROJECT
- Primitive name:
- One-sentence thesis:
- Repository:
- Category:
- Why GenLayer is load-bearing:

IDEA / COLLISION AUDIT
- Owner repositories reviewed:
- Closest existing primitives:
- Why this is distinct:
- DECISION.md:

GIT
- Starting HEAD:
- Starting branch:
- Backup branch:
- Final HEAD:
- Default branch:
- Main pushed:
- Working tree clean:

CONTRACT
- Canonical contract path:
- Number of canonical deployable contracts:
- SDK/GenVM dependency version:
- Contract changed during finalization:
- Current contract blob SHA:

LOCAL VERIFICATION
- Python version:
- genlayer-test version:
- genlayer-py version:
- Direct command:
- Direct collected/passed/failed/skipped:
- Pickling:
- Preflight:
- GenVM linter version:
- AST lint:
- SDK validate:
- genvm-lint JSON exit code:
- Supplemental typecheck:

WINDOWS/HOST WORKAROUNDS
- Any host-only workaround:
- Exact reason:
- Committed or local-only:
- Contract affected: yes/no

GENLAYER CLI / ACCOUNT
- GenLayer CLI version:
- Network:
- Account route used:
- Account name if CLI:
- Public deployer address:
- Account created/imported/unlocked:
- Secrets exposed: no

CANONICAL STUDIONET DEPLOYMENT
- Deployment method:
- Deployment source commit:
- Deployment source contract blob:
- Canonical contract address:
- Explorer URL:
- Deployment tx:
- Lifecycle/finality:
- Consensus result:
- Deployed schema verified:
- Deployed code/source verified:

LIVE RUNTIME EVIDENCE
- Success scenario:
- Success tx(s):
- Success stored result:
- Negative/adversarial scenario:
- Negative tx(s):
- Negative stored result:
- Recovery/lifecycle scenario:
- Recovery tx(s):
- Recovery stored result:

INTEGRATION
- Integration file:
- Command:
- Collected/passed/failed/skipped:
- Important tests run individually:
- Individual result:
- Disposable deployments distinguished from canonical: yes/no

SOURCE PARITY
- Deployment source blob:
- Current main blob:
- Match:
- Redeployment needed: yes/no

DOCUMENTATION
- README:
- DECISION.md:
- docs/CONSENSUS.md:
- docs/SECURITY.md:
- docs/INTEGRATION.md:
- docs/DEPLOYMENT.md:
- SUBMISSION.md:
- Portal description under limit:
- Required Explorer evidence URL prepared:

SCOPE
- Frontend added: no
- Unnecessary CI added: no
- Secrets committed: no
- Unbounded state introduced: no

REMAINING
- Genuine blocker(s), if any:
```

If there is no meaningful remaining work, end with exactly:

```text
NOTHING MEANINGFUL REMAINS BEFORE SUBMISSION.
```

---

# 46. PRIMARY SOURCES TO RE-CHECK AT EXECUTION TIME

These URLs are intentionally included so the agent can re-check current behavior rather than rely on this file's snapshot.

## GenLayer fit / ideas

```text
https://docs.genlayer.com/developers/intelligent-contracts/when-to-use-genlayer
https://docs.genlayer.com/developers/intelligent-contracts/ideas
https://docs.genlayer.com/understand-genlayer-protocol/typical-use-cases
```

## Intelligent Contract engineering

```text
https://docs.genlayer.com/developers/intelligent-contracts/introduction
https://docs.genlayer.com/developers/intelligent-contracts/features/non-determinism
https://docs.genlayer.com/developers/intelligent-contracts/features/calling-llms
https://docs.genlayer.com/developers/intelligent-contracts/features/web-access
https://docs.genlayer.com/developers/intelligent-contracts/security-and-best-practices/prompt-injection
https://docs.genlayer.com/developers/intelligent-contracts/testing
https://docs.genlayer.com/developers/intelligent-contracts/tooling-setup
```

## Test SDK

```text
https://docs.genlayer.com/api-references/genlayer-test
https://docs.genlayer.com/api-references/genlayer-test/direct
https://docs.genlayer.com/api-references/genlayer-test/integration
```

## Linter

```text
https://docs.genlayer.com/api-references/genlayer-linter
```

## Deployment / networks / CLI

```text
https://docs.genlayer.com/developers/networks
https://docs.genlayer.com/developers/intelligent-contracts/deploying
https://docs.genlayer.com/developers/intelligent-contracts/deploying/cli-deployment
https://docs.genlayer.com/developers/intelligent-contracts/deploying/network-configuration
https://docs.genlayer.com/api-references/genlayer-cli
https://docs.genlayer.com/api-references/genlayer-cli/accounts/account/create
https://docs.genlayer.com/api-references/genlayer-cli/accounts/account/unlock
https://docs.genlayer.com/api-references/genlayer-cli/accounts/account/import
https://docs.genlayer.com/api-references/genlayer-cli/accounts/account/list
https://docs.genlayer.com/api-references/genlayer-cli/accounts/account/show
https://docs.genlayer.com/api-references/genlayer-cli/accounts/account/use
```

## GitHub CLI

```text
https://cli.github.com/manual/gh_auth_login
https://cli.github.com/manual/gh_auth_status
https://cli.github.com/manual/gh_auth_switch
https://cli.github.com/manual/gh_auth_setup-git
https://cli.github.com/manual/gh_repo_create
```

---

# 47. HOSTED STUDIONET VS LOCAL STUDIO / SIMULATOR

Do not accidentally require local Docker for a hosted Studionet validation path.

## Hosted Studionet

For the hosted development network:

```text
RPC: https://studio.genlayer.com/api
Chain ID: 61999
Explorer: https://explorer-studio.genlayer.com
```

A normal hosted Studionet integration run is:

```bash
gltest tests/integration/ -v -s --network studionet
```

It should connect to the hosted environment; do not start/reset a local Studio merely because the generic Studio Mode documentation also describes local Docker.

## Local Studio

Use local Studio when you explicitly need a local controllable network:

```bash
genlayer init
genlayer up
```

Then use the local RPC currently documented/configured by the CLI, normally under localhost.

Do not confuse a local deployment address with the canonical Studionet submission address.

## Local simulator

If the current `genlayer-test` release provides GLSim/simulator tooling and it materially speeds integration development, it may be used as an intermediate gate.

A simulator is not a replacement for the final real Studionet consensus evidence.

Never submit a local-only address as Explorer evidence.

---

# 48. DIRECT MODE MOCKING AND VALIDATOR-ERROR DISCIPLINE

## 48.1 Strict mocks

Mocks should be narrow enough that an unexpected nondeterministic call fails rather than silently returning a convenient default.

When available:

- clear mocks between tests;
- mock the exact URL/request;
- mock the exact LLM stage;
- assert unexpected extra fetches/prompts;
- make unreachable/error behavior explicit.

This catches accidental additional consensus work and hidden second fetches.

## 48.2 Test failure envelopes

If nondeterministic functions return structured envelopes such as:

```json
{"ok": false, "error_class": "TRANSIENT"}
```

test every meaningful error class.

Validators must agree on the security-relevant failure semantics, not necessarily identical error prose.

## 48.3 Custom validator leader errors

A custom validator may receive either a successful leader return or a leader error/result wrapper depending on the current SDK.

Test:

- successful leader return;
- malformed leader return;
- expected leader failure;
- external/transient leader failure;
- validator independently seeing a different failure class.

Do not assume every validator input is the same ordinary Python value produced by the happy-path leader.

Use the current `gl.vm.Return`/error types documented by the installed SDK.

## 48.4 No hidden network in Direct Mode

Direct Mode should not unexpectedly call the real internet.

If a Direct test reaches live web/LLM infrastructure, treat that as a test-isolation defect unless the current framework explicitly documents otherwise.

---

# 49. FINALITY, CALLBACKS, AND CROSS-CONTRACT MESSAGES

A reusable primitive may be consumed by another contract before a human ever sees it.

That makes finality semantics important.

## 49.1 Do not notify consumers from an unsafe intermediate result

If the SDK supports message/callback emission tied to finalization, use the finality-safe mechanism for notifications whose downstream effects should only happen after the adjudication is final.

Document whether:

- a callback/message is emitted;
- it is emitted on accepted or finalized state;
- the downstream consumer must still re-read the primitive.

## 49.2 Pull verification is safer than trusting callback arguments alone

A consumer receiving a callback can often re-read:

```text
request id
stored verdict
definition hash
finalized receipt
```

from the primitive.

Prefer a small authoritative stored result over a large callback payload.

## 49.3 Cross-contract writes

Treat cross-contract writes/messages according to current GenLayer asynchronous semantics.

Do not write code that assumes EVM-like synchronous return behavior if GenLayer messages are asynchronous.

Integration tests should prove the actual message/callback flow if it is load-bearing.

---

# 50. CLEAN-CLONE REPRODUCIBILITY GATE

Before declaring the repository complete, prove that success does not depend on forgotten local files.

## 50.1 Record current state

```bash
git status --short
git rev-parse HEAD
```

## 50.2 Clone a fresh copy

Outside the working directory:

```bash
gh repo clone OWNER/REPO <temporary-clean-directory>
cd <temporary-clean-directory>
git rev-parse HEAD
```

The HEAD must match the intended final remote commit.

## 50.3 Reinstall from committed dependency files

Create a fresh environment and install only what the repository/documentation says is needed.

Then rerun as many non-destructive gates as practical:

```text
preflight
Direct Mode
pickling
GenVM lint/validate
```

Run Studionet integration too when reasonable and when it will not create unwanted side effects beyond documented disposable test deployments.

## 50.4 Detect hidden dependencies

If the clean clone fails but the original directory passes, look for:

- untracked helper modules;
- local `runtime_plugin.py`;
- uncommitted fixtures;
- environment variables;
- editable package installs;
- patched site-packages;
- cached GenVM artifacts;
- a global package version not represented in requirements;
- local source files outside the repo.

Decide deliberately whether the dependency should:

- be committed;
- be documented as an environment prerequisite;
- remain an explicitly local host workaround.

Do not conceal it.

The historical Windows Direct Mode tempfile shim is an example of a legitimate **host workaround** that may remain external, but the README/testing notes must make that distinction honest.

---

# 51. CONTRIBUTION-PORTAL PRE-SUBMISSION CHECK

Before opening the form, verify the repository and evidence are reviewer-accessible.

## 51.1 Repository visibility

If the contribution program requires a public repository, confirm:

```bash
gh repo view OWNER/REPO --json visibility,url,defaultBranchRef
```

Do not change a private repository to public without authorization. If the mission requires public evidence and the repository is private, surface that as an actual submission blocker.

## 51.2 Default branch

Do not assume the default branch is `main`.

The canonical links, raw fixtures, README, and submission evidence must point to the actual default branch or a stable commit.

If the repo uses `master`, do not create an unnecessary parallel `main` branch merely for convention.

## 51.3 Contribution date

Use the actual current submission date in the user's/local portal context.

Do not reuse a build date if the field asks for contribution date.

## 51.4 Title

Use:

```text
<Primitive Name> — <short exact primitive function>
```

A clear title is better than leaving the optional title blank.

## 51.5 Notes / description

Keep within the current portal limit and include only verified facts:

```text
what it is
what validators independently do
what deterministic code does
why it is reusable
test counts
live deployment
```

## 51.6 Evidence

At minimum prepare:

```text
GenLayer Explorer contract URL
GitHub repository URL
deployment evidence document URL
```

If the form specifically requires `genlayer-explorer-contract`, the Explorer **address** page is the required evidence.

## 51.7 Final portal sanity check

Before pressing submit:

- address in form == canonical address in README;
- Explorer opens that address;
- repository opens;
- default branch contains the contract;
- README deployment source matches;
- description does not claim stale test counts;
- transaction/finality statements are current.

---

# 52. FINAL PRINCIPLE

A strong GenLayer Intelligent Contract is not strong because it has an LLM.

It is strong because:

```text
a normal smart contract cannot independently know or judge the required fact
+
the evidence can be independently observed by validators
+
validators agree on the small decision fields that actually matter
+
deterministic code constrains exactly what that agreement can change
+
failure and disagreement cannot silently become a positive verdict
+
the result is reusable by contracts that do not need to understand the
web/LLM/consensus machinery themselves
+
the repository proves all of that with code, adversarial tests,
real consensus, source-parity evidence, and a live deployment
```

Build **that**, prove **that**, push **that**, and then freeze it.
