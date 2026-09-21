class TrustVerification:
    def verify(self,anchor,node):
        return anchor.trusted(node)
