from app.services.usage_service import get_usage_logs
from app.core.pricing import compute_price
from datetime import datetime
from collections import defaultdict
from typing import Dict, List


def get_billing_summary(project_id: str):
    logs = get_usage_logs(project_id)
    total_tokens = sum(log.tokens_used for log in logs)
    total_cost = compute_price(total_tokens)
    return {
        "project_id": project_id,
        "total_tokens": total_tokens,
        "total_cost": total_cost,
        "entries": len(logs)
    }


def get_billing_by_day(project_id: str) -> List[Dict]:
    logs = get_usage_logs(project_id)
    day_totals = defaultdict(int)

    for log in logs:
        day = log.timestamp.split("T")[0]
        day_totals[day] += log.tokens_used

    return [
        {
            "date": day,
            "tokens_used": tokens,
            "cost": compute_price(tokens)
        }
        for day, tokens in sorted(day_totals.items())
    ]


def get_billing_by_model(project_id: str) -> List[Dict]:
    logs = get_usage_logs(project_id)
    model_totals = defaultdict(int)

    for log in logs:
        model_totals[log.model] += log.tokens_used

    return [
        {
            "model": model,
            "tokens_used": tokens,
            "cost": compute_price(tokens)
        }
        for model, tokens in sorted(model_totals.items())
    ]


def get_billing_by_endpoint(project_id: str) -> List[Dict]:
    logs = get_usage_logs(project_id)
    endpoint_totals = defaultdict(int)

    for log in logs:
        endpoint_totals[log.endpoint] += log.tokens_used

    return [
        {
            "endpoint": ep,
            "tokens_used": tokens,
            "cost": compute_price(tokens)
        }
        for ep, tokens in sorted(endpoint_totals.items())
    ]
