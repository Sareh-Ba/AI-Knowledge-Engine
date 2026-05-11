from fastapi import FastAPI
from src.routers import health, documents, query

app = FastAPI(
    title="AI Knowledge Engine",
    description="AI-powered knowledge management API",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(documents.router)
app.include_router(query.router)


@app.get("/")
def root():
    return {"message": "AI Knowledge Engine API", "version": "0.1.0"}
