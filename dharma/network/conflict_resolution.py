class ConflictResolution:
    def choose(self,left,right):
        return max(left,right,key=lambda x:x["version"])
