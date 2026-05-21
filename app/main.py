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

@app.post("/predict", response_model=PredictionOutput, status_code=200)
def get_prediction(payload: PredictionInput):

    score = payload.feature_one * 0.4 + payload.feature_two * 0.6
    prediction_label = 1 if score >= 0.5 else 0

    probability_value = min(max(abs(score), 0.0), 1.0)

    return {
        "prediction": prediction_label,
        "probability": round(probability_value, 2)
    }