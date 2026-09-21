"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.auth import SessionAuth
from dharma.network.token import SessionToken


def test_auth_success():
    t = SessionToken.create()
    assert SessionAuth(t).authenticate(t.value)


def test_auth_fail():
    t = SessionToken.create()
    assert not SessionAuth(t).authenticate("wrong")


def test_short_matches():
    t = SessionToken.create()
    assert SessionAuth(t).short() == t.short()


def test_token_exists():
    assert SessionAuth(SessionToken.create()).token is not None


def test_empty_fails():
    t = SessionToken.create()
    assert not SessionAuth(t).authenticate("")
