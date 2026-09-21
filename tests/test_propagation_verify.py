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


def test_propagates_true():
    assert RevocationPropagation(build()).propagates("A", "D")


def test_propagates_false():
    assert not RevocationPropagation(build()).propagates("C", "A")


def test_count_root():
    assert RevocationPropagation(build()).count("A") == 3


def test_count_middle():
    assert RevocationPropagation(build()).count("B") == 2


def test_count_leaf():
    assert RevocationPropagation(build()).count("D") == 0
