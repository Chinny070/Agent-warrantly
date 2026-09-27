# Studionet deployment record — chain 61999 only

## Release status

The initial hardened source is deployed to GenLayer Studionet (chain 61999). A follow-up release addresses evidence-source binding, funding/performance timing, and semantic consistency. The follow-up has not yet been deployed, and no complete live lifecycle is claimed until its source parity and settlement are verified.

## Initial hardened deployment (superseded before lifecycle validation)

- Network: GenLayer Studionet, chain ID `61999`
- Contract: `0xbC483C99118D8dFA1d29eF82eE873d79A785CE5b`
- Deployment transaction: `0xacb6e177edee76153acb5b0fb95a10c05c88d8b73b7687df4a09e9e8e6c7f543`
- Receipt: finalized, `MAJORITY_AGREE`; leader and validator executions succeeded
- Deploying/requester account: `0xaffe15eec45b68835cc9e5b4ab85dd5deaE8e70b` (active and unlocked GenLayer CLI account at deployment)
- Provider account: `0x94988d2e6ad5fd385e38630c0ed3bbf219c9a43a` (`rc-provider`, unlocked CLI account)
- Warranty ID: `agent-warranty-reviewer-2026-09`
- Specification SHA-256: `169323f068781f22cd6e727ab803d4131dc5e7494da778293f4e112b75c84c0d` (the repository's supplied audit/benchmark document)
- Evidence-policy SHA-256: `f85e3ea44cd1e7d2883820cad92790a8d320930f6f923dbf2543e05674555808`
- Deadline: Unix `1793127401` (2026-10-27 18:56:41 UTC)
- Cure deadline: Unix `1793991401` (2026-11-06 18:56:41 UTC)
- Agreement amount: `1000000000000000` wei (`0.001` GEN); escrowed: `0`
- Live `get_warranty` read: status `DRAFT`, obligation count `0`, escrow `0`, settled `0`, provider payout `0`, requester refund `0`
- Live `get_evidence_policy` read matched the submitted frozen policy and returned the hash above
- Live deployed-source parity: exact text match; SHA-256 `ffbcede63a98f6173e8b1354ffd16e83a1f64c778a57179b47ed60ab3e96d357` (same as `contracts/agent_warranty.py`)

The provider account and agreement terms were selected from available CLI context and the prior `0.001` GEN agreement amount to carry out the deployment autonomously. They are immutable constructor terms. No claim is made that the provider has accepted this new agreement or that any funds have been transferred to it.

## Historical deployment: v3 (superseded)

- Network: GenLayer Studionet, chain ID `61999`
- Contract: `0xaf74155cD6E44a4C13D17FD57EE3E1883b6CDF5D`
- Deployment transaction: `0x21ac96214a56c514852aeb287cf3fb3edd9ac33c16cf1dbe60ace9d4f103f5bb`
- Consensus: `MAJORITY_AGREE`, `ACCEPTED`
- Source commit: `1ee2b52ea9ec6b917942a7cb54320b145df05148`
- Source parity: exact match from `gen_getContractCode`; SHA-256 `c1bc559425f84acfc1876c8cdd76752c05f767504c4c9a77ffb1c4bac394fdcf`

The live `get_warranty` view returned warranty ID `agent-warranty-v3`, bond `1000000000000000` wei, settled `0`, and status `OPEN`.

## Historical v3 live tests

- Root obligation stored successfully (root marker `NONE`): transaction `0xf2d4acbc1b6a53da462cf1d8468f870ef73cad3ac28f73c3c686276b5ae3e12e`; readback showed `OPEN`.
- Changed/hostile evidence path: evidence transaction `0x6abe794ad014f9bf3e42e3df08bcaa7efed087ba7f9e05376236c68274564387`, assessment transaction `0xcb943f8e6bacc9ede7de8e612bebbbef6590bc93623aadced7455df0e2f7b9c4`; live readback was `INCONCLUSIVE`.
- Positive pinned text path (`Hello World`, SHA-256 `a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e`): submission transaction `0x96c4abe7287ab0feabe06889848c19c1b53e9cc966d2d27870340f1148584fe1`, assessment transaction `0x0899e72e2fe1834ab20b22809277036cdc0019dcd0d9c518415524ad995ba122`; live readback was `FULFILLED`.

## Historical v3 escrow state (observed 2026-09-27)

- The live `get_warranty` view now shows escrow `1000000000000000` wei (the full `0.001` GEN bond), settled `0`, and status `OPEN`.
- `smoke-positive` is `FULFILLED`. `smoke-1` is `INCONCLUSIVE` (severity 10000 bps).
- Settlement was blocked because deployed v3 does not allow replacement evidence after an `INCONCLUSIVE` finding. The v3 contract is immutable; its `expire` method can terminalize unresolved items only after its cure deadline, then its 10000-bps obligation refunds the full bond to the requester on settlement. V3 does not expose that deadline.
- The escrow value was confirmed by a live read. A transaction hash for the user's funding write was not captured in this task.

## Follow-up source work (not yet deployed)

- Follow-up source binds the exact evidence URL into the semantic prompt and validator result, separates funding cutoff from the performance window, and fails closed on inconsistent semantic findings.
- The updated checks and generated schema are release-gated in CI. The local GenLayer CLI patch used during the earlier v3 funding experiment is not upstream-supported and is not a deployment prerequisite or evidence for this release.
- The new lifecycle deployment address, transaction, parity, and settlement will be recorded here only after live verification.

The global GenLayer CLI 0.39.1 installed in the task environment was locally patched to accept `genlayer write <address> fund --value <wei>`; this patch is not part of the Agentwarrantly repository or the upstream CLI release. Direct Mode verified payable funding and settlement. Live funding is verified as above; live payout has not been completed because the deployed v3 inconclusive obligation cannot be retried before its cure deadline.

## Earlier superseded deployment attempts

- `0x79626c070079af6a6200909f773f061393c2475b6dd9b2683a81e24d2c69ee12` failed construction because bare generic `TreeMap()` values did not match their storage descriptors.
- `0xb02838e6e73263b79e939f4d034a77c39f137ce60bbb96e8332d649eb63cd0a6` reported acceptance at `0x8C55E001F083cb8C08906d07A7c041137670A625`, but the address was absent from Studionet reads.
- `0xe2d82782d2c18c130fb06fa2740b999854469c8c8689bdd19fbff8d09570d95b` exposed the CLI empty-string argument issue. The CLI dropped it, producing a failed root obligation. Version 3 uses `NONE` for root obligations.
