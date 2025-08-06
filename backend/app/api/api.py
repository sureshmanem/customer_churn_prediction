from fastapi import FastAPI
from app.api.customer_routes import router as customer_router

app = FastAPI()
app.include_router(customer_router)

@app.get("/")
def read_root():
    return {"message": "Customer Churn Prediction API is running."}
