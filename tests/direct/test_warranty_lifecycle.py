from datetime import datetime, timezone
from pathlib import Path


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
