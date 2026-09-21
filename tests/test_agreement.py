"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.agreement import (
    TrustAgreement,
    PENDING,
    ACCEPTED,
    REJECTED,
)


def test_default_pending():
    assert TrustAgreement("A", "B").status == PENDING


def test_accept():
    a = TrustAgreement("A", "B")
    a.accept()
    assert a.status == ACCEPTED


def test_reject():
    a = TrustAgreement("A", "B")
    a.reject()
    assert a.status == REJECTED


def test_pending_not_final():
    assert not TrustAgreement("A", "B").is_final()


def test_final_after_accept():
    a = TrustAgreement("A", "B")
    a.accept()
    assert a.is_final()
