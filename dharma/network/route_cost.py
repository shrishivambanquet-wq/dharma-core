from dataclasses import dataclass, field

@dataclass
class RouteCostRouter:
    routes: dict = field(default_factory=dict)

    def add(self, source, dest, path, cost):
        if len(path) != len(set(path)):
            raise ValueError("routing loop")
        self.routes.setdefault((source, dest), []).append((cost, path))

    def best(self, source, dest):
        options = self.routes.get((source, dest))
        if not options:
            return None
        return sorted(options, key=lambda x: (x[0], x[1]))[0]

    def next_hop(self, source, dest):
        result = self.best(source, dest)
        if not result:
            return None
        _, path = result
        return path[1] if len(path) > 1 else path[0]
