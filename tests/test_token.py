"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.token import SessionToken


def test_create():
    assert isinstance(SessionToken.create().value, str)


def test_not_empty():
    assert len(SessionToken.create().value) > 0


def test_short():
    assert len(SessionToken.create().short()) == 8


def test_unique():
    assert SessionToken.create().value != SessionToken.create().value


def test_same_short():
    t = SessionToken.create()
    assert t.short() == t.value[:8]
