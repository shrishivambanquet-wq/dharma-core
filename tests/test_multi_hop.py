from dharma.network.multi_hop import MultiHopRouter

def build():
    r = MultiHopRouter()
    r.add_route("A","B",["A","B"])
    r.add_route("A","C",["A","B","C"])
    return r

def test_one_hop():
    assert build().resolve("A","B") == ["A","B"]

def test_two_hop():
    assert build().resolve("A","C") == ["A","B","C"]

def test_unknown():
    assert build().resolve("X","Y") is None

def test_next_hop():
    assert build().next_hop("A","C") == "B"

def test_direct_next():
    assert build().next_hop("A","B") == "B"

def test_loop():
    r = MultiHopRouter()
    r.add_route("A","C",["A","B","A","C"])
    assert r.resolve("A","C") is None

def test_empty():
    assert MultiHopRouter().resolve("A","B") is None

def test_order():
    assert build().resolve("A","C")[1] == "B"
