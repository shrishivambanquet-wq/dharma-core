from dharma.network.auto_connect import AutoConnect

A = {
    "protocol":"0.2.0-alpha",
    "features":["wire","heartbeat","routing"]
}

B = {
    "protocol":"0.2.0-alpha",
    "features":["wire","heartbeat","fragmentation"]
}

def test_connect():
    assert AutoConnect.connect(A,B)["connected"]

def test_protocol():
    assert AutoConnect.connect(A,B)["protocol"]=="0.2.0-alpha"

def test_shared():
    assert AutoConnect.connect(A,B)["shared"]==["heartbeat","wire"]

def test_same():
    assert AutoConnect.connect(A,A)["connected"]

def test_fail():
    bad={"protocol":"0.3","features":["wire"]}
    assert AutoConnect.connect(A,bad) is None

def test_empty():
    x={"protocol":"0.2.0-alpha","features":[]}
    assert AutoConnect.connect(x,x)["shared"]==[]

def test_one_feature():
    x={"protocol":"0.2.0-alpha","features":["wire"]}
    assert AutoConnect.connect(A,x)["shared"]==["wire"]

def test_result_keys():
    assert set(AutoConnect.connect(A,B).keys())=={"connected","protocol","shared"}
