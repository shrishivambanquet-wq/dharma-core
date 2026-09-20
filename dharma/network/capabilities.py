from dataclasses import dataclass, field

DEFAULT_CAPABILITIES = {
    "wire_v1",
    "ed25519",
    "replay_guard",
    "session_resume",
}

@dataclass
class CapabilitySet:
    supported: set = field(default_factory=lambda: set(DEFAULT_CAPABILITIES))

    def advertise(self):
        return sorted(self.supported)

    def negotiate(self, remote):
        return sorted(self.supported.intersection(remote.supported))
