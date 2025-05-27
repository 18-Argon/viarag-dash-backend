def get_current_rate(token_type: str, endpoint: str) -> float:
    if token_type == "gpt-4-in": return 0.03
    if token_type == "gpt-4-out": return 0.06
    if token_type == "embedding": return 0.0004
    return 0.01  # default fallback


def compute_price(tokens: int, rate_per_1k: float) -> float:
    return round((tokens / 1000) * rate_per_1k, 4)
