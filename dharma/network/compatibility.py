class Compatibility:
    @staticmethod
    def negotiate(a, b):
        if a["protocol"] != b["protocol"]:
            return None

        return {
            "protocol": a["protocol"],
            "shared": sorted(
                list(set(a["features"]) & set(b["features"]))
            )
        }
