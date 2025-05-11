from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
models_path = os.path.join(os.path.dirname(__file__), "models")
with open(os.path.join(models_path, 'dt_model.pkl'), 'rb') as f:
    dt_model = pickle.load(f)

with open(os.path.join(models_path, 'rf_model.pkl'), 'rb') as f:
    rf_model = pickle.load(f)

with open(os.path.join(models_path, 'lr_model.pkl'), 'rb') as f:
    lr_model = pickle.load(f)

class AQIInput(BaseModel):
    co: float
    no: float
    no2: float
    o3: float
    so2: float
    pm10: float
    nh3: float
    UP_AQI: float
    Haryana_AQI: float
    Wind_Speed_kmph: float
    Wind_Direction_deg: float
    Wind_Speed_kmph_UP: float
    Wind_Direction_deg_UP: float

@app.post("/predict/")
def predict(data: AQIInput):
    input_arr = np.array([[data.co, data.no, data.no2, data.o3, data.so2, data.pm10, data.nh3,
                           data.UP_AQI, data.Haryana_AQI,
                           data.Wind_Speed_kmph, data.Wind_Direction_deg,
                           data.Wind_Speed_kmph_UP, data.Wind_Direction_deg_UP]])
    
    dt_pred = dt_model.predict(input_arr)[0] * 5
    rf_pred = rf_model.predict(input_arr)[0] * 4
    lr_pred = lr_model.predict(input_arr)[0] * 7

    return {
        "DecisionTree": round(dt_pred, 2),
        "RandomForest": round(rf_pred, 2),
        "LinearRegression": round(lr_pred, 2)
    }
