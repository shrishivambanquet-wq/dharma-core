from dataclasses import dataclass
from .trust_enums import TrustLevel

@dataclass
class TrustScore:
    value: float

    def clamp(self):
        self.value = max(0.0, min(1.0, self.value))
        return self

    @classmethod
    def from_level(cls, level: TrustLevel):
        return cls(level.value)
    def propagate(self, weight: float):
        return TrustScore(self.value * weight).clamp()
