from .graph import AuthorityGraph

class AuthorityResolver:
    def __init__(self, graph: AuthorityGraph):
        self.graph = graph

    def can_reach(self, source_id: str, target_id: str) -> bool:
        if source_id == target_id:
            return True

        visited = set()
        queue = [source_id]

        while queue:
            current = queue.pop(0)

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.graph.neighbors(current):
                if neighbor == target_id:
                    return True
                queue.append(neighbor)

        return False

