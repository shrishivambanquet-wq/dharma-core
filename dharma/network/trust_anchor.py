class TrustAnchor:
    def __init__(self):
        self.anchors={}

    def add(self,node,key):
        self.anchors[node]=key

    def get(self,node):
        return self.anchors.get(node)

    def trusted(self,node):
        return node in self.anchors

    def count(self):
        return len(self.anchors)
