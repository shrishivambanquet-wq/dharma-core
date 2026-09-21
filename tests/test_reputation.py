"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.reputation import Reputation

def test_default():
    assert Reputation().score("A")==0

def test_reward():
    r=Reputation(); r.reward("A")
    assert r.score("A")==1

def test_reward_many():
    r=Reputation(); r.reward("A",5)
    assert r.score("A")==5

def test_penalty():
    r=Reputation(); r.penalize("A")
    assert r.score("A")==-1

def test_penalty_many():
    r=Reputation(); r.penalize("A",4)
    assert r.score("A")==-4

def test_reset():
    r=Reputation(); r.reward("A"); r.reset("A")
    assert r.score("A")==0

def test_known():
    r=Reputation(); r.reward("A")
    assert r.known("A")

def test_unknown():
    assert not Reputation().known("X")

def test_top():
    r=Reputation()
    r.reward("A",2); r.reward("B",5)
    assert r.top()=="B"

def test_empty_top():
    assert Reputation().top() is None

def test_count():
    r=Reputation()
    r.reward("A"); r.reward("B")
    assert r.count()==2

def test_mixed():
    r=Reputation()
    r.reward("A",5); r.penalize("A",2)
    assert r.score("A")==3
