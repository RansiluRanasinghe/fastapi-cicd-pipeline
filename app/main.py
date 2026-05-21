from fastapi import FastAPI
from app.schemas import PredictionInput, PredictionOutput

app = FastAPI(
    title="FastAPI CI/CD Microservice",
    description="A lightweight API built to demonstrate automated CI/CD workflows.",
    version="1.0.0"
)

@app.get("/health", status_code=200)
def health_check():
    return {"status": "healthy", "environment": "production"}