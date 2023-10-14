from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import OrderResponse, OrderBase
from . import db_service
from . import kafka_service
from .database import get_db

router = APIRouter()

@router.post("/order", response_model=OrderResponse)
def create_order(order: OrderBase, db: Session = Depends(get_db)):
    # Store in DB
    new_order = db_service.create_order(order.dict(), db)
    order_response = OrderResponse.from_orm(new_order)
    # Send to Kafka
    kafka_service.send_order_event(order_response.dict())
    return order_response

@router.get("/order/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order = db_service.get_order_by_id(order_id, db)
    return OrderResponse.from_orm(order)
