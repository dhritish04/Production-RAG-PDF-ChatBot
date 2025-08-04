🚀 Production-Grade PDF RAG Chatbot with FastAPI, LangChain, FAISS & HuggingFace
This project is a modular, intelligent Retrieval-Augmented Generation (RAG) chatbot that can answer complex queries from one or more PDFs. Built for production-readiness, it integrates modern NLP tools like LangChain, Hugging Face Transformers, and FAISS with a clean FastAPI backend.

🧠 Why This Project Stands Out
✅ Robust and modular codebase

✅ Uses modern LLMs (Mistral-7B via Hugging Face Hub)

✅ Streamlined PDF-to-Answer pipeline with LangChain

✅ Real-time API interface with file upload and query support

✅ Easily extensible: agent routing, metadata filtering, summarization, memory

🧱 Project Structure
graphql
Copy
Edit
pdf_rag_chatbot/
├── app/
│   ├── main.py            # FastAPI API endpoints
│   ├── rag.py             # Retrieval chain + agents
│   ├── model.py           # LLM loader
│   ├── loaders.py         # PDF parsing & text chunking
│   ├── vector_store.py    # FAISS index management
│   ├── tools.py           # QA + summarizer tools for agent
│   ├── config.py          # Env vars and paths
│   ├── utils.py           # Shared utilities
│
├── vector_store/          # Saved FAISS index and chunks
├── data/                  # User-uploaded PDFs
├── .env                   # Hugging Face API token
├── requirements.txt
├── README.md
🌟 Key Features
📄 Ask Anything From Your PDFs
Upload one or more PDFs

Text is chunked intelligently using LangChain

Top-k relevant chunks are retrieved via FAISS

Answer generated using Mistral-7B-Instruct (Hugging Face)

🧩 Modular and Maintainable Design
LangChain handles document loading, chunking, embeddings, retrieval

Easy plug-and-play LLM support via model.py

VectorDB abstracted through LangChain's FAISS wrapper

FastAPI decouples upload/query endpoints

🧠 Multi-Turn Chat Support
Add conversation memory to maintain context

Ideal for interviews, follow-ups, and exploratory Q&A

🗂️ Metadata-Aware Retrieval
Chunks tagged with document name, page number

Filter answers by source

Trace every answer back to where it came from

🤖 Smart Agent-Orchestrated Behavior
Use LangChain agents to decide whether to:

Answer a query

Summarize a PDF

Route to other tools

Tools are modular and extendable (e.g., QA, summarizer)

⚙️ Setup Instructions
1. Clone and Install Dependencies
bash
Copy
Edit
git clone https://github.com/ari2612sarkar/Production_RAG_PDF_ChatBOT
cd Production_RAG_PDF_ChatBOT
pip install -r requirements.txt
2. Add Your HuggingFace Token
Create a .env file in the root:

ini
Copy
Edit
HUGGINGFACEHUB_API_TOKEN=your_token_here
3. Run the FastAPI Backend
bash
Copy
Edit
uvicorn app.main:app --reload
Or start the interactive frontend:

bash
Copy
Edit
streamlit run streamlit_app.py
🚀 Try It Out
Upload PDF
POST /upload/
Form field: file (PDF file)

Ask a Question
POST /query/
Form field: q (your question)

📬 Example API Output
json
Copy
Edit
{
  "response": "Retrieval-Augmented Generation (RAG) is a technique that combines document retrieval with large language models...",
  "sources": [
    {"doc": "AI_Assignment.pdf", "page": 3},
    {"doc": "LangChain_Guide.pdf", "page": 7}
  ]
}
📦 Requirements
nginx
Copy
Edit
fastapi
uvicorn
langchain
sentence-transformers
faiss-cpu
transformers
huggingface_hub
PyMuPDF
nltk
python-dotenv

🧠 Built For RMgX
This chatbot was developed as part of the RMgX AI Developer Assignment, with clean modularization, agent tooling, multi-level abstraction, and best practices in LLM-based application engineering.

