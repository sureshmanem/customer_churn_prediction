from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.api.crud import get_customer, get_customers, create_customer, update_customer, delete_customer

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers")
def create_customer_endpoint(customer: dict, db: Session = Depends(get_db)):
    return create_customer(db, customer)

@router.get("/customers/{customer_id}")
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/customers")
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_customers(db, skip=skip, limit=limit)

@router.put("/customers/{customer_id}")
def update_customer_endpoint(customer_id: int, update_data: dict, db: Session = Depends(get_db)):
    return update_customer(db, customer_id, update_data)

@router.delete("/customers/{customer_id}")
def delete_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    return delete_customer(db, customer_id)
