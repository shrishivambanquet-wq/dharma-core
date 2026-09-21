class ScopeValidation:
    def allowed(self,scope,action):
        return action in scope
