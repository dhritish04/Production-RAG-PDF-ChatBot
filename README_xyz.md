# 🚀 Production-Grade PDF RAG Chatbot  
### FastAPI | LangChain | FAISS | HuggingFace

This project is a modular, intelligent **Retrieval-Augmented Generation (RAG) chatbot** that can answer complex queries from one or more PDFs.  
Built for **production-readiness**, it integrates modern NLP tools like **LangChain**, **Hugging Face Transformers**, and **FAISS** with a clean **FastAPI backend**.

---

## 🧠 Why This Project Stands Out
- ✅ Robust and modular codebase  
- ✅ Uses modern LLMs (**Mistral-7B via Hugging Face Hub**)  
- ✅ Streamlined **PDF-to-Answer pipeline** with LangChain  
- ✅ Real-time **API interface** with file upload & query support  
- ✅ Easily extensible: agents, metadata filtering, summarization, memory  

---

## 🧱 Project Structure
```
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
```


---

## 🌟 Key Features

### 📄 Ask Anything From Your PDFs
- Upload one or more PDFs  
- Text is chunked intelligently using LangChain  
- Top-k relevant chunks retrieved via FAISS  
- Answers generated using **Mistral-7B-Instruct**  

### 🧩 Modular & Maintainable Design
- LangChain handles document loading, chunking, embeddings, retrieval  
- Plug-and-play LLMs via `model.py`  
- VectorDB abstracted through FAISS wrapper  
- FastAPI decouples upload/query endpoints  

### 🧠 Multi-Turn Chat Support
- Add **conversation memory** to maintain context  
- Ideal for interviews, follow-ups, exploratory Q&A  

### 🗂️ Metadata-Aware Retrieval
- Chunks tagged with **document name + page number**  
- Filter answers by source  
- Full answer traceability  

### 🤖 Smart Agent-Orchestrated Behavior
- LangChain Agents decide whether to:  
  - Answer a query  
  - Summarize a PDF  
  - Route to other tools  
- Modular tools extend easily (QA, summarizer, etc.)  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone and Install
git clone https://github.com/dhritish04/Production-RAG-PDF-ChatBot
cd Production_RAG_PDF_ChatBOT
pip install -r requirements.txt

### 2️⃣ Add Your HuggingFace Token
Create a .env file in the root:
GROQ_API_KEY=your_groq_api_key_here

### 3️⃣ Run the FastAPI Backend
uvicorn app.main:app --reload
Or start the interactive frontend:
streamlit run streamlit_app.py

### 🚀 Try It Out
Upload PDF
POST /upload/
Form field: file (PDF file)

### Ask a Question
POST /query/
Form field: q (your question)

### 📬 Example API Output
json
```
{
  "response": "Retrieval-Augmented Generation (RAG) is a technique that combines document retrieval with large language models...",
  "sources": [
    {"doc": "AI_Assignment.pdf", "page": 3},
    {"doc": "LangChain_Guide.pdf", "page": 7}
  ]
}

```

### 📦 Requirements

```
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
```
