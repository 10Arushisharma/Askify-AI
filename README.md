# 🚀 Askify-AI — RAG-Based Intelligent Q&A System

🔗 **Live App:** https://askify-aigit-3g7zyibr3wxpappcjvhcsbt.streamlit.app/

---

## 📌 Overview

**Askify-AI** is a Retrieval-Augmented Generation (RAG) based AI application that allows users to upload PDF documents and ask questions based on their content.

Unlike traditional chatbots, Askify-AI ensures **accurate, context-based answers** by retrieving relevant information from the uploaded document before generating responses using an LLM.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Intelligent document chunking & embedding
- ⚡ Semantic search using vector database (FAISS)
- 🤖 LLM-powered answer generation (via OpenRouter)
- 📚 Context-aware responses (no hallucination)
- 💬 Clean Streamlit UI for interaction
- 🔐 Secure API handling using environment variables

---

## 🧠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM API:** OpenRouter (LLaMA 3 / GPT models)  
- **Framework:** LangChain  
- **Vector Store:** FAISS  
- **PDF Processing:** PyPDFLoader  
- **Embeddings:** OpenAI / compatible embeddings  

---

## ⚙️ Project Structure
# 🚀 Askify-AI — RAG-Based Intelligent Q&A System

🔗 **Live App:** https://askify-aigit-3g7zyibr3wxpappcjvhcsbt.streamlit.app/

---

## 📌 Overview

**Askify-AI** is a Retrieval-Augmented Generation (RAG) based AI application that allows users to upload PDF documents and ask questions based on their content.

Unlike traditional chatbots, Askify-AI ensures **accurate, context-based answers** by retrieving relevant information from the uploaded document before generating responses using an LLM.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Intelligent document chunking & embedding
- ⚡ Semantic search using vector database (FAISS)
- 🤖 LLM-powered answer generation (via OpenRouter)
- 📚 Context-aware responses (no hallucination)
- 💬 Clean Streamlit UI for interaction
- 🔐 Secure API handling using environment variables

---

## 🧠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM API:** OpenRouter (LLaMA 3 / GPT models)  
- **Framework:** LangChain  
- **Vector Store:** FAISS  
- **PDF Processing:** PyPDFLoader  
- **Embeddings:** OpenAI / compatible embeddings  

---

## ⚙️ Project Structure
askify-ai/
│
├── app.py # Main Streamlit app
├── loader.py # PDF loading logic
├── chunking.py # Text chunking
├── vector_store.py # FAISS setup
├── retrieval.py # Document retrieval
├── llm.py # LLM interaction
├── test_api.py # API testing
├── requirements.txt # Dependencies
└── README.md

---

## 🔄 How It Works (RAG Pipeline)

1. 📄 User uploads PDF  
2. ✂️ Text is split into chunks  
3. 🔢 Chunks converted into embeddings  
4. 📦 Stored in FAISS vector database  
5. 🔍 Relevant chunks retrieved based on query  
6. 🤖 LLM generates answer using context  

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/10Arushisharma/Askify-AI.git
cd Askify-AI

2️⃣ Create virtual environment
python -m venv venv
Activate:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create .env file:
OPENROUTER_API_KEY=your_api_key_here

5️⃣ Run the app
streamlit run app.py

🌐 Deployment
Deployed on Streamlit Community Cloud

👉 Make sure to add secrets:

OPENROUTER_API_KEY="your_key_here"

📊 Use Cases
📚 Study assistant for PDFs
📑 Research paper summarization
🧾 Legal / document analysis
🏢 Internal company knowledge base
🎓 Academic projects
🚀 Future Improvements
Multi-document support
Chat history memory
Advanced UI/UX
Source highlighting in answers
Voice-based queries

👩‍💻 Author
Arushi Sharma

💼 Aspiring Software Engineer & AI Developer
🚀 Passionate about building real-world AI products
⭐ If you like this project

Give it a ⭐ on GitHub and share it!
