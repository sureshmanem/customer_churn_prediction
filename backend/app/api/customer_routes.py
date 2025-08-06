from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.api.crud import get_customer, get_customers, create_customer, update_customer, delete_customer
from app.models.schemas import CustomerCreate, CustomerUpdate, CustomerOut
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers", response_model=CustomerOut)
def create_customer_endpoint(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer.dict())

@router.get("/customers/{customer_id}", response_model=CustomerOut)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/customers", response_model=List[CustomerOut])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_customers(db, skip=skip, limit=limit)

@router.put("/customers/{customer_id}", response_model=CustomerOut)
def update_customer_endpoint(customer_id: int, update_data: CustomerUpdate, db: Session = Depends(get_db)):
    customer = get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return update_customer(db, customer_id, update_data.dict())

@router.delete("/customers/{customer_id}", response_model=CustomerOut)
def delete_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    customer = get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return delete_customer(db, customer_id)
