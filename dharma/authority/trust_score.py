class TrustScore:
    def __init__(self, value=0.0):
        self.value = max(0.0, min(1.0, value))

    def increase(self, amount):
        self.value = min(1.0, self.value + amount)

    def decrease(self, amount):
        self.value = max(0.0, self.value - amount)

    def is_verified(self):
        return self.value == 1.0

