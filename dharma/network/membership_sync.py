class MembershipSync:
    def merge(self,a,b):
        return sorted(set(a)|set(b))

    def same(self,a,b):
        return set(a)==set(b)
