"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.delegation_proof import DelegationProof
from dharma.authority.certificate_chain import CertificateChain
from dharma.authority.signed_certificate import SignedCertificate


def build_chain():
    c = CertificateChain()
    c.add(SignedCertificate("A", "B", "delegates"))
    c.add(SignedCertificate("B", "C", "delegates"))
    return c


def test_valid_proof():
    assert DelegationProof(build_chain()).is_valid()


def test_broken_chain():
    c = CertificateChain()
    c.add(SignedCertificate("A", "B", "delegates"))
    c.add(SignedCertificate("X", "C", "delegates"))
    assert not DelegationProof(c).is_valid()


def test_root():
    assert DelegationProof(build_chain()).root() == "A"


def test_target():
    assert DelegationProof(build_chain()).target() == "C"


def test_empty_chain():
    assert DelegationProof(CertificateChain()).is_valid()
