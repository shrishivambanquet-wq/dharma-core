import copy
import time

class AuthoritySnapshot:
    def __init__(self):
        self.snapshots = []

    def capture(self, authority_state):
        snap = {
            "timestamp": int(time.time()),
            "state": copy.deepcopy(authority_state),
        }
        self.snapshots.append(snap)
        return snap

    def latest(self):
        return self.snapshots[-1] if self.snapshots else None

    def get(self, index):
        return self.snapshots[index]

    def count(self):
        return len(self.snapshots)
