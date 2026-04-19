import streamlit as st
import tempfile
import os
import warnings

# Configure page to ensure sidebar is open by default
st.set_page_config(page_title="Askify AI", page_icon="🤖", initial_sidebar_state="expanded")

# 🔇 Optional: hide unnecessary warnings
warnings.filterwarnings("ignore")

# 📌 Sidebar
with st.sidebar:
    st.markdown("## 🤖 Askify AI")
    st.caption("Your personal document assistant")

    st.markdown("---")

    st.markdown("### 📖 How to use")
    st.markdown("""
    1. **Upload a PDF** using the file uploader.
    2. **Wait** for the document to be processed.
    3. **Ask questions** about the content of your PDF.
    """)

    st.markdown("---")
    
    st.markdown("### ⚙️ Controls")
    clear_chat = st.button("🗑 Clear Chat", use_container_width=True)
    if clear_chat:
        st.session_state.history = []
        st.rerun()

    st.markdown("---")
    st.caption("⚡ Powered by RAG + LLM")

# 🧠 Chat memory
if "history" not in st.session_state:
    st.session_state.history = []

# 🎯 Premium Styling & Animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

/* Animated Background Gradient */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #312e81, #0f172a);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Outfit', sans-serif;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating Title Animation */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}
.animated-title {
    animation: float 4s ease-in-out infinite;
    text-align: center;
    background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
    font-size: 3.5rem !important;
    margin-bottom: 0px;
    padding-top: 1rem;
}

/* Glassmorphism for elements */
div[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.6) !important;
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.stChatMessage {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease;
}

.stChatMessage:hover {
    transform: translateY(-2px);
}

/* Styled Uploader Box */
section[data-testid="stFileUploader"] {
    background: rgba(255, 255, 255, 0.03);
    border: 2px dashed rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    padding: 1rem;
    transition: all 0.3s ease;
}
section[data-testid="stFileUploader"]:hover {
    border-color: #38bdf8;
    background: rgba(56, 189, 248, 0.05);
}

/* Custom Text styling */
p, li, span, div {
    font-family: 'Outfit', sans-serif !important;
    color: #e2e8f0;
}
</style>

<h1 class='animated-title'>Askify AI</h1>
<p style='text-align: center; font-size: 1.2rem; color: #94a3b8; font-weight: 300;'>Intelligent Document Analysis</p>
<br>
""", unsafe_allow_html=True)

# 📤 Upload on Main Screen
uploaded_file = st.file_uploader("📄 Upload your PDF here", type=["pdf"], help="Limit 200MB per file")

# 💬 Chat Input (Must be at root level to stick to bottom)
query = st.chat_input("Ask something about your PDF...")

if uploaded_file is None:
    st.info("👋 **Welcome to Askify AI!** Please upload a PDF document above to get started. Once uploaded, you can ask questions about its contents.")


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