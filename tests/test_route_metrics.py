"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.route_metrics import RouteMetrics

def test_add():
    r = RouteMetrics()
    r.add("C","B",2)
    assert r.best("C") == ("B",2)

def test_update():
    r = RouteMetrics()
    r.add("C","B",2)
    r.update("C","D",1)
    assert r.best("C") == ("D",1)

def test_unknown():
    assert RouteMetrics().best("X") is None

def test_count():
    r = RouteMetrics()
    r.add("A","B",1)
    r.add("C","D",2)
    assert r.count() == 2

def test_cost():
    r = RouteMetrics()
    r.add("Z","Y",5)
    assert r.best("Z")[1] == 5

def test_overwrite():
    r = RouteMetrics()
    r.add("X","A",4)
    r.add("X","B",3)
    assert r.best("X") == ("B",3)

def test_multiple():
    r = RouteMetrics()
    for i in range(5):
        r.add(str(i),"N",i)
    assert r.count() == 5

def test_next_hop():
    r = RouteMetrics()
    r.add("K","H",7)
    assert r.best("K")[0] == "H"
