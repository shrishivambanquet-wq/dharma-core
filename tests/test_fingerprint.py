from dharma.authority.fingerprint import Fingerprint

def test_same_text_same_hash():
    assert Fingerprint.of("Dharma") == Fingerprint.of("Dharma")

def test_different_text_different_hash():
    assert Fingerprint.of("A") != Fingerprint.of("B")

def test_sha256_length():
    assert len(Fingerprint.of("Dharma")) == 64

def test_empty_string():
    assert len(Fingerprint.of("")) == 64

def test_case_sensitive():
    assert Fingerprint.of("dharma") != Fingerprint.of("Dharma")
