# Agent Warranty Protocol

Agent Warranty Protocol is a GenLayer Intelligent Contract primitive for escrow-backed autonomous-agent performance warranties. It freezes the specification and evidence policy before funding, records a bounded dependency graph, preserves cure lineage, and keeps settlement state deterministic.

## What it guarantees

- Immutable specification and evidence-policy hashes before escrow funding.
- A dependency can only point to an already-recorded obligation, which makes cycles impossible in this bounded v1 graph.
- Evidence is a 32-byte SHA-256 hex commitment; content interpretation belongs to GenLayer consensus, while state transitions and funds remain deterministic.
- Cure rounds and delegated liability caps are bounded on chain.
- Unknown, unavailable, or ambiguous evidence is represented as `INCONCLUSIVE`, never upgraded to success.

## Contract

`contracts/agent_warranty.py` exposes `fund`, `add_obligation`, `delegate`, `submit_evidence`, `record_finding`, and public views. `record_finding` accepts only typed, consensus-agreed result categories; it does not let an LLM decide recipients or amounts.

## Checks

Run `genvm-lint check contracts/agent_warranty.py` and `gltest tests/direct -v`.

## Deployment evidence

The canonical Studionet deployment address and transaction hashes are recorded in `DEPLOYMENT.md` only after they are independently confirmed. No address is fabricated.

## Limits

This first contract records evidence identity and workflow controls. It does not itself download URLs or pay out to external addresses yet, so it must not be represented as a completed external-evidence or escrow-payout implementation.
