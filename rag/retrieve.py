from rag.ingest import collection


def retrieve(query):
    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    return results["documents"][0]
