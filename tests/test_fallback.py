from notifier.fallback import fallback_explanation

def test_fallback_message():
    context = {
        "alert": {"metric": "Revenue"},
        "values": {"current": 80, "baseline": 100}
    }

    msg = fallback_explanation(context)

    assert "Revenue" in msg
    assert "80" in msg
    assert "100" in msg
