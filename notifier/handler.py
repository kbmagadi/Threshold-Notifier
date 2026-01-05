from notifier.context_builder import build_context
from notifier.explainer import generate_explanation
from notifier.fallback import fallback_explanation
from notification.dispatcher import dispatch_notification
from models.threshold_event import ThresholdEvent

def handle_threshold_event(event: ThresholdEvent):
    context = build_context(event)

    try:
        explanation = generate_explanation(context)
    except Exception:
        explanation = fallback_explanation(context)

    dispatch_notification(
        title=f"Alert: {event.rule_name}",
        message=explanation
    )
