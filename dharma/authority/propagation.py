"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .authority_graph import AuthorityGraph


@dataclass
class RevocationPropagation:
    graph: AuthorityGraph

    def affected(self, root):
        seen = set()
        stack = [root]

        while stack:
            node = stack.pop()

            if node in seen:
                continue

            seen.add(node)

            for child in self.graph.children(node):
                stack.append(child)

        seen.discard(root)
        return sorted(seen)

    def propagates(self, root, target):
        return target in self.affected(root)

    def count(self, root):
        return len(self.affected(root))
