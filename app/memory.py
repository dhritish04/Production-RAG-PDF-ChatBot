# app/memory.py

from langchain.memory import ConversationBufferMemory

# This memory stores chat history in a simple buffer
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
