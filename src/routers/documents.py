from fastapi import APIRouter, UploadFile, File, HTTPException
from src.services.pdf import extract_text, chunk_text
from src.services.vectorstore import store_chunks

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename or not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    contents = await file.read()
    text = extract_text(contents)

    if not text.strip():
        raise HTTPException(status_code=422, detail="Could not extract text from PDF.")

    try:
        chunks = chunk_text(text)
        stored = store_chunks(chunks, source=file.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Storage error: {e}")

    return {
        "filename": file.filename,
        "chunks_stored": stored,
    }
