from dharma.network.discovery import Discovery

def test_announce():
    assert Discovery().announce("node")

def test_name_a():
    assert Discovery().announce("A")

def test_name_b():
    assert Discovery().announce("B")

def test_name_c():
    assert Discovery().announce("C")

def test_numeric():
    assert Discovery().announce("123")

def test_long():
    assert Discovery().announce("node-001")

def test_repeat():
    d=Discovery()
    assert d.announce("x")
    assert d.announce("x")

def test_empty():
    assert Discovery().announce("")
