from functools import wraps


def debug(func):
    fname = func.__qualname__

    @wraps(func)
    def wrapper(*arg, **kwargs):
        print('Calling {}'.format(fname))

        return func(*arg, **kwargs)

    return wrapper


def debugmethods(cls):
    for attr, value in vars(cls).items():
        if callable(value):
            setattr(cls, attr, debug(value))

    return cls


@debugmethods
class Panda:

    def be_panda(self):
        print('Being panda')

    def awesome(self):
        print('Pandas are awesome!')


if __name__ == '__main__':
    p = Panda()
    p.be_panda()
    p.awesome()
