from class_decorators import debugmethods


class mytype(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        print('Constructed new type')
        return clsobj


class Panda(metaclass=mytype):
    pass

p = Panda()


class debugmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        # Decoration here.
        clsobj = debugmethods(clsobj)
        return clsobj


class Base(metaclass=debugmeta):
    pass


class Person(Base):
    def be_awesome(self):
        pass


person = Person()
person.be_awesome()


class no_multiple_inheritence(type):
    def __new__(cls, name, bases, clsdict):
        if len(bases) > 1:
            raise TypeError('No multiple inheritence!')

        return super().__new__(cls, name, bases, clsdict)


class Base(metaclass=no_multiple_inheritence):
    pass


class A(Base):
    pass


class B(Base):
    pass


class C(A, B):
    pass
