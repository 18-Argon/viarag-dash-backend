def compute_price(tokens: int, rate_per_1k=0.01) -> float:
    return round((tokens / 1000) * rate_per_1k, 4)