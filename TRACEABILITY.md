# Dharma Traceability Matrix

## Rule

Every canonical DRFC MUST map to an implementation module and a verification test.

| DRFC Range | Layer | Primary Module | Test Suite |
|------------|-------|----------------|------------|
|0001–0010|Constitution|spec|core|
|0011–0025|Identity|identity|identity|
|0026–0045|Network|network|network|
|0046–0065|Sessions|session|session|
|0066–0083|Consensus|consensus|consensus|
|0084–0100|Federation/Security|federation/security|federation/security|

## Verification Requirement

- Every implementation MUST reference its governing DRFC.
- Every test SHOULD reference the DRFC it validates.
- Missing mappings MUST be treated as audit findings.

