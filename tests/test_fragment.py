from dharma.network.fragment import Fragmenter, Reassembler

def test_split():
    assert len(Fragmenter.split("abcdefgh",4)) == 2

def test_join():
    f = Fragmenter.split("hello world",5)
    assert Reassembler.join(f) == "hello world"

def test_sequence():
    f = Fragmenter.split("abcdef",2)
    assert f[1]["seq"] == 1

def test_total():
    f = Fragmenter.split("abcdef",2)
    assert f[0]["total"] == 3

def test_missing():
    f = Fragmenter.split("abcdef",2)
    assert Reassembler.join(f[:-1]) is None

def test_empty():
    assert Reassembler.join([]) is None

def test_order():
    f = Fragmenter.split("network",3)
    assert Reassembler.join(list(reversed(f))) == "network"

def test_exact_size():
    assert len(Fragmenter.split("abcd",4)) == 1
