from dataclasses import dataclass


@dataclass(frozen=True)
class DharmaRelease:
    name: str = "Dharma"
    version: str = "v0.1-alpha"
    frozen: bool = True
    protocol_level: int = 30

    def banner(self):
        return f"{self.name} {self.version}"

    def is_alpha(self):
        return self.version.endswith("alpha")
