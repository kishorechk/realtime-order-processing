import logging

from sqlalchemy.orm import Session
from .models import Inventory

logger = logging.getLogger(__name__)
def create_inventory_item(db: Session, item_data):
    item = Inventory(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def check_and_update_inventory(db: Session, order_data):
    product = db.query(Inventory).filter_by(product_name=order_data['product_name']).first()
    logger.info(f'found product {product}')
    if product and product.quantity >= order_data['quantity']:
        product.quantity -= order_data['quantity']
        db.commit()
        logger.info('database updated')
        # Optionally, send a confirmation message to another Kafka topic.
    else:
        # Handle stock-out situation.
        raise Exception('Out of stock!!')

def get_all_inventory(db: Session):
    return db.query(Inventory).all()