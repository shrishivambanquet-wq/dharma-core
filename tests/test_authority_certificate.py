from dharma.network.authority_certificate import AuthorityCertificate
import time

def test_node():
    c=AuthorityCertificate("A","pk").issue()
    assert c["node"]=="A"

def test_key():
    c=AuthorityCertificate("A","pk").issue()
    assert c["public_key"]=="pk"

def test_issue():
    c=AuthorityCertificate("A","pk").issue()
    assert c["issued_at"]>0

def test_expiry():
    c=AuthorityCertificate("A","pk",10).issue()
    assert c["expires_at"]==c["issued_at"]+10

def test_valid():
    c=AuthorityCertificate("A","pk",10).issue()
    assert AuthorityCertificate.valid(c,c["issued_at"]+5)

def test_expired():
    c=AuthorityCertificate("A","pk",1).issue()
    assert not AuthorityCertificate.valid(c,c["issued_at"]+2)

def test_zero_ttl():
    c=AuthorityCertificate("A","pk",0).issue()
    assert AuthorityCertificate.valid(c,c["issued_at"])

def test_many():
    for i in range(5):
        AuthorityCertificate(str(i),"pk").issue()

def test_public():
    assert AuthorityCertificate("A","PUB").issue()["public_key"]=="PUB"

def test_repeat():
    a=AuthorityCertificate("A","pk").issue()
    b=AuthorityCertificate("A","pk").issue()
    assert a["node"]==b["node"]

def test_future():
    c=AuthorityCertificate("A","pk",100).issue()
    assert AuthorityCertificate.valid(c,c["issued_at"]+99)

def test_fields():
    c=AuthorityCertificate("A","pk").issue()
    assert set(c.keys())=={"node","public_key","issued_at","expires_at"}
