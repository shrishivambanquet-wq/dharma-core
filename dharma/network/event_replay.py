class EventReplay:
    def replay(self, events):
        return list(events)

    def last(self, events):
        return events[-1] if events else None

    def count(self, events):
        return len(events)
