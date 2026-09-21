"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.certificate_registry import CertificateRegistry

CERT={"node":"A","public_key":"pk","issued_at":1,"expires_at":100}

def test_register():
    r=CertificateRegistry()
    assert r.register(CERT)

def test_exists():
    r=CertificateRegistry(); r.register(CERT)
    assert r.exists("A")

def test_get():
    r=CertificateRegistry(); r.register(CERT)
    assert r.get("A")["public_key"]=="pk"

def test_missing():
    assert CertificateRegistry().get("X") is None

def test_count():
    r=CertificateRegistry()
    r.register(CERT)
    r.register({"node":"B","public_key":"k","issued_at":1,"expires_at":2})
    assert r.count()==2

def test_revoke():
    r=CertificateRegistry(); r.register(CERT)
    assert r.revoke("A")

def test_revoke_missing():
    assert not CertificateRegistry().revoke("X")

def test_overwrite():
    r=CertificateRegistry()
    r.register(CERT)
    r.register({"node":"A","public_key":"new","issued_at":1,"expires_at":2})
    assert r.get("A")["public_key"]=="new"

def test_exists_false():
    assert not CertificateRegistry().exists("Z")

def test_count_empty():
    assert CertificateRegistry().count()==0

def test_multiple():
    r=CertificateRegistry()
    for i in range(5):
        r.register({"node":str(i),"public_key":"k","issued_at":1,"expires_at":2})
    assert r.count()==5

def test_after_revoke():
    r=CertificateRegistry(); r.register(CERT); r.revoke("A")
    assert not r.exists("A")
