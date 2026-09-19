from dharma.authority.ledger import Ledger


def test_append():
    l = Ledger()
    l.append("Genesis")
    assert l.count() == 1


def test_chain_valid():
    l = Ledger()
    l.append("A")
    l.append("B")
    l.append("C")
    assert l.verify()


def test_tamper_detected():
    l = Ledger()
    l.append("A")
    l.append("B")
    l.entries[1].previous_hash = "broken"
    assert not l.verify()


def test_genesis_previous_empty():
    l = Ledger()
    l.append("Genesis")
    assert l.entries[0].previous_hash == ""


def test_multiple_entries():
    l = Ledger()
    for i in range(5):
        l.append(str(i))
    assert l.count() == 5
