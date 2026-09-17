from .graph import AuthorityGraph

class AuthorityResolver:
    def __init__(self, graph: AuthorityGraph):
        self.graph = graph

    def can_reach(self, source_id, target_id):
        visited = set()
        stack = [source_id]

        while stack:
            current = stack.pop()
            if current == target_id:
                return True

            if current in visited:
                continue

            visited.add(current)

            for edge in self.graph.outgoing(current):
                stack.append(edge.target.id)

        return False
