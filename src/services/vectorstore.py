import chromadb
from pathlib import Path

_DB_PATH = Path(__file__).parent.parent.parent / "data" / "chromadb"
_client = None


def get_client() -> chromadb.ClientAPI:
    global _client
    if _client is None:
        _DB_PATH.mkdir(parents=True, exist_ok=True)
        _client = chromadb.PersistentClient(path=str(_DB_PATH))
    return _client


def get_collection(name: str = "knowledge"):
    return get_client().get_or_create_collection(name)


def store_chunks(chunks: list[str], source: str, collection_name: str = "knowledge") -> int:
    collection = get_collection(collection_name)
    ids = [f"{source}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": source, "chunk_index": i} for i in range(len(chunks))]
    collection.upsert(documents=chunks, ids=ids, metadatas=metadatas)
    return len(chunks)


def search_chunks(query: str, n_results: int = 5, collection_name: str = "knowledge") -> list[dict]:
    collection = get_collection(collection_name)
    if collection.count() == 0:
        return []
    results = collection.query(query_texts=[query], n_results=min(n_results, collection.count()))
    docs = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]
    return [
        {"text": doc, "source": meta["source"], "chunk_index": meta["chunk_index"], "score": round(1 - dist, 4)}
        for doc, meta, dist in zip(docs, metadatas, distances)
    ]
