from app.ml.model import ChurnModel
import os

# Example business logic for churn prediction


def get_churn_risk(customer_data):
    model_path = 'app/ml/churn_model.pkl'
    if not os.path.exists(model_path):
        return "Model not trained. Please run training script."
    model = ChurnModel()
    model.load(model_path)
    try:
        # Extract features in the correct order
        features = [
            customer_data["engagement_score"],
            customer_data["claim_count"],
            customer_data["payment_history_score"]
        ]
        risk_score = model.predict([features])[0]
        return risk_score
    except Exception as e:
        return f"Prediction error: {str(e)}"
