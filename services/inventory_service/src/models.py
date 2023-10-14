from sqlalchemy import create_engine, Column, Integer, String, Float
from .database import Base

class Inventory(Base):
    __tablename__ = 'inventory'

    product_name = Column(String, primary_key=True)
    quantity = Column(Integer)
    price = Column(Float)