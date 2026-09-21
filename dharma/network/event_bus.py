class EventBus:
    def __init__(self):
        self.events=[]

    def publish(self,name,payload=None):
        e={"name":name,"payload":payload}
        self.events.append(e)
        return e

    def latest(self):
        return self.events[-1] if self.events else None

    def count(self):
        return len(self.events)

    def by_name(self,name):
        return [e for e in self.events if e["name"]==name]
