from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

# A class that maps to a table, inherits from Base
Base = declarative_base()


# Our class will be mapped to a table with name student
# Each field is a Column with the given type and constraints
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)
