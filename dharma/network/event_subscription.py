class EventSubscription:
    def __init__(self):
        self.subscribers={}

    def subscribe(self,name,listener):
        self.subscribers.setdefault(name,[]).append(listener)

    def publish(self,name,payload=None):
        for l in self.subscribers.get(name,[]):
            l(payload)

    def count(self,name):
        return len(self.subscribers.get(name,[]))
