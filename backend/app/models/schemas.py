from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    engagement_score: float
    claim_count: int
    payment_history_score: float

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int
    churned: bool

    class Config:
        orm_mode = True
