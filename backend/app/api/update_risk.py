from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.models.database import SessionLocal
from app.core.business import get_churn_risk

def update_churn_risk_for_all():
    db = SessionLocal()
    customers = db.query(Customer).all()
    for customer in customers:
        data = {
            "name": customer.name,
            "engagement_score": customer.engagement_score,
            "claim_count": customer.claim_count,
            "payment_history_score": customer.payment_history_score
        }
        risk = get_churn_risk(data)
        try:
            customer.churn_risk_score = float(risk)
        except:
            customer.churn_risk_score = None
    db.commit()
    db.close()
    print("Churn risk scores updated for all customers.")

if __name__ == "__main__":
    update_churn_risk_for_all()
