from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    feature_one: float = Field(..., description="First measurement value")
    feature_two: float = Field(..., description="Second measurement value")