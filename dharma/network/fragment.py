"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class Fragmenter:
    @staticmethod
    def split(text, size):
        return [
            {"seq": i, "total": (len(text)+size-1)//size, "data": text[i*size:(i+1)*size]}
            for i in range((len(text)+size-1)//size)
        ]

class Reassembler:
    @staticmethod
    def join(frags):
        if not frags:
            return None
        frags = sorted(frags, key=lambda x: x["seq"])
        total = frags[0]["total"]
        if len(frags) != total:
            return None
        return "".join(f["data"] for f in frags)
