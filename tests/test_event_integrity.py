from dharma.network.event_integrity import EventIntegrity

def test_digest():
    e=EventIntegrity(); assert len(e.digest({"a":1}))==64
def test_verify():
    e=EventIntegrity(); d=e.digest({"a":1}); assert e.verify({"a":1},d)
def test_fail():
    e=EventIntegrity(); d=e.digest({"a":1}); assert not e.verify({"a":2},d)
def test_same():
    e=EventIntegrity(); assert e.digest({"x":1})==e.digest({"x":1})
def test_diff():
    e=EventIntegrity(); assert e.digest({"x":1})!=e.digest({"x":2})
def test_empty():
    e=EventIntegrity(); assert e.verify({},e.digest({}))
def test_string():
    e=EventIntegrity(); assert e.verify({"s":"a"},e.digest({"s":"a"}))
def test_many():
    e=EventIntegrity(); [e.digest({"i":i}) for i in range(5)]
def test_hash_length():
    assert len(EventIntegrity().digest({"a":1}))==64
def test_bool():
    e=EventIntegrity(); assert e.verify({"b":True},e.digest({"b":True}))
def test_nested():
    e=EventIntegrity(); d=e.digest({"a":{"b":1}}); assert e.verify({"a":{"b":1}},d)
def test_list():
    e=EventIntegrity(); d=e.digest({"l":[1,2]}); assert e.verify({"l":[1,2]},d)
