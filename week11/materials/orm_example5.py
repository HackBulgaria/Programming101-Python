from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


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


# One student can have many grades
# So we will have one-to-many relationship here
class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", backref="grades")

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

session.commit()

# SELECT * FROM student WHERE name = "Rado" LIMIT 1;
rado = session.query(Student).filter(Student.name == "Rado").one()

# Now, lets add some grades to rado:
rado.grades = [Grade(value=6), Grade(value=5), Grade(value=3)]

# And add grades to ivo

ivo = session.query(Student).filter(Student.name == "Ivo").one()
ivo.grades.append(Grade(value=6))

session.commit()
