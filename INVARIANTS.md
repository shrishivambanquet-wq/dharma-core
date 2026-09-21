# Protocol Invariants

1. Node ID is immutable.
2. Session replay is forbidden.
3. Every accepted consensus commit requires quorum proof.
4. Invalid signatures MUST be rejected.
5. Clock drift beyond tolerance MUST reject authentication.

