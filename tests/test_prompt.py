from notifier.prompt import build_prompt

def test_prompt_contains_required_fields():
    context = {
        "alert": {
            "name": "Revenue Drop",
            "metric": "Revenue",
            "time_window": "Today vs Yesterday"
        },
        "threshold": {
            "condition": "Drop > 10%",
            "breached_by": "20%"
        },
        "values": {
            "current": 80,
            "baseline": 100
        },
        "supporting_metrics": {
            "Conversion Rate": {"current": "2.1%", "baseline": "2.8%"}
        }
    }

    prompt = build_prompt(context)

    assert "Revenue Drop" in prompt
    assert "Drop > 10%" in prompt
    assert "2.8%" in prompt
    assert "2.1%" in prompt
