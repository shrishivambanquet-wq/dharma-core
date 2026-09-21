from dharma.network.authority_snapshot import AuthoritySnapshot

def test_capture():
    s=AuthoritySnapshot()
    assert s.capture({"A":1})["state"]=={"A":1}

def test_latest():
    s=AuthoritySnapshot(); s.capture({"A":1})
    assert s.latest()["state"]=={"A":1}

def test_count():
    s=AuthoritySnapshot(); s.capture({}); s.capture({})
    assert s.count()==2

def test_empty():
    assert AuthoritySnapshot().latest() is None

def test_get():
    s=AuthoritySnapshot(); s.capture({"A":1})
    assert s.get(0)["state"]=={"A":1}

def test_deepcopy():
    s=AuthoritySnapshot()
    d={"A":[1]}
    s.capture(d)
    d["A"].append(2)
    assert s.latest()["state"]["A"]==[1]

def test_timestamp():
    assert AuthoritySnapshot().capture({})["timestamp"]>0

def test_many():
    s=AuthoritySnapshot()
    [s.capture({"i":i}) for i in range(5)]
    assert s.count()==5

def test_first():
    s=AuthoritySnapshot()
    s.capture({"A":1}); s.capture({"A":2})
    assert s.get(0)["state"]["A"]==1

def test_second():
    s=AuthoritySnapshot()
    s.capture({"A":1}); s.capture({"A":2})
    assert s.get(1)["state"]["A"]==2

def test_latest_changes():
    s=AuthoritySnapshot()
    s.capture({"A":1}); s.capture({"A":3})
    assert s.latest()["state"]["A"]==3

def test_keys():
    snap=AuthoritySnapshot().capture({})
    assert set(snap.keys())=={"timestamp","state"}
