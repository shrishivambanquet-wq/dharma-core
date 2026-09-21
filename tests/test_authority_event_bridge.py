from dharma.network.authority_event_bridge import AuthorityEventBridge

def test_grant():
    b=AuthorityEventBridge()
    assert b.grant("A","B")["name"]=="authority.grant"

def test_revoke():
    b=AuthorityEventBridge()
    assert b.revoke("A","B")["name"]=="authority.revoke"

def test_join():
    b=AuthorityEventBridge()
    assert b.join("A")["name"]=="federation.join"

def test_leave():
    b=AuthorityEventBridge()
    assert b.leave("A")["name"]=="federation.leave"

def test_payload():
    b=AuthorityEventBridge()
    assert b.grant("A","B")["payload"]["target"]=="B"

def test_count():
    b=AuthorityEventBridge()
    b.join("A"); b.leave("A")
    assert b.count()==2

def test_many():
    b=AuthorityEventBridge()
    [b.join(str(i)) for i in range(5)]
    assert b.count()==5

def test_actor():
    b=AuthorityEventBridge()
    assert b.grant("X","Y")["payload"]["actor"]=="X"

def test_target():
    b=AuthorityEventBridge()
    assert b.revoke("X","Y")["payload"]["target"]=="Y"

def test_join_payload():
    b=AuthorityEventBridge()
    assert b.join("node1")["payload"]["node"]=="node1"

def test_leave_payload():
    b=AuthorityEventBridge()
    assert b.leave("node1")["payload"]["node"]=="node1"

def test_order():
    b=AuthorityEventBridge()
    b.join("A"); b.leave("A")
    assert b.count()==2
