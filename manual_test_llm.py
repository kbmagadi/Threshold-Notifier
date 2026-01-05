from notifier.handler import handle_threshold_event
from models.threshold_event import ThresholdEvent

# event = ThresholdEvent(
#     rule_name="Revenue Drop DoD",
#     metric="Revenue",
#     current_value=84230,
#     baseline_value=101450,
#     threshold_type="PERCENT_DROP_GT",
#     threshold_value=10,
#     time_window="Today vs Yesterday",
#     supporting_metrics={
#         "Conversion Rate": {
#             "current": "2.1%",
#             "baseline": "2.8%"
#         },
#         "Traffic": {
#             "current": 18500,
#             "baseline": 19000
#         }
#     }
# )

# handle_threshold_event(event)

# -----------------------------

# event = ThresholdEvent(
#     rule_name="Conversion Rate Drop DoD",
#     metric="Conversion Rate",
#     current_value=1.9,
#     baseline_value=2.6,
#     threshold_type="PERCENT_DROP_GT",
#     threshold_value=20,
#     time_window="Today vs Yesterday",
#     supporting_metrics={
#         "Traffic": {
#             "current": 42000,
#             "baseline": 41800
#         },
#         "Revenue": {
#             "current": 79300,
#             "baseline": 98200
#         }
#     }
# )

# handle_threshold_event(event)

# -----------------------------------

event = ThresholdEvent(
    rule_name="Traffic Spike Without Revenue",
    metric="Traffic",
    current_value=58000,
    baseline_value=41000,
    threshold_type="PERCENT_INCREASE_GT",
    threshold_value=30,
    time_window="Last 1 Hour vs Previous Hour",
    supporting_metrics={
        "Conversion Rate": {
            "current": "1.2%",
            "baseline": "2.4%"
        },
        "Revenue": {
            "current": 31200,
            "baseline": 39800
        }
    }
)

handle_threshold_event(event)
