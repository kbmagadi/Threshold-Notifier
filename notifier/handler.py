from notifier.context_builder import build_context
from notifier.prompt import build_prompt
from notifier.explainer import generate_explanation
from notifier.fallback import fallback_explanation
from notification.dispatcher import dispatch_notification
from models.threshold_event import ThresholdEvent


def handle_threshold_event(event: ThresholdEvent):
    print("HANDLER CALLED")
    context = build_context(event)

    try:
        prompt = build_prompt(context)
        explanation = generate_explanation(prompt)

        if not explanation or len(explanation.strip()) < 20:
            raise ValueError("Weak LLM response")

    except Exception:
        explanation = fallback_explanation(context)

    dispatch_notification(
        title=f"Alert: {event.rule_name}",
        message=explanation
    )
