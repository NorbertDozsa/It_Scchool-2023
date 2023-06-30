from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from pathlib import Path


ROOT = Path(__file__).parent
DB_PATH = ROOT / "db.sqlite3"

Base = declarative_base()

engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

