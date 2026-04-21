import os
import joblib

# Absolute base directory of this file (backend/core/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go 2 levels up → project root → models/
MODEL_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "models", "fraud_model.pkl")
)

SCALER_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "models", "scaler.pkl")
)

# Load model
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

# Load scaler (only if used during training)
def load_scaler():
    if not os.path.exists(SCALER_PATH):
        print("⚠️ Scaler not found, skipping...")
        return None
    return joblib.load(SCALER_PATH)

# Load once (global)
model = load_model()
scaler = load_scaler()

# Debug (optional, remove later)
print("✅ Model loaded from:", MODEL_PATH)
print("✅ Scaler loaded from:", SCALER_PATH if scaler else "Not used")
print("MODEL TYPE:", type(model))