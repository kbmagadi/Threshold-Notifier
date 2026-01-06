def build_context(event):
    def pct_change(curr, base):
        if base == 0:
            return 0
        return round(((curr - base) / base) * 100, 2)

    metric_change = pct_change(event.current_value, event.baseline_value)

    causation = []

    for name, values in event.supporting_metrics.items():
        curr = float(str(values["current"]).replace("%", ""))
        base = float(str(values["baseline"]).replace("%", ""))
        change = pct_change(curr, base)

        causation.append({
            "metric": name,
            "direction": "down" if change < 0 else "up",
            "change_percent": abs(change)
        })

    return {
        "alert": {
            "name": event.rule_name,
            "metric": event.metric,
            "time_window": event.time_window
        },
        "threshold": {
            "type": event.threshold_type,
            "value": event.threshold_value,
            "breached_by": abs(metric_change)
        },
        "values": {
            "current": event.current_value,
            "baseline": event.baseline_value
        },
        "causation_signals": causation
    }
