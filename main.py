from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Modell laden
with open("train_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class IrisFeatures(BaseModel):
    features: list

@app.get("/")
def read_root():
    return {
        "message": "Willkommen zur Iris-ML-API!",
        "usage": "POST /predict mit JSON {'features': [5.1, 3.5, 1.4, 0.2]}"
    }

@app.post("/predict")
def predict(data: IrisFeatures):
    prediction = model.predict([np.array(data.features)])
    return {"prediction": int(prediction[0])}

@app.get("/status")
def model_status():
    return {
        "status": "ready",
        "model": "LogisticRegression",
        "version": "1.0"
    }


