def build_context(event):
    percent_change = round(
        ((event.current_value - event.baseline_value) / event.baseline_value) * 100,
        2
    ) if event.baseline_value != 0 else 0

    return {
        "alert": {
            "name": event.rule_name,
            "metric": event.metric,
            "time_window": event.time_window
        },
        "threshold": {
            "condition": f"{event.threshold_type} {event.threshold_value}",
            "breached_by": f"{abs(percent_change)}%"
        },
        "values": {
            "current": event.current_value,
            "baseline": event.baseline_value
        },
        "supporting_metrics": event.supporting_metrics
    }
