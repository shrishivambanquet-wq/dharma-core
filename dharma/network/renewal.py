from dataclasses import dataclass

from .token import SessionToken


@dataclass
class SessionRenewal:
    old_token: SessionToken

    def renew(self):
        return SessionToken.create()

    def changed(self):
        return self.renew().value != self.old_token.value
