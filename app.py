import streamlit as st
import tempfile
import os
import warnings

# 🔇 Optional: hide unnecessary warnings
warnings.filterwarnings("ignore")

# 📌 Sidebar
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

    st.caption("⚡ Powered by RAG + LLM")

# 🧠 Chat memory
if "history" not in st.session_state:
    st.session_state.history = []

# 🎯 Title
st.markdown("<h1 style='text-align: center;'>🤖 Askify AI</h1>", unsafe_allow_html=True)
st.caption("Chat with your PDF intelligently")

# 📤 Upload + Query
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
query = st.text_input("Ask something about your PDF...")

# 📦 Imports
from loader import load_pdf
from chunking import chunk_docs
from vector_store import create_vector_store
from retrieval import retrieve_docs
from llm import generate_answer

retrieved_docs = None
answer = None

# 🚀 MAIN LOGIC
if uploaded_file is not None and query:

    # ✅ FIX 1: Proper temp file with .pdf extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())   # ✅ IMPORTANT FIX
        tmp_path = tmp_file.name

    # ✅ FIX 2: Prevent empty file crash
    if os.path.getsize(tmp_path) == 0:
        st.error("❌ Uploaded file is empty. Please upload a valid PDF.")
    else:
        try:
            docs = load_pdf(tmp_path)
            chunks = chunk_docs(docs)
            db = create_vector_store(chunks)

            retrieved_docs = retrieve_docs(db, query)

            # 🧠 Spinner
            with st.spinner("🧠 Thinking..."):
                answer = generate_answer(query, retrieved_docs)

            # 💬 Save chat
            st.session_state.history.append(("User", query))
            st.session_state.history.append(("AI", answer))

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

# 💬 Chat UI
st.divider()
for role, msg in st.session_state.history:
    if role == "User":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# 📚 Show sources
if retrieved_docs:
    st.divider()
    st.write("### 📚 Sources:")
    with st.expander("🔍 View Reference Documents"):
        for i, doc in enumerate(retrieved_docs):
            # Clean up messy newlines from the PDF text
            clean_text = doc.page_content[:300].replace('\n', ' ').strip()
            st.info(f"**Source {i+1}:** {clean_text}...")