import json
from rag.retrieve import retrieve
from rag.prompt import build_prompt
from utils.openai_client import get_llm_response
from models.schema import AnswerSchema


def answer_query(query):
    docs = retrieve(query)
    prompt = build_prompt(query, docs)

    response = get_llm_response(prompt)
    parsed = json.loads(response)

    validated = AnswerSchema(**parsed)
    return validated.dict()
