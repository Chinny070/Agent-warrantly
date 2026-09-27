# Studionet deployment record — chain 61999 only

## Release status

The current hardened source is deployed to GenLayer Studionet (chain 61999), matches the checked-in source, and has completed a full live acceptance → funding → evidence → adjudication → settlement test. This is a transparent protocol-integration test using a public repository fixture, not a third-party commercial performance attestation.

## Current hardened lifecycle deployment

- Network: GenLayer Studionet, chain ID `61999`
- CLI: global GenLayer CLI `0.39.1`
- Contract: `0x939f91C18b8Bea9e650B2349dD68aFc99713f904`
- Deployment transaction: `0x6b0057513d75e96631fc294437e86f684c9e3ae07ad5d43650c32e6d6e01b7e1`
- Deployment receipt: finalized, `MAJORITY_AGREE`; constructor executed successfully
- Exact deployed source parity: SHA-256 `dd2da382acb3da1320d3503fa1f24724ee37f07d8a1878fc3a414d5676318210` (matches `contracts/agent_warranty.py`)
- Deploying/requester account: `0xaffe15eec45b68835cc9e5b4ab85dd5deaE8e70b` (`my-studionet-wallet`, active and unlocked)
- Provider account: `0x94988d2e6ad5fd385e38630c0ed3bbf219c9a43a` (`rc-provider`, unlocked)
- Warranty ID: `live-lifecycle-2026-09`
- Specification SHA-256: `169323f068781f22cd6e727ab803d4131dc5e7494da778293f4e112b75c84c0d`
- Frozen policy SHA-256: `cbc11205ac37af31037d7ac68c1296fe83bc75ac0758d7b4dc87409a45199fa6`
- Funding cutoff: Unix `1793132050`; performance duration `2592000` seconds; cure duration `864000` seconds
- Full funding started the performance window at Unix `1790540237`; performance deadline `1793132237`; cure deadline `1793996237`
- Accepted configuration digest: `5b64bd5f09f6fb6e2b4c94d9f55c2810b128945497cb8df2697a1f3c324e7880`

### Live lifecycle transactions and readbacks

1. Requester configured obligation `live-proof`: `0xff2cf5134101cc6bb0c49eedfb606c00bf4ab4f7f337e59f763f313f1aead9ed`.
2. Provider accepted the exact on-chain configuration digest: `0xd48510db9e3e926f356e11e1f23375bddbb9f15b964daf22177e230cde91485d`.
3. Requester funded `1000000000000000` wei (`0.001` GEN): `0x50697cefd32652523681961f92b7394b2a1a59990b0b5c6007008aa32efb2dd0`. Live readback showed `PERFORMANCE` and full escrow.
4. Provider submitted pinned evidence: `0xab86ac3902d5fb20f32994d135047bff7dbbb0e1fa83eb14cbfa7fb44b3da059`.
5. Evidence source: `https://raw.githubusercontent.com/Chinny070/Agent-warrantly/08cf02b843a878eb230b20161a448537951b2d6f/tests/fixtures/live_evidence.txt`; SHA-256 `cba608ac408c7179b494273f769b6da37f779a489142a893589b6acf283997f0`; retrieved live as 199 bytes and byte-matched to the committed fixture.
6. Permissionless adjudication: `0x3723335097c51758516d30d03eebd2a5368bb6b669352f9bf9ff96750033e465`. Live readback recorded `FULFILLED`, no retrieval failure, and a rationale confirming the exact frozen policy URL matched.
7. Permissionless settlement: `0xa46db370e0494de051c642a53d5dfd382c2178b67f70852dd12910061ea9c28d`, finalized `MAJORITY_AGREE`; receipt contains a `1000000000000000`-wei transfer to the provider.

Final `get_warranty`: `SETTLED`, escrowed and settled `1000000000000000`, provider payout `1000000000000000`, requester refund `0`. `get_settlement` returned `(1000000000000000, 1000000000000000, 0)`. Post-settlement balances were requester `239.346999999999999988 GEN` and provider `0.0025 GEN` (up from `0.0015 GEN`).

An earlier follow-up deployment attempt finalized with constructor error `invalid warranty ID` because its test ID exceeded the 32-character bound; it created no contract and was not used. The successful deployment above uses a valid ID.

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

## Current source and release checks

- Current source binds the exact evidence URL into semantic policy evaluation and validator results, starts the agreed performance window only when full funding is received, and rejects economically contradictory findings.
- The strict local Direct Mode gate passes 57 tests; GenVM lint and generated ABI comparison pass. GitHub Actions exposed the earlier failure: its Direct Mode loader followed a moving latest-release URL and received HTTP 404. Tests now pin the runner release to `v0.3.0-rc7` in both address setup and contract deployment. The remote run for this pin is still pending.
- The local CLI patch used during an earlier funding experiment is not an upstream-supported deployment prerequisite or evidence for this release.

The active CLI supported the payable write used for this live test. The historical v3 payout remains blocked by its immutable inconclusive obligation and is unrelated to the completed payout on the current deployment.

## Earlier superseded deployment attempts

- `0x79626c070079af6a6200909f773f061393c2475b6dd9b2683a81e24d2c69ee12` failed construction because bare generic `TreeMap()` values did not match their storage descriptors.
- `0xb02838e6e73263b79e939f4d034a77c39f137ce60bbb96e8332d649eb63cd0a6` reported acceptance at `0x8C55E001F083cb8C08906d07A7c041137670A625`, but the address was absent from Studionet reads.
- `0xe2d82782d2c18c130fb06fa2740b999854469c8c8689bdd19fbff8d09570d95b` exposed the CLI empty-string argument issue. The CLI dropped it, producing a failed root obligation. Version 3 uses `NONE` for root obligations.
