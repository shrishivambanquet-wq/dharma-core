from dataclasses import dataclass


@dataclass
class CertificateChain:

    def validate(self, chain):
        if not chain:
            return False

        for i in range(len(chain)-1):
            if chain[i].subject != chain[i+1].issuer:
                return False

        return True
