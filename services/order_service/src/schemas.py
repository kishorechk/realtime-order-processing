from pydantic import BaseModel

class OrderBase(BaseModel):
    product_name: str
    quantity: int
    price: float
    status: str = 'Pending'
    class Config:
        from_attributes = True

class OrderResponse(OrderBase):
    id: int