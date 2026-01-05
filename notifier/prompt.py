def build_prompt(context: dict) -> str:
    supporting = "\n".join(
        [
            f"- {k}: {v['baseline']} → {v['current']}"
            for k, v in context["supporting_metrics"].items()
        ]
    )

    return f"""
System:
You are a data analyst explaining why an alert was triggered.
Use ONLY the provided data. Do NOT speculate.

User:
An alert was triggered.

Alert:
- Name: {context['alert']['name']}
- Metric: {context['alert']['metric']}
- Time Window: {context['alert']['time_window']}

Threshold:
- Condition: {context['threshold']['condition']}
- Breached by: {context['threshold']['breached_by']}

Values:
- Current: {context['values']['current']}
- Baseline: {context['values']['baseline']}

Supporting Metrics:
{supporting}

Explain in 2–3 clear sentences why this alert was triggered.
"""
