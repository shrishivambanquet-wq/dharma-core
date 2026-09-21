"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import pytest
from dharma.network.session_lifecycle import SessionLifecycle

def test_default():
    assert SessionLifecycle().current() == "DISCOVERED"

def test_negotiating():
    s = SessionLifecycle()
    assert s.transition("NEGOTIATING") == "NEGOTIATING"

def test_connected():
    s = SessionLifecycle()
    s.transition("CONNECTED")
    assert s.current() == "CONNECTED"

def test_active():
    s = SessionLifecycle()
    s.transition("ACTIVE")
    assert s.current() == "ACTIVE"

def test_disconnect():
    s = SessionLifecycle()
    s.transition("DISCONNECTED")
    assert s.current() == "DISCONNECTED"

def test_invalid():
    with pytest.raises(ValueError):
        SessionLifecycle().transition("BROKEN")

def test_multiple():
    s = SessionLifecycle()
    s.transition("NEGOTIATING")
    s.transition("CONNECTED")
    s.transition("ACTIVE")
    assert s.current() == "ACTIVE"

def test_back():
    s = SessionLifecycle()
    s.transition("CONNECTED")
    s.transition("DISCONNECTED")
    assert s.current() == "DISCONNECTED"
