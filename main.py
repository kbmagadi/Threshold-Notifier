from pathlib import Path
from models.threshold_event import ThresholdEvent
from notifier.handler import handle_threshold_event


def main():
    """
    Production entry point for Dashboard Notifier.
    Creates a ThresholdEvent and routes it through the alert pipeline.
    """

    # --------------------------------------------------
    # Load causal graph (YAML for LLM explanation only)
    # --------------------------------------------------
    causal_graph_yaml = Path("causal_graph.yaml").read_text()

    # --------------------------------------------------
    # Example alert event (in production, this comes
    # from your metrics / BI / scheduler layer)
    # --------------------------------------------------
    event = ThresholdEvent(
        rule_name="Revenue Drop DoD",
        metric="Revenue",
        current_value=84230,
        baseline_value=101450,
        threshold_type="PERCENT_DROP_GT",
        threshold_value=10,
        time_window="Today vs Yesterday",
        supporting_metrics={
            "Conversion Rate": {
                "current": "2.1%",
                "baseline": "2.8%"
            },
            "Traffic": {
                "current": 18500,
                "baseline": 19000
            }
        },
        causal_graph_yaml=causal_graph_yaml
    )

    # --------------------------------------------------
    # Send through alert pipeline
    # --------------------------------------------------
    handle_threshold_event(event)


if __name__ == "__main__":
    main()
