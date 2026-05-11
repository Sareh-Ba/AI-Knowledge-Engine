import os
from google import genai

_client = None

_SYSTEM_PROMPT = (
    "You are a knowledgeable AI assistant that answers questions strictly based on "
    "the provided document context. If the context does not contain enough information "
    "to answer, say so clearly. Be concise and cite the source when helpful."
)


def get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    return _client


def ask(question: str, chunks: list[dict]) -> str:
    context = "\n\n".join(
        f"[Source: {c['source']}, chunk {c['chunk_index']}]\n{c['text']}"
        for c in chunks
    )
    response = get_client().models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{_SYSTEM_PROMPT}\n\nContext:\n{context}\n\nQuestion: {question}",
    )
    return response.text
