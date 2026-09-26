# Agent Warranty Protocol

Agent Warranty Protocol is a GenLayer Intelligent Contract primitive for escrow-backed autonomous-agent performance warranties. It freezes the specification and evidence policy before funding, records a bounded dependency graph, preserves cure lineage, and keeps settlement state deterministic.

## Protocol behavior

- Immutable specification and evidence-policy hashes before escrow funding.
- A dependency can only point to an already-recorded obligation, which makes cycles impossible in this bounded v1 graph.
- Evidence is fetched from a public HTTPS URL by validators, checked against its SHA-256 commitment, and bounded to 12,000 bytes before semantic review.
- GenLayer validators independently reproduce retrieval, hash verification, and classification. A mismatch becomes `INCONCLUSIVE`.
- Cure rounds and delegated liability caps are bounded on chain; obligations must be added before their prerequisites, so cycles cannot form.
- Settlement caps aggregate liability at the escrow amount and emits deterministic GEN transfers. Expired unresolved obligations become breached.

## Contract

`contracts/agent_warranty.py` exposes `fund`, `add_obligation`, `delegate`, `submit_evidence`, `record_finding`, `expire`, `settle`, and public views. Pass `NONE` as the dependency ID for a root obligation (including through the CLI). The model classifies evidence only; contract code determines cure, liability, and transfer amounts.

## Checks

Run `genvm-lint check contracts/agent_warranty.py` and `gltest tests/direct -v`.

## Deployment evidence

Deployment transactions and live-read status are tracked in `DEPLOYMENT.md`.

## Limits

URL admission is intentionally limited to HTTPS hostnames, but DNS-level private-address resolution is not pinned; deployments should use trusted evidence hosts. The text-only evidence path does not support visual claims. A rejected or unavailable web observation yields no positive finding.
