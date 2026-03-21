def build_prompt(query, context_docs):
    context = "\n".join(context_docs)

    return f"""
You are a policy document assistant.

Context:
{context}

Question: {query}

STRICT RULES:
- Answer only from context
- Return valid JSON
- No hallucination

FORMAT:
{{
  "answer": "string",
  "sources": ["string"],
  "confidence": float
}}
"""
