from dharma.network.event_replay import EventReplay

def test_replay():
    r=EventReplay(); assert r.replay([1,2])==[1,2]
def test_last():
    r=EventReplay(); assert r.last([1,2])==2
def test_empty():
    r=EventReplay(); assert r.last([]) is None
def test_count():
    r=EventReplay(); assert r.count([1,2,3])==3
def test_copy():
    r=EventReplay(); x=[1]; y=r.replay(x); assert y==x
def test_many():
    r=EventReplay(); assert r.count(list(range(5)))==5
def test_single():
    r=EventReplay(); assert r.last([7])==7
def test_zero():
    r=EventReplay(); assert r.count([])==0
def test_strings():
    r=EventReplay(); assert r.last(["a","b"])=="b"
def test_dict():
    r=EventReplay(); assert r.last([{"a":1}])["a"]==1
def test_order():
    r=EventReplay(); assert r.replay([3,2,1])[0]==3
def test_identity():
    r=EventReplay(); assert isinstance(r.replay([]),list)
