"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.event_system import EventSystem

class AuthorityEventBridge:
    def __init__(self):
        self.events = EventSystem()

    def grant(self, actor, target):
        return self.events.publish("authority.grant", {"actor": actor, "target": target})

    def revoke(self, actor, target):
        return self.events.publish("authority.revoke", {"actor": actor, "target": target})

    def join(self, node):
        return self.events.publish("federation.join", {"node": node})

    def leave(self, node):
        return self.events.publish("federation.leave", {"node": node})

    def count(self):
        return self.events.bus.count()
