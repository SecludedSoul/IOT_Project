from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# การตั้งค่าการเชื่อมต่อกับ PostgreSQL
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/CRUDIOT"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

