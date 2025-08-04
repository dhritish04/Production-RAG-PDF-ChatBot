# app/summarizer.py

from app.model import get_llm

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following:\n\n{text}\n\nSummary:"
    llm = get_llm()
    return llm.invoke(prompt)
