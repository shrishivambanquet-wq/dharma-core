from dharma.network.handshake import DCPHandshake


def test_hello_type():
    assert DCPHandshake("A").hello("B").message_type == "hello"


def test_sender():
    assert DCPHandshake("A").hello("B").sender == "A"


def test_receiver():
    assert DCPHandshake("A").hello("B").receiver == "B"


def test_accept_same_version():
    h = DCPHandshake("A")
    assert h.accepts(h.hello("B"))


def test_reject_wrong_version():
    h = DCPHandshake("A")
    msg = h.hello("B")
    msg.payload["version"] = "9.9"
    assert not h.accepts(msg)
