"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import time
from dharma.network.chain_validation import CertificateChain
from dharma.network.federation_certificate import FederationCertificate


def cert(i,s):
    now=int(time.time())
    return FederationCertificate(i,s,now,now+3600,b"x")


def test_single():
    assert CertificateChain().validate([cert("Root","Root")])


def test_two():
    assert CertificateChain().validate([cert("Root","A"),cert("A","B")])


def test_three():
    assert CertificateChain().validate([
        cert("Root","A"),
        cert("A","B"),
        cert("B","C")
    ])


def test_broken():
    assert not CertificateChain().validate([
        cert("Root","A"),
        cert("X","B")
    ])


def test_order():
    assert not CertificateChain().validate([
        cert("A","B"),
        cert("Root","A")
    ])


def test_empty():
    assert not CertificateChain().validate([])


def test_root():
    assert CertificateChain().validate([cert("Root","Root")])


def test_duplicate():
    c=[cert("Root","Root")]
    assert CertificateChain().validate(c)
    assert CertificateChain().validate(c)


def test_subject():
    assert cert("A","B").subject=="B"


def test_issuer():
    assert cert("A","B").issuer=="A"


def test_chain_length():
    c=[cert("Root","Root")]
    assert len(c)==1
