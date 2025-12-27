from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from typing import List
from pipeline_utils import DataCleaner, FlagVariableGenerator, DateTimeExtractor


# Load model artifact
with open("api/models/xgb_pipeline.pkl", "rb") as f:
    artifact = pickle.load(f)

pipeline = artifact["pipeline"]
label_encoder = artifact["le"]


# FastAPI app
app = FastAPI(title="Ride Status Prediction API")


# Input schema (RAW DATA ONLY)
class RideInput(BaseModel):
    Date: str                     # "2024-08-25 14:30:00"
    Vehicle_Type: str
    Pickup_Location: str
    Drop_Location: str
    V_TAT: float
    C_TAT: float
    Booking_Value: int
    Payment_Method: str
    Ride_Distance: int
    Driver_Ratings: float
    Customer_Rating: float

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def health():
    return {"status": "API is live"}

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict_ride_status(data: RideInput):
    # Convert input to DataFrame (single row)
    df = pd.DataFrame([data.dict()])

    # Predict (encoded)
    y_pred_encoded = pipeline.predict(df)

    # Decode label
    y_pred = label_encoder.inverse_transform(y_pred_encoded)

    return {
        "prediction": y_pred[0]
    }


@app.post("/predict-batch")
def predict_ride_status_batch(data: List[RideInput]):

    df = pd.DataFrame([d.dict() for d in data])

    y_pred_encoded = pipeline.predict(df)
    y_pred = label_encoder.inverse_transform(y_pred_encoded)

    return {
        "predictions": y_pred.tolist()
    }
