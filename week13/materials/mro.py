# http://stackoverflow.com/questions/2010692/what-does-mro-do-in-python


# class A extends object
class A:
    def hit_me(self):
        print('hit_me defined in A')


# class B extends A
class B(A):
    def hit_me(self):
        print('hit_me defined in B')


# class C extends A
class C(A):
    def hit_me(self):
        print('hit_me defined in C')


# class D extends B, C
class D(B, C):
    pass


def print_mro(cls):
    print('{}: {}'.format(cls.__name__, cls.__mro__))


print_mro(A)
print_mro(B)
print_mro(C)
print_mro(D)

print('''
issubclass(D, A))
=>''')
print(issubclass(D, A))

print('''
a = A()
a.hit_me()
==>''')
a = A()
a.hit_me()

print('''
b = B()
b.hit_me()
==>''')
b = B()
b.hit_me()

print('''
c = C()
c.hit_me()
==>''')
c = C()
c.hit_me()

print('''
d = D()
d.hit_me()
==>''')
d = D()
d.hit_me()
