"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .event_bus import EventBus
from .event_subscription import EventSubscription
from .event_replay import EventReplay
from .event_integrity import EventIntegrity

class EventSystem:
    def __init__(self):
        self.bus = EventBus()
        self.subscriptions = EventSubscription()
        self.replay = EventReplay()
        self.integrity = EventIntegrity()

    def publish(self, name, payload=None):
        event = self.bus.publish(name, payload)
        self.subscriptions.publish(name, payload)
        return event

    def digest(self, event):
        return self.integrity.digest(event)

    def verify(self, event, digest):
        return self.integrity.verify(event, digest)
