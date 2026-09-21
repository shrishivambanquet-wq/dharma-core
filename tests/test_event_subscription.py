"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.event_subscription import EventSubscription

def test_subscribe():
    s=EventSubscription(); s.subscribe("x",lambda p:None); assert s.count("x")==1
def test_publish():
    s=EventSubscription(); out=[]; s.subscribe("x",lambda p:out.append(p)); s.publish("x",1); assert out==[1]
def test_count():
    s=EventSubscription(); s.subscribe("x",lambda p:None); s.subscribe("x",lambda p:None); assert s.count("x")==2
def test_empty():
    assert EventSubscription().count("x")==0
def test_other():
    s=EventSubscription(); s.subscribe("a",lambda p:None); assert s.count("b")==0
def test_many():
    s=EventSubscription(); [s.subscribe("x",lambda p:None) for _ in range(5)]; assert s.count("x")==5
def test_none():
    s=EventSubscription(); out=[]; s.subscribe("x",lambda p:out.append(p)); s.publish("x"); assert out==[None]
def test_order():
    s=EventSubscription(); out=[]; s.subscribe("x",lambda p:out.append(1)); s.subscribe("x",lambda p:out.append(2)); s.publish("x"); assert out==[1,2]
def test_payload():
    s=EventSubscription(); out=[]; s.subscribe("x",lambda p:out.append(p["a"])); s.publish("x",{"a":5}); assert out==[5]
def test_multi_event():
    s=EventSubscription(); out=[]; s.subscribe("a",lambda p:out.append("a")); s.subscribe("b",lambda p:out.append("b")); s.publish("a"); assert out==["a"]
def test_publish_unknown():
    EventSubscription().publish("unknown")
def test_listener():
    s=EventSubscription(); called=[]; s.subscribe("x",lambda p:called.append(True)); s.publish("x"); assert called==[True]
