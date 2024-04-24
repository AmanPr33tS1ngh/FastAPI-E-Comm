import sqlalchemy as sql
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///./database.db'

engine = sql.create_engine(DATABASE_URI, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative.declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()