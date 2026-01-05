from notifier.handler import handle_threshold_event
from models.threshold_event import ThresholdEvent

def test_handler_uses_llm_and_sends_notification(mocker):
    mock_explainer = mocker.patch(
        "notifier.handler.generate_explanation",
        return_value="Revenue dropped by 20%."
    )

    mock_dispatch = mocker.patch(
        "notifier.handler.dispatch_notification"
    )

    event = ThresholdEvent(
        rule_name="Revenue Drop",
        metric="Revenue",
        current_value=80,
        baseline_value=100,
        threshold_type="PERCENT_DROP_GT",
        threshold_value=10,
        time_window="DoD",
        supporting_metrics={}
    )

    handle_threshold_event(event)

    mock_explainer.assert_called_once()
    mock_dispatch.assert_called_once()

def test_handler_falls_back_on_llm_failure(mocker):
    mocker.patch(
        "notifier.handler.generate_explanation",
        side_effect=Exception("LLM down")
    )

    mock_fallback = mocker.patch(
        "notifier.handler.fallback_explanation",
        return_value="Fallback explanation"
    )

    mock_dispatch = mocker.patch(
        "notifier.handler.dispatch_notification"
    )

    event = ThresholdEvent(
        rule_name="Revenue Drop",
        metric="Revenue",
        current_value=80,
        baseline_value=100,
        threshold_type="PERCENT_DROP_GT",
        threshold_value=10,
        time_window="DoD",
        supporting_metrics={}
    )

    handle_threshold_event(event)

    mock_fallback.assert_called_once()
    mock_dispatch.assert_called_once()
