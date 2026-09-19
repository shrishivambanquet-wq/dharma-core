from dharma.authority.snapshot import AuthoritySnapshot
from dharma.authority.index import AuthorityIndex
from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind


def test_snapshot_size():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "A", "A"))
    snap = AuthoritySnapshot(idx)
    assert snap.size() == 1


def test_snapshot_restore():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "A", "A"))
    snap = AuthoritySnapshot(idx)

    idx.add(AuthorityNode(AuthorityKind.PERSON, "B", "B"))
    snap.restore(idx)

    assert idx.count() == 1
def test_empty_snapshot():
    idx = AuthorityIndex()
    snap = AuthoritySnapshot(idx)
    assert snap.size() == 0

def test_restore_empty():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "A", "A"))
    snap = AuthoritySnapshot(AuthorityIndex())
    snap.restore(idx)
    assert idx.count() == 0

def test_snapshot_independent():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "A", "A"))
    snap = AuthoritySnapshot(idx)
    idx.add(AuthorityNode(AuthorityKind.PERSON, "B", "B"))
    assert snap.size() == 1

def test_double_restore():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "A", "A"))
    snap = AuthoritySnapshot(idx)
    snap.restore(idx)
    snap.restore(idx)
    assert idx.count() == 1

def test_restore_keeps_original_name():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "Alpha", "A"))
    snap = AuthoritySnapshot(idx)
    snap.restore(idx)
    assert idx.get("A").name == "Alpha"

def test_snapshot_after_multiple_adds():
    idx = AuthorityIndex()
    for i in range(5):
        idx.add(AuthorityNode(AuthorityKind.PERSON, str(i), str(i)))
    snap = AuthoritySnapshot(idx)
    assert snap.size() == 5

def test_restore_after_clear():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "A", "A"))
    snap = AuthoritySnapshot(idx)
    idx._authorities.clear()
    snap.restore(idx)
    assert idx.count() == 1

def test_snapshot_is_deep_copy():
    idx = AuthorityIndex()
    node = AuthorityNode(AuthorityKind.PERSON, "A", "A")
    idx.add(node)
    snap = AuthoritySnapshot(idx)
    node.name = "Changed"
    snap.restore(idx)
    assert idx.get("A").name == "A"
