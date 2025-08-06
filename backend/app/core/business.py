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
        risk_score = model.predict([customer_data])[0]
        return risk_score
    except Exception as e:
        return f"Prediction error: {str(e)}"
