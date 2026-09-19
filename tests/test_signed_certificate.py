from dharma.authority.signed_certificate import SignedCertificate
from dharma.authority.signer import AuthoritySigner


def test_fingerprint_exists():
    c = SignedCertificate("A", "B", "delegates")
    assert len(c.fingerprint()) == 64


def test_sign_and_verify():
    s = AuthoritySigner.generate()
    c = SignedCertificate("A", "B", "delegates")
    sig = c.sign(s)
    assert c.verify(s, sig)


def test_tampered_subject_fails():
    s = AuthoritySigner.generate()
    c1 = SignedCertificate("A", "B", "delegates")
    sig = c1.sign(s)
    c2 = SignedCertificate("A", "C", "delegates")
    assert not c2.verify(s, sig)


def test_tampered_relation_fails():
    s = AuthoritySigner.generate()
    c1 = SignedCertificate("A", "B", "delegates")
    sig = c1.sign(s)
    c2 = SignedCertificate("A", "B", "represents")
    assert not c2.verify(s, sig)


def test_same_payload_same_fingerprint():
    c1 = SignedCertificate("A", "B", "delegates")
    c2 = SignedCertificate("A", "B", "delegates")
    assert c1.fingerprint() == c2.fingerprint()
