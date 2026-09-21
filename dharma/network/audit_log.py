import time

class AuditLog:
    def __init__(self):
        self.entries = []

    def record(self, actor, action, target=None):
        entry = {
            "timestamp": int(time.time()),
            "actor": actor,
            "action": action,
            "target": target,
        }
        self.entries.append(entry)
        return entry

    def latest(self):
        return self.entries[-1] if self.entries else None

    def count(self):
        return len(self.entries)

    def all(self):
        return list(self.entries)
