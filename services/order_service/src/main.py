import logging
from fastapi import FastAPI
from .migration_utils import run_flyway_migration
from .routes import router as order_routes

logger = logging.getLogger(__name__)

app = FastAPI()

# Run Flyway migrations at startup
try:
    run_flyway_migration()
except Exception as e:
    logger.error(f"Failed to run migrations: {e}")
    exit(1)

app.include_router(order_routes)