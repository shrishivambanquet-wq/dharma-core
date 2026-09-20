class FederationJoin:
    def __init__(self):
        self.members = {}

    def join(self, node_id, endpoint):
        if node_id in self.members:
            return False
        self.members[node_id] = endpoint
        return True

    def leave(self, node_id):
        return self.members.pop(node_id, None) is not None

    def exists(self, node_id):
        return node_id in self.members

    def endpoint(self, node_id):
        return self.members.get(node_id)

    def count(self):
        return len(self.members)

    def list_members(self):
        return sorted(self.members.keys())
