from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    engagement_score = Column(Float)
    claim_count = Column(Integer)
    payment_history_score = Column(Float)
    churned = Column(Boolean, default=False)
