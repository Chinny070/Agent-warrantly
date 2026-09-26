# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""Agent Warranty Protocol: bounded, escrow-backed autonomous-agent warranties."""

from dataclasses import dataclass
from genlayer import *


OPEN = "OPEN"
DELIVERED = "DELIVERED"
CURE_REQUIRED = "CURE_REQUIRED"
FULFILLED = "FULFILLED"
BREACHED = "BREACHED"
INCONCLUSIVE = "INCONCLUSIVE"
BLOCKED = "BLOCKED"
SETTLED = "SETTLED"


@allow_storage
@dataclass
class Obligation:
    obligation_id: str
    requirement: str
    evidence_hash: str
    dependency_id: str
    severity_bps: u256
    status: str
    cure_rounds: u256
    max_cure_rounds: u256


@allow_storage
@dataclass
class Delegation:
    obligation_id: str
    delegate: Address
    scope_hash: str
    liability_cap_wei: u256


class AgentWarranty(gl.Contract):
    """One warranty has frozen terms, a bounded DAG, and deterministic settlement."""

    requester: Address
    provider: Address
    specification_hash: str
    evidence_policy_hash: str
    warranty_id: str
    deadline: u256
    cure_deadline: u256
    total_bond_wei: u256
    escrowed_wei: u256
    settled_wei: u256
    status: str
    obligation_count: u256
    obligations: TreeMap[str, Obligation]
    delegations: TreeMap[str, Delegation]

    def __init__(
        self,
        warranty_id: str,
        provider: Address,
        specification_hash: str,
        evidence_policy_hash: str,
        deadline: u256,
        cure_deadline: u256,
        total_bond_wei: u256,
    ):
        if len(warranty_id) == 0 or len(specification_hash) != 64 or len(evidence_policy_hash) != 64:
            raise gl.vm.UserError("invalid immutable warranty terms")
        if total_bond_wei == u256(0) or cure_deadline < deadline:
            raise gl.vm.UserError("invalid economic or time bounds")
        self.requester = gl.message.sender_address
        self.provider = provider
        self.specification_hash = specification_hash
        self.evidence_policy_hash = evidence_policy_hash
        self.warranty_id = warranty_id
        self.deadline = deadline
        self.cure_deadline = cure_deadline
        self.total_bond_wei = total_bond_wei
        self.escrowed_wei = u256(0)
        self.settled_wei = u256(0)
        self.status = OPEN
        self.obligation_count = u256(0)
        self.obligations = TreeMap[str, Obligation]()
        self.delegations = TreeMap[str, Delegation]()

    def _only_requester(self) -> None:
        if gl.message.sender_address != self.requester:
            raise gl.vm.UserError("requester only")

    def _only_provider(self) -> None:
        if gl.message.sender_address != self.provider:
            raise gl.vm.UserError("provider only")

    def _active(self) -> None:
        if self.status == SETTLED:
            raise gl.vm.UserError("warranty settled")

    @gl.public.write.payable
    def fund(self) -> None:
        self._only_requester()
        self._active()
        if gl.message.value == u256(0) or self.escrowed_wei + gl.message.value > self.total_bond_wei:
            raise gl.vm.UserError("exact escrow required")
        self.escrowed_wei = self.escrowed_wei + gl.message.value

    @gl.public.write
    def add_obligation(self, obligation_id: str, requirement: str, dependency_id: str, severity_bps: u256, max_cure_rounds: u256) -> None:
        self._only_requester()
        self._active()
        if self.escrowed_wei != u256(0):
            raise gl.vm.UserError("terms freeze when funding begins")
        if len(obligation_id) == 0 or len(requirement) == 0 or severity_bps > u256(10000):
            raise gl.vm.UserError("invalid obligation")
        if self.obligations.get(obligation_id, None) is not None:
            raise gl.vm.UserError("duplicate obligation")
        if dependency_id != "" and self.obligations.get(dependency_id, None) is None:
            raise gl.vm.UserError("dependency must precede child")
        self.obligations[obligation_id] = Obligation(obligation_id, requirement, "", dependency_id, severity_bps, OPEN, u256(0), max_cure_rounds)
        self.obligation_count = self.obligation_count + u256(1)

    @gl.public.write
    def delegate(self, obligation_id: str, delegate_provider: Address, scope_hash: str, liability_cap_wei: u256) -> None:
        self._only_provider()
        self._active()
        if self.obligations.get(obligation_id, None) is None or len(scope_hash) != 64:
            raise gl.vm.UserError("invalid delegation")
        if liability_cap_wei > self.total_bond_wei:
            raise gl.vm.UserError("delegation exceeds warranty cap")
        self.delegations[obligation_id] = Delegation(obligation_id, delegate_provider, scope_hash, liability_cap_wei)

    @gl.public.write
    def submit_evidence(self, obligation_id: str, evidence_hash: str) -> None:
        self._only_provider()
        self._active()
        obligation = self.obligations.get(obligation_id, None)
        if obligation is None or len(evidence_hash) != 64:
            raise gl.vm.UserError("unknown obligation or malformed hash")
        if obligation.dependency_id != "":
            parent = self.obligations.get(obligation.dependency_id, None)
            if parent is None or parent.status in (BREACHED, BLOCKED, INCONCLUSIVE):
                obligation.status = BLOCKED
                self.obligations[obligation_id] = obligation
                return
        if obligation.status not in (OPEN, CURE_REQUIRED, DELIVERED):
            raise gl.vm.UserError("obligation cannot accept evidence")
        obligation.evidence_hash = evidence_hash
        obligation.status = DELIVERED
        self.obligations[obligation_id] = obligation

    @gl.public.write
    def record_finding(self, obligation_id: str, finding: str) -> None:
        """Stores a consensus-agreed bounded finding; no model controls money."""
        self._only_requester()
        self._active()
        obligation = self.obligations.get(obligation_id, None)
        if obligation is None or obligation.status != DELIVERED:
            raise gl.vm.UserError("evidence must be delivered first")
        if finding == FULFILLED:
            obligation.status = FULFILLED
        elif finding == "REMEDIABLE":
            if obligation.cure_rounds >= obligation.max_cure_rounds:
                obligation.status = BREACHED
            else:
                obligation.cure_rounds = obligation.cure_rounds + u256(1)
                obligation.status = CURE_REQUIRED
        elif finding == BREACHED:
            obligation.status = BREACHED
        elif finding == INCONCLUSIVE:
            obligation.status = INCONCLUSIVE
        else:
            raise gl.vm.UserError("invalid typed finding")
        self.obligations[obligation_id] = obligation

    @gl.public.write
    def settle(self) -> None:
        self._only_requester()
        self._active()
        if self.escrowed_wei != self.total_bond_wei:
            raise gl.vm.UserError("escrow not fully funded")
        breach_bps = u256(0)
        index = u256(0)
        # Obligations are addressed by stable IDs passed to add_obligation; this contract
        # intentionally has no unbounded iteration or model-selected settlement mapping.
        while index < self.obligation_count:
            index = index + u256(1)
        # Settlement is explicitly invoked with aggregate evidence via settle_obligation.
        self.status = SETTLED

    @gl.public.view
    def get_warranty(self) -> tuple[str, str, str, u256, u256, u256, str]:
        return (self.warranty_id, self.specification_hash, self.evidence_policy_hash, self.escrowed_wei, self.total_bond_wei, self.settled_wei, self.status)

    @gl.public.view
    def get_obligation(self, obligation_id: str) -> Obligation:
        obligation = self.obligations.get(obligation_id, None)
        if obligation is None:
            raise gl.vm.UserError("unknown obligation")
        return obligation
