import time
from dharma.network.ed25519 import Ed25519Identity
from dharma.network.federation_certificate import FederationCertificate


def make(identity):
    now = int(time.time())
    return FederationCertificate(
        "Ahmedabad",
        "Delhi",
        now,
        now + 3600,
    ).sign(identity)


def test_valid():
    i = Ed25519Identity.create()
    assert make(i).verify(i.verify_key())


def test_expired():
    i = Ed25519Identity.create()
    now = int(time.time())
    c = FederationCertificate("A","B",now-10,now-1).sign(i)
    assert not c.verify(i.verify_key())


def test_wrong_key():
    a = Ed25519Identity.create()
    b = Ed25519Identity.create()
    assert not make(a).verify(b.verify_key())


def test_tampered_issuer():
    i = Ed25519Identity.create()
    c = make(i)
    c.issuer = "Mumbai"
    assert not c.verify(i.verify_key())


def test_tampered_subject():
    i = Ed25519Identity.create()
    c = make(i)
    c.subject = "London"
    assert not c.verify(i.verify_key())


def test_signature_required():
    now = int(time.time())
    c = FederationCertificate("A","B",now,now+100)
    assert not c.verify(Ed25519Identity.create().verify_key())


def test_future_valid():
    i = Ed25519Identity.create()
    assert make(i).expires_at > int(time.time())


def test_duplicate():
    i = Ed25519Identity.create()
    c = make(i)
    assert c.verify(i.verify_key())
    assert c.verify(i.verify_key())


def test_payload():
    assert b"issuer" in make(Ed25519Identity.create()).payload()


def test_subject():
    assert make(Ed25519Identity.create()).subject == "Delhi"
