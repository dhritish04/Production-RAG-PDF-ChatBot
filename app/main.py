from fastapi import FastAPI, UploadFile, File, Form, Query
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from app.rag import answer_query
from app.vector_store import LangchainVectorStore
from app.loaders import load_and_split
from app.config import INDEX_DIR
from app.agent import get_agent
import os
import shutil

app = FastAPI()
vector_store = LangchainVectorStore()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_path = os.path.join("data", file.filename)
    with open(pdf_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    docs = load_and_split(pdf_path)
    vector_store.build_index(docs)
    vector_store.save(INDEX_DIR)

    return {"message": f"{file.filename} uploaded and indexed."}


@app.post("/query/")
async def query_llm(
    q: str = Form(...),
    filename: str = Query(default=None),
    page_number: int = Query(default=None)
):
    try:
        vector_store.load(INDEX_DIR)

        # Search top-k first
        docs = vector_store.search(q, k=5)

        # Apply metadata filtering
        def filter_fn(doc):
            if filename and doc.metadata.get("source") != filename:
                return False
            if page_number is not None and doc.metadata.get("page") != page_number:
                return False
            return True

        filtered_docs = list(filter(filter_fn, docs))

        if not filtered_docs:
            return JSONResponse(content={"response": "No relevant documents found with given filters."})

        # Get final answer + metadata
        result = answer_query(q, filtered_docs)

        return JSONResponse(content={
            "answer": result["answer"],
            "sources": result["sources"]
        })

    except Exception as e:
        print(f"❌ Error during query: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/agent/")
async def run_agent(query: str = Form(...)):
    try:
        agent = get_agent()
        print(f"🤖 Running agent with query: {query}")
        response = agent.run(query)
        return {"response": response}
    except Exception as e:
        print(f"❌ Agent failed: {e}")
        raise HTTPException(status_code=500, detail="Agent error")
