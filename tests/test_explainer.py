from notifier.explainer import generate_explanation

def test_generate_explanation_calls_llm(mocker):
    mock_llm = mocker.patch(
        "notifier.explainer.call_llm",
        return_value="Revenue dropped due to lower conversions."
    )

    context = {
        "alert": {"name": "Revenue Drop", "metric": "Revenue", "time_window": "DoD"},
        "threshold": {"condition": "Drop > 10%", "breached_by": "20%"},
        "values": {"current": 80, "baseline": 100},
        "supporting_metrics": {}
    }

    explanation = generate_explanation(context)

    mock_llm.assert_called_once()
    assert "Revenue dropped" in explanation
