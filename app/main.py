from fastapi import FastAPI
from app.schemas import PredictionInput, PredictionOutput

app = FastAPI(
    title="FastAPI CI/CD Microservice",
    description="A lightweight API built to demonstrate automated CI/CD workflows.",
    version="1.0.0"
)