"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import time
from dharma.network.session_timeout import SessionTimeout

def test_active():
    assert SessionTimeout("A").active()

def test_timeout():
    s = SessionTimeout("A", timeout=1)
    s.last_activity -= 2
    assert not s.active()

def test_reconnect():
    s = SessionTimeout("A", timeout=1)
    s.last_activity -= 2
    assert s.reconnect()
    assert s.active()

def test_touch():
    s = SessionTimeout("A")
    old = s.last_activity
    time.sleep(0.01)
    s.touch()
    assert s.last_activity > old

def test_session_id():
    assert SessionTimeout("xyz").session_id == "xyz"

def test_timeout_value():
    assert SessionTimeout("A", timeout=99).timeout == 99

def test_multiple_reconnect():
    s = SessionTimeout("A", timeout=1)
    for _ in range(3):
        s.reconnect()
    assert s.active()

def test_last_activity_exists():
    assert SessionTimeout("A").last_activity > 0
