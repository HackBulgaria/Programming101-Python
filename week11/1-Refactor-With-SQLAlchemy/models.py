from base import Base
from sqlalchemy import Column, Integer, String


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
