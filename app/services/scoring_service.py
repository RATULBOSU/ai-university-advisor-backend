def facilities_score_from_text(facilities_text: str) -> float:
    if not facilities_text:
        return 0.0

    weights = {
        "library": 1.5,
        "lab": 2.0,
        "laboratory": 2.0,
        "hostel": 1.5,
        "gym": 1.0,
        "sports": 1.0,
        "campus": 1.0,
        "facility": 1.0,
        "facilities": 1.0,
        "transport": 1.0,
        "bus": 1.0,
        "shuttle": 1.0,
    }

    low = facilities_text.lower()
    score = 0.0
    for k, w in weights.items():
        if k in low:
            score += w

    return min(10.0, score)


def transport_score_from_text(facilities_text: str) -> float:
    if not facilities_text:
        return 0.0

    low = facilities_text.lower()
    score = 0.0

    if "transport" in low or "bus" in low or "shuttle" in low:
        score += 7.0
    if "near" in low or "accessible" in low:
        score += 2.0

    return min(10.0, score)


def research_score_placeholder(programs_text: str | None = None) -> float:
    return 5.0