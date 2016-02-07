# Step by step, working with SQLAlchemy

We are going to take it slow and work step by step with the ORM.

## Basic Concepts

SQLAlchemy gives us the opportunity to map Python classes to SQL Tables.

This means that we can describe the structure of our database using classes, rather than plain old SQL file.

We are going to call our classes, that maps to tables with a new name: **models**

## Install

In a proper virtual env, run the following command:

```
$ pip install SQLAlchemy
```

This should install the latest version.

## Getting around the ORM system

We will start with a small chunk of Python code, that will create a table, called `student` and map it to `Student` class.

```python
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
```

If we run this program, lets call it `orm_example1.py`:

```
$ python orm_example1.py
$ ls
orm.py university.db
```

We are going to see that `university.db` was created.

If we open the file with `sqlite3` and ask for `.tables` and `.schema`:

```
$ sqlite3 university.db
SQLite version 3.7.9 2011-11-01 00:52:41
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
students
sqlite> .schema
CREATE TABLE students (
  id INTEGER NOT NULL, 
  name VARCHAR, 
  age INTEGER, 
  PRIMARY KEY (id)
);
```

We will see that student table was created.

## Adding new record to our database

Now, if we want to insert new rows in our database, this means that we have to create new objects from our model classes & save them somehow.

Since SQLAlchemy uses the **Data Mapper** approach, there is going to be a special `Session` object that handles the saving & updating of our models.

To get a good understanding of the `Session` object, [read the explanation from the docs](http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#what-does-the-session-do)

```python
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
```

Now if we run the script and check our database:

```
$ python3 orm_example2.py
Adding new student to the database via the session object
$ sqlite3 university.db
sqlite> select * from student;
1|Rado|23
```

## Adding multiple records & querying them

Lets add 3 students and query back to display them.

We do the querying, again, from the `Session` object.

```python
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
```

Now if we run the program:

```
$ python orm_example3.py
Adding new student to the database via the session object
[1 - Rado, 2 - Ivo, 3 - Ivan]
```

This is a list of Student objects, but we have `__str__` and `__repr__` implemented.

### More on queyring - WHERE statement via filter

In order to get a good understanding of how querying works, you can read this part from the [SQLAlchemy tutorial](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#querying)

```python
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
```

If we run the program, we will get the following output:

```
$ python orm_example4.py
Adding new student to the database via the session object
[1 - Rado]
Name Rado with age 23
Name Ivan with age 23
```

### We call it relationship. And we build it with Foreign Keys!

Now, we are going to introduce another class (table), called `Grade`.

We will keep many grades for our students. The relationship here is:

* 1 student has many grades.
* Many grades can be assigned to one student

We will introduce foreign key, when creating the new class:

```python
# One student can have many grades
# So we will have one-to-many relationship here
class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", backref="grades")
```

Here is the entire program. Don't forget to remove `university.db` before running.

```python
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
```
