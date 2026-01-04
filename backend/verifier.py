import wikipedia

UNIVERSAL_FACTS = {
    "sun rises in the east": True,
    "earth revolves around the sun": True,
    "water boils at 100 degrees celsius": True,
    "sun produces heat and light": True
}

SCIENTIFIC_FALSES = {
    "sun rises in the west": "Contradicts basic astronomy",
    "earth is flat": "Contradicts established scientific evidence",
    "humans can breathe in space without oxygen": "Contradicts biology"
}

def verify_claim(claim):
    claim_l = claim.lower().strip()

    # 1️⃣ Universal facts
    if claim_l in UNIVERSAL_FACTS:
        return {
            "status": "verified",
            "source": "Universal Scientific Knowledge",
            "confidence": 95,
            "evidence": "Widely accepted scientific fact"
        }

    # 2️⃣ Known false scientific claims
    if claim_l in SCIENTIFIC_FALSES:
        return {
            "status": "false",
            "source": None,
            "confidence": 0,
            "evidence": SCIENTIFIC_FALSES[claim_l]
        }

    # 3️⃣ Wikipedia check (STRICT)
    try:
        summary = wikipedia.summary(claim, sentences=2, auto_suggest=False)

        # 🚫 Ignore movies, books, fiction
        if any(word in summary.lower() for word in ["film", "movie", "novel", "song"]):
            return {
                "status": "false",
                "source": "Wikipedia (Non-factual page)",
                "confidence": 0,
                "evidence": "Matched a fictional or non-scientific topic"
            }

        return {
            "status": "verified",
            "source": "Wikipedia",
            "confidence": 70,
            "evidence": summary
        }

    except wikipedia.exceptions.DisambiguationError:
        return {
            "status": "uncertain",
            "source": "Wikipedia",
            "confidence": 40,
            "evidence": "Ambiguous topic"
        }

    except wikipedia.exceptions.PageError:
        return {
            "status": "false",
            "source": None,
            "confidence": 0,
            "evidence": "No reliable source found"
        }
