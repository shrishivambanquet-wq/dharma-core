class DelegationChain:
    def __init__(self):
        self.chain={}

    def delegate(self,parent,child):
        self.chain[child]=parent

    def parent(self,node):
        return self.chain.get(node)

    def root(self,node):
        while node in self.chain:
            node=self.chain[node]
        return node
