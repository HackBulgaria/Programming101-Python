from functools import wraps


def debugger(func):
    msg = func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(msg)
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result

    return wrapper


@debugger
def add(a, b):
    return a + b


@debugger
def ivo():
    return 'panda'

print(add(1, 2))
ivo()
