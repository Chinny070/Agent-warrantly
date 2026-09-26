# Deployment evidence

The initial live deploy at transaction `0x79626c070079af6a6200909f773f061393c2475b6dd9b2683a81e24d2c69ee12`
was rejected at contract construction by GenVM because bare `TreeMap()` initialization lost
its generic storage descriptor. It is retained here as a transparent failed-live-test record,
not a canonical deployment. The source now uses explicit generic storage constructors.

The corrected deployment transaction is `0xb02838e6e73263b79e939f4d034a77c39f137ce60bbb96e8332d649eb63cd0a6`,
which received `MAJORITY_AGREE` / `ACCEPTED` at address
`0x8C55E001F083cb8C08906d07A7c041137670A625`. An immediate cold RPC read reported
that the contract was not found, so this address is deliberately **not** presented as a canonical
deployment until a subsequent `get_warranty` read succeeds.

Direct RPC confirmed the transaction lifecycle as `FINALIZED`, while `gen_getContractCode`
returned `-32001 Contract not found` for the reported address. This source has since been expanded
with byte-pinned evidence assessment and bounded settlement; it requires a new live deployment
and post-deployment checks before any address can be called canonical.
