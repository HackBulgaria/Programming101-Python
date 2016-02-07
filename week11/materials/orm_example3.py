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

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Session is our Data Mapper
session = Session()

print("Adding new student to the database via the session object")
session.add_all([
    Student(name="Rado", age=23),
    Student(name="Ivo", age=21),
    Student(name="Ivan", age=23)])

# Save changes to DB
session.commit()


# SELECT * FROM student;
all_students = session.query(Student).all()
# list of Student objects
print(all_students)
