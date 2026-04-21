import numpy as np
from fastapi import HTTPException
from core.model_loader import model, scaler


def predict_transaction(features):
    try:
        # Validate input length
        if len(features) != 30:
            raise HTTPException(
                status_code=400,
                detail=f"Expected 30 features, got {len(features)}"
            )

        # Convert to numpy
        data = np.array(features, dtype=float).reshape(1, -1)

        # Apply scaler only if available
        if scaler is not None:
            data = scaler.transform(data)

        # Prediction
        prediction = int(model.predict(data)[0])

        # Probability (fraud class = 1)
        probability = None
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(data)[0][1])

        # Risk level (based on probability)
        risk = None
        if probability is not None:
            if probability > 0.8:
                risk = "High"
            elif probability > 0.6:
                risk = "Medium"
            else:
                risk = "Low"

        return {
            "prediction": prediction,
            "result": "Fraud" if prediction == 1 else "Not Fraud",
            "confidence": round(probability, 4) if probability is not None else None,
            "risk_level": risk
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )