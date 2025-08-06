from app.models.customer import Customer, Base
from app.models.database import engine, SessionLocal

Base.metadata.create_all(bind=engine)

def populate():
    db = SessionLocal()
    customers = [
        {"name": "Alice", "engagement_score": 0.7, "claim_count": 1, "payment_history_score": 0.8, "churned": False},
        {"name": "Bob", "engagement_score": 0.4, "claim_count": 3, "payment_history_score": 0.5, "churned": True},
        {"name": "Charlie", "engagement_score": 0.9, "claim_count": 0, "payment_history_score": 0.95, "churned": False},
        {"name": "Diana", "engagement_score": 0.3, "claim_count": 2, "payment_history_score": 0.6, "churned": True},
    ]
    for c in customers:
        db_customer = Customer(**c)
        db.add(db_customer)
    db.commit()
    db.close()
    print("Sample data populated.")

if __name__ == "__main__":
    populate()
