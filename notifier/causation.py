CAUSAL_GRAPH = {
    "Revenue": ["Conversion Rate", "Traffic"],
    "Conversion Rate": ["Traffic"],
    "Traffic": []
}


def pct_change(curr, base):
    if base == 0:
        return 0.0
    return round(((curr - base) / base) * 100, 2)


def extract_numeric(value):
    if isinstance(value, str):
        return float(value.replace("%", ""))
    return float(value)


def derive_causation(event):
    target_metric = event.metric
    allowed_causes = CAUSAL_GRAPH.get(target_metric, [])

    target_change = pct_change(
        event.current_value, event.baseline_value
    )

    causes = []

    for metric, values in event.supporting_metrics.items():
        if metric not in allowed_causes:
            continue

        curr = extract_numeric(values["current"])
        base = extract_numeric(values["baseline"])
        change = pct_change(curr, base)

        # Direction must align
        if (target_change < 0 and change < 0) or (target_change > 0 and change > 0):
            causes.append({
                "metric": metric,
                "change_percent": abs(change)
            })

    # Rank by impact
    causes.sort(key=lambda x: x["change_percent"], reverse=True)

    return causes
