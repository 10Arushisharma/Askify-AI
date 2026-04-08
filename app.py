import streamlit as st
import tempfile

with st.sidebar:
    st.markdown("## 🤖 Askify AI")
    st.caption("Your personal document assistant")

    st.markdown("---")

    st.markdown("### ⚙️ Controls")
    
    clear_chat = st.button("🗑 Clear Chat")
    
    if clear_chat:
        st.session_state.history = []
        st.rerun()

    st.markdown("---")

    st.markdown("### ℹ️ About")
    st.write(
        "Askify lets you chat with your documents using AI. "
        "It retrieves relevant content and generates answers instantly."
    )

    st.caption("⚡ Powered by RAG + Local LLM")

# 🧠 Chat memory
if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("<h1 style='text-align: center;'>🤖 Askify AI</h1>", unsafe_allow_html=True)
st.caption("Chat with your PDF intelligently")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
query = st.text_input("Ask something about your PDF...")

from loader import load_pdf
from chunking import chunk_docs
from vector_store import create_vector_store
from retrieval import retrieve_docs
from llm import generate_answer

# 👉 Store docs separately so we can use later
retrieved_docs = None
answer = None

if uploaded_file and query:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())

        docs = load_pdf(tmp_file.name)
        chunks = chunk_docs(docs)
        db = create_vector_store(chunks)

        retrieved_docs = retrieve_docs(db, query)

        # 🧠 Spinner
        with st.spinner("🧠 Thinking..."):
            answer = generate_answer(query, retrieved_docs)

        # 💬 Save chat
        st.session_state.history.append(("User", query))
        st.session_state.history.append(("AI", answer))

# 💬 Chat UI
st.divider()
for role, msg in st.session_state.history:
    if role == "User":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# 📚 Show sources ONLY after answer
if retrieved_docs:
    st.divider()
    st.write("### 📚 Sources:")
    for doc in retrieved_docs:
        st.write(doc.page_content[:200])