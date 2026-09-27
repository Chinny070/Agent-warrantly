# Agent Warranty Protocol

Agent Warranty Protocol is a GenLayer Intelligent Contract for escrow-backed performance warranties and payment assurance. The requester funds a bounded escrow; the provider receives the agreed payout for fulfilled work, while deterministic breach penalties are refunded to the requester. This is requester-funded performance escrow, not a provider-posted warranty bond.

## Agreement lifecycle

`DRAFT → ACCEPTED → PERFORMANCE → TERMINAL → SETTLED`

- The requester defines the SHA-256 specification commitment, bounded evidence-policy text, a funding cutoff, performance and cure durations, economic cap, obligations, dependencies, cure limits, and severities in `DRAFT`.
- The provider accepts the contract-computed configuration digest. It binds the warranty ID, requester/provider, specification commitment, evidence-policy text and hash, funding cutoff, performance/cure durations, total bond, ordered obligation set, dependency edges, severities, cure limits, and any delegation metadata.
- After acceptance, terms cannot change. The requester may fund in partial transfers, but the performance clock starts only when escrow reaches the full agreed amount. Its deadline is calculated from that full-funding time, so a late-but-valid requester funding does not consume the provider's performance window. Excess funding is rejected.
- If partial funding is never completed by the separate funding cutoff, anyone may cancel and the requester receives the partial amount back.
- A fully funded agreement enters `PERFORMANCE`. Terminal obligation findings move it to `TERMINAL`; anyone may then call deterministic settlement. Replays are rejected.

## Evidence and adjudication

The provider or the one pre-agreed delegate submits an HTTPS URL and SHA-256 commitment. The contract records every attempt's URL, hash, submitter, timestamp, attempt number, classification, retrieval failure code, and concise rationale. It bounds evidence to 12,000 bytes and allows three replacement attempts, independently of cure rounds.

The full bounded evidence policy is stored on-chain and passed with the frozen obligation requirement and exact submitted evidence URL to semantic review. The exact URL is also carried in the leader result and checked by each validator; validators independently re-fetch that source, check the HTTP status, exact committed bytes and UTF-8, then assess the same policy, requirement, and source URL. A positive finding requires a requirement match, policy/source match, and sufficient evidence. A `BREACHED` or `REMEDIABLE` finding requires a policy/source match, sufficient evidence, and a negative requirement match; contradictory combinations fail closed to `INCONCLUSIVE`. HTTP failures, malformed output, retrieval exceptions, invalid encoding, empty/oversized bodies, and hash mismatches also fail closed; an inconclusive result never consumes cure rounds.

Review is permissionless after evidence delivery: neither requester nor provider controls the classification. Validators must agree on the classification, requirement match, policy match, and evidence sufficiency. Rationale and transport diagnostics are not compared exactly because they are explanatory metadata, not settlement inputs.

## Dependencies, delegation, and settlement

At most 16 obligations are accepted. Dependencies must name an earlier, different obligation, so cycles cannot form. A child whose parent fails becomes `BLOCKED`; blocked children inherit the prerequisite failure and add no separate penalty. `BREACHED` obligations contribute their agreed severity, with aggregate recovery capped at escrow.

Provider-approved delegates are recorded before acceptance. The provider remains responsible for the complete agreed warranty. A delegate's internal liability cap is metadata only: it never reduces requester recovery. Self-delegation and replacement are rejected.

Settlement is calculated only from terminal state. Provider payout plus requester refund equals the escrow amount; successful work pays the provider, while breach severity refunds the requester. No caller supplies payout values.

## Evidence-source limits

The URL gate requires HTTPS and rejects IP literals, userinfo, explicit ports, fragments, malformed authorities, whitespace/control characters, backslashes, and common local/private suffixes. This application-level check cannot prevent DNS rebinding or guarantee redirect safety. HTTPS alone does not prove publisher identity or source authenticity; choose trusted evidence domains and express required provenance in the frozen policy. The contract currently assesses bounded UTF-8 text, not visual evidence.

## Development and release

The authoritative release checks are pinned in `requirements-dev.txt` and `.github/workflows/release-gate.yml`. They run the Direct Mode behavioral suite, GenVM lint, and regenerate/compare the committed schema. Use `python -m pip install -r requirements-dev.txt` and `pytest tests/direct -v` locally.

Only GenLayer Studionet (chain ID 61999) is an intended deployment target. Deployment status, exact source hashes, and live evidence are recorded in `DEPLOYMENT.md`. The older v3 contract is historical and is not the hardened release.
