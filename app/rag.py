import os

from app.model import get_llm


def answer_query(query: str, context_docs: list) -> dict:
    print(f"Generating answer from filtered context ({len(context_docs)} docs)...")

    llm = get_llm()
    context = "\n\n".join(doc.page_content for doc in context_docs)
    prompt = f"""Use the following context to answer the user's question.

Context:
{context}

Question: {query}
Answer:"""

    response = llm.invoke(prompt)
    answer = response.content if hasattr(response, "content") else str(response)

    sources = [
        {
            "source": doc.metadata.get("source_doc") or os.path.basename(doc.metadata.get("source", "unknown")),
            "page": doc.metadata.get("page", "unknown"),
        }
        for doc in context_docs
    ]

    return {
        "answer": answer,
        "sources": sources,
    }
