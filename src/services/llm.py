import anthropic

_client = None

_SYSTEM_PROMPT = (
    "You are a knowledgeable AI assistant that answers questions strictly based on "
    "the provided document context. If the context does not contain enough information "
    "to answer, say so clearly. Be concise and cite the source when helpful."
)


def get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


def ask(question: str, chunks: list[dict]) -> str:
    context = "\n\n".join(
        f"[Source: {c['source']}, chunk {c['chunk_index']}]\n{c['text']}"
        for c in chunks
    )

    with get_client().messages.stream(
        model="claude-opus-4-7",
        max_tokens=8192,
        system=[{
            "type": "text",
            "text": _SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}",
        }],
    ) as stream:
        message = stream.get_final_message()

    return next(block.text for block in message.content if block.type == "text")
