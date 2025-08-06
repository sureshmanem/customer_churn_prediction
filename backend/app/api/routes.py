from fastapi import APIRouter
from app.core.business import get_churn_risk

router = APIRouter()

@router.post("/predict")
def predict_churn(customer: dict):
    risk = get_churn_risk(customer)
    return {"churn_risk": risk}
