from dataclasses import dataclass


@dataclass(frozen=True)
class DharmaConstitution:
    protocol_name: str = "Dharma"
    version: str = "0.1-alpha"
    compatibility: str = "backward-compatible"
    governance: str = "DRFC"

    def identity(self):
        return f"{self.protocol_name}/{self.version}"

    def promises(self):
        return {
            "compatibility": self.compatibility,
            "governance": self.governance,
        }
