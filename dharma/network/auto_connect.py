from dharma.network.compatibility import Compatibility

class AutoConnect:
    @staticmethod
    def connect(local_card, remote_card):
        result = Compatibility.negotiate(local_card, remote_card)
        if result is None:
            return None
        return {
            "connected": True,
            "protocol": result["protocol"],
            "shared": result["shared"],
        }
