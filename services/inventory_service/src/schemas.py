from pydantic import BaseModel

class InventoryBase(BaseModel):
    product_name: str
    quantity: int
    price: float
    class Config:
        from_attributes = True