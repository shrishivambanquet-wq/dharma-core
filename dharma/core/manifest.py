"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class DharmaManifest:
    protocol: str = "Dharma"
    release: str = "v0.1-alpha"
    drfc: int = 30
    stable_api: bool = True

    def summary(self):
        return {
            "protocol": self.protocol,
            "release": self.release,
            "drfc": self.drfc,
            "stable_api": self.stable_api,
        }
