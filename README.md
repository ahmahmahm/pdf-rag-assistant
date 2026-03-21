# PolicyGPT: Intelligent PDF Q&A System using RAG, OpenAI & ChromaDB
## pdf-rag-assistant
Build a Production-Ready RAG system for intelligent Q&amp;A over PDFs (policies, contracts, resumes). Powered by OpenAI Structured Outputs, Pydantic for schema enforcement, ChromaDB for local vector storage, and a Streamlit UI. Ideal for enterprise AI in legal, banking, and HR. Scalable, deterministic, and easy to deploy locally.

## Architecture Overview

PDFs → Text Extraction → Chunking → Embeddings → ChromaDB User Query → Retrieval → Prompt → OpenAI → JSON Output → UI

## Project Strature:

pdf-rag-assistant/
│── app.py
│── main.py
│── rag/
│   ├── ingest.py
│   ├── retrieve.py
│   ├── prompt.py
│   ├── pdf_loader.py
│── models/
│   ├── schema.py
│── utils/
│   ├── openai_client.py
│── data/
│   ├── sample.pdf
│── chroma_db/
│── requirements.txt
│── README.md
│── .env

## 🔥 Key Features
- 📄 Upload and process PDF documents
- 🔍 Semantic search using embeddings (vector database)
- 🧠 RAG pipeline (Retrieval + Generation)
- 📊 Structured JSON output (Pydantic schema)
- ⚡ Fast Streamlit UI for interaction
- 🏗️ Modular and production-ready architecture

---

## ⚙️ Tech Stack

- Python 3
- OpenAI API (LLM + Embeddings)
- ChromaDB (Vector Database)
- Pydantic (Structured Output Validation)
- Streamlit (Frontend UI)
- PyPDF (PDF Parsing)

---

## 🚀 Installation & Setup

```bash
git clone https://github.com/NxtGenCodeBase/pdf-rag-assistant.git
cd policygpt

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt