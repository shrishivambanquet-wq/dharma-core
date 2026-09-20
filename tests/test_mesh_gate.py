from dharma.network.mesh_gate import MeshGate

def test_forward():
    assert MeshGate().forward("a",3) == "forward"

def test_duplicate():
    m = MeshGate()
    m.forward("x",3)
    assert m.forward("x",3) == "duplicate"

def test_expired():
    assert MeshGate().forward("t",1) == "expired"

def test_new_packet():
    assert MeshGate().forward("n",5) == "forward"

def test_multiple():
    m = MeshGate()
    assert m.forward("1",5) == "forward"
    assert m.forward("2",5) == "forward"

def test_duplicate_after_forward():
    m = MeshGate()
    m.forward("z",5)
    assert m.forward("z",5) == "duplicate"

def test_ttl_survives():
    assert MeshGate().forward("ttl",2) == "forward"

def test_many_packets():
    m = MeshGate()
    for i in range(10):
        assert m.forward(str(i),3) == "forward"
