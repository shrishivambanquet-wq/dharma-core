"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field

from .ledger_entry import LedgerEntry


@dataclass
class Ledger:
    entries: list[LedgerEntry] = field(default_factory=list)

    def append(self, payload: str):
        previous = self.entries[-1].hash() if self.entries else ""
        self.entries.append(LedgerEntry(payload, previous))

    def count(self):
        return len(self.entries)

    def verify(self):
        previous = ""

        for entry in self.entries:
            if entry.previous_hash != previous:
                return False
            previous = entry.hash()

        return True
