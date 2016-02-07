from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
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

# Save changes to database
session.commit()


# SELECT * FROM student WHERE name = "Rado";
rado = session.query(Student).filter(Student.name == "Rado").all()
print(rado)

# SELECT name, age FROM student WHERE age = 23
twenty_three = session.query(Student.name, Student.age).\
    filter(Student.age == 23).all()

for student in twenty_three:
    print("Name {} with age {}".format(student.name, student.age))
