from sqlalchemy import create_engine, Column, Integer, String, Float
from .database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    status = Column(String, default='Pending')