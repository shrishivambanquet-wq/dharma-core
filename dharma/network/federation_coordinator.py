class FederationCoordinator:
    def __init__(self):
        self.members=set()

    def join(self,node):
        self.members.add(node)

    def leave(self,node):
        self.members.discard(node)

    def active(self,node):
        return node in self.members

    def count(self):
        return len(self.members)
