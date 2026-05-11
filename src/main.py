from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.routers import health, documents, query

_STATIC = Path(__file__).parent.parent / "static"

app = FastAPI(
    title="AI Knowledge Engine",
    description="AI-powered knowledge management API",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(documents.router)
app.include_router(query.router)

app.mount("/static", StaticFiles(directory=_STATIC), name="static")


@app.get("/")
def root():
    return FileResponse(_STATIC / "index.html")
