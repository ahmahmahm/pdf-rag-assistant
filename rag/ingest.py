import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import os
from rag.pdf_loader import load_pdf

client = chromadb.Client()

embedding_function = OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-small"
)

collection = client.create_collection(
    name="pdf_docs",
    embedding_function=embedding_function
)


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks


def ingest_pdf(file_path):
    text = load_pdf(file_path)
    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{"source": file_path}],
            ids=[str(i)]
        )
