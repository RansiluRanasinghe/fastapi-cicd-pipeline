from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    feature_one: float = Field(..., description="First measurement value")
    feature_two: float = Field(..., description="Second measurement value")

class PredictionOutput(BaseModel):
    prediction: int = Field(..., description="Predicted class label (0 or 1)")
    probability: float = Field(..., description="Confidence score between 0.0 and 1.0")    