from datetime import datetime, timezone
from pathlib import Path
import hashlib
import pytest


POLICY = (
    "Accept only signed delivery receipts from evidence.example.com; require the "
    "receipt to identify the warranty and completion time; reject unsigned or "
    "self-authored assertions."
)
BODY = "signed receipt: warranty=review-1; completed=2026-09-27T12:00:00Z"


def _genlayer_address(raw_address):
    from gltest.direct.sdk_loader import setup_sdk_paths

    setup_sdk_paths(Path("contracts/agent_warranty.py").resolve())
    from genlayer import Address

    return Address("0x" + raw_address.hex())


def _new_contract(direct_deploy, direct_vm, owner, provider, *, bond=100, suffix="case", policy=POLICY):
    now = int(datetime.now(timezone.utc).timestamp())
    direct_vm.sender = owner
    return direct_deploy(
        "contracts/agent_warranty.py",
        "warranty-" + suffix,
        _genlayer_address(provider),
        hashlib.sha256(b"frozen spec").hexdigest(),
        policy,
        now + 600,
        now + 1200,
        bond,
    )


def _add_root(contract, obligation_id="root", severity=10000, max_cures=1):
    contract.add_obligation(
        obligation_id,
        "The signed receipt proves completion",
        "NONE",
        severity,
        max_cures,
    )


def _accept_and_fund(contract, direct_vm, owner, provider, *, bond=100, partial=None):
    direct_vm.sender = provider
    contract.accept(contract.configuration_digest())
    direct_vm.sender = owner
    direct_vm.value = bond if partial is None else partial
    contract.fund()
    direct_vm.value = 0
    if partial is not None and partial < bond:
        return
    assert contract.get_warranty()[3] == "PERFORMANCE"


def _mock_assessment(direct_vm, url, body, finding="FULFILLED", match=True, sufficiency="SUFFICIENT"):
    direct_vm.mock_web(
        r"evidence\.example\.com/receipt",
        {"method": "GET", "status": 200, "body": body},
    )
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"%s","requirement_match":%s,"policy_match":true,"evidence_sufficiency":"%s","rationale":"verified"}'
        % (finding, "true" if match else "false", sufficiency),
    )


def _submit(contract, direct_vm, provider, body=BODY, obligation_id="root", url="https://evidence.example.com/receipt"):
    direct_vm.sender = provider
    contract.submit_evidence(obligation_id, url, hashlib.sha256(body.encode()).hexdigest())


@pytest.mark.parametrize("invalid_case,expected", [
    ("zero-bond", "bond out of bounds"),
    ("bad-hash", "SHA-256"),
    ("same-party", "must differ"),
])
def test_constructor_rejects_invalid_terms_and_zero_bond(direct_vm, direct_deploy, direct_owner, direct_bob, invalid_case, expected):
    now = int(datetime.now(timezone.utc).timestamp())
    args = (
        "warranty-invalid", _genlayer_address(direct_bob), hashlib.sha256(b"spec").hexdigest(),
        POLICY, now + 600, now + 1200, 100,
    )
    direct_vm.sender = direct_owner
    deploy_args = list(args)
    if invalid_case == "zero-bond":
        deploy_args[6] = 0
    elif invalid_case == "bad-hash":
        deploy_args[2] = "z" * 64
    else:
        deploy_args[1] = _genlayer_address(direct_owner)
    with direct_vm.expect_revert(expected):
        direct_deploy("contracts/agent_warranty.py", *deploy_args)


def test_configuration_acceptance_freezes_terms_and_requires_digest(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="freeze")
    _add_root(contract)
    digest = contract.configuration_digest()

    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("does not match"):
        contract.accept("0" * 64)
    contract.accept(digest)
    assert contract.get_warranty()[3] == "ACCEPTED"

    direct_vm.sender = direct_owner
    with direct_vm.expect_revert("only in DRAFT"):
        contract.add_obligation("late", "late terms", "NONE", 1, 0)
    assert contract.configuration_digest() == digest


def test_funding_requires_acceptance_full_amount_and_no_overfunding(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="funding")
    _add_root(contract)
    direct_vm.sender = direct_owner
    direct_vm.value = 10
    with direct_vm.expect_revert("accept before funding"):
        contract.fund()
    direct_vm.value = 0

    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob, bond=100, partial=40)
    assert contract.get_warranty()[3] == "ACCEPTED"
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("fully funded"):
        contract.submit_evidence("root", "https://evidence.example.com/receipt", hashlib.sha256(BODY.encode()).hexdigest())
    direct_vm.sender = direct_owner
    direct_vm.value = 61
    with direct_vm.expect_revert("cannot exceed"):
        contract.fund()
    direct_vm.value = (1 << 256) - 1
    with direct_vm.expect_revert("cannot exceed"):
        contract.fund()
    direct_vm.value = 60
    contract.fund()
    direct_vm.value = 0
    assert contract.get_warranty()[3] == "PERFORMANCE"


def test_only_provider_accepts_and_requester_funds(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="roles")
    _add_root(contract)
    digest = contract.configuration_digest()
    with direct_vm.prank(direct_owner):
        with direct_vm.expect_revert("provider only"):
            contract.accept(digest)
    direct_vm.sender = direct_bob
    contract.accept(digest)
    direct_vm.sender = direct_bob
    direct_vm.value = 100
    with direct_vm.expect_revert("requester only"):
        contract.fund()


def test_evidence_is_blocked_before_acceptance_and_activation(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="prework")
    _add_root(contract)
    with direct_vm.prank(direct_bob):
        with direct_vm.expect_revert("fully funded"):
            contract.submit_evidence("root", "https://evidence.example.com/receipt", hashlib.sha256(BODY.encode()).hexdigest())
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob, bond=100, partial=1)
    with direct_vm.prank(direct_bob):
        with direct_vm.expect_revert("fully funded"):
            contract.submit_evidence("root", "https://evidence.example.com/receipt", hashlib.sha256(BODY.encode()).hexdigest())


@pytest.mark.parametrize("url", [
    "http://evidence.example.com/receipt",
    "https://127.0.0.1/receipt",
    "https://10.0.0.1/receipt",
    "https://[::1]/receipt",
    "https://localhost/receipt",
    "https://name.local/receipt",
    "https://name.internal/receipt",
    "https://user@evidence.example.com/receipt",
    "https://evidence.example.com:443/receipt",
    "https://evidence.example.com/receipt#fragment",
    "https://evidence.example.com\\@evil.example/receipt",
    "https://evidence.example.com/white space",
])
def test_rejects_unsafe_evidence_urls(direct_vm, direct_deploy, direct_owner, direct_bob, url):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="bad-url")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    with direct_vm.prank(direct_bob):
        with direct_vm.expect_revert("invalid evidence hash or public HTTPS URL"):
            contract.submit_evidence("root", url, hashlib.sha256(BODY.encode()).hexdigest())


def test_evidence_url_length_boundary(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="url-length")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    prefix = "https://evidence.example.com/"
    too_long = prefix + ("a" * (513 - len(prefix)))
    with direct_vm.prank(direct_bob):
        with direct_vm.expect_revert("invalid evidence hash or public HTTPS URL"):
            contract.submit_evidence("root", too_long, hashlib.sha256(BODY.encode()).hexdigest())
    valid_url = prefix + ("a" * (512 - len(prefix)))
    direct_vm.sender = direct_bob
    contract.submit_evidence("root", valid_url, hashlib.sha256(BODY.encode()).hexdigest())
    direct_vm.mock_web(r"evidence\.example\.com/", {"method": "GET", "status": 200, "body": BODY})
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"FULFILLED","requirement_match":true,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"valid"}',
    )
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "FULFILLED"


def test_graph_is_bounded_dag_with_valid_deep_chain_and_bad_dependencies(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="dag")
    contract.add_obligation("root", "root condition", "NONE", 0, 0)
    contract.add_obligation("child", "child condition", "root", 0, 0)
    contract.add_obligation("leaf", "leaf condition", "child", 0, 0)
    with direct_vm.expect_revert("prior, different"):
        contract.add_obligation("missing", "bad", "unknown", 0, 0)
    with direct_vm.expect_revert("prior, different"):
        contract.add_obligation("self", "bad", "self", 0, 0)
    with direct_vm.expect_revert("maximum obligation"):
        for index in range(14):
            contract.add_obligation("node" + str(index), "node", "NONE", 0, 0)
    assert contract.get_warranty()[11] == 16


@pytest.mark.parametrize("policy_length,should_fail", [(2048, False), (2049, True)])
def test_policy_length_is_bounded(direct_vm, direct_deploy, direct_owner, direct_bob, policy_length, should_fail):
    now = int(datetime.now(timezone.utc).timestamp())
    direct_vm.sender = direct_owner
    if should_fail:
        with direct_vm.expect_revert("policy length"):
            direct_deploy(
                "contracts/agent_warranty.py", "policy-boundary", _genlayer_address(direct_bob),
                hashlib.sha256(b"spec").hexdigest(), "p" * policy_length, now + 600, now + 1200, 100,
            )
    else:
        contract = direct_deploy(
            "contracts/agent_warranty.py", "policy-boundary", _genlayer_address(direct_bob),
            hashlib.sha256(b"spec").hexdigest(), "p" * policy_length, now + 600, now + 1200, 100,
        )
        assert len(contract.get_evidence_policy()[0]) == policy_length


def test_obligation_and_cure_round_lengths_are_bounded(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="bounds")
    contract.add_obligation("x" * 32, "r" * 512, "NONE", 0, 3)
    with direct_vm.expect_revert("ID or requirement"):
        contract.add_obligation("x" * 33, "requirement", "NONE", 1, 0)
    with direct_vm.expect_revert("ID or requirement"):
        contract.add_obligation("long", "r" * 513, "NONE", 1, 0)
    with direct_vm.expect_revert("cure rounds"):
        contract.add_obligation("cures", "requirement", "NONE", 1, 4)


def test_permissionless_assessment_and_requester_cannot_veto_delivered_evidence(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="permissionless-review")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    attempt = contract.get_evidence_attempt("root", 1)
    assert attempt.finding == "PENDING"

    _mock_assessment(direct_vm, attempt.evidence_url, BODY)
    direct_vm.sender = direct_charlie
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "FULFILLED", contract.get_evidence_attempt("root", 1)
    assert contract.get_evidence_attempt("root", 1).finding == "FULFILLED"
    assert contract.get_warranty()[3] == "TERMINAL"


def test_delivered_evidence_is_not_expired_before_permissionless_review(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="no-veto")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    direct_vm.warp("2030-01-01T00:00:00Z")
    contract.expire()
    assert contract.get_obligation("root").status == "DELIVERED"
    _mock_assessment(direct_vm, "https://evidence.example.com/receipt", BODY)
    direct_vm.sender = direct_charlie
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "FULFILLED"


def test_unresolved_open_obligation_expires_into_terminal_breach(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="expiry")
    _add_root(contract, severity=2500)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    direct_vm.warp("2030-01-01T00:00:00Z")
    contract.expire()
    assert contract.get_obligation("root").status == "BREACHED"
    assert contract.get_warranty()[3] == "TERMINAL"
    contract.settle()
    assert contract.get_settlement() == (100, 75, 25)


def test_permissionless_settlement_is_conservative_and_replay_protected(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="permissionless-settle")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    _mock_assessment(direct_vm, "https://evidence.example.com/receipt", BODY)
    direct_vm.sender = direct_bob
    contract.record_finding("root")
    direct_vm.sender = direct_charlie
    contract.settle()
    assert contract.get_warranty()[3] == "SETTLED"
    assert contract.get_settlement() == (100, 100, 0)
    with direct_vm.expect_revert("not terminal"):
        contract.settle()
    with direct_vm.prank(direct_owner):
        with direct_vm.expect_revert("only in DRAFT"):
            contract.add_obligation("late", "late", "NONE", 1, 0)


def test_zero_and_tiny_internal_delegation_caps_never_reduce_requester_recovery(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie, direct_alice):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="delegate-zero")
    contract.add_obligation("root", "failed delivery", "NONE", 2000, 0)
    contract.add_obligation("child", "also failed", "NONE", 2000, 0)
    direct_vm.sender = direct_bob
    contract.delegate("root", _genlayer_address(direct_charlie), hashlib.sha256(b"scope").hexdigest(), 0)
    contract.delegate("child", _genlayer_address(direct_alice), hashlib.sha256(b"scope-2").hexdigest(), 1)
    with direct_vm.expect_revert("replacement is not allowed"):
        contract.delegate("root", _genlayer_address(direct_charlie), hashlib.sha256(b"other").hexdigest(), 1)
    with direct_vm.expect_revert("self-delegation"):
        contract.delegate("root", _genlayer_address(direct_bob), hashlib.sha256(b"self").hexdigest(), 0)
    digest = contract.configuration_digest()
    contract.accept(digest)
    direct_vm.sender = direct_owner
    direct_vm.value = 100
    contract.fund()
    direct_vm.value = 0
    _submit(contract, direct_vm, direct_charlie, body="verified failed delivery", obligation_id="root")
    _submit(contract, direct_vm, direct_alice, body="verified failed delivery", obligation_id="child")
    direct_vm.clear_mocks()
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": "verified failed delivery"})
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"BREACHED","requirement_match":false,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"non-delivery"}',
    )
    direct_vm.sender = direct_charlie
    contract.record_finding("root")
    contract.record_finding("child")
    direct_vm.sender = direct_owner
    contract.settle()
    assert contract.get_settlement() == (100, 60, 40)


def test_unauthorized_delegation_is_rejected(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="delegate-auth")
    _add_root(contract)
    with direct_vm.expect_revert("provider only"):
        contract.delegate("root", _genlayer_address(direct_charlie), hashlib.sha256(b"scope").hexdigest(), 0)


def test_dependency_failure_blocks_child_without_double_penalty(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="blocked")
    contract.add_obligation("root", "root delivered", "NONE", 4000, 0)
    contract.add_obligation("child", "dependent delivered", "root", 4000, 0)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob, body="root did not deliver", obligation_id="root")
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": "root did not deliver"})
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"BREACHED","requirement_match":false,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"failure"}',
    )
    direct_vm.sender = direct_charlie
    contract.record_finding("root")
    _submit(contract, direct_vm, direct_bob, body="child evidence", obligation_id="child")
    assert contract.get_obligation("child").status == "BLOCKED"
    assert contract.get_warranty()[3] == "TERMINAL"
    contract.settle()
    assert contract.get_settlement() == (100, 60, 40)


def test_aggregate_penalty_caps_at_total_escrow(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="aggregate-cap")
    contract.add_obligation("a", "failure one", "NONE", 8000, 0)
    contract.add_obligation("b", "failure two", "NONE", 8000, 0)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    for obligation_id in ("a", "b"):
        _submit(contract, direct_vm, direct_bob, body="documented failure", obligation_id=obligation_id)
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": "documented failure"})
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"BREACHED","requirement_match":false,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"breach"}',
    )
    direct_vm.sender = direct_charlie
    contract.record_finding("a")
    contract.record_finding("b")
    contract.settle()
    assert contract.get_settlement() == (100, 0, 100)


def test_parent_inconclusive_does_not_terminally_block_child(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="parent-uncertain")
    contract.add_obligation("root", "root condition", "NONE", 5000, 0)
    contract.add_obligation("child", "child condition", "root", 5000, 0)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob, body="wrong")
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": "wrong"})
    direct_vm.sender = direct_owner
    contract.record_finding("root")
    with direct_vm.prank(direct_bob):
        with direct_vm.expect_revert("prerequisite evidence is inconclusive"):
            contract.submit_evidence("child", "https://evidence.example.com/receipt", hashlib.sha256(BODY.encode()).hexdigest())
    assert contract.get_obligation("child").status == "OPEN"


def test_parent_fulfillment_unblocks_child_evidence(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="parent-fulfilled")
    contract.add_obligation("root", "root condition", "NONE", 5000, 0)
    contract.add_obligation("child", "child condition", "root", 5000, 0)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob, obligation_id="root")
    _mock_assessment(direct_vm, "https://evidence.example.com/receipt", BODY)
    direct_vm.sender = direct_charlie
    contract.record_finding("root")
    direct_vm.clear_mocks()
    _submit(contract, direct_vm, direct_bob, obligation_id="child")
    _mock_assessment(direct_vm, "https://evidence.example.com/receipt", BODY)
    contract.record_finding("child")
    assert contract.get_obligation("root").status == "FULFILLED"
    assert contract.get_obligation("child").status == "FULFILLED"
    assert contract.get_warranty()[3] == "TERMINAL"


@pytest.mark.parametrize("status,expected", [
    (404, "HTTP_INVALID"),
    (429, "HTTP_RETRYABLE"),
    (500, "HTTP_RETRYABLE"),
])
def test_http_errors_fail_closed_even_if_body_hash_matches(direct_vm, direct_deploy, direct_owner, direct_bob, status, expected):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="http-" + str(status))
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": status, "body": BODY})
    direct_vm.sender = direct_charlie_if_available(direct_vm)
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "INCONCLUSIVE"
    assert contract.get_evidence_attempt("root", 1).failure_code == expected


def direct_charlie_if_available(direct_vm):
    from gltest.direct.pytest_plugin import create_address

    return create_address("independent-reviewer")


@pytest.mark.parametrize("body,expected", [
    ("", "EMPTY_BODY"),
    ("x" * 12001, "BODY_TOO_LARGE"),
    ("not the committed body", "HASH_MISMATCH"),
    (b"\xff", "INVALID_UTF8"),
    (None, "INVALID_BODY_TYPE"),
])
def test_invalid_external_bodies_fail_closed(direct_vm, direct_deploy, direct_owner, direct_bob, body, expected):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="body-" + expected)
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    if expected == "INVALID_UTF8":
        direct_vm.sender = direct_bob
        contract.submit_evidence(
            "root", "https://evidence.example.com/receipt", hashlib.sha256(body).hexdigest()
        )
    else:
        _submit(contract, direct_vm, direct_bob)
    if expected == "INVALID_BODY_TYPE":
        direct_vm.mock_web(
            r"evidence\.example\.com/receipt",
            {"method": "GET", "response": {"status": 200, "headers": {}, "body": None}},
        )
    else:
        direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": body})
    direct_vm.sender = direct_bob
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "INCONCLUSIVE"
    assert contract.get_evidence_attempt("root", 1).failure_code == expected


def test_exact_maximum_evidence_size_is_accepted(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="max-evidence")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    body = "x" * 12000
    direct_vm.sender = direct_bob
    contract.submit_evidence("root", "https://evidence.example.com/receipt", hashlib.sha256(body.encode()).hexdigest())
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": body})
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"FULFILLED","requirement_match":true,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"bounded"}',
    )
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "FULFILLED"


@pytest.mark.parametrize("llm_output", [
    "{}",
    '{"finding":"NOT_A_FINDING","requirement_match":true,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"bad"}',
    '{"finding":"FULFILLED","requirement_match":false,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"contradictory"}',
])
def test_semantic_output_must_be_structured_and_use_frozen_policy(direct_vm, direct_deploy, direct_owner, direct_bob, llm_output):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="policy")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": BODY})
    direct_vm.mock_llm("Accept only signed delivery receipts from evidence.example.com", llm_output)
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "INCONCLUSIVE"
    if llm_output == "{}" or "NOT_A_FINDING" in llm_output:
        assert contract.get_evidence_attempt("root", 1).failure_code == "MALFORMED_SEMANTIC_OUTPUT"
    else:
        assert contract.get_evidence_attempt("root", 1).finding == "INCONCLUSIVE"
    policy, policy_hash = contract.get_evidence_policy()
    assert policy == POLICY
    assert policy_hash == hashlib.sha256(POLICY.encode()).hexdigest()


def test_fetch_exception_fails_closed_and_is_retryable(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="fetch-exception")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    direct_vm._strict_mock_mode = True
    contract.record_finding("root")
    attempt = contract.get_evidence_attempt("root", 1)
    assert contract.get_obligation("root").status == "INCONCLUSIVE"
    assert attempt.failure_code == "FETCH_EXCEPTION"
    assert contract.get_obligation("root").evidence_retries == 0


def test_validator_rechecks_body_and_rejects_disagreement(direct_vm, direct_deploy, direct_owner, direct_bob, direct_charlie):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="validator-disagreement")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    reads = [0]

    def changing_source(_request):
        reads[0] += 1
        body = BODY.encode() if reads[0] == 1 else b"different validator bytes"
        return {"ok": {"response": {"status": 200, "headers": {}, "body": body}}}

    direct_vm._live_web_handler = changing_source
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"FULFILLED","requirement_match":true,"policy_match":true,"evidence_sufficiency":"SUFFICIENT","rationale":"leader"}',
    )
    direct_vm.sender = direct_charlie
    contract.record_finding("root")
    # Direct Mode commits leader state locally; invoke its captured validator to
    # assert that the divergent re-fetch is rejected by the consensus validator.
    assert direct_vm.run_validator() is False


def test_three_inconclusive_retries_are_bounded_and_a_fourth_is_rejected(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="retry-limit")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    expected_hash = hashlib.sha256(b"expected evidence").hexdigest()
    direct_vm.sender = direct_bob
    contract.submit_evidence("root", "https://evidence.example.com/receipt", expected_hash)
    for retry in range(4):
        direct_vm.clear_mocks()
        direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": "changed evidence"})
        direct_vm.sender = direct_charlie_if_available(direct_vm)
        contract.record_finding("root")
        obligation = contract.get_obligation("root")
        if retry < 3:
            assert obligation.evidence_retries == retry
            direct_vm.sender = direct_bob
            contract.submit_evidence("root", "https://evidence.example.com/receipt", expected_hash)
        else:
            assert obligation.status == "INCONCLUSIVE"
            assert obligation.evidence_retries == 3
            direct_vm.sender = direct_bob
            with direct_vm.expect_revert("retry limit"):
                contract.submit_evidence("root", "https://evidence.example.com/receipt", expected_hash)
    assert contract.get_obligation("root").attempt_count == 4
    for attempt_number in range(1, 5):
        attempt = contract.get_evidence_attempt("root", attempt_number)
        assert attempt.attempt_number == attempt_number
        assert attempt.finding == "INCONCLUSIVE"
        assert attempt.evidence_hash == expected_hash


def test_cure_rounds_and_evidence_retries_are_independent(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="cure-vs-retry")
    _add_root(contract, max_cures=1)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob)
    _submit(contract, direct_vm, direct_bob)
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": BODY})
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"REMEDIABLE","requirement_match":false,"policy_match":true,"evidence_sufficiency":"INSUFFICIENT","rationale":"needs signature"}',
    )
    direct_vm.sender = direct_bob
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "CURE_REQUIRED"
    assert contract.get_obligation("root").cure_rounds == 1
    assert contract.get_obligation("root").evidence_retries == 0
    direct_vm.clear_mocks()
    _submit(contract, direct_vm, direct_bob)
    direct_vm.mock_web(r"evidence\.example\.com/receipt", {"method": "GET", "status": 200, "body": BODY})
    direct_vm.mock_llm(
        "Accept only signed delivery receipts",
        '{"finding":"REMEDIABLE","requirement_match":false,"policy_match":true,"evidence_sufficiency":"INSUFFICIENT","rationale":"still needs signature"}',
    )
    contract.record_finding("root")
    assert contract.get_obligation("root").status == "BREACHED"
    assert contract.get_obligation("root").cure_rounds == 1
    assert contract.get_warranty()[3] == "TERMINAL"


def test_unfunded_agreement_can_be_cancelled_and_partial_amount_refunded(direct_vm, direct_deploy, direct_owner, direct_bob):
    contract = _new_contract(direct_deploy, direct_vm, direct_owner, direct_bob, suffix="cancel-partial")
    _add_root(contract)
    _accept_and_fund(contract, direct_vm, direct_owner, direct_bob, bond=100, partial=25)
    direct_vm.warp("2030-01-01T00:00:00Z")
    contract.cancel_unfunded()
    assert contract.get_warranty()[3] == "CANCELLED"
    assert contract.get_settlement() == (25, 0, 25)
