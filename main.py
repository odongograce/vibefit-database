from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

DATABASE_URL = "sqlite:///db/vibefit.db"
if __name__ == "__main__":
    engine = create_engine(DATABASE_URL, echo=True)

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    print("Database Created")