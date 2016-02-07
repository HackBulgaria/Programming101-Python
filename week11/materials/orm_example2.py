from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Session is our Data Mapper
session = Session()

print("Adding new student to the database via the session object")
student1 = Student(name="Rado", age=23)
session.add(student1)
session.commit()
