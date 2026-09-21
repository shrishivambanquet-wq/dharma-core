from dharma.network.event_bus import EventBus

class AuthorityEventBridge:
    def __init__(self):
        self.bus = EventBus()

    def grant(self, actor, target):
        return self.bus.publish("authority.grant", {"actor":actor,"target":target})

    def revoke(self, actor, target):
        return self.bus.publish("authority.revoke", {"actor":actor,"target":target})

    def join(self, node):
        return self.bus.publish("federation.join", {"node":node})

    def leave(self, node):
        return self.bus.publish("federation.leave", {"node":node})

    def count(self):
        return self.bus.count()
