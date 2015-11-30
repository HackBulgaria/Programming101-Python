class Panda:

    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight

    def eat(self, amount):
        self._weight += amount

    def sleep(self):
        self._age += 1

    def get_age(self):
        return self._age

    def get_weight(self):
        pass

    def __str__(self):
        return "I am {} and i am a proud Panda!".format(self._name)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self._name + str(self._age))

    def __eq__(self, other):
        return self._name == other._name

ivo = Panda("Ivo", 22, 90)
rado = Panda("Ivo", 22, 80)

print(ivo == rado)
print(hash(ivo))
