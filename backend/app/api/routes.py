from fastapi import APIRouter
from app.core.business import get_churn_risk
from app.models.schemas import CustomerCreate

router = APIRouter()

@router.post("/predict")
def predict_churn(customer: CustomerCreate):
    risk = get_churn_risk(customer.dict())
    return {"churn_risk": risk}
