class A:
    def hit_me(self):
        return 1 + self.where_am_i()


class B:
    def where_am_i(self):
        return 42


class C(B, A):
    pass


c = C()
print(C.__mro__)
print(c.hit_me())
