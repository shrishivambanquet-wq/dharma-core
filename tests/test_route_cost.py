"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import pytest
from dharma.network.route_cost import RouteCostRouter

def build():
    r = RouteCostRouter()
    r.add("A","C",["A","B","C"],4)
    r.add("A","C",["A","D","C"],6)
    return r

def test_lower_cost():
    assert build().best("A","C")[0] == 4

def test_next_hop():
    assert build().next_hop("A","C") == "B"

def test_unknown():
    assert build().best("X","Y") is None

def test_direct():
    r = RouteCostRouter()
    r.add("A","B",["A","B"],1)
    assert r.next_hop("A","B") == "B"

def test_equal_cost():
    r = RouteCostRouter()
    r.add("A","C",["A","B","C"],5)
    r.add("A","C",["A","D","C"],5)
    assert r.best("A","C")[0] == 5

def test_cost_preserved():
    assert build().best("A","C")[0] == 4

def test_multiple():
    assert len(build().routes[("A","C")]) == 2

def test_loop():
    with pytest.raises(ValueError):
        RouteCostRouter().add("A","C",["A","B","A","C"],5)
