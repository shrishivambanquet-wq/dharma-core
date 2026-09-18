from .trust_score import TrustScore


class ConflictResolver:
    def choose(self, left: TrustScore, right: TrustScore):
        if left.value >= right.value:
            return left
        return right

    def tie(self, left: TrustScore, right: TrustScore):
        return left.value == right.value

    def confidence_gap(self, left: TrustScore, right: TrustScore):
        return abs(left.value - right.value)

