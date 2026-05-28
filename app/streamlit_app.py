# streamlit_app.py

import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="PDF RAG Chatbot", layout="centered")
st.title("📄 PDF RAG Chatbot")
st.markdown("Upload a PDF and ask questions from it!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload PDF
st.subheader("1. Upload PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
if uploaded_file is not None:
    with st.spinner("Uploading and indexing..."):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        response = requests.post(f"{FASTAPI_URL}/upload/", files=files)
        if response.status_code == 200:
            st.success("✅ PDF uploaded and indexed.")
        else:
            st.error(f"❌ Upload failed: {response.text}")

# Chat History Display
st.subheader("2. Chat")
for chat in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {chat['question']}")
    st.markdown(f"**🤖 Bot:** {chat['answer']}")
    st.divider()

# Ask Question
query = st.text_input("Enter your question:")
if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        response = requests.post(f"{FASTAPI_URL}/query/", data={"q": query})
        if response.status_code == 200:
            result = response.json()
            st.session_state.chat_history.append({
                "question": query,
                "answer": result["answer"]
            })
            st.rerun()
        else:
            st.error(f"❌ Error: {response.text}")