from dharma.federation.trust import TrustRequest, TrustResponse


def test_request_id():
    assert TrustRequest("A", "Company").authority_id == "A"


def test_requester():
    assert TrustRequest("A", "Company").requester == "Company"


def test_response_true():
    assert TrustResponse("A", True, "University").trusted


def test_response_false():
    assert not TrustResponse("A", False, "University").trusted


def test_responder():
    assert TrustResponse("A", True, "University").responder == "University"
