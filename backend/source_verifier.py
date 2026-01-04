import wikipedia

def verify_with_sources(claim):
    try:
        summary = wikipedia.summary(claim, sentences=2)
        return {
            "status": "verified",
            "source": "Wikipedia",
            "confidence": 85,
            "evidence": summary
        }
    except wikipedia.exceptions.PageError:
        return {
            "status": "false",
            "source": None,
            "confidence": 0,
            "evidence": "No reliable source found"
        }
    except wikipedia.exceptions.DisambiguationError:
        return {
            "status": "uncertain",
            "source": "Wikipedia",
            "confidence": 40,
            "evidence": "Multiple meanings found"
        }
