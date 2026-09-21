from dharma.network.federation_state import FederationState

def test_join():
    f=FederationState(); assert f.join("A","1")
def test_active():
    f=FederationState(); f.join("A","1"); assert f.active("A")
def test_leave():
    f=FederationState(); f.join("A","1"); f.leave("A"); assert not f.active("A")
def test_revoke():
    f=FederationState(); f.join("A","1"); f.revoke("A"); assert not f.active("A")
def test_block_rejoin():
    f=FederationState(); f.revoke("A"); assert not f.join("A","1")
def test_count():
    f=FederationState(); f.join("A","1"); f.join("B","2"); assert f.count()==2
def test_empty():
    assert FederationState().count()==0
def test_leave_missing():
    assert not FederationState().leave("X")
def test_revoke_missing():
    FederationState().revoke("X")
def test_multiple():
    f=FederationState(); [f.join(str(i),str(i)) for i in range(5)]; assert f.count()==5
def test_revoke_removes():
    f=FederationState(); f.join("A","1"); f.revoke("A"); assert f.count()==0
def test_other_member():
    f=FederationState(); f.join("A","1"); f.join("B","2"); f.revoke("A"); assert f.active("B")
