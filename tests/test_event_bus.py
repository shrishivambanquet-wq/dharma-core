from dharma.network.event_bus import EventBus

def test_publish():
    b=EventBus(); assert b.publish("join")["name"]=="join"
def test_payload():
    b=EventBus(); assert b.publish("join",{"n":"A"})["payload"]["n"]=="A"
def test_latest():
    b=EventBus(); b.publish("x"); assert b.latest()["name"]=="x"
def test_count():
    b=EventBus(); b.publish("a"); b.publish("b"); assert b.count()==2
def test_empty():
    assert EventBus().latest() is None
def test_filter():
    b=EventBus(); b.publish("a"); b.publish("b"); b.publish("a"); assert len(b.by_name("a"))==2
def test_unknown():
    assert EventBus().by_name("x")==[]
def test_many():
    b=EventBus(); [b.publish(str(i)) for i in range(5)]; assert b.count()==5
def test_order():
    b=EventBus(); b.publish("1"); b.publish("2"); assert b.latest()["name"]=="2"
def test_none_payload():
    assert EventBus().publish("x")["payload"] is None
def test_payload_obj():
    b=EventBus(); p={"k":1}; b.publish("x",p); assert b.latest()["payload"]==p
def test_first():
    b=EventBus(); b.publish("a"); assert b.by_name("a")[0]["name"]=="a"
