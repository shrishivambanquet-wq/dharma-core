"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.certificate import AuthorityCertificate
from dharma.authority.revocation_engine import RevocationEngine


def test_new_certificate_valid():
    e = RevocationEngine()
    c = AuthorityCertificate("a", "b", "represents")
    assert e.is_valid(c)


def test_revoke_invalidates():
    e = RevocationEngine()
    c = AuthorityCertificate("a", "b", "represents")
    e.revoke(c)
    assert not e.is_valid(c)


def test_revoked_count():
    e = RevocationEngine()
    c1 = AuthorityCertificate("a", "b", "represents")
    c2 = AuthorityCertificate("b", "c", "delegates")
    e.revoke(c1)
    e.revoke(c2)
    assert e.revoked_count() == 2


def test_certificate_marked_revoked():
    e = RevocationEngine()
    c = AuthorityCertificate("a", "b", "represents")
    e.revoke(c)
    assert c.revoked


def test_unknown_certificate_stays_valid():
    e = RevocationEngine()
    c = AuthorityCertificate("x", "y", "verify")
    assert e.is_valid(c)

