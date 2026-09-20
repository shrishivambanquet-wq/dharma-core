from dharma.network.compatibility import Compatibility

A = {
    "protocol":"0.2.0-alpha",
    "features":["wire","heartbeat","routing"]
}

B = {
    "protocol":"0.2.0-alpha",
    "features":["wire","heartbeat","fragmentation"]
}

def test_protocol():
    assert Compatibility.negotiate(A,B)["protocol"]=="0.2.0-alpha"

def test_shared():
    assert Compatibility.negotiate(A,B)["shared"]==["heartbeat","wire"]

def test_same():
    assert Compatibility.negotiate(A,A)["shared"]

def test_empty():
    x={"protocol":"0.2.0-alpha","features":[]}
    assert Compatibility.negotiate(x,x)["shared"]==[]

def test_mismatch():
    y={"protocol":"0.3","features":["wire"]}
    assert Compatibility.negotiate(A,y) is None

def test_one_feature():
    x={"protocol":"0.2.0-alpha","features":["wire"]}
    assert Compatibility.negotiate(A,x)["shared"]==["wire"]

def test_sorted():
    x={"protocol":"0.2.0-alpha","features":["wire","heartbeat"]}
    assert Compatibility.negotiate(A,x)["shared"]==["heartbeat","wire"]

def test_duplicate():
    x={"protocol":"0.2.0-alpha","features":["wire","wire"]}
    assert Compatibility.negotiate(A,x)["shared"]==["wire"]
