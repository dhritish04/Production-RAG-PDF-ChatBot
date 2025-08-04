from langchain.chains import RetrievalQA
from app.vector_store import get_vectorstore
from app.model import get_llm

def answer_query(query: str, context_docs: list) -> dict:
    print(f"🔍 Generating answer from filtered context ({len(context_docs)} docs)...")

    llm = get_llm()

    # Rebuild chain with manual context
    context = "\n\n".join([doc.page_content for doc in context_docs])
    prompt = f"""[INST] Use the following context to answer the user's question.

Context:
{context}

Question: {query}
Answer: [/INST]"""

    answer = llm.invoke(prompt)

    # Extract metadata
    sources = [
        {
            "source": doc.metadata.get("source", "unknown"),
            "page": doc.metadata.get("page", "unknown")
        }
        for doc in context_docs
    ]

    return {
        "answer": answer,
        "sources": sources
    }
