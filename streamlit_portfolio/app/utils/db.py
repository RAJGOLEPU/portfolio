from sqlalchemy import create_engine
import os

def get_engine():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_folder = os.path.join(base_dir, "..", "data")
    os.makedirs(db_folder, exist_ok=True)

    db_path = os.path.join(db_folder, "portfolio.db")
    db_url = f"sqlite:///{os.path.abspath(db_path)}"

    return create_engine(db_url, echo=False)
