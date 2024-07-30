from sqlalchemy import Column, Integer, String
from config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    address = Column(String)
    email = Column(String, unique=True, index=True)
    image_url = Column(String)
    description = Column(String)
