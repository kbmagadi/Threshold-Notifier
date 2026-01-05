from notifier.context_builder import build_context
from models.threshold_event import ThresholdEvent

def test_build_context_percent_drop():
    event = ThresholdEvent(
        rule_name="Revenue Drop",
        metric="Revenue",
        current_value=80,
        baseline_value=100,
        threshold_type="PERCENT_DROP_GT",
        threshold_value=10,
        time_window="Today vs Yesterday",
        supporting_metrics={}
    )

    context = build_context(event)

    assert context["alert"]["name"] == "Revenue Drop"
    assert context["values"]["current"] == 80
    assert context["values"]["baseline"] == 100
    assert context["threshold"]["breached_by"] == "20.0%"
