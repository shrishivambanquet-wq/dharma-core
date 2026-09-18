from .trust_score import TrustScore


class TrustPolicy:
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def allows(self, score: TrustScore):
        return score.value >= self.threshold

    def deny(self, score: TrustScore):
        return not self.allows(score)

    def set_threshold(self, value):
        self.threshold = value

