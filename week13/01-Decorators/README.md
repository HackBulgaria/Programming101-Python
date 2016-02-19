# @accepts
Make a decorator ``accepts`` that takes as many arguments as the function takes. That decorator specify the types of the arguments that your function takes. If any of the arguments does not match the type in the decorator raise a ``TypeError``

## Examples
```python
@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

say_hello(4)

TypeError: Argument 1 of say_hello is not str!
```

```python
@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

say_hello("Hacker")
```

```python
@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

deposit("RadoRado", 10)
```

Note that this is just a nice example. In real life you don't want use this!

# @encrypt(key)

Make a decorator ``encrypt`` that takes an integer. The decorator should encrypts the returned string of a function using the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). That integer is the encryptions key.

## Example

```python
@encrypt(2)
def get_low():
    return "Get get get low"

get_low()

Igv igv igv nqy
```

# @log(file_name)
Make a decorator ``log`` that takes an ``file_name`` and writes in to this file a log. New line for every call of the decorated function. 


## Example

```python
@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

get_low()

Igv igv igv nqy
```

And the log file should look like this:

```
get_low was called at 2015-08-04 02:51:41.929980
get_low was called at 2015-08-04 02:51:45.992980
get_low was called at 2015-08-04 02:51:42.999923
```

# @performance(file_name)
Make a decorator ``performance`` that takes an ``file_name`` and writes in to this file a log. New line for every call of the decorated function. This decorator should log the time needed for the decorated function to execute.

## Example

```python
@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"

something_heavy()

I am done!
```

And the log file should look like this:

```
get_low was called and took 2.00 seconds to complete
get_low was called and took 2.10 seconds to complete
```
