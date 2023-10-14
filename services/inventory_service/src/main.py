import logging

from fastapi import FastAPI, BackgroundTasks
from .database import get_db
from .db_service import check_and_update_inventory
from .kafka_service import consumer
from .migration_utils import run_flyway_migration
from .routes import router as inventory_routes

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(inventory_routes)

def kafka_consumer():
    for message in consumer:
        logger.info(f'received message: {message}')
        order_data = message.value
        db = get_db()
        check_and_update_inventory(db, order_data)

@app.on_event("startup")
async def startup_event():
    # Run Flyway migrations at startup
    run_flyway_migration()
    # Start Kafka consumer as a background task
    bg_tasks = BackgroundTasks()
    bg_tasks.add_task(kafka_consumer)
