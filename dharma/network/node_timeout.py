class NodeTimeout:
    def expired(self,last_seen,now,limit):
        return (now-last_seen)>limit
