from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from src.services.vectorstore import search_chunks
from src.services.llm import ask

router = APIRouter(prefix="/query", tags=["query"])


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The question to search for")
    n_results: int = Field(3, ge=1, le=20, description="Number of chunks to return")


class ChunkResult(BaseModel):
    text: str
    source: str
    chunk_index: int
    score: float


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[ChunkResult]


@router.post("", response_model=QueryResponse)
def query_knowledge(body: QueryRequest):
    chunks = search_chunks(body.question, n_results=body.n_results)
    if not chunks:
        raise HTTPException(status_code=404, detail="No knowledge found. Upload a PDF first.")
    try:
        answer = ask(body.question, chunks)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"AI service error: {e}")
    return QueryResponse(question=body.question, answer=answer, sources=chunks)
