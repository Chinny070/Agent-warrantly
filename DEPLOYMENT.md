# Studionet deployment and live evidence

## Current deployment

- Network: GenLayer Studionet, chain ID `61999`
- Contract: `0xaf74155cD6E44a4C13D17FD57EE3E1883b6CDF5D`
- Deployment transaction: `0x21ac96214a56c514852aeb287cf3fb3edd9ac33c16cf1dbe60ace9d4f103f5bb`
- Consensus: `MAJORITY_AGREE`, `ACCEPTED`
- Source commit: `1ee2b52ea9ec6b917942a7cb54320b145df05148`
- Source parity: exact match from `gen_getContractCode`; SHA-256 `c1bc559425f84acfc1876c8cdd76752c05f767504c4c9a77ffb1c4bac394fdcf`

The live `get_warranty` view returned warranty ID `agent-warranty-v3`, escrow `0`, bond `1000000000000000` wei, settled `0`, and status `OPEN`.

## Live Studionet tests

- Root obligation stored successfully (root marker `NONE`): transaction `0xf2d4acbc1b6a53da462cf1d8468f870ef73cad3ac28f73c3c686276b5ae3e12e`; readback showed `OPEN`.
- Changed/hostile evidence path: evidence transaction `0x6abe794ad014f9bf3e42e3df08bcaa7efed087ba7f9e05376236c68274564387`, assessment transaction `0xcb943f8e6bacc9ede7de8e612bebbbef6590bc93623aadced7455df0e2f7b9c4`; live readback was `INCONCLUSIVE`.
- Positive pinned text path (`Hello World`, SHA-256 `a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e`): submission transaction `0x96c4abe7287ab0feabe06889848c19c1b53e9cc966d2d27870340f1148584fe1`, assessment transaction `0x0899e72e2fe1834ab20b22809277036cdc0019dcd0d9c518415524ad995ba122`; live readback was `FULFILLED`.

## Local checks

- `genvm-lint check contracts/agent_warranty.py`: passed lint and SDK validation.
- `genvm-lint schema contracts/agent_warranty.py`: schema generated.
- `gltest tests/direct -v`: 7 passed, including dependency gating, funding, hash mismatch, and successful settlement.

The Studionet CLI write command hardcodes `value: 0`, so escrow funding and the resulting recipient transfer were exercised in Direct Mode but not with a payable live transaction. The live warranty therefore remains `OPEN` with zero escrow; no live payout is claimed.

## Superseded attempts

- `0x79626c070079af6a6200909f773f061393c2475b6dd9b2683a81e24d2c69ee12` failed construction because bare generic `TreeMap()` values did not match their storage descriptors.
- `0xb02838e6e73263b79e939f4d034a77c39f137ce60bbb96e8332d649eb63cd0a6` reported acceptance at `0x8C55E001F083cb8C08906d07A7c041137670A625`, but the address was absent from Studionet reads.
- `0xe2d82782d2c18c130fb06fa2740b999854469c8c8689bdd19fbff8d09570d95b` exposed the CLI empty-string argument issue. The CLI dropped it, producing a failed root obligation. Version 3 uses `NONE` for root obligations.
