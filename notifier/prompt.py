def build_prompt(context: dict) -> str:
    causation_lines = "\n".join(
        [
            f"- {c['metric']} moved {c['direction']} by {c['change_percent']}%"
            for c in context["causation_signals"]
        ]
    )

    return f"""
System:
You are a data analyst explaining why an alert was triggered.
Use ONLY the provided data.
Explain causation ONLY using the causation signals below.
Do NOT speculate beyond these signals.

User:
An alert was triggered.

Alert:
- Name: {context['alert']['name']}
- Metric: {context['alert']['metric']}
- Time Window: {context['alert']['time_window']}

Threshold:
- Type: {context['threshold']['type']}
- Value: {context['threshold']['value']}%
- Breached by: {context['threshold']['breached_by']}%

Values:
- Current: {context['values']['current']}
- Baseline: {context['values']['baseline']}

Causation Signals:
{causation_lines}

Explain in 2–3 concise sentences:
1. Why the threshold was breached
2. Which metric changes most directly contributed to it
"""
