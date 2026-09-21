"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class ScopeValidation:
    def allowed(self,scope,action):
        return action in scope
