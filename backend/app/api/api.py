from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.customer_routes import router as customer_router
from app.api.routes import router as predict_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer_router)
app.include_router(predict_router)

@app.get("/")
def read_root():
    return {"message": "Customer Churn Prediction API is running."}
