from dataclasses import dataclass, field

@dataclass
class MultiHopRouter:
    routes: dict = field(default_factory=dict)

    def add_route(self, source, dest, path):
        self.routes[(source, dest)] = path

    def resolve(self, source, dest):
        path = self.routes.get((source, dest))
        if not path:
            return None
        if len(path) != len(set(path)):
            return None
        return path

    def next_hop(self, source, dest):
        path = self.resolve(source, dest)
        if not path:
            return None
        return path[1] if len(path) > 1 else path[0]
