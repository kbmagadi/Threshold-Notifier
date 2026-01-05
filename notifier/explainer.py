from notifier.prompt import build_prompt
from llm.ollama_client import call_llm

def generate_explanation(context: dict) -> str:
    prompt = build_prompt(context)

    response = call_llm(
        prompt=prompt,
        temperature=0.2
    )

    return response.strip()
