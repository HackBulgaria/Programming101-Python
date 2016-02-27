class Duck:
    def quack(self):
        print('Duck quacks!')


class Panda:
    def quack(self):
        print('Panda quacks!')


class Person:
    def __init__(self, name):
        self.quack = name


def duck_duck_go(obj):
    if hasattr(obj, 'quack')\
            and callable(getattr(obj, 'quack')):
        obj.quack()


duck_duck_go(Duck())
duck_duck_go(Panda())
duck_duck_go(1)
duck_duck_go(Person('Ivo'))
