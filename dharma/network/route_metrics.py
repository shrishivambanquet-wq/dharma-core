from dataclasses import dataclass, field

@dataclass
class RouteMetrics:
    routes: dict = field(default_factory=dict)

    def add(self, dest, next_hop, cost):
        self.routes[dest] = (next_hop, cost)

    def best(self, dest):
        return self.routes.get(dest)

    def update(self, dest, next_hop, cost):
        self.routes[dest] = (next_hop, cost)

    def count(self):
        return len(self.routes)
