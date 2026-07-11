from fastapi import FastAPI

app = FastAPI(
    title="OpenMemory",
    description="The open-source memory layer for AI applications.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "OpenMemory",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }