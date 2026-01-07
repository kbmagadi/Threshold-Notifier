# Dashboard Notifier — Intelligent Threshold Alerts with Causal Explanations
Dashboard Notifier is a Python alerting pipeline that detects metric threshold breaches and produces clear, causal-friendly explanations. LLMs are used only for narrative synthesis—never for decision logic.

## Why it's different
- Deterministic threshold detection with direction-aware change analysis
- Causal graph hints (YAML) to ground explanations
- Strict prompt design to avoid hallucinations or invented metrics
- Guaranteed delivery via deterministic fallback when LLMs time out or fail
- Slack and email dispatch out of the box; easy to extend (PagerDuty, webhooks, SMS)

## Quickstart
1) Install dependencies (Python 3.10+):
```bash
pip install -r requirements.txt
```
2) Configure environment:
- Ensure an Ollama model is available and reachable.
- Set any needed tokens/URLs for Slack/email in your environment or config.
3) Run a manual exercise:
```bash
python manual_test_llm.py
```
This instantiates sample `ThresholdEvent` objects, runs the full pipeline, and prints Slack-style output (LLM + fallback).

## How it works (pipeline)
1) Threshold rule triggers → `ThresholdEvent`
2) `Context Builder` (`notifier/context_builder.py`): calculates % deltas, aligns metric directions, collects causation signals, and packages structured context (no LLM here).
3) `Prompt Builder` (`notifier/prompt.py`): strict, safety-focused prompt using deterministic context + causal graph YAML for structure only.
4) `LLM Explainer` (`notifier/explainer.py`): calls Ollama with timeouts and temperature control.
5) `Fallback` (`notifier/fallback.py`): deterministic explanation if the LLM errors, times out, or returns nothing.
6) `Notification Dispatcher` (`notification/dispatcher.py`): routes to Slack/email; extensible to other channels.

## Project layout
```
Dashboard Notifier/
├── llm/
│   └── ollama_client.py        # Ollama integration (timeouts, model selection)
├── models/
│   └── threshold_event.py      # Core alert data model
├── notifier/
│   ├── context_builder.py      # Deterministic context assembly
│   ├── prompt.py               # Safe prompt construction
│   ├── explainer.py            # LLM call surface
│   ├── fallback.py             # Deterministic backup explanation
│   └── handler.py              # Orchestrates build → explain → dispatch
├── notification/
│   ├── dispatcher.py           # Channel routing
│   ├── slack.py                # Slack formatting & delivery
│   └── email.py                # Email delivery
├── causal_graph.yaml           # Human-friendly causal hints (for explanations only)
├── manual_test_llm.py          # Manual end-to-end runner
└── main.py                     # Production entry point (wire your trigger here)
```

## Safety guardrails
- LLMs do **not** influence alert triggering or calculations.
- No invented metrics; conditional language only.
- Deterministic fallback ensures alerts always send.

## Configuration tips
- `llm/ollama_client.py`: prefer higher `timeout` for cold starts (e.g., 30s); set the correct model name.
- `causal_graph.yaml`: keep concise, directional hints; version-control to review changes.
- Notification credentials: supply via environment variables or your secret manager.

## Testing
- Manual: `python manual_test_llm.py`
- Add unit tests under `tests/` for context building, prompt assembly, and fallback behavior.
- When mocking LLMs, cover: slow response, empty response, and error paths.

## Future enhancements
- Confidence scoring and source tagging (LLM vs fallback)
- Multi-hop causal explanations
- Latency optimizations and streaming responses
- UI visualization of causal graphs
