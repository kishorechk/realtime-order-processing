from sqlalchemy.orm import Session
from .models import Order

def create_order(order_data, db: Session):
    new_order = Order(**order_data)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
def get_order_by_id(order_id: int, db: Session):
    return db.query(Order).filter(Order.id == order_id).first()

