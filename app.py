import streamlit as st
from main import answer_query
from rag.ingest import ingest_pdf

st.title("PolicyGPT - PDF RAG Chatbot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    ingest_pdf("temp.pdf")
    st.success("PDF processed!")

query = st.text_input("Ask question from PDF:")

if st.button("Ask"):
    result = answer_query(query)
    st.write(result)
