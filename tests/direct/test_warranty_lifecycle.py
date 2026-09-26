from datetime import datetime, timezone
from pathlib import Path
import hashlib


def _genlayer_address(raw_address):
    from gltest.direct.sdk_loader import setup_sdk_paths

    setup_sdk_paths(Path("contracts/agent_warranty.py").resolve())
    from genlayer import Address

    return Address("0x" + raw_address.hex())


def test_terms_graph_funding_and_dependency_gate(direct_vm, direct_deploy, direct_owner, direct_bob):
    now = int(datetime.now(timezone.utc).timestamp())
    contract = direct_deploy(
        "contracts/agent_warranty.py",
        "direct-test",
        _genlayer_address(direct_bob),
        "a" * 64,
        "b" * 64,
        now + 600,
        now + 1200,
        100,
    )

    contract.add_obligation("root", "Deliver the signed report", "", 6000, 1)
    contract.add_obligation("child", "Confirm report accuracy", "root", 4000, 1)

    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("prerequisite is not fulfilled"):
        contract.submit_evidence("child", "https://evidence.example/report", "c" * 64)

    direct_vm.sender = direct_owner
    direct_vm.value = 100
    contract.fund()
    warranty = contract.get_warranty()
    assert warranty[3] == 100
    assert warranty[4] == 100
    assert warranty[6] == "OPEN"


def test_evidence_rejects_non_public_or_unpinned_inputs(direct_vm, direct_deploy, direct_owner, direct_bob):
    now = int(datetime.now(timezone.utc).timestamp())
    contract = direct_deploy(
        "contracts/agent_warranty.py",
        "direct-test-invalid-url",
        _genlayer_address(direct_bob),
        "a" * 64,
        "b" * 64,
        now + 600,
        now + 1200,
        100,
    )
    contract.add_obligation("root", "Deliver the signed report", "", 10000, 1)
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("public HTTPS URL"):
        contract.submit_evidence("root", "http://localhost/report", "c" * 64)


def test_changed_evidence_fails_closed_as_inconclusive(direct_vm, direct_deploy, direct_owner, direct_bob):
    now = int(datetime.now(timezone.utc).timestamp())
    contract = direct_deploy(
        "contracts/agent_warranty.py",
        "direct-test-hash-mismatch",
        _genlayer_address(direct_bob),
        "a" * 64,
        "b" * 64,
        now + 600,
        now + 1200,
        100,
    )
    contract.add_obligation("root", "Deliver the signed report", "", 10000, 1)
    body = "changed report"
    direct_vm.mock_web(
        r"evidence\.example/report",
        {"method": "GET", "status": 200, "body": body},
    )
    direct_vm.sender = direct_bob
    contract.submit_evidence(
        "root",
        "https://evidence.example/report",
        hashlib.sha256(b"committed report").hexdigest(),
    )
    direct_vm.sender = direct_owner
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "INCONCLUSIVE"
