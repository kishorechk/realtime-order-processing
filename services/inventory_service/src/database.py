from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

# Create an engine instance
engine = create_engine(DATABASE_URL)

# Create a local session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create a base class for models to inherit from
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

