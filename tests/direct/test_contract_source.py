from pathlib import Path


SOURCE = Path("contracts/agent_warranty.py").read_text(encoding="utf-8")


def test_contract_has_frozen_terms_and_payable_escrow():
    assert "specification_hash" in SOURCE
    assert "evidence_policy_hash" in SOURCE
    assert "@gl.public.write.payable" in SOURCE
    assert "gl.message.value" in SOURCE


def test_contract_has_bounded_cure_and_dependency_guards():
    assert "max_cure_rounds" in SOURCE
    assert "dependency must precede child" in SOURCE
    assert "CURE_REQUIRED" in SOURCE
    assert "INCONCLUSIVE" in SOURCE
    assert "MAX_EVIDENCE_RETRIES = u256(3)" in SOURCE


def test_contract_uses_genlayer_persistent_collections():
    assert "TreeMap[str, Obligation]" in SOURCE
    assert "DynArray" not in SOURCE or "from genlayer import" in SOURCE
