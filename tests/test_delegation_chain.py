"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.delegation_chain import DelegationChain
def test_delegate():
 c=DelegationChain();c.delegate("A","B");assert c.parent("B")=="A"
def test_root():
 c=DelegationChain();c.delegate("A","B");c.delegate("B","C");assert c.root("C")=="A"
def test_missing():
 assert DelegationChain().parent("X") is None
def test_self():
 c=DelegationChain();assert c.root("A")=="A"
def test_chain():
 c=DelegationChain();c.delegate("A","B");assert c.root("B")=="A"
def test_three():
 c=DelegationChain();c.delegate("A","B");c.delegate("B","C");assert c.parent("C")=="B"
def test_overwrite():
 c=DelegationChain();c.delegate("A","B");c.delegate("X","B");assert c.parent("B")=="X"
def test_empty():
 assert DelegationChain().root("Z")=="Z"
def test_many():
 c=DelegationChain();[c.delegate("R",str(i)) for i in range(5)];assert c.parent("4")=="R"
def test_direct():
 c=DelegationChain();c.delegate("A","B");assert c.parent("B")=="A"
def test_root2():
 c=DelegationChain();c.delegate("A","B");c.delegate("B","C");c.delegate("C","D");assert c.root("D")=="A"
def test_leaf():
 c=DelegationChain();c.delegate("A","B");assert c.root("B")=="A"
