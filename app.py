from fastapi import FastAPI
import pickle
import numpy as np

# Create app
app = FastAPI()

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Home route (test)
@app.get("/")
def home():
    return {"message": "API is working"}

# Prediction route
@app.post("/predict")
def predict(data: dict):
    try:
        user_input = data["input"]
        prediction = model.predict(np.array([[user_input]]))
        return {"prediction": float(prediction[0])}
    except:
        return {"error": "Invalid input"}