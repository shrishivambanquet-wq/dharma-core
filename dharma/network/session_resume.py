from dataclasses import dataclass

@dataclass
class SessionResume:
    session_id: str
    _active: bool = True

    def interrupt(self):
        self._active = False

    def resume(self, session_id=None):
        if session_id is not None and session_id != self.session_id:
            return False
        self._active = True
        return True

    def active(self):
        return self._active

    def state(self):
        return "ACTIVE" if self._active else "INTERRUPTED"
