from dharma.authority.trust_path import TrustPath

def test_path_starts_empty():
    p = TrustPath()
    assert p.length() == 0

def test_add_one_node():
    p = TrustPath()
    p.add("A")
    assert p.length() == 1

def test_add_two_nodes():
    p = TrustPath()
    p.add("A")
    p.add("B")
    assert p.length() == 2

def test_first_node():
    p = TrustPath()
    p.add("A")
    p.add("B")
    assert p.first() == "A"

def test_last_node():
    p = TrustPath()
    p.add("A")
    p.add("B")
    assert p.last() == "B"
