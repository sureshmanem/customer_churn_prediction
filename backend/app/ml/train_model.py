import pandas as pd
from app.models.customer import Customer, Base
from app.models.database import engine, SessionLocal
from app.ml.model import ChurnModel

# Example: Load data from database and train model

def fetch_data():
    db = SessionLocal()
    customers = db.query(Customer).all()
    db.close()
    data = [c.__dict__ for c in customers]
    df = pd.DataFrame(data)
    return df

def main():
    df = fetch_data()
    if df.empty:
        print("No data available for training.")
        return
    X = df[["engagement_score", "claim_count", "payment_history_score"]]
    y = df["churned"]
    model = ChurnModel()
    model.train(X, y)
    model.save("app/ml/churn_model.pkl")
    print("Model trained and saved.")

if __name__ == "__main__":
    main()
