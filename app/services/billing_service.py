from app.services.usage_service import get_usage_logs
from app.core.pricing import compute_price
from collections import defaultdict
from typing import Dict, List


def get_billing_summary(project_id: str):
    logs = get_usage_logs(project_id)
    total_tokens = sum(log.tokens_used for log in logs)
    total_cost = sum((log.tokens_used / 1000) * log.price_per_1k for log in logs)
    return {
        "project_id": project_id,
        "total_tokens": total_tokens,
        "total_cost": round(total_cost, 4),
        "entries": len(logs)
    }


def get_billing_by_day(project_id: str) -> List[Dict]:
    logs = get_usage_logs(project_id)
    day_totals = defaultdict(lambda: {"tokens": 0, "cost": 0.0})

    for log in logs:
        day = log.timestamp.split("T")[0]
        day_totals[day]["tokens"] += log.tokens_used
        day_totals[day]["cost"] += (log.tokens_used / 1000) * log.price_per_1k

    return [
        {
            "date": day,
            "tokens_used": entry["tokens"],
            "cost": round(entry["cost"], 4)
        }
        for day, entry in sorted(day_totals.items())
    ]


def get_billing_by_token_type(project_id: str) -> List[Dict]:
    logs = get_usage_logs(project_id)
    token_type_totals = defaultdict(lambda: {"tokens": 0, "cost": 0.0})

    for log in logs:
        token_type_totals[log.token_type]["tokens"] += log.tokens_used
        token_type_totals[log.token_type]["cost"] += (log.tokens_used / 1000) * log.price_per_1k

    return [
        {
            "token_type": token_type,
            "tokens_used": entry["tokens"],
            "cost": round(entry["cost"], 4)
        }
        for token_type, entry in sorted(token_type_totals.items())
    ]


def get_billing_by_endpoint(project_id: str) -> List[Dict]:
    logs = get_usage_logs(project_id)
    endpoint_totals = defaultdict(lambda: {"tokens": 0, "cost": 0.0})

    for log in logs:
        endpoint_totals[log.endpoint]["tokens"] += log.tokens_used
        endpoint_totals[log.endpoint]["cost"] += (log.tokens_used / 1000) * log.price_per_1k

    return [
        {
            "endpoint": ep,
            "tokens_used": entry["tokens"],
            "cost": round(entry["cost"], 4)
        }
        for ep, entry in sorted(endpoint_totals.items())
    ]
