from dharma.network.session import TrustSession


def test_session_id():
    assert TrustSession("s1","A","B").session_id == "s1"


def test_active_default():
    assert TrustSession("s1","A","B").is_active()


def test_close():
    s = TrustSession("s1","A","B")
    s.close()
    assert not s.is_active()


def test_requester():
    assert TrustSession("s1","A","B").requester == "A"


def test_responder():
    assert TrustSession("s1","A","B").responder == "B"
