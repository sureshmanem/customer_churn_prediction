from app.ml.model import ChurnModel

# Example business logic for churn prediction

def get_churn_risk(customer_data):
    model = ChurnModel()
    model.load('app/ml/churn_model.pkl')
    risk_score = model.predict([customer_data])[0]
    return risk_score
