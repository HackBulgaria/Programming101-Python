class Enumerable:
    def take(self, n):
        pass

    def drop(self, n):
        pass

    def take_while(self, predicate):
        pass

    def drop_while(self, predicate):
        pass

    def map(self, callable):
        r = []

        for x in self:
            r.append(callable(x))

        return self.__class__(*r)

    def filter(self, predicate):
        pass

    def reduce(self, start_value, operator):
        pass


class Extensible:
    def __add__(self, other):
        data = list(self) + list(other)
        return self.__class__(*data)


class Collection(Enumerable, Extensible):
    def __init__(self, *args):
        self.__data = args

    def __iter__(self):
        return iter(self.__data)

    def __repr__(self):
        return repr(self.__data)

    def __str__(self):
        return str(self.__data)

    def __eq__(self, other):
        return list(self) == list(other)

c = Collection(1, 2, 3)
assert c == c.map(lambda x: x)

c1 = c + [1, 2, 3]
print(c1)
