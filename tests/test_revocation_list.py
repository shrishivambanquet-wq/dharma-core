"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.revocation_list import RevocationList


def test_starts_empty():
    r = RevocationList()
    assert r.count() == 0


def test_revoke_one():
    r = RevocationList()
    r.revoke("cert-1")
    assert r.is_revoked("cert-1")


def test_not_revoked():
    r = RevocationList()
    assert not r.is_revoked("missing")


def test_count_two():
    r = RevocationList()
    r.revoke("a")
    r.revoke("b")
    assert r.count() == 2


def test_clear():
    r = RevocationList()
    r.revoke("a")
    r.clear()
    assert r.count() == 0

