class ProtocolFreeze:
    def __init__(self):
        self.frozen=False

    def freeze(self):
        self.frozen=True

    def status(self):
        return self.frozen
