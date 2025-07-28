from sqlalchemy import create_engine
import os

def get_engine():
    db_url = os.getenv("DATABASE_URL")
    return create_engine(db_url)
