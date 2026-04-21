from fastapi import APIRouter, HTTPException
from schema import Transaction   # make sure schema name is correct
from services.predict_service import predict_transaction

router = APIRouter()


@router.post("/predict")
def predict(data: Transaction):
    features = data.features

    # Validate length
    if len(features) != 30:
        raise HTTPException(
            status_code=400,
            detail="Expected exactly 30 features"
        )

    # Validate numeric
    try:
        features = [float(x) for x in features]
    except:
        raise HTTPException(
            status_code=400,
            detail="All features must be numeric"
        )

    # Call service
    return predict_transaction(features)