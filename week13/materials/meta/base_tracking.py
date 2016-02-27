class basetracking(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(cls, 'registry'):
            cls.registry = set()

        cls.registry.add(clsobj)

        return clsobj


class Base(metaclass=basetracking):
    pass


class A(Base):
    pass


class B(Base):
    pass


class C(A, B):
    pass

print(Base.registry)
