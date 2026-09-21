class ConformanceSuite:
    def run(self,results):
        return all(results)

    def passed(self,results):
        return sum(results)

    def total(self,results):
        return len(results)
