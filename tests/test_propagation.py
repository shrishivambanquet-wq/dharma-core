"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.authority_graph import AuthorityGraph
from dharma.authority.propagation import RevocationPropagation


def build():
    g = AuthorityGraph()
    g.connect("A", "B")
    g.connect("B", "C")
    g.connect("C", "D")
    return g


def test_direct_child():
    assert "B" in RevocationPropagation(build()).affected("A")


def test_recursive():
    assert "D" in RevocationPropagation(build()).affected("A")


def test_middle():
    assert RevocationPropagation(build()).affected("B") == ["C", "D"]


def test_leaf():
    assert RevocationPropagation(build()).affected("D") == []


def test_unknown():
    assert RevocationPropagation(build()).affected("X") == []
