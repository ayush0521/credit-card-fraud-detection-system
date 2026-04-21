from pyexpat import model

from fastapi import FastAPI
from routes.predict import router as predict_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}

# Include route
app.include_router(predict_router)

from core.model_loader import model

print("Model loaded successfully:", type(model))