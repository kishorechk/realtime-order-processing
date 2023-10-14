from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import db_service
from .database import get_db
from .schemas import InventoryBase

router = APIRouter()

@router.post("/inventory", response_model=InventoryBase)
def create_inventory_item(item: InventoryBase, db: Session = Depends(get_db)):
    new_inventory = db_service.create_inventory_item(db, item.dict())
    InventoryBase.from_orm(new_inventory)

@router.get("/inventory", response_model=List[InventoryBase])
def list_inventory(db: Session = Depends(get_db)):
    return db_service.get_all_inventory(db)
