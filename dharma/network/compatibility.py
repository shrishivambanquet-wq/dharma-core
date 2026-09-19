from dataclasses import dataclass


@dataclass
class Compatibility:
    local_version: str = "0.1"

    def supports(self, remote_version: str):
        return remote_version == self.local_version

    def negotiate(self, remote_version: str):
        if self.supports(remote_version):
            return self.local_version
        return None
