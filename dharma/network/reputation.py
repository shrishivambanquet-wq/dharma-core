class Reputation:
    def __init__(self):
        self.scores = {}

    def score(self, node):
        return self.scores.get(node, 0)

    def reward(self, node, points=1):
        self.scores[node] = self.score(node) + points
        return self.scores[node]

    def penalize(self, node, points=1):
        self.scores[node] = self.score(node) - points
        return self.scores[node]

    def reset(self, node):
        self.scores.pop(node, None)

    def known(self, node):
        return node in self.scores

    def top(self):
        if not self.scores:
            return None
        return max(self.scores, key=self.scores.get)

    def count(self):
        return len(self.scores)
