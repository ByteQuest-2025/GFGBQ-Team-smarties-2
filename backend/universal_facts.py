UNIVERSAL_FACTS = {
    "sun rises in the east",
    "earth revolves around the sun",
    "water boils at 100 degrees celsius",
    "humans need oxygen to survive"
}

def check_universal_fact(claim: str):
    claim = claim.lower().strip()
    if claim in UNIVERSAL_FACTS:
        return {
            "status": "verified",
            "source": "Universal Scientific Knowledge",
            "confidence": 95,
            "evidence": "Established scientific fact accepted globally"
        }
    return None
